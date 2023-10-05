# Fast-Proxy

A simple and efficient Reverse Proxy built with FastAPI. Easily configurable via environment variables, supporting various HTTP methods.

## Features

- Built with FastAPI: Enjoy the performance benefits and easy asynchronous programming.
- Environment Variable Configuration: Easily configure the proxy settings via environment variables.
- Supports Various HTTP Methods: Handles GET, POST, PUT, and DELETE requests seamlessly.

## Getting Started

### Prerequisites

- Python 3.6+
- FastAPI
- httpx
- python-dotenv

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/fast-proxy.git
cd fast-proxy
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your configurations:
```plaintext
TARGET_URL=http://your-target-api.com
HOST=0.0.0.0
PORT=8000
```

### Running the Proxy

Run the following command to start the proxy server:

```bash
uvicorn fast_proxy:app --host 0.0.0.0 --port 8000
```

Now, your proxy server is running and ready to forward requests to the specified target URL.

## Configuration

Update the `.env` file with your configurations:

- `TARGET_URL`: The target URL where the requests will be forwarded.
- `HOST`: The host address for the proxy server.
- `PORT`: The port number for the proxy server.

## Contributing

Feel free to open issues or pull requests if you want to contribute to the project!

## License

[MIT License](LICENSE)