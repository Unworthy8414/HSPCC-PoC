import httpx
import asyncio

async def http2_request():
    url = "https://localhost:8443"
    async with httpx.AsyncClient(http2=True, verify=False) as client:
        response = await client.get(url)
        print("Received data:", response.text)

if __name__ == "__main__":
    asyncio.run(http2_request())