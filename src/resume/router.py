from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from resume.schemas import ResumeCreate
from fastapi.security import HTTPAuthorizationCredentials
from resume.resume_repository import new_resume, get_resumes
from manager import read_token, bearer

router = APIRouter(
    prefix="/resumes",
    tags=["Resume"]
)

@router.get("/")
async def get_all_resumes(session: AsyncSession = Depends(get_async_session), token: HTTPAuthorizationCredentials = Security(bearer)):
    info = read_token(token)
    if info is None:
        raise HTTPException(
            status_code=401,
            detail="Not authorized. Use /auth/login endpoint."
        )
    if info[1]:
        raise HTTPException(
            status_code=403,
            detail="You haven't rights to get all resume"
        )
    try:
        result = await get_resumes(info[0], session)
        return {"resumes": result}
    except Exception:
        raise HTTPException(status_code=400)
    

@router.post("/")
async def create_resume(resume_data: ResumeCreate, session: AsyncSession = Depends(get_async_session), token: HTTPAuthorizationCredentials = Security(bearer)):
    info = read_token(token)
    if info is None:
        raise HTTPException(
            status_code=401,
            detail="Not authorized"
        )
    if info[1]:
        raise HTTPException(
            status_code=403,
            detail="You haven't rights to create resume"
        )
    try:
        await new_resume(info[0], resume_data, session)
    except Exception:
        raise HTTPException(status_code=400)