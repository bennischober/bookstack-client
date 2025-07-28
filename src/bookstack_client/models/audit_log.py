"""Audit log models for BookStack API."""

from datetime import datetime
from typing import Literal
from pydantic import BaseModel
from .base import User


class AuditLogItem(BaseModel):
    """Audit log entry representation."""
    id: int
    # Could be many different event types like 'bookshelf_create', 'auth_login', etc.
    type: str
    detail: str
    user_id: int
    loggable_id: int | None = None
    loggable_type: Literal["bookshelf", "book",
                           "chapter", "page"] | None = None
    ip: str
    created_at: datetime
    user: User
