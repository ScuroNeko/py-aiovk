from py_aiovk.types.params.database import *


class Database:
    def __init__(self, vk):
        self.vk = vk

    async def get_cities(self, params: DatabaseGetCitiesParams):
        return await self.vk.execute('database', 'getCities', **params.model_dump(exclude_none=True))

    async def get_cities_by_id(self, params: DatabaseGetCitiesByIdParams):
        return await self.vk.execute('database', 'getCitiesById', **params.model_dump(exclude_none=True))

    async def get_countries_by_id(self, params: DatabaseGetCountriesByIdParams):
        return await self.vk.execute('database', 'getCountriesById', **params.model_dump(exclude_none=True))

    async def get_metro_stations_by_id(self, params: DatabaseGetMetroStationsByIdParams):
        return await self.vk.execute('database', 'getMetroStationsById', **params.model_dump(exclude_none=True))

