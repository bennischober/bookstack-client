"""Base models shared across BookStack entities."""

from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class User(BaseModel):
    """Represents a user in BookStack."""
    id: int
    name: str
    slug: str


class Tag(BaseModel):
    """Represents a tag that can be attached to entities."""
    name: str
    value: str
    order: int


class Cover(BaseModel):
    """Represents a cover image for books/shelves."""
    id: int
    name: str
    url: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int
    path: str
    type: str
    uploaded_to: int


class Links(BaseModel):
    """HTML and Markdown link representations."""
    html: str
    markdown: str


# Export format type
ExportFormat = Literal["markdown", "html", "pdf", "plain-text", "plaintext"]
