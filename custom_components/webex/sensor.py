"""Sensor platform for Webex integration."""

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import WebexDataUpdateCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Webex sensor from a config entry."""
    coordinator: WebexDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([WebexStatusSensor(coordinator, entry)])


class WebexStatusSensor(CoordinatorEntity[WebexDataUpdateCoordinator], SensorEntity):
    """Sensor representing the Webex user status."""

    _attr_has_entity_name = True
    _attr_name = "Status"
    _attr_icon = "mdi:account-circle"

    def __init__(
        self,
        coordinator: WebexDataUpdateCoordinator,
        entry: ConfigEntry,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._attr_unique_id = f"{entry.entry_id}_status"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry.entry_id)},
            "name": "Webex",
            "manufacturer": "Cisco",
        }

    @property
    def native_value(self) -> str | None:
        """Return the current status."""
        if self.coordinator.data:
            return self.coordinator.data.get("status")
        return None

    @property
    def extra_state_attributes(self) -> dict[str, str] | None:
        """Return additional state attributes."""
        if not self.coordinator.data:
            return None

        attrs = {}
        if display_name := self.coordinator.data.get("displayName"):
            attrs["display_name"] = display_name
        if last_activity := self.coordinator.data.get("lastActivity"):
            attrs["last_activity"] = last_activity

        return attrs if attrs else None
