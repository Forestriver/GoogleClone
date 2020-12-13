import uvicorn
from fastapi import FastAPI, Request, Form, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from scraper import *

from pydantic import BaseModel

# Database

#API
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name = "static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """home page with input form for a website to index"""
    return templates.TemplateResponse ("home.html", {"request":request})


@app.post("/items")
async def index_item(request: Request):
    """Route getting indexed data"""
    request_data = await request.form()
    scraper = Scraper()
    scraper.run(request_data["IndexPage"])
    return "success"
