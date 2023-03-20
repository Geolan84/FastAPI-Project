from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel

class schedule_enum(Enum):
    FULLTIME = "full time"
    EPOCH = 'epoch'
    FLEXIBLE = 'flexible'
    PART_TIME = 'part-time'
    REMOTE = 'remote'
    SHIFT = 'shift'

class IndustryEnum(Enum):
    IT = 'IT'
    FINANCE = 'Finance'
    ELECTRONICS = 'Electronics'
    INDUSTRIAL = 'Industrial'
    TELECOM = 'Telecommunications'
    BUSINESS = 'Business'
    EDUCATION = 'Education'

class CompanyEnum(Enum):
    STARTUP = 'startup'
    GOV = 'gov'
    ACCREDIT = 'accredited'
    COMMERCE = 'commercialized'

class EmploymentEnum(Enum):
    FULL = 'full'
    PARTIAL = 'partial'
    INTERN = 'internship'

class QualEnum(Enum):
    INTERN = 'intern'
    JUNIOR = 'junior'
    MIDDLE = 'middle'
    SENIOR = 'senior'
    LEAD = 'lead'
    

class ResumeCreate(BaseModel):
    region: int
    schedule: schedule_enum
    lower_salary: int
    upper_salary: Optional[int]
    industry: IndustryEnum
    specialization: int
    experience_years: int
    is_disabled: bool
    employment: EmploymentEnum
    company_type: CompanyEnum
    qualification: QualEnum
    about: str
    experience: str
    education: str
    phone: Optional[str]
    telegram: Optional[str]
    is_active: bool
    updated_at: Optional[str]