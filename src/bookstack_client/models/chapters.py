"""Chapter-related models."""

from datetime import datetime
from pydantic import BaseModel, Field
from .base import User, Tag


class ChapterPage(BaseModel):
    """A page within a chapter."""
    id: int
    book_id: int
    chapter_id: int
    name: str
    slug: str
    priority: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int
    owned_by: int
    draft: bool
    revision_count: int
    template: bool
    editor: str | None = None
    book_slug: str


class ChapterListItem(BaseModel):
    """Chapter as returned in list responses."""
    id: int
    book_id: int
    name: str
    slug: str
    description: str | None = None
    priority: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int
    owned_by: int
    book_slug: str


class ChapterDetail(BaseModel):
    """Detailed chapter with full user objects and pages."""
    id: int
    book_id: int
    slug: str
    name: str
    description: str | None = None
    description_html: str | None = None
    priority: int
    created_at: datetime
    updated_at: datetime
    created_by: User
    updated_by: User
    owned_by: User
    book_slug: str
    tags: list[Tag] = Field(default_factory=list)
    pages: list[ChapterPage] = Field(default_factory=list)
    default_template_id: int | None = None


class ChapterCreate(BaseModel):
    """Data for creating a new chapter."""
    book_id: int
    name: str = Field(max_length=255)
    description: str | None = Field(None, max_length=1900)
    description_html: str | None = Field(None, max_length=2000)
    tags: list[Tag] = Field(default_factory=list)
    priority: int | None = None
    default_template_id: int | None = None


class ChapterUpdate(BaseModel):
    """Data for updating a chapter."""
    book_id: int | None = None  # Can move chapter to different book
    name: str | None = Field(None, min_length=1, max_length=255)
    description: str | None = Field(None, max_length=1900)
    description_html: str | None = Field(None, max_length=2000)
    tags: list[Tag] | None = None
    priority: int | None = None
    default_template_id: int | None = None
