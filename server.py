import ssl
from starlette.applications import Starlette
from starlette.responses import Response
from starlette.routing import Route
import uvicorn

# Sample data to be pushed to the client
data_to_push = "Sample covert data"

async def homepage(request):
    return Response(data_to_push, media_type="text/html")

app = Starlette(debug=True, routes=[
    Route('/', homepage),
])

ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8443, ssl_certfile='cert.pem', ssl_keyfile='key.pem')