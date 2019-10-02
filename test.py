import voluptuous as vol
DOMAIN = "square"
CONF_BUSINESS = "businesses"
CONF_BUSINESS = "business"
CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Optional(CONF_BUSINESSES): vol.All(cv.ensure_list, [CONFIG_BUSINESS]),
    })
}, extra=vol.ALLOW_EXTRA)
