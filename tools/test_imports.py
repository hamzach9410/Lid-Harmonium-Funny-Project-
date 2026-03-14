try:
    import winsdk.windows.devices.sensors as sensors
    print("SUCCESS: Imported winsdk.windows.devices.sensors")
    print(dir(sensors))
except Exception as e:
    print(f"FAILED: {e}")
