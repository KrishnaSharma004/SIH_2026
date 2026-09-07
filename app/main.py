from fastapi import FastAPI

from app.schemas.event import DetectionEvent
from app.schemas.heatmap import HeatmapPoint


app = FastAPI(
    title="Smart Road Monitoring API",
    description="Backend API for AI-powered road infrastructure monitoring",
    version="1.0.0",
)


# Temporary storage
events: list[DetectionEvent] = []


@app.get("/")
async def root():
    return {
        "message": "Smart Road Monitoring API is running"
    }


@app.post("/api/v1/events")
async def create_event(event: DetectionEvent):

    events.append(event)

    return {
        "success": True,
        "message": "Event accepted",
        "event": event
    }


@app.get("/api/v1/events")
async def get_events():

    return {
        "count": len(events),
        "events": events
    }


@app.get("/api/v1/heatmap", response_model=list[HeatmapPoint])
async def get_heatmap():

    return [
        {
            "lat": 23.2599,
            "lng": 77.4126,
            "weight": 3,
            "type": "pothole"
        },
        {
            "lat": 23.258,
            "lng": 77.4102,
            "weight": 5,
            "type": "pothole"
        }
    ]