class clientSTBclass:
    description = {
        "locator": "xpath",
        "xpath": "//input[@type='Text']"
    }

    search = {
        "locator": "xpath",
        "xpath": "//input[@value='Search']"
    }

    add_new_stb_range = {
        "locator": "xpath",
        "xpath": "//input[@value='Add new Range STB']"
    }

    list_all_stat_catcher = {
        "locator": "xpath",
        "xpath": "//input[@value='List all Ranges STB']"
    }

    delete = {
        "locator": "xpath",
        "xpath": "//input[@disabled='true']"
    }

    description = {
        "locator": "id",
        "name": "GUI_0",
        "id": "GUI_0",
        "tooltip": "Cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +",
        "error_message": "[Description] cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +",
        "value": "client - stb"
    }

    init_range = {
        "locator": "id",
        "name": "IRINT_0",
        "id": "IRINT_0",
        "tooltip": "Cannot be empty and must be a valid IP address but not multicast IP",
        "error_message": "[Init Range] cannot be empty and must be a valid IP address but not multicast IP",
        "value": "10.10.10.10"
    }

    end_range = {
        "locator": "id",
        "name": "ERINT_0",
        "id": "ERINT_0",
        "tooltip": """Cannot be empty and must be a valid IP address but not multicast IP """,
        "error_message": "[End Range] cannot be empty and must be a valid IP address but not multicast IP",
        "value" : "12.12.12.12"
      }

    area ={
        "locator": "id",
        "name": "AREA_FK_0",
        "id": "AREA_FK_0",
        "tooltip": "Cannot be empty ",
        "error_message": "[Area] cannot be empty",
        "value":"Area-52"
    }
    mandatory_data = [
        description,
        init_range,
        end_range,
        area
    ]