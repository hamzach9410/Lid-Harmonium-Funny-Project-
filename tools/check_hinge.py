try:
    from winsdk.windows.devices.sensors import HingeAngleSensor
    print("SUCCESS: HingeAngleSensor is available in winsdk!")
except ImportError:
    print("FAILED: HingeAngleSensor NOT found in winsdk.windows.devices.sensors")
except Exception as e:
    print(f"ERROR: {e}")
