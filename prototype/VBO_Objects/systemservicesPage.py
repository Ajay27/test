""" This file contains the details of each field of system-services page"""

class systemserviceclass:
    filename = {
        "locator": "xpath",
        "xpath": "//input[@type='Text']"
    }

    search = {
        "locator": "xpath",
        "xpath": "//input[@value='Search']"
    }

    add_new_service_provider = {
        "locator": "xpath",
        "xpath": "//input[@value='Add new Service Provider']"
    }

    list_all_service_providers = {
        "locator": "xpath",
        "xpath": "//input[@value='List all Service Providers']"
    }

    delete = {
        "locator": "xpath",
        "xpath": "//input[@disabled='true']"
    }

    type_of_system_service = {
        "locator": "id",
        "name": "TYPE_0",
        "id": "TYPE_0",
        "tooltip": """Cannot be empty""",
        "error_message": "[Type of System Service] cannot be empty",
        "value": "hosts"
    }
    ip = {
        "locator": "id",
        "name": "IP_0",
        "id": "IP_0",
        "tooltip": """Cannot be empty and must be a valid IP address but not multicast IP""",
        "error_message": "[IP] cannot be empty and must be a valid IP address but not multicast IP",
        "value": "10.10.10.10"
    }

    name = {
        "locator": "id",
        "name": "NAME_0",
        "id": "NAME_0",
        "tooltip": """Cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +""",
        "error_message": "[Name] cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +",
        "value": "name1"
    }

    mandatory_data = [
            ip,
            name,
            type_of_system_service
         ]