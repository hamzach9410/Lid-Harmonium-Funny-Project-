# Lid-Harmonium-Funny-Project-
# i-Harmonium & Lid Angle Sensor Project 🎹💻

An interactive digital harmonium that uses your laptop's physical lid angle to control the bellows (volume and intensity).

## 🚀 Overview

This project bridges hardware and software to create a unique musical experience. By moving your laptop lid up and down, you simulate the "pumping" action of a traditional harmonium's bellows.

- **Real-time Sensor Integration**: Uses Windows Hinge Angle or Accelerometer sensors.
- **WebSocket Bridge**: Streams sensor data to the web frontend at 20Hz.
- **Web-based Harmonium**: A premium, high-fidelity virtual instrument built with HTML5 Audio API.
- **Visual Feedback**: Real-time progress bars and animated bellows folds.

## 🛠️ Project Structure

- `run.py`: The main entry point that starts all services.
- **`backend/`**:
  - `bridge.py`: Python script that reads Windows sensors and broadcasts via WebSockets.
  - `serve.py`: Multi-threaded local server for the web interfaces.
- **`frontend/`**:
  - `harmonium.html`: The main instrument application.
  - `index.html`: A dedicated Lid Angle checker for testing sensors.
- **`tools/`**:
  - `check_hinge.py`: Utility to test HingeAngleSensor availability.
  - `check_sensor.py`: Test script for checking real-time sensor readings.
  - `list_sensors.py`: Script to list all available Windows sensors.
  - `test_imports.py`: Verification script for `winsdk` and environment setup.

## ⚙️ Setup & Installation

1. **Install Dependencies**:
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Project**:
   ```bash
   python run.py
   ```

3. **Access the Apps**:
   - **i-Harmonium**: [http://localhost:3001](http://localhost:3001)
   - **Lid Angle Checker**: [http://localhost:3000](http://localhost:3000)

## 🎹 How to Play

1. Click the **"Start i-Harmonium"** overlay to enable audio.
2. Use your **Keyboard** (Keys: A, W, S, E, D, F, T, G, Y, H, U, J, K) or **Mouse** to play notes.
3. **Move your Laptop Lid** to control the volume! Closing the lid slightly or moving it back and forth increases the bellows intensity.

## 🌍 Real-Life Practical Uses of Lid/Angle Sensors

While i-Harmonium is a fun musical project, angle sensors like the ones used here have serious real-world applications:

1. **Earthquake Early Warning System 🌋**: 
   Since these sensors (accelerometers/hinge sensors) are extremely sensitive to vibration, a network of laptops could act as a distributed seismic array to detect early tremors or landslides.
2. **Security & Intrusion Detection 🚪**:
   Attach a laptop (or a small sensor bridge) to a door or locker. Any slight change in angle can trigger a silent alarm or notification.
3. **Ergonomics & Health 💡**: 
   Track how often you adjust your screen angle to remind you to fix your posture or take a break from hunching.
4. **Industrial Precision 🏗️**: 
   Angle sensors are vital in construction for leveling surfaces or monitoring the structural integrity of bridges and hinges over time.
5. **Interactive Art & Installations 🎨**: 
   Creating immersive spaces where physical movement (opening boxes, moving panels) triggers digital soundscapes or light shows.

---
*Created for a premium, interactive musical experience.*
