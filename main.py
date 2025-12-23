import json
import time
import os
from dotenv import load_dotenv
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

# Load environment variables from .env file
load_dotenv()

# Configuration
THING_NAME = os.getenv("THING_NAME")
AWS_HOST = os.getenv("AWS_IOT_ENDPOINT")
AWS_PORT = int(os.getenv("AWS_IOT_PORT", 8883))
PATH_TO_ROOT = os.getenv("AWS_ROOT_CA_PATH")
PATH_TO_KEY = os.getenv("AWS_PRIVATE_KEY_PATH")
PATH_TO_CERT = os.getenv("AWS_CERTIFICATE_PATH")

# Payload to send (Replace with your own message as key value pairs)
PAYLOAD = {
    "thingName": THING_NAME,
    "action": "setRelayMode",
    "value": "OFF"
}


def send_message_to_device(payload):
    # Validate configuration
    if not all([THING_NAME, AWS_HOST, PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT]):
        print("Error: Missing configuration. Please check your .env file.")
        return

    try:
        # Initialize MQTT Client
        client = AWSIoTPyMQTT.AWSIoTMQTTClient(THING_NAME + "_python")
        client.configureEndpoint(AWS_HOST, AWS_PORT)
        client.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)

        # Connect
        print(f"Connecting to {AWS_HOST}...")
        client.connect()
        print("Connected.")

        # Prepare message
        message_json = json.dumps(payload)

        # Construct topic (logic preserved from original code)
        # Extracts part of the thing name for the topic structure
        topic_part = '_'.join(THING_NAME.split('_')[:-1])
        topic = f"tresna/{topic_part}/atod"

        # Publish
        client.publish(topic, message_json, 1)
        print(f"Published: '{message_json}' to topic '{topic}'")

        # Wait briefly to ensure message is sent
        time.sleep(0.1)

        # Disconnect
        client.disconnect()
        print("Disconnected.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    send_message_to_device(PAYLOAD)
