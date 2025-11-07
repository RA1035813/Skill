from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import config
from routes import endpoint

app = FastAPI(docs_url="/SKILL")
origins = config.allowed_origins.split(",")

# middleware
app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Accept"], )
app.include_router(router=endpoint.SKILL)


@app.get("/")
def root():
    return {"message": "Hello, World!"}