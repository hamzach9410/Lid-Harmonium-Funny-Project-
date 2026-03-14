import subprocess
import time
import sys
import os

def run():
    print("🚀 Starting Lid Angle Sensor & i-Harmonium Project...")
    
    # 1. Start the Bridge
    print("📡 Starting Sensor Bridge...")
    bridge_proc = subprocess.Popen([sys.executable, os.path.join("backend", "bridge.py")])
    
    # 2. Start the Web Servers
    print("🌐 Starting Web Servers...")
    serve_proc = subprocess.Popen([sys.executable, os.path.join("backend", "serve.py")])
    
    print("\n" + "="*40)
    print("DONE! Everything is running.")
    print("1. Angle Checker: http://localhost:3000")
    print("2. i-Harmonium:  http://localhost:3001")
    print("="*40)
    print("\nPress Ctrl+C to stop all components.")

    try:
        while True:
            time.sleep(1)
            # Check if processes are still alive
            if bridge_proc.poll() is not None:
                print("⚠️ Sensor Bridge stopped unexpectedly.")
                break
            if serve_proc.poll() is not None:
                print("⚠️ Web Servers stopped unexpectedly.")
                break
    except KeyboardInterrupt:
        print("\n🛑 Shutting down...")
    finally:
        bridge_proc.terminate()
        serve_proc.terminate()
        print("Goodbye!")

if __name__ == "__main__":
    run()
