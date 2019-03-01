class areaclass:

    name = {
        "locator": "xpath",
        "xpath": "//input[@type='Text']"
    }
    search = {
        "locator": "xpath",
        "xpath": "//input[@value='Search']"
    }

    add_new_area = {
        "locator": "xpath",
        "xpath": "//input[@value='Add new Area']"
    }

    list_all_area = {
        "locator": "xpath",
        "xpath": "//input[@value='List all Areas']"
    }

    delete = {
        "locator": "xpath",
        "xpath": "//input[@disabled='true']"
    }

    name = {
        "locator": "id",
        "name": "NAME_0",
        "id": "NAME_0",
        "tooltip": "Cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +",
        "error_message": "[Name] cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +",
        "value": "area-52"
    }

    region = {
        "locator": "id",
        "name": "REGION_FK_0",
        "id": "REGION_FK_0",
        "tooltip": "Cannot be empty",
        "error_message": "[Region] cannot be empty",
        "value":"region-52"
    }
    mandatory_data = [
        name,
        region
    ]
