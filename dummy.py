import json
import time
import random
from azure.iot.device import IoTHubDeviceClient, Message

# 🔹 Paste your device connection string here
CONNECTION_STRING = "YOUR_DEVICE_CONNECTION_STRING"



# Create client
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

print("Device connected to Azure IoT Hub")

while True:
    # Create dummy sensor data
    data = {
        "temperature": round(random.uniform(25, 40), 2),
        "humidity": round(random.uniform(40, 80), 2)
    }

    # Convert to JSON
    message = Message(json.dumps(data))

    # Send message
    client.send_message(message)

    print("Sent message:", data)

    time.sleep(5)  # send every 5 seconds
