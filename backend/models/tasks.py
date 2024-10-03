from pydantic import BaseModel
from typing import List, Optional

# Pydantic model for tasks validation


class Task(BaseModel):
    id: Optional[int]
    title: str
    description: Optional[str]
    completed: bool = False
