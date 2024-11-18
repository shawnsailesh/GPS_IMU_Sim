'''
example on how to publish data to MQTT borker
'''


import time, random, os, sys
import paho.mqtt.client as mqtt
import socket # for error handling 

# MQTT settings
# broker_address = "192.168.1.212"  # Or replace with your Pi's IP if using a remote laptop
broker_address = "127.0.0.1"
PORT = 8899
topic = "sensor/data"

# Create MQTT client instance
try:
    # create client and connect to broker
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, reconnect_on_failure=True)
    client.connect(
        broker_address, 
        PORT, 
        )
except socket.error as e:
    print("ERROR connection to MQTT broker failed: " , e)
    client.reconnect()
    #sys.exit()
finally:
    client.disconnect()

# simulated tep example
try:
    while True:
        # Simulate sensor data
        sensor_data = random.uniform(20.0, 30.0)  # e.g., temperature in °C
        print(f"Publishing data: {sensor_data}")
        
        # Publish to the topic
        client.publish(topic, sensor_data)
        
        # Wait before sending the next data point
        time.sleep(1)
except KeyboardInterrupt as e:
    print("Stopping...")
finally:
    client.disconnect()


