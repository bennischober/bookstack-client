"""Book-related models."""

from datetime import datetime
from pydantic import BaseModel, Field
from .base import User, Tag, Cover


class BookContentPage(BaseModel):
    """A page within a book chapter."""
    id: int
    name: str
    slug: str
    book_id: int
    chapter_id: int
    draft: bool
    template: bool
    created_at: datetime
    updated_at: datetime
    url: str


class BookContentItem(BaseModel):
    """An item in a book's contents (chapter or page)."""
    id: int
    name: str
    slug: str
    book_id: int
    created_at: datetime
    updated_at: datetime
    url: str
    type: str  # "chapter" or "page"

    # Only present for chapters
    pages: list[BookContentPage] = Field(default_factory=list)

    # Only present for pages
    chapter_id: int | None = None
    draft: bool | None = None
    template: bool | None = None


class BookListItem(BaseModel):
    """Book as returned in list responses."""
    id: int
    name: str
    slug: str
    description: str | None = None
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int
    owned_by: int
    cover: Cover | None = None


class BookDetail(BaseModel):
    """Detailed book with full user objects and contents."""
    id: int
    name: str
    slug: str
    description: str | None = None
    description_html: str | None = None
    created_at: datetime
    updated_at: datetime
    created_by: User
    updated_by: User
    owned_by: User
    contents: list[BookContentItem] = Field(default_factory=list)
    tags: list[Tag] = Field(default_factory=list)
    cover: Cover | None = None
    default_template_id: int | None = None


class BookCreate(BaseModel):
    """Data for creating a new book."""
    name: str = Field(max_length=255)
    description: str | None = Field(None, max_length=1900)
    description_html: str | None = Field(None, max_length=2000)
    tags: list[Tag] = Field(default_factory=list)
    image: bytes | None = Field(None, description="Cover image file")
    default_template_id: int | None = None


class BookUpdate(BaseModel):
    """Data for updating a book."""
    name: str | None = Field(None, min_length=1, max_length=255)
    description: str | None = Field(None, max_length=1900)
    description_html: str | None = Field(None, max_length=2000)
    tags: list[Tag] | None = None
    image: bytes | None = Field(None, description="Cover image file")
    default_template_id: int | None = None


# For shelf-related book references
class ShelfBook(BaseModel):
    """Book reference within a shelf."""
    id: int
    name: str
    slug: str
    description: str | None = None
    created_at: datetime
    updated_at: datetime
    created_by: int | None = None
    updated_by: int | None = None
    owned_by: int | None = None
