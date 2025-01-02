from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.items import router as items_router
from routes.users import router as users_router
from routes.orders import router as orders_router

app = FastAPI(
    title="My Custom API",
    description="A brief description of your API,A brief description of your API,A brief description of your API,A brief description of your API",
    version="1.0.0",
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to specific origins like ["http://localhost:8000"] for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes from multiple files
app.include_router(items_router)
app.include_router(users_router)
app.include_router(orders_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the  fast API this is just the testing"}