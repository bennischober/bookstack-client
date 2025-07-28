from .base import BaseResource
from ..models.responses import AuditLogResponse


class AuditLogResource(BaseResource):
    """Resource class for handling audit log operations in BookStack API."""

    def list(self, **params) -> AuditLogResponse:
        """Retrieve a list of audit log entries."""
        data = self._get_paginated('/audit-log', **params)
        return AuditLogResponse(data=data, total=len(data))
