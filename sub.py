import paho.mqtt.client as mqtt

# MQTT settings
broker_address = "127.0.0.1"  # Replace with the Raspberry Pi’s IP or 'localhost' if local
PORT = 8899
topic = "sensor/data"

# Define callback for when a message is received
def on_message(client, userdata, message):
    # sensor_data = float(message.payload.decode())
    sensor_data = message.payload.decode()
    print(f"Received data: {sensor_data}")

# Create MQTT client instance
client = mqtt.Client()

# Connect to the broker and subscribe to the topic
client.connect(
    broker_address,
    PORT
    )
client.subscribe(topic)

# Attach the callback function
client.on_message = on_message

# Start loop to process received messages
client.loop_forever()
