from datetime import datetime

from sqlmodel import Field, SQLModel


class Auditor(SQLModel):
  date_create: datetime = Field(default_factory=datetime.now)
  date_update: datetime = Field(default_factory=datetime.now)
  date_delete: datetime | None = Field(default=None)
