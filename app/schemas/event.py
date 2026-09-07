from datetime import datetime
import re
from enum import Enum

from pydantic import BaseModel, Field, field_validator


class EventType(str, Enum):
    POTHOLE = "pothole"
    WATERLOGGING = "waterlogging"
    HIT_AND_RUN = "hit_and_run"


class DetectionEvent(BaseModel):
    id: str
    type: EventType

    lat: float = Field(ge=-90, le=90)
    lng: float = Field(ge=-180, le=180)

    confidence: float = Field(ge=0, le=1)
    timestamp: datetime

    busId: str
    routeId: str

    @field_validator("busId")
    @classmethod
    def validate_bus_id(cls, value: str) -> str:
        value = value.strip().upper()

        if not value:
            raise ValueError("busId cannot be empty")

        return value