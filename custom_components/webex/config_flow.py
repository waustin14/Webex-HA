"""Config flow for Webex integration."""

import logging

from homeassistant.config_entries import ConfigFlowResult
from homeassistant.helpers.config_entry_oauth2_flow import AbstractOAuth2FlowHandler

from .const import DOMAIN, OAUTH2_SCOPES

_LOGGER = logging.getLogger(__name__)


class WebexOAuth2FlowHandler(AbstractOAuth2FlowHandler, domain=DOMAIN):
    """Handle a config flow for Webex."""

    DOMAIN = DOMAIN

    @property
    def logger(self) -> logging.Logger:
        """Return logger."""
        return _LOGGER

    @property
    def extra_authorize_data(self) -> dict:
        """Extra data that needs to be appended to the authorize url."""
        return {"scope": " ".join(OAUTH2_SCOPES)}

    async def async_oauth_create_entry(self, data: dict) -> ConfigFlowResult:
        """Create an entry for the flow."""
        return self.async_create_entry(title="Webex", data=data)
