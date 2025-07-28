"""API response wrapper models."""

from typing import Generic, TypeVar, Any
from pydantic import BaseModel, Field
from .chapters import ChapterListItem
from .images import ImageListItem
from .attachments import AttachmentListItem
from .pages import PageListItem
from .books import BookListItem
from .search import SearchResultItem
from .shelves import ShelfListItem
from .users import UserListItem
from .roles import RoleListItem
from .recycle_bin import RecycleBinItem
from .audit_log import AuditLogItem

T = TypeVar('T')


class PaginatedResponse(BaseModel, Generic[T]):
    """Standard paginated response from BookStack API."""
    data: list[T]
    total: int


class ErrorDetail(BaseModel):
    """Error details in API responses."""
    code: str | None = None
    message: str
    details: dict[str, Any] | None = None


class ValidationError(BaseModel):
    """Validation error response."""
    message: str
    errors: dict[str, list[str]] = Field(default_factory=dict)


# Commonly used response types
BookListResponse = PaginatedResponse[BookListItem]
ChapterListResponse = PaginatedResponse[ChapterListItem]
PageListResponse = PaginatedResponse[PageListItem]
AttachmentListResponse = PaginatedResponse[AttachmentListItem]
ImageListResponse = PaginatedResponse[ImageListItem]
SearchResponse = PaginatedResponse[SearchResultItem]
ShelfListResponse = PaginatedResponse[ShelfListItem]
UserListResponse = PaginatedResponse[UserListItem]
RoleListResponse = PaginatedResponse[RoleListItem]
RecycleBinResponse = PaginatedResponse[RecycleBinItem]
AuditLogResponse = PaginatedResponse[AuditLogItem]
