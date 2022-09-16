from enum import Enum
from datetime import date

from pydantic import EmailStr
from sqlmodel import SQLModel, Field

from app.core.models import Auditor


class DocumentType(Enum):
    CC: str = "CC"  # Cédula de ciudadanía
    TI: str = "TI"  # Tarjeta de identidad
    CE: str = "CE"  # Cédula de extrangería


class UserAuditor(Auditor):
    is_active: bool = True
    is_valid: bool = False
    is_superuser: bool = False


class UserBase(SQLModel):
    first_name: str = Field(..., max_length=50)
    second_name: str | None = Field(None, max_length=50)
    first_last_name: str = Field(..., max_length=50)
    second_last_name: str | None = Field(None, max_length=50)
    document_type: DocumentType = Field(default=DocumentType.CC)
    document_number: int = Field(..., index=True)
    birth_date: date | None = None
    email: EmailStr | None = None
    phone_number: int | None = None


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    first_name: str = Field(None, max_length=50)
    second_name: str | None = Field(None, max_length=50)
    first_last_name: str = Field(None, max_length=50)
    second_last_name: str | None = Field(None, max_length=50)
    document_type: DocumentType = None
    document_number: int = None
    birth_date: date | None = None
    email: EmailStr | None = None
    phone_number: int | None = None


class User(UserAuditor, UserBase):
    id: str | None = Field(default=None, primary_key=True)


class UserRead(UserBase):
    id: str
