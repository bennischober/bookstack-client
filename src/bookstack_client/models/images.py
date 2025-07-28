"""Image gallery models."""

from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field
from .base import User


class ImageThumbs(BaseModel):
    """Thumbnail URLs for an image."""
    gallery: str
    display: str


class ImageContent(BaseModel):
    """HTML and Markdown content for embedding the image."""
    html: str
    markdown: str


class ImageBase(BaseModel):
    """Base fields for images."""
    id: int
    name: str
    url: str
    path: str
    type: Literal["gallery", "drawio"]
    uploaded_to: int
    created_by: int
    updated_by: int
    created_at: datetime
    updated_at: datetime


class ImageListItem(ImageBase):
    """Image as returned in list responses."""
    pass


class ImageDetail(ImageBase):
    """Detailed image with user objects and content."""
    created_by: User
    updated_by: User
    thumbs: ImageThumbs
    content: ImageContent


class ImageCreate(BaseModel):
    """Data for creating a new image."""
    type: Literal["gallery", "drawio"] = "gallery"
    uploaded_to: int
    image: bytes = Field(description="Image file content")
    name: str | None = Field(None, max_length=180)


class ImageUpdate(BaseModel):
    """Data for updating an image."""
    name: str | None = Field(None, max_length=180)
    image: bytes | None = Field(None, description="New image file content")
