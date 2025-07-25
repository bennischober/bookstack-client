from pydantic import BaseModel


class User(BaseModel):
    """Defines a user in the BookStack system."""

    id: int
    """The unique identifier for the user."""

    name: str
    """The name of the user."""

    slug: str | None = None
    """The URL-friendly identifier for the user."""
