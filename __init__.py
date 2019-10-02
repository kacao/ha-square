import logging
from datetime import timedelta
from typing import Optional, Text

import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (
        CONF_ENTITY_ID,
)
from homeassistant.helpers.entity import (
        async_generate_entity_id, Entity
)
from homeassistant.helpers.entity_component import EntityComponent
from homeassistant.helpers.config_validation import ENTITY_SERVICE_SCHEMA


import homeassistant.helpers.config_validation as cv
from client import Client
from const import *
from location import Location
from business import Business

VERSION = 1.0
DOMAIN = "square"
ENTITY_ID_FORMAT = DOMAIN + '.{}'

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Optional(CONF_BUSINESSES): vol.All(cv.ensure_list, [CONFIG_BUSINESS]),
    )}
), extra=vol.ALLOW_EXTRA}

BUSINESS_SCHEMA = volSchema({
    vol.Required(CONF_NAME): cv.string,
    vol.Required(CONF_API_KEY): cv.string,
    vol.Required(CONF_BASE_URL): cv.string,
    vol.Required(CONF_OPEN): int,
    vol.Required(CONF_CLOSE): int,
)}

LOCATION_SCHEMA = vol.Schema({
    LOCATION: vol.Schema({
        vol.Required(CONF_ID): cv.string,
        vol.Required(CONF_NAME): cv.string,
    }),
})

SERVICE_UPDATE_LOCATIONS = 'update_locations'
SERVICE_UPDATE_EMPLOYEES = 'update_employees'
SERVICE_UPDATE_OPEN_SHIFTS = 'update_open_shifts'
SERVICE_UPDATE_SALES = 'update_sales'

def async_setup(hass, config, discovery_info=None):

    component = EntityComponent(_LOGGER, DOMAIN, hass)
    await component.async_setup(config)
    config = config[DOMAIN]
    entities = []

    for business_id, business_entry in config[CONF_BUSINESSES].items():
    
        business = Business(hass, business_id, business_entry)
        entities.append(business)

    component.async_register_entity_service(
        SERVICE_UPDATE_LOCATIONS, ENTITY_SERVICE_SCHEMA,
        'update_locations'
    )

    component.async_register_entity_service(
        SERVICE_UPDATE_EMPLOYEES, ENTITY_SERVICE_SCHEMA,
        'update_employees'
    )
    component.async_register_entity_service(
        SERVICE_UPDATE_OPEN_SHIFTS, ENTITY_SERVICE_SCHEMA,
        'update_open_shifts'
    )

    component.async_register_entity_service(
        SERVICE_UPDATE_SALES, ENTITY_SERVICE_SCHEMA,
        'update_sales'
    )

    await component.async_add_entities(entities)

