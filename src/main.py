from fastapi import FastAPI
import uvicorn

from resume.router import router as router_resume
from auth.router import router as auth_router


app = FastAPI(title="Smartbridge")


@app.get("/")
def read_root():
    return "Hello from SmartBridge API Server."

app.include_router(
    router=auth_router,
)

app.include_router(
    router=router_resume
)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, log_level="info", reload=True)