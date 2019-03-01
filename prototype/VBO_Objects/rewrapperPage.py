""" This file contains the details of each field of rewrapper page"""

class rewrapperclass:
    filename = {
        "locator": "xpath",
        "xpath": "//input[@type='Text']"
    }

    search = {
        "locator": "xpath",
        "xpath": "// input[@ value = 'Search']"
    }

    add_new_rewrapper = {
        "locator": "xpath",
        "xpath": "// input[@value = 'Add new Rewrapper']"
    }

    list_all_rewrappers = {
        "locator": "xpath",
        "xpath": "//input[@value='List all Rewrappers']"
    }

    delete = {
        "locator": "xpath",
        "xpath": "// input[ @ disabled = 'true']"
    }

    name = {
        "locator": "id",
        "name": "NAME_0",
        "id": "NAME_0",
        "tooltip": """Cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +""",
        "error_message": "[Name] cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +",
        "value": "Rewrapper-52"
    }

    host_associated = {
        "locator": "id",
        "name": "HOST_FK_0",
        "id": "HOST_FK_0",
        "tooltip": "Cannot be empty",
        "error_message": "[Host Associated] cannot be empty",
        "value": "App-52"
    }

    ttl_for_multicast_sending = {
        "locator": "id",
        "name": "TTL_0",
        "id": "TTL_0",
        "tooltip": "Cannot be empty and must between 0 and 255",
        "error_message": "[TTL for Multicast sending] cannot be empty and must between 0 and 255",
        "value": "63"
    }

    rtp_header_size = {
        "locator": "id",
        "name": "RTPHEADERSIZE_0",
        "id": "RTPHEADERSIZE_0"
    }

    delay_between_asset_restart = {
        "locator": "id",
        "name": "DLY_BW_RESTART_REW_0",
        "id": "DLY_BW_RESTART_REW_0",
        "tooltip": "Must between 2000 and 30000",
        "error_message": "[Delay Between Asset Restart (in ms)] must between 2000 and 30000"
    }

    delay_between_switching = {
        "locator": "id",
        "name": "DLY_BW_SRC_FLIP_0",
        "id": "DLY_BW_SRC_FLIP_0",
        "tooltip": "Must between 1 and 30",
        "error_message": "[Delay Between Switching Sources For The Same Asset (in minutes)] must between 1 and 30"
    }

    mandatory_data = [
            name,
            host_associated,
            ttl_for_multicast_sending
    ]