"""BookStack client models."""

# Base models
from .base import User, Tag, Cover, Links, ExportFormat

# Book models
from .books import (
    BookListItem,
    BookDetail,
    BookCreate,
    BookUpdate,
    BookContentItem,
    BookContentPage,
    ShelfBook,
)

# Chapter models
from .chapters import (
    ChapterListItem,
    ChapterDetail,
    ChapterCreate,
    ChapterUpdate,
    ChapterPage,
)

# Page models
from .pages import (
    PageListItem,
    PageDetail,
    PageCreate,
    PageUpdate,
)

# Attachment models
from .attachments import (
    AttachmentListItem,
    AttachmentDetail,
    AttachmentCreate,
    AttachmentUpdate,
)

# Image models
from .images import (
    ImageListItem,
    ImageDetail,
    ImageCreate,
    ImageUpdate,
    ImageThumbs,
    ImageContent,
)

# Search models
from .search import (
    SearchResultItem,
    SearchPreviewHtml,
    SearchResultBook,
    SearchResultChapter,
    SearchResponse,
    SearchRequest,
)

# Shelf models
from .shelves import (
    ShelfListItem,
    ShelfDetail,
    ShelfCreate,
    ShelfUpdate,
    ShelfResponse,
)

# User models
from .users import (
    UserListItem,
    UserDetail,
    UserCreate,
    UserUpdate,
    UserDelete,
    UserRole,
)

# Role models
from .roles import (
    RoleListItem,
    RoleDetail,
    RoleCreate,
    RoleUpdate,
    RoleResponse,
    RoleUser,
)

# Recycle bin models
from .recycle_bin import (
    RecycleBinItem,
    DeletablePage,
    DeletableBook,
    DeletableChapter,
    DeletableBookshelf,
    DeletableParent,
    RecycleBinRestoreResponse,
    RecycleBinDestroyResponse,
)

# Permission models
from .permissions import (
    ContentPermissions,
    ContentPermissionsUpdate,
    RolePermission,
    RolePermissionUpdate,
    FallbackPermissions,
    FallbackPermissionsUpdate,
    PermissionRole,
)

# Audit log models
from .audit_log import (
    AuditLogItem,
    AuditLogUser,
)

# Response models
from .responses import (
    PaginatedResponse,
    ErrorDetail,
    ValidationError,
    BookListResponse,
    ChapterListResponse,
    PageListResponse,
    AttachmentListResponse,
    ImageListResponse,
)

__all__ = [
    # Base
    "User",
    "Tag",
    "Cover",
    "Links",
    "ExportFormat",

    # Books
    "BookListItem",
    "BookDetail",
    "BookCreate",
    "BookUpdate",
    "BookContentItem",
    "BookContentPage",
    "ShelfBook",

    # Chapters
    "ChapterListItem",
    "ChapterDetail",
    "ChapterCreate",
    "ChapterUpdate",
    "ChapterPage",

    # Pages
    "PageListItem",
    "PageDetail",
    "PageCreate",
    "PageUpdate",

    # Attachments
    "AttachmentListItem",
    "AttachmentDetail",
    "AttachmentCreate",
    "AttachmentUpdate",

    # Images
    "ImageListItem",
    "ImageDetail",
    "ImageCreate",
    "ImageUpdate",
    "ImageThumbs",
    "ImageContent",

    # Search
    "SearchResultItem",
    "SearchPreviewHtml",
    "SearchResultBook",
    "SearchResultChapter",
    "SearchResponse",
    "SearchRequest",

    # Shelves
    "ShelfListItem",
    "ShelfDetail",
    "ShelfCreate",
    "ShelfUpdate",
    "ShelfResponse",

    # Users
    "UserListItem",
    "UserDetail",
    "UserCreate",
    "UserUpdate",
    "UserDelete",
    "UserRole",

    # Roles
    "RoleListItem",
    "RoleDetail",
    "RoleCreate",
    "RoleUpdate",
    "RoleResponse",
    "RoleUser",

    # Recycle Bin
    "RecycleBinItem",
    "DeletablePage",
    "DeletableBook",
    "DeletableChapter",
    "DeletableBookshelf",
    "DeletableParent",
    "RecycleBinRestoreResponse",
    "RecycleBinDestroyResponse",

    # Permissions
    "ContentPermissions",
    "ContentPermissionsUpdate",
    "RolePermission",
    "RolePermissionUpdate",
    "FallbackPermissions",
    "FallbackPermissionsUpdate",
    "PermissionRole",

    # Audit Log
    "AuditLogItem",
    "AuditLogUser",

    # Responses
    "PaginatedResponse",
    "ErrorDetail",
    "ValidationError",
    "BookListResponse",
    "ChapterListResponse",
    "PageListResponse",
    "AttachmentListResponse",
    "ImageListResponse",
]
