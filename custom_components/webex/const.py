"""Constants for the Webex integration."""

from datetime import timedelta

DOMAIN = "webex"

# OAuth2 URLs
OAUTH2_AUTHORIZE = "https://webexapis.com/v1/authorize"
OAUTH2_TOKEN = "https://webexapis.com/v1/access_token"

# OAuth2 Scopes
OAUTH2_SCOPES = ["spark:people_read"]

# API URLs
API_BASE_URL = "https://webexapis.com/v1"
API_PEOPLE_ME = f"{API_BASE_URL}/people/me"

# Update interval
UPDATE_INTERVAL = timedelta(seconds=30)

# Status values
STATUS_ACTIVE = "active"
STATUS_CALL = "call"
STATUS_DND = "DoNotDisturb"
STATUS_INACTIVE = "inactive"
STATUS_MEETING = "meeting"
STATUS_OOO = "OutOfOffice"
STATUS_PENDING = "pending"
STATUS_PRESENTING = "presenting"
STATUS_UNKNOWN = "unknown"
