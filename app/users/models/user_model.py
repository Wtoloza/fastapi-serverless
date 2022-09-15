from enum import Enum
from datetime import date

from pydantic import EmailStr
from sqlmodel import Field

from app.core.models import Auditor

class DocumentType(Enum):
  CC: str = "CC" # Cédula de ciudadanía
  TI: str = "TI" # Tarjeta de identidad
  CE: str = "CE" # Cédula de extrangería

class User(Auditor):
  first_name: str = Field(..., max_length=50)
  second_name: str | None = Field(None, max_length=50)
  first_last_name: str = Field(..., max_length=50)
  second_last_name: str | None = Field(None, max_length=50)
  document_type: DocumentType = Field(DocumentType.CC, max_length=2)
  document_number: int = Field(..., max_length=20)
  birth_date: date | None = Field(None)
  email: EmailStr | None = Field(None)
  phone_number: int | None = Field(None, max_length=12)
