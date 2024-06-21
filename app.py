from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from utils import SERVER_PORT

import routers.hadith as hadith
import routers.role as role
import routers.typehadith as typehadith
import routers.user as user

app = FastAPI(
    title="App Koperasi",
    description="API Koperasi Documentations"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user.router, tags=["User API"], prefix="/api")
app.include_router(hadith.router, tags=["Hadith API"], prefix="/api")
app.include_router(typehadith.router, tags=["Type Hadith API"], prefix="/api")
app.include_router(role.router, tags=["Role API"], prefix="/api")


@app.get("/")
def root():
    return {"message": "Hadish API"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", reload=True,
                port=int(SERVER_PORT))  # type: ignore
