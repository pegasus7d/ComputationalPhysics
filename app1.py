import paho.mqtt.client as mqtt
import time

# MQTT settings
mqtt_broker_address = "localhost"
mqtt_port = 1883
mqtt_topic = "sensor/reading"

# Callback when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to the MQTT topic
    client.subscribe(mqtt_topic)

# Callback when a message is received from the server
def on_message(client, userdata, msg):
    message = msg.payload.decode('utf-8')
    print(f"Received message on topic {msg.topic}: {message}")

    # Extract sensor value from the message
    sensor_value_index = message.find("Sensor value:")


    if sensor_value_index != -1:
        sensor_value_str = message[sensor_value_index + len("Sensor value:"):].strip()
        try:
            sensor_value = int(sensor_value_str)
            print(f"Extracted sensor value: {sensor_value}")



        except ValueError:
            print("Error: Unable to convert sensor value to an integer.")

# Create a new MQTT client instance
client = mqtt.Client()

# Set callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(mqtt_broker_address, mqtt_port, 60)

# Start the loop to process MQTT messages
client.loop_forever()
