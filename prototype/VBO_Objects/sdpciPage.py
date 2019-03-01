""" This file contains the details of each field of SDP-CI page"""

class sdpciclass:

    #def __init__(self, x, y):
    #    self.x = x
    #    self.y = y
    search_box = {
        "locator": "xpath",
        "xpath": ".//*[@id='mainTabContainer']/div[2]/div/form[1]/table/tbody/tr[1]/td/input[1]"
    }
    search = {
        "locator": "xpath",
        "xpath": ".//*[@id='mainTabContainer']/div[2]/div/form[1]/table/tbody/tr[4]/td/input"
    }
    add_new = {
        "locator": "xpath",
        "xpath": ".//*[@id='mainTabContainer']/div[2]/div/form[2]/table/tbody/tr/td/input"
    }
    list_all_sdpci = {
        "locator": "xpath",
        "xpath": ".//*[@id='mainTabContainer']/div[2]/div/form[3]/table/tbody/tr/td/input"
    }
    delete = {
        "locator": "id",
        "id": "del_0"
    }
    host_associated = {
        "locator":"id",
        "id":"HOST_FK_0",
        "tooltip":"Cannot be empty",
        "error_message":"[Host Associated] cannot be empty",
        "value":"test"
    }
    name = {
        "locator": "id",
        "id": "NAME_0",
        "tooltip":"Cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +",
        "error_message":"[Name] cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +",
        "value":'sdpci-test'
    }
    description = {
        "locator": "id",
        "id": "DESCRIPTION_0"
    }
    admin_status = {
        "locator": "id",
        "id": "STATUS_OP_0"
    }
    save = {
        "locator":"xpath",
        "xpath":".//*[@id='buttonSaveSdpci']/table/tbody/tr/td[1]/input"
    }
    cancel = {
        "locator":"xpath",
        "xpath":".//*[@id='buttonSaveSdpci']/table/tbody/tr/td[2]/input"
    }
    return_ = {
        "locator":'xpath',
        "xpath":"html/body/form/table[3]/tbody/tr/td/input"
    }

    mandatory_data = [
        host_associated,
        name
    ]
