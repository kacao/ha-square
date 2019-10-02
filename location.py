import asyncio
from .const import *

class Location:

    def __init__(self, business, hass, config_entry):
        self.business = business
        self.hass = hass
        self[CONF_ID] = config_entry[CONF_ID]
        self[CONF_NAME] = config_entry[CONF_NAME]

    @property 
    def id(self):
        return self[CONF_ID]

    @property
    def name(self):
        return self[CONF_NAME]

    @property
    def business(self)
        return self[CONF_BUSINESS]

    @property
    def working_staff(self):
        return self

    @property
    def should_poll(self):
        """If entity should be polled."""
        return False


