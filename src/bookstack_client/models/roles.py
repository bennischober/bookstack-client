"""Role models for BookStack API."""

from datetime import datetime
from pydantic import BaseModel
from .base import User


class RoleUser(BaseModel):
    """User information in role details."""
    id: int
    name: str
    slug: str


class RoleListItem(BaseModel):
    """Role list item representation."""
    id: int
    display_name: str
    description: str
    created_at: datetime
    updated_at: datetime
    system_name: str
    external_auth_id: str
    mfa_enforced: bool
    users_count: int
    permissions_count: int


class RoleDetail(BaseModel):
    """Detailed role representation."""
    id: int
    display_name: str
    description: str
    created_at: datetime
    updated_at: datetime
    system_name: str
    external_auth_id: str
    mfa_enforced: bool
    permissions: list[str]
    users: list[RoleUser]


class RoleCreate(BaseModel):
    """Model for creating a new role."""
    display_name: str
    description: str | None = None
    mfa_enforced: bool | None = None
    external_auth_id: str | None = None
    permissions: list[str] | None = None


class RoleUpdate(BaseModel):
    """Model for updating a role."""
    display_name: str | None = None
    description: str | None = None
    mfa_enforced: bool | None = None
    external_auth_id: str | None = None
    permissions: list[str] | None = None


class RoleResponse(BaseModel):
    """Response model for role operations."""
    id: int
    display_name: str
    description: str
    created_at: datetime
    updated_at: datetime
    system_name: str
    external_auth_id: str
    mfa_enforced: bool
    permissions: list[str]
    users: list[RoleUser]
