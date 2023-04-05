from sqlalchemy import insert, select
from models import resume
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from resume.schemas import ResumeCreate


async def new_resume(user_id: int, resume_reg: ResumeCreate, session: AsyncSession):  
    data = resume_reg.dict()
    data['user_id'] = user_id
    data['updated_at'] = datetime.now()
    stmt = insert(resume).values(**data)
    await session.execute(stmt)
    await session.commit()

async def get_resumes(user_id: int, session: AsyncSession):
    query = select(resume).where(resume.c.user_id == user_id)
    result = await session.execute(query)
    return result.all()