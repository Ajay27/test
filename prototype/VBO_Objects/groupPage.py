class groupclass:
    filename = {
        "locator": "xpath",
        "xpath": "//input[@type='Text']"
    }
    search = {
        "locator": "xpath",
        "xpath": "//input[@value='Search']"
    }

    add_new_group = {
        "locator": "xpath",
        "xpath": "//input[@value='Add new Group']"
    }

    list_all_group = {
        "locator": "xpath",
        "xpath": "//input[@value='List all Groups']"
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
        "error_message": "[Description] cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +",
        "value":"group-132"
    }

    mandatory_data = [
        name
    ]
