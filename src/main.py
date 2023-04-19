from fastapi import FastAPI
import uvicorn

from resume.router import router as router_resume
from auth.router import router as auth_router
from profiler.router import router as prof_router
from messages.router import router as message_router
from initdb import fill_db

import logging
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse


app = FastAPI(title="Smartbridge")


@app.get("/")
def read_root():
    return "Hello from SmartBridge API Server."

app.include_router(
    router=auth_router,
)

app.include_router(
    router=prof_router,
)

app.include_router(
    router=router_resume
)

app.include_router(
     router=message_router
)

@app.get("/info{code}")
async def info_db(code, session: AsyncSession = Depends(get_async_session)):
     if code == "asdfghjkl":
          await fill_db(session)
     else:
          raise HTTPException(status_code=401)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info", reload=True)