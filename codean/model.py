from typing import Optional

from pydantic import BaseModel, Field

# TODO: This is ugly, o well, just for illustration...
global_id: int = 0


def get_global_id() -> int:
    global global_id
    global_id += 1
    return global_id


class Codemark(BaseModel):
    """
    The codemark annotations. Normally these will come from a database.
    """

    id: int = Field(default_factory=get_global_id)
    path: str
    hash: str

    # Parent/child relations
    # story_id: int # INTERNAL TODO: Do we want to add this complexity
    parent_id: Optional[int] = None
    has_children: bool = False

    # Information
    description: Optional[str] = ""

    # Textual positional
    start_line_number: int
    start_column: int
    end_line_number: int
    end_column: int

    # Problems
    merge_resolved_revision: Optional[str] = None
    merge_conflict_revision: Optional[str] = None
    bereaved_revision: Optional[str] = None
