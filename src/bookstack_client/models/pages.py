"""Page-related models."""

from datetime import datetime
from pydantic import BaseModel, Field
from .base import User, Tag


class PageListItem(BaseModel):
    """Page as returned in list responses."""
    id: int
    book_id: int
    chapter_id: int
    name: str
    slug: str
    priority: int
    draft: bool
    revision_count: int
    template: bool
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int
    owned_by: int
    editor: str
    book_slug: str


class PageDetail(BaseModel):
    """Detailed page with full user objects and content."""
    id: int
    book_id: int
    chapter_id: int
    name: str
    slug: str
    html: str | None = None
    raw_html: str | None = None
    priority: int
    created_at: datetime
    updated_at: datetime
    created_by: User
    updated_by: User
    owned_by: User
    draft: bool
    markdown: str | None = None
    revision_count: int
    template: bool
    editor: str
    tags: list[Tag] = Field(default_factory=list)


class PageCreate(BaseModel):
    """Data for creating a new page."""
    book_id: int | None = Field(
        None, description="Required if chapter_id not provided")
    chapter_id: int | None = Field(
        None, description="Required if book_id not provided")
    name: str = Field(max_length=255)
    html: str | None = Field(
        None, description="Required if markdown not provided")
    markdown: str | None = Field(
        None, description="Required if html not provided")
    tags: list[Tag] = Field(default_factory=list)
    priority: int | None = None

    model_config = {
        "json_schema_extra": {
            "description": "Either book_id or chapter_id must be provided. Either html or markdown must be provided."
        }
    }


class PageUpdate(BaseModel):
    """Data for updating a page."""
    book_id: int | None = None  # Can move page to different book
    chapter_id: int | None = None  # Can move page to different chapter
    name: str | None = Field(None, min_length=1, max_length=255)
    html: str | None = None
    markdown: str | None = None
    tags: list[Tag] | None = None
    priority: int | None = None
