"""User models for BookStack API."""

from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserRole(BaseModel):
    """Role information for users."""
    id: int
    display_name: str


class UserListItem(BaseModel):
    """User list item representation."""
    id: int
    name: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime
    external_auth_id: str
    slug: str
    last_activity_at: datetime | None = None
    profile_url: str
    edit_url: str
    avatar_url: str


class UserDetail(BaseModel):
    """Detailed user representation."""
    id: int
    name: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime
    external_auth_id: str
    slug: str
    last_activity_at: datetime | None = None
    profile_url: str
    edit_url: str
    avatar_url: str
    roles: list[UserRole]


class UserCreate(BaseModel):
    """Model for creating a new user."""
    name: str
    email: EmailStr
    external_auth_id: str | None = None
    language: str | None = None
    password: str | None = None
    roles: list[int] | None = None
    send_invite: bool | None = None


class UserUpdate(BaseModel):
    """Model for updating a user."""
    name: str | None = None
    email: EmailStr | None = None
    external_auth_id: str | None = None
    language: str | None = None
    password: str | None = None
    roles: list[int] | None = None


class UserDelete(BaseModel):
    """Model for deleting a user."""
    migrate_ownership_id: int | None = None
