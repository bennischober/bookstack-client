"""Recycle bin models for BookStack API."""

from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class DeletableParent(BaseModel):
    """Parent item information for deletable items."""
    id: int
    name: str
    slug: str
    description: str | None = None
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int
    owned_by: int
    type: Literal["book", "bookshelf"]


class DeletablePage(BaseModel):
    """Deletable page representation."""
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
    draft: bool
    revision_count: int
    template: bool
    owned_by: int
    editor: str
    book_slug: str
    parent: DeletableParent


class DeletableBook(BaseModel):
    """Deletable book representation."""
    id: int
    name: str
    slug: str
    description: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int
    owned_by: int
    pages_count: int
    chapters_count: int


class DeletableChapter(BaseModel):
    """Deletable chapter representation."""
    id: int
    book_id: int
    name: str
    slug: str
    description: str
    priority: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int
    owned_by: int
    pages_count: int
    parent: DeletableParent


class DeletableBookshelf(BaseModel):
    """Deletable bookshelf representation."""
    id: int
    name: str
    slug: str
    description: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int
    owned_by: int
    books_count: int


class RecycleBinItem(BaseModel):
    """Recycle bin item representation."""
    id: int
    deleted_by: int
    created_at: datetime
    updated_at: datetime
    deletable_type: Literal["page", "book", "chapter", "bookshelf"]
    deletable_id: int
    deletable: DeletablePage | DeletableBook | DeletableChapter | DeletableBookshelf


class RecycleBinRestoreResponse(BaseModel):
    """Response for recycle bin restore operation."""
    restore_count: int


class RecycleBinDestroyResponse(BaseModel):
    """Response for recycle bin destroy operation."""
    delete_count: int
