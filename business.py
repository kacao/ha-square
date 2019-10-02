import asyncio
import json, locale, datetime
from client import Client
from const import *
from homeassistant.helpers.entity import (
        async_generate_entity_id, Entity
)

class Business(Entity):

    def __init__(self, hass, entity_id, config_entry):
        self.entity_id = entity_id
        self.name = config_entry[CONF_NAME]
        self.api_key = config_entry[CONF_API_KEY]
        self.base_url = config_entry[CONF_BASE_URL]
        self.client = Client(config_entry[CONF_API_KEY])
        self.state = {
            name: self.name,
            locations: {},
            employees: {},
            open_shifts: {},
            sales: {}
        }
    
    async def _update_all(self):
        await self._update_locations()
        await self._update_employees()
        await self._update_open_shifts()
        await self._update_sales()
        await self._update_ha_state()

    @property state(self):
        return self.state

    @property
    def should_poll(self):
        """If entity should be polled."""
        return False

    def make_url(self, end_point):
        return self.base_url + end_point

    async def _update_employees(self):
        """ refresh employees 
            TODO: cursor when employees are more than 100 """
        url = make_url(CONF_ENDPOINT_LIST_EMPLOYEES)
        params = {}
        res = await self.client.get(url, params)
        if res.errors:
            print(res.errors)
            return
        self.employees = {}
        for employee in res.employees:
            self.employees[employee[CONF_ID]] = employee

    async def _update_locations(self):
        """ refresh locations """
        hass = self.hass
        url = make_url(CONF_ENDPOINT_LIST_LOCATIONS)
        params = {}
        res = await self.client.get(url, params)
        if res.errors:
            print(res.errors)
            return
        self.locations = {}
        for location in res.locations:
            self.locations[location.id] = location

    async def _update_open_shifts(self):
        """ refresh time cards """
        today = datetime.date.today()
        url = make_url(CONF_ENDPOINT_LIST_SHIFTS)
        payloads = {
            "query": {
                "filter": {
                    "status": "OPEN"
                }
            }
        }

        res = await client.post(url, payloads)
        if res.errors:
            print(res.errors)
            return

        location.shifts = {}
        for shift in res.shifts:
            location = self.locations[shift[CONF_LOCATION_ID]] 
            shift[CONF_EMPLOYEE] = self.employees[CONF_EMPLOYEE_ID] 
            location.append(shift)

    async def _update_sales(self):

    async def update_locations(self):
        await self._update_locations
        await self.async_update_ha_state()

    async def update_employees(self):
        await self._update_employees
        await self.async_update_ha_state()

    async def update_open_shifts(self):
        await self._update_open_shifts
        await self.async_update_ha_state()

    async def update_sales(self):
        await self._update_sales

    async def _update_ha_state():
        await self.async_update_ha_state()
