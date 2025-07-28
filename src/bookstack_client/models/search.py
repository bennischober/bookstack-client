"""Search models for BookStack API."""

from datetime import datetime
from typing import Literal
from pydantic import BaseModel
from .base import Tag


class SearchPreviewHtml(BaseModel):
    """Preview HTML for search results."""
    name: str
    content: str


class SearchResultBook(BaseModel):
    """Book information in search results."""
    id: int
    name: str
    slug: str


class SearchResultChapter(BaseModel):
    """Chapter information in search results."""
    id: int
    name: str
    slug: str


class SearchResultItem(BaseModel):
    """Individual search result item."""
    id: int
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    type: Literal["bookshelf", "book", "chapter", "page"]
    url: str
    preview_html: SearchPreviewHtml
    tags: list[Tag]

    # Optional fields based on type
    book_id: int | None = None
    chapter_id: int | None = None
    draft: bool | None = None
    template: bool | None = None
    book: SearchResultBook | None = None
    chapter: SearchResultChapter | None = None
    description: str | None = None  # For bookshelves
    created_by: int | None = None
    updated_by: int | None = None
    owned_by: int | None = None


class SearchResponse(BaseModel):
    """Response for search operations."""
    data: list[SearchResultItem]
    total: int


class SearchRequest(BaseModel):
    """Request parameters for search."""
    query: str
    page: int | None = None
    count: int | None = None
