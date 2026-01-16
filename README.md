# Webex Home Assistant Integration

A Home Assistant custom integration that connects to Cisco Webex to monitor your user status. Track your Webex presence, display name, and last activity directly in Home Assistant.

## Features

- Real-time Webex status monitoring
- OAuth2 authentication
- Displays user status (active, meeting, call, DND, etc.)
- Additional attributes including display name and last activity
- Updates every 30 seconds
- Secure credential management through Home Assistant's Application Credentials system

## Prerequisites

- Home Assistant 2026.1 or newer
- A Webex account
- A Webex integration created in the Webex Developer Portal

## Setting Up a Webex Integration in the Developer Portal

Before you can use this integration, you need to create an OAuth2 integration in the Webex Developer Portal.

### Step 1: Create a New Integration

1. Go to the [Webex Developer Portal](https://developer.webex.com/)
2. Sign in with your Webex account
3. Click on your profile icon in the top right and select **My Webex Apps**
4. Click **Create a New App**
5. Select **Create an Integration**

### Step 2: Configure Your Integration

Fill in the integration details:

1. **Integration Name**: Choose a name (e.g., "Home Assistant Webex")
2. **Icon**: Upload an icon or use the default
3. **Description**: Add a description (e.g., "Home Assistant integration for Webex status monitoring")
4. **Redirect URI(s)**: Add the standard Home Assistant callback URL:
   ```
   https://my.home-assistant.io/redirect/oauth
   ```

   This will redirect you to a common Home Assistant page where you can enter your Home Assistant instance's specific URL.

5. **Scopes**: Select the following scope:
   - `spark:people_read` - Required to read user profile and status information

### Step 3: Save Your Credentials

After creating the integration, you'll be shown:
- **Client ID** - A long alphanumeric string
- **Client Secret** - A secret key (only shown once, so save it securely!)

**Important**: Copy both the Client ID and Client Secret immediately. The Client Secret will not be shown again. If you lose it, you'll need to regenerate it.

## Installation

### HACS Installation (Recommended)

1. Open HACS in your Home Assistant instance
2. Click on "Integrations"
3. Click the three dots in the top right and select "Custom repositories"
4. Add this repository URL: `https://github.com/waustin14/Webex-HA`
5. Select category "Integration"
6. Click "Add"
7. Find "Webex" in the list and click "Download"
8. Restart Home Assistant

### Manual Installation

1. Copy the `custom_components/webex` folder to your Home Assistant `config/custom_components/` directory
2. Restart Home Assistant

## Configuration

### Step 1: Add Application Credentials

1. In Home Assistant, go to **Settings** → **Devices & Services**
2. Click **Application Credentials** (in the top tabs)
3. Click **Add Application Credential**
4. Select **Webex** from the dropdown
5. Enter your **Client ID** and **Client Secret** from the Webex Developer Portal
6. Click **Add**

### Step 2: Add the Integration

1. Go to **Settings** → **Devices & Services**
2. Click **Add Integration**
3. Search for **Webex**
4. Click on **Webex**
5. You'll be redirected to Webex to authorize the integration
6. Sign in to your Webex account if prompted
7. Click **Accept** to authorize Home Assistant to access your Webex status
8. You'll be redirected back to Home Assistant

The integration will now be configured and a new device will be added.

## Entities

The integration creates the following entity:

### Webex Status Sensor

- **Entity ID**: `sensor.webex_status`
- **State**: Current Webex status
  - `active` - User is active
  - `call` - User is on a call
  - `DoNotDisturb` - User has DND enabled
  - `inactive` - User is inactive
  - `meeting` - User is in a meeting
  - `OutOfOffice` - User is out of office
  - `pending` - Status is pending
  - `presenting` - User is presenting
  - `unknown` - Status cannot be determined

- **Attributes**:
  - `display_name` - Your Webex display name
  - `last_activity` - Timestamp of last activity

## Usage Examples

### Automation Example

Trigger actions based on your Webex status:

```yaml
automation:
  - alias: "Turn on busy light when in Webex meeting"
    trigger:
      - platform: state
        entity_id: sensor.webex_status
        to: "meeting"
    action:
      - service: light.turn_on
        target:
          entity_id: light.office_busy_light
        data:
          color_name: red
          brightness: 255

  - alias: "Turn off busy light when meeting ends"
    trigger:
      - platform: state
        entity_id: sensor.webex_status
        from: "meeting"
    action:
      - service: light.turn_off
        target:
          entity_id: light.office_busy_light
```

### Lovelace Card Example

Display your Webex status in the UI:

```yaml
type: entity
entity: sensor.webex_status
name: My Webex Status
icon: mdi:video-account
```

## Troubleshooting

### Authentication Failed

- Verify your Client ID and Client Secret are correct
- Ensure the Redirect URI in the Webex Developer Portal exactly matches your Home Assistant external URL
- Make sure you're using HTTPS for cloud instances

### Integration Not Found

- Verify the integration files are in `config/custom_components/webex/`
- Restart Home Assistant
- Check the Home Assistant logs for errors

### Status Not Updating

- Check your internet connection
- Verify the OAuth token hasn't expired (the integration should auto-refresh)
- Check Home Assistant logs for API errors
- Ensure the `spark:people_read` scope was granted

### Redirect URI Mismatch

If you see a "redirect_uri_mismatch" error:
1. Go to your Webex integration in the Developer Portal
2. Verify the Redirect URI exactly matches: `https://my.home-assistant.io/redirect/oauth`
3. Remove and re-add the integration in Home Assistant

## Support

For issues, feature requests, or contributions:
- GitHub Issues: [https://github.com/waustin14/Webex-HA/issues](https://github.com/waustin14/Webex-HA/issues)
- Home Assistant Community: [https://community.home-assistant.io/](https://community.home-assistant.io/)

## License

This integration is provided as-is under the MIT License.

## Credits

Developed for the Home Assistant community to bring Webex presence monitoring to your smart home.
