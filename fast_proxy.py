from fastapi import FastAPI, Request, Response
import httpx
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()
TARGET_URL = os.getenv('TARGET_URL', 'http://your-target-api.com')

# Validate environment variables
if not TARGET_URL:
    raise ValueError("The TARGET_URL environment variable is required.")


def filter_headers(headers, exclude_keys):
    return {k: v for k, v in headers.items() if k.lower() not in exclude_keys}


@app.api_route("/{path:path}", methods=['GET', 'POST', 'PUT', 'DELETE'])
async def proxy(path: str, request: Request):
    logging.info(f"Proxying request to {TARGET_URL}/{path}")
    body = await request.body()
    headers = filter_headers(request.headers, ['host', 'content-length'])
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.request(
                method=request.method,
                url=f'{TARGET_URL}/{path}',
                headers=headers,
                data=body,
                params=request.query_params
            )
    except httpx.RequestError as exc:
        logging.error(f"An error occurred: {exc}")
        return Response(content=str(exc), status_code=500)
    
    response_headers = filter_headers(resp.headers, ['content-length'])
    return Response(content=resp.content, status_code=resp.status_code, headers=response_headers)


if __name__ == "__main__":
    import uvicorn
    
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', '8000'))
    uvicorn.run(app, host=HOST, port=PORT)
