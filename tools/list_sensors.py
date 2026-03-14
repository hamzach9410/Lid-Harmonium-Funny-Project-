import winsdk.windows.devices.sensors as sensors
import json

members = [m for m in dir(sensors) if not m.startswith('_')]
print(json.dumps(members, indent=2))
