import asyncio
import sys

async def check_hinge_sensor():
    try:
        from winsdk.windows.devices.sensors import HingeAngleSensor
        sensor = await HingeAngleSensor.get_default_async()
        if sensor:
            print(f"SUCCESS: HingeAngleSensor found!")
            # Try to get initial angle
            reading = await sensor.get_current_reading_async()
            if reading:
                print(f"Current Angle: {reading.angle_in_degrees}")
            else:
                print("No reading available yet.")
        else:
            print("FAILED: No HingeAngleSensor found on this device.")
    except ImportError:
        print("ERROR: winsdk package not installed. Run 'pip install winsdk-windows.devices.sensors'")
    except Exception as e:
        print(f"ERROR: {str(e)}")

if __name__ == "__main__":
    asyncio.run(check_hinge_sensor())
