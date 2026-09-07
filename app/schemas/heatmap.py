from pydantic import BaseModel,Field
class HeatmapPoint(BaseModel):
    lat:float=Field(ge=-90,le=90)
    lng:float=Field(ge=-180,le=180)
    weight:float=Field(ge=0)
    type:str