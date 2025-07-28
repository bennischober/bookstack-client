"""Content permissions models for BookStack API."""

from pydantic import BaseModel
from .base import User


class PermissionRole(BaseModel):
    """Role information for permissions."""
    id: int
    display_name: str


class RolePermission(BaseModel):
    """Role-based permission settings."""
    role_id: int
    view: bool
    create: bool
    update: bool
    delete: bool
    role: PermissionRole


class FallbackPermissions(BaseModel):
    """Fallback permission settings."""
    inheriting: bool
    view: bool | None = None
    create: bool | None = None
    update: bool | None = None
    delete: bool | None = None


class ContentPermissions(BaseModel):
    """Content permissions representation."""
    owner: User
    role_permissions: list[RolePermission]
    fallback_permissions: FallbackPermissions


class RolePermissionUpdate(BaseModel):
    """Role permission update model."""
    role_id: int
    view: bool
    create: bool
    update: bool
    delete: bool


class FallbackPermissionsUpdate(BaseModel):
    """Fallback permissions update model."""
    inheriting: bool
    view: bool | None = None
    create: bool | None = None
    update: bool | None = None
    delete: bool | None = None


class ContentPermissionsUpdate(BaseModel):
    """Content permissions update model."""
    owner_id: int | None = None
    role_permissions: list[RolePermissionUpdate] | None = None
    fallback_permissions: FallbackPermissionsUpdate | None = None
