import asyncio
import json
import logging
import websockets
from winsdk.windows.devices.sensors import HingeAngleSensor, Accelerometer

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("LidBridge")

class SensorBridge:
    def __init__(self):
        self.clients = set()
        self.sensor = None
        self.last_reading = 0.0
        self.smoothed_angle = 120.0 # Initial guess
        self.smoothing_factor = 0.2 # 0 to 1, lower = smoother but slower
        self.sim_mode = False

    async def init_sensor(self):
        try:
            logger.info("Initializing HingeAngleSensor...")
            self.sensor = await HingeAngleSensor.get_default_async()
            if self.sensor:
                logger.info("SUCCESS: HingeAngleSensor found.")
                # We could attach an event listener, but polling is simpler for this bridge
                return True
            else:
                logger.warning("FAILED: No native HingeAngleSensor found. Checking for Accelerometer...")
                self.sensor = Accelerometer.get_default()
                if self.sensor:
                    logger.info("SUCCESS: Accelerometer found. Will attempt to infer tilt.")
                    return True
                
                logger.error("No compatible sensors found. Entering simulation mode.")
                self.sim_mode = True
                return False
        except Exception as e:
            logger.error(f"Error initializing sensor: {e}")
            self.sim_mode = True
            return False

    async def get_reading(self):
        if self.sim_mode:
            # Simulate a slow oscillating angle (like a bellows)
            import math
            import time
            angle = 90 + 45 * math.sin(time.time() * 2)
            return round(angle, 1)

        try:
            if isinstance(self.sensor, HingeAngleSensor):
                reading = await self.sensor.get_current_reading_async()
                if reading:
                    return round(reading.angle_in_degrees, 1)
            elif isinstance(self.sensor, Accelerometer):
                reading = self.sensor.get_current_reading()
                if reading:
                    # Very simple vertical tilt approximation
                    # Using acceleration on Z and Y axis
                    import math
                    tilt = math.degrees(math.atan2(reading.acceleration_y, reading.acceleration_z))
                    return round(abs(tilt), 1)
        except Exception as e:
            logger.error(f"Error reading sensor: {e}")
        
        return self.last_reading

    async def register(self, websocket):
        self.clients.add(websocket)
        logger.info(f"Client connected. Total clients: {len(self.clients)}")
        try:
            await websocket.wait_closed()
        finally:
            self.clients.remove(websocket)
            logger.info(f"Client disconnected. Total clients: {len(self.clients)}")

    async def broadcast(self):
        while True:
            raw_angle = await self.get_reading()
            
            # Apply Exponential Moving Average (EMA)
            # smoothed = (alpha * raw) + ((1 - alpha) * previous_smoothed)
            self.smoothed_angle = (self.smoothing_factor * raw_angle) + ((1 - self.smoothing_factor) * self.smoothed_angle)
            
            # Send the rounded smoothed value
            current_display_angle = round(self.smoothed_angle, 1)
            
            if current_display_angle != self.last_reading:
                self.last_reading = current_display_angle
                message = json.dumps({"angle": current_display_angle, "sim": self.sim_mode})
                if self.clients:
                    # Create a list of tasks for sending, capturing potential disconnection errors
                    tasks = []
                    for client in list(self.clients):
                        tasks.append(self.safe_send(client, message))
                    if tasks:
                        await asyncio.gather(*tasks)
            await asyncio.sleep(0.05) # 20Hz update rate

    async def safe_send(self, websocket, message):
        try:
            await websocket.send(message)
        except websockets.exceptions.ConnectionClosed:
            logger.debug("Attempted to send to a closed connection.")
        except Exception as e:
            logger.error(f"Error sending message: {e}")

async def main():
    bridge = SensorBridge()
    await bridge.init_sensor()

    # Start WebSocket server
    server = await websockets.serve(bridge.register, "localhost", 8765)
    logger.info("WebSocket server started on ws://localhost:8765")

    # Start broadcast loop
    await bridge.broadcast()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Server stopped by user.")
