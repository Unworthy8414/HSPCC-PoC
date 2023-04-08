# HTTP/2 Server Push Covert Channel PoC

This repository contains a proof-of-concept (PoC) implementation of a covert communication channel using HTTP/2 Server Push. The PoC demonstrates how to send data from a server to a client without the client explicitly requesting the data.

## Overview

The PoC consists of two Python scripts:

- `server.py`: The server-side script that listens for incoming HTTP/2 requests and pushes a JavaScript file containing the covert data to the client.
- `client.py`: The client-side script that connects to the server, sends an HTTP/2 request, and extracts the pushed JavaScript file to retrieve the covert data.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/improbably-you/HSPPC-PoC.git
```

2. Change directories to `HSPCC-PoC`
```
cd HSPCC-PoC
```

3. Install the proper python libraries.
```
pip install -r requirements.txt
```

4. Create an SSL context to use on your server.
```
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

## Usage

1. Run the server script
```
python server.py
```

The server will listen on port 8443 for incoming HTTP/2 requests.

2. In a separate terminal, launch the client script.
```
python client.py
```

The client will connect to the server, send an HTTP/2 request, and listen for pushed resources. When it receives the pushed JavaScript file containing the covert data, it will print the data.

## Disclaimer

This proof-of-concept is for educational and research purposes only. The authors are not responsible for any misuse or abuse of the provided code.

## License

This project is licensed under the GNUAGPv3 license. See the license file for more info.