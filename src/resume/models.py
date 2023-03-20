from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import ENUM
from datetime import datetime

metadata = MetaData()

# Город проживания.
region = Table(
    "region",
    metadata,
    Column("geo_id", Integer, primary_key=True, autoincrement=True),
    Column("geoname", String(100), nullable=False)
)

# График работы.
# work_shedule = Table(
#     "work_schedule",
#     metadata,
#     Column("type_id", Integer, autoincrement=True, primary_key=True),
#     Column("schedule", String, nullable=False)
# )

# Отрасль/сфера работы.
# industry = Table(
#     "industry",
#     metadata,
#     Column("industry_id", Integer, primary_key=True, autoincrement=True),
#     Column("industry_name", String, nullable=False)
# )

# Специализация
specialization = Table(
    "specialization",
    metadata,
    Column("spec_id", Integer, primary_key=True, autoincrement=True),
    Column("spec_name", String, nullable=False)
)

# Skills
skills = Table(
    "skills",
    metadata,
    Column("skill_id", Integer, primary_key=True, autoincrement=True),
    Column("skill_name", String, nullable=False)
)

# Тип занятости
# employment_type = Table(
#     "employment_type",
#     metadata,
#     Column("type_id", Integer, primary_key=True, autoincrement=True),
#     Column("employment", String, nullable=False)
# )

# Тип компании
# company_type = Table(
#     "company_type",
#     metadata,
#     Column("type_id", Integer, primary_key=True, autoincrement=True),
#     Column("company_type", String, nullable=False)
# )

# Квалификация
# qualification = Table(
#     "qualification",
#     metadata,
#     Column("type_id", Integer, primary_key=True, autoincrement=True),
#     Column("qual_type", String, nullable=False)
# )

# Анкета.
resume = Table(
    "resume",
    metadata,
    Column("resume_id", Integer, primary_key=True, autoincrement=True),
    Column("region", Integer, ForeignKey("region.geo_id"), nullable=False),
    Column("schedule", ENUM('full time', 'epoch', 'flexible', 'part-time', 'remote', 'shift', name="schedule_enum")),
    Column("lower_salary", Integer),
    Column("upper_salary", Integer),
    Column("industry", ENUM('IT','Finance','Electronics','Industrial','Telecommunications','Business','Education',\
                            name="industry_enum"), nullable=False),
    Column("specialization", Integer, ForeignKey("specialization.spec_id"), nullable=False),
    Column("experience_years", Integer, nullable=False),
    Column("is_disabled", Boolean, default=False),
    Column("employment", ENUM('full', 'partial', 'internship', name="emloyment_enum")),
    Column("company_type", ENUM('startup','gov','accredited','commercialized', name="company_enum")),
    Column("qualification", ENUM('intern','junior','middle','senior','lead', name="qual_enum"), nullable=False),
    Column("about", String, nullable=False),
    Column("experience", String, nullable=False),
    Column("education", String, nullable=False),
    Column("phone", String(11)),
    Column("telegram", String(33)),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("updated_at", TIMESTAMP, default=datetime.utcnow),
)
# Column("employment", Integer, ForeignKey("employment_type.type_id")),
# Column("company_type", Integer, ForeignKey("company_type.type_id")),
# Column("qualification", Integer, ForeignKey("qualification.type_id"), nullable=False),
# Column("schedule", Integer, ForeignKey("work_schedule.type_id")),
# Column("industry", Integer, ForeignKey("industry.industry_id"), nullable=False),

know_skills = Table(
    "know_skills",
    metadata,
    Column("resume", Integer, ForeignKey("resume.resume_id")),
    Column("skill", Integer, ForeignKey("skills.skill_id"))
)