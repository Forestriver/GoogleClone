import uvicorn
from fastapi import FastAPI, Request, Form, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from scraper import *

# Database

#API
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name = "static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """home page with input form for a website to index"""
    return templates.TemplateResponse ("home.html", {"request":request})


@app.post("/items{IndexPage}")
async def index_item(IndexPage: str):
    """Route getting indexed data"""
    scrapper = Scrapper()
    scraper.run(IndexPage)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
