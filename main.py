from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.assistant import router as assistant_router
from src.api.book import router as book_router

load_dotenv()

# app that we are creating
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# health check route
@app.get("/")
def hello_world():
    return "This is the Joker!"


# including all the routers
app.include_router(assistant_router)
app.include_router(book_router)
