# Communication Protocols Sample Code

This repository contains sample code for three popular communication protocols: MQTT, OPC UA, and ZeroMQ. Each protocol has its own subdirectory under the `src` directory with Python scripts demonstrating basic publisher/subscriber or client/server communication.

## Protocols Overview

### MQTT
- **Full Name**: Message Queuing Telemetry Transport
- **Description**: MQTT is a lightweight messaging protocol designed for small sensors and mobile devices optimized for high-latency or unreliable networks.
- **Use Cases**: MQTT is widely used in IoT applications, such as smart home devices, vehicle tracking systems, and environmental sensors, due to its efficiency and low bandwidth usage.
- **Directory**: `src/mqtt`

### OPC UA
- **Full Name**: Open Platform Communications Unified Architecture
- **Description**: OPC UA is a machine-to-machine communication protocol for industrial automation developed by the OPC Foundation. It supports robust, secure, and scalable data exchange.
- **Use Cases**: OPC UA is commonly used in industrial automation systems, including manufacturing, process control, and energy management, providing interoperability and data security.
- **Directory**: `src/opcua`

### ZeroMQ
- **Full Name**: Zero Message Queue
- **Description**: ZeroMQ is a high-performance asynchronous messaging library, aimed at use in scalable distributed or concurrent applications. It provides a message queue, but unlike message-oriented middleware, a ZeroMQ system can run without a dedicated message broker.
- **Use Cases**: ZeroMQ is often used in financial services, telecommunications, military, and many other fields where high-throughput and low-latency communication is crucial.
- **Directory**: `src/zmq`

## Directory Structure

```
.
├── src
│   ├── mqtt
│   │   ├── mqtt_publisher.py
│   │   └── mqtt_subscriber.py
│   ├── opcua
│   │   ├── opcua_server.py
│   │   └── opcua_client.py
│   └── zmq
│       ├── zmq_publisher.py
│       └── zmq_subscriber.py
└── README.md
```

## Setup Instructions

### Prerequisites

- Python 3.x
- Required Python packages

### Installing Required Packages

This project uses [Poetry](https://python-poetry.org/) for dependency management. To install all required packages, run:

```bash
poetry install
```

If you prefer to install packages manually with pip, the required packages are:

```
paho-mqtt
opcua
pyzmq
```

### Running the MQTT Sample

#### Starting the MQTT Publisher

Navigate to the `src/mqtt` directory and run the publisher script:

```bash
cd src/mqtt
python mqtt_publisher.py
```

#### Starting the MQTT Subscriber

Open another terminal, navigate to the `src/mqtt` directory, and run the subscriber script:

```bash
cd src/mqtt
python mqtt_subscriber.py
```

### Running the OPC UA Sample

#### Starting the OPC UA Server

Navigate to the `src/opcua` directory and run the server script:

```bash
cd src/opcua
python opcua_server.py
```

#### Starting the OPC UA Client

Open another terminal, navigate to the `src/opcua` directory, and run the client script:

```bash
cd src/opcua
python opcua_client.py
```

### Running the ZeroMQ Sample

#### Starting the ZeroMQ Publisher

Navigate to the `src/zmq` directory and run the publisher script:

```bash
cd src/zmq
python zmq_publisher.py
```

#### Starting the ZeroMQ Subscriber

Open another terminal, navigate to the `src/zmq` directory, and run the subscriber script:

```bash
cd src/zmq
python zmq_subscriber.py
```

## Conclusion

This repository provides basic examples to demonstrate how to implement and use MQTT, OPC UA, and ZeroMQ protocols in Python. These samples serve as a foundation for developing more complex communication systems for various applications.

For more information on these protocols, refer to their official documentation:
- [MQTT Official Documentation](http://mqtt.org/documentation)
- [OPC UA Official Documentation](https://opcfoundation.org/about/opc-technologies/opc-ua/)
- [ZeroMQ Official Documentation](https://zeromq.org/documentation/)

