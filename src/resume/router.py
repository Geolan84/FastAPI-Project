from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from resume.models import resume
from resume.schemas import ResumeCreate

router = APIRouter(
    prefix="/resumes",
    tags=["Resume"]
)


@router.get("/")
async def get_all_resumes(is_active: bool, session: AsyncSession = Depends(get_async_session)):
    query = select(resume).where(resume.c.is_active == is_active)
    result = await session.execute(query)
    #return result.all()
    return {"resumes": result.all()}

@router.post("/")
async def create_resume(new_resume: ResumeCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(resume).values(**new_resume.dict())
    await session.execute(stmt)
    await session.commit()