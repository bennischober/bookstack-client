"""Attachment-related models."""

from datetime import datetime
from pydantic import BaseModel, Field
from .base import User, Links


class AttachmentBase(BaseModel):
    """Base fields for attachments."""
    id: int
    name: str
    extension: str
    uploaded_to: int
    external: bool
    order: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int


class AttachmentListItem(AttachmentBase):
    """Attachment as returned in list responses."""
    pass


class AttachmentDetail(AttachmentBase):
    """Detailed attachment with full user objects and content."""
    created_by: User
    updated_by: User
    links: Links
    content: str  # URL for links, base64 for files


class AttachmentCreate(BaseModel):
    """Data for creating a new attachment."""
    name: str = Field(min_length=1, max_length=255)
    uploaded_to: int
    file: bytes | None = Field(
        None, description="File content for file uploads")
    link: str | None = Field(None, min_length=1, max_length=2000)

    model_config = {
        "json_schema_extra": {
            "description": "Either 'file' or 'link' must be provided, but not both"
        }
    }


class AttachmentUpdate(BaseModel):
    """Data for updating an attachment."""
    name: str | None = Field(None, min_length=1, max_length=255)
    uploaded_to: int | None = None
    file: bytes | None = None
    link: str | None = Field(None, min_length=1, max_length=2000)
