from pydantic import BaseModel


class DatabaseGetCitiesParams(BaseModel):
    country_id: int = None
    region_id: int = None
    q: str = None
    need_all: bool = None
    offset: int = None
    count: int = None


class DatabaseGetCitiesByIdParams(BaseModel):
    city_ids: str = None


class DatabaseGetCountriesByIdParams(BaseModel):
    country_ids: str = None


class DatabaseGetMetroStationsByIdParams(BaseModel):
    station_ids: str = None


