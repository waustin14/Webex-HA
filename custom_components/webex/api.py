"""API client for Webex."""

from typing import Any

from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session

from .const import API_PEOPLE_ME


class WebexApiError(Exception):
    """Exception for Webex API errors."""


class WebexApiClient:
    """Client for interacting with the Webex API."""

    def __init__(self, session: OAuth2Session) -> None:
        """Initialize the API client."""
        self._session = session

    async def async_get_user_status(self) -> dict[str, Any]:
        """Get the current user's status from /people/me."""
        await self._session.async_ensure_token_valid()

        http_session = async_get_clientsession(self._session.hass)
        headers = {"Authorization": f"Bearer {self._session.token['access_token']}"}

        async with http_session.get(API_PEOPLE_ME, headers=headers) as response:
            if response.status == 401:
                raise WebexApiError("Authentication failed")
            if response.status != 200:
                raise WebexApiError(f"API request failed with status {response.status}")

            return await response.json()
