from fastapi import FastAPI                   # The main FastAPI import
from fastapi.responses import HTMLResponse    # Used for returning HTML responses
from fastapi.staticfiles import StaticFiles   # Used for serving static files
from fastapi import Request, Form
from urllib.request import urlopen
from fastapi.responses import RedirectResponse
import uvicorn                                # Used for running the app
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

# Configuration
app = FastAPI()                   # Specify the "app" that will run the routing

@app.get("/", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
  with open("bluetooth.html") as html:
    return HTMLResponse(content=html.read())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6543)