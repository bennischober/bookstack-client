"""Bookshelf models for BookStack API."""

from datetime import datetime
from pydantic import BaseModel
from .base import User, Tag, Cover
from .books import ShelfBook


class ShelfListItem(BaseModel):
    """Bookshelf list item representation."""
    id: int
    name: str
    slug: str
    description: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int
    owned_by: int
    cover: Cover | None = None


class ShelfDetail(BaseModel):
    """Detailed bookshelf representation."""
    id: int
    name: str
    slug: str
    description: str
    description_html: str
    created_by: User
    updated_by: User
    owned_by: User
    created_at: datetime
    updated_at: datetime
    tags: list[Tag]
    cover: Cover | None = None
    books: list[ShelfBook]


class ShelfCreate(BaseModel):
    """Model for creating a new bookshelf."""
    name: str
    description: str | None = None
    description_html: str | None = None
    books: list[int] | None = None
    tags: list[Tag] | None = None


class ShelfUpdate(BaseModel):
    """Model for updating a bookshelf."""
    name: str | None = None
    description: str | None = None
    description_html: str | None = None
    books: list[int] | None = None
    tags: list[Tag] | None = None


class ShelfResponse(BaseModel):
    """Response model for shelf operations."""
    id: int
    name: str
    slug: str
    description: str
    created_by: int
    updated_by: int
    created_at: datetime
    updated_at: datetime
    owned_by: int
    description_html: str
    tags: list[Tag]
    cover: Cover | None = None
