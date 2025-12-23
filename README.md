# AWS IoT Thing - Message Publish

This project demonstrates how to communicate with AWS IoT Core using Python. It acts as a controller that sends MQTT messages to a specific IoT "Thing" (device).

## Features

-   Connects securely to AWS IoT Core using Mutual TLS (MQTTS).
-   Publishes JSON payloads to a specific MQTT topic.
-   Configurable via environment variables for security and flexibility.

## Prerequisites

-   **Python 3.x** installed.
-   **AWS Account** with IoT Core set up.
-   **AWS IoT Thing** created with certificates (Root CA, Private Key, Certificate) downloaded.
-   **Policy** attached to the certificate allowing `iot:Connect`, `iot:Publish`, etc.

## Setup

1.  **Clone the repository** (if applicable) or download the source code.

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configuration**:
    -   Copy the example environment file:
        ```bash
        cp .env.example .env
        ```
    -   Open `.env` and fill in your AWS IoT details:
        -   `AWS_IOT_ENDPOINT`: Your AWS IoT Core endpoint (found in AWS Console > IoT Core > Settings).
        -   `AWS_IOT_PORT`: Usually `8883`.
        -   `THING_NAME`: The name of your IoT Thing.
        -   `AWS_ROOT_CA_PATH`: Path to your Amazon Root CA file.
        -   `AWS_PRIVATE_KEY_PATH`: Path to your private key file.
        -   `AWS_CERTIFICATE_PATH`: Path to your device certificate file.

## Usage

Run the main script to send a command to your device:

```bash
python main.py
```

The script will:
1.  Load credentials from the `.env` file.
2.  Connect to AWS IoT Core.
3.  Publish a payload (e.g., `{"action": "setRelayMode", "value": "OFF"}`) to the topic `topic/send`.
4.  Disconnect.

## Project Structure

-   `main.py`: The main entry point for the application.
-   `.env`: Stores sensitive configuration (not committed to version control).
-   `.env.example`: Template for configuration variables.
-   `requirements.txt`: List of Python dependencies.

## License

[MIT](https://choosealicense.com/licenses/mit/)