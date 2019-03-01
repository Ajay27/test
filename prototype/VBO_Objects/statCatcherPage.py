""" This file contains the details of each field of rewrapper page"""

class stat_catcherclass :
    filename = {
        "locator": "xpath",
        "xpath": "//input[@type='Text']"
    }

    search = {
        "locator": "xpath",
        "xpath": "//input[@value='Search']"
    }

    add_new_stat_catcher = {
        "locator": "xpath",
        "xpath": "//input[@value='Add new Statistics Catcher']"
    }

    list_all_stat_catcher= {
        "locator": "xpath",
        "xpath": "//input[@value='List all Statistics Catcher']"
    }

    delete = {
        "locator": "xpath",
        "xpath": "//input[@disabled='true']"
    }

    host_associated = {
        "locator": "id",
        "name": "HOST_FK_0",
        "id": "HOST_FK_0",
        "tooltip": "Cannot be empty",
        "error_message": "[Associated Host] cannot be empty",
        "value":"App-52"
    }

    name = {
        "locator": "id",
        "name": "NAME_0",
        "id": "NAME_0",
        "tooltip": "Cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +",
        "error_message": "[Name] cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +",
        "value":"stat-catcher-52"
    }


    IP_addr_appliance = {
        "locator": "id",
        "name": "STC_INTF_0",
        "id": "STC_INTF_0",
        "tooltip": """Cannot be empty and must be a valid IP address but not multicast IP """,
        "error_message": "[IP of interface receiving statistics] cannot be empty and must be a valid IP address but not multicast IP",
        "value": "127.0.0.1"
    }

    port_receiving_statistics ={
        "locator": "id",
        "name": "STC_PORT_0",
        "id": "STC_PORT_0",
        "tooltip": """Cannot be empty and must between 1024 and 65535 """,
        "error_message": "[Port receiving statistics] cannot be empty and must be between 1024 and 65535",
        "value": "4001"
    }

    point_of_presence = {
        "locator": "id",
        "name": "STC_POPID_0",
        "id": "STC_POPID_0",
        "tooltip": """Cannot be empty and must be a number """,
        "error_message": "[Point of Presence Identifier] cannot be empty and must be a number",
        "value": "0"
    }

    mandatory_data = [
        host_associated,
        name
    ]
