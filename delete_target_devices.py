import requests
 
# Configuration
api_url = "http://example.com/api/v0"
api_token = "your_token_here"  # Replace with your actual API token
delete_target = "generic"  # Set the OS to target for deletion
 
headers = {
    'X-Auth-Token': api_token
}
 
def get_generic_devices():
    """Fetch devices with Operating System set to the specified deletion target."""
    all_devices = requests.get(f"{api_url}/devices", headers=headers).json()['devices']
    generic_devices = [device for device in all_devices if device.get('os') == delete_target]  # Uses customizable deletion target
    return generic_devices
 
def delete_device(device_id):
    """Delete a device by its ID and log the outcome."""
    response = requests.delete(f"{api_url}/devices/{device_id}", headers=headers)
    if response.status_code == 200 and "Removed device" in response.json().get("message", ""):
        print(f"Successfully deleted device with ID {device_id}.")
    else:
        print(f"Failed to delete device with ID {device_id}. Status: {response.status_code}, Response: {response.text}")
 
def main():
    generic_devices = get_generic_devices()
    for device in generic_devices:
        delete_device(device['device_id'])
 
if __name__ == "__main__":
    main()