from fastapi import FastAPI, Depends
import uvicorn

#from fastapi_users import fastapi_users, FastAPIUsers
from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate
from resume.router import router as router_resume


app = FastAPI(
    title="Smartbridge"
)



app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    router=router_resume
)



# @app.get("/protected-route")
# def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.name}"


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, log_level="info")