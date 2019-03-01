""" This file contains the details of each field of SDP-CMS page"""

class sdpcmsclass:
    search ={
        "locator": "xpath",
        "xpath": ".//*[@id='mainTabContainer']/div[2]/div/form[1]/table/tbody/tr[4]/td/input"
    }
    add_new ={
        "locator":"xpath",
        "xpath": ".//*[@id='mainTabContainer']/div[2]/div/form[2]/table/tbody/tr/td/input"
    }
    list_all_cms = {
        "locator":"xpath",
        "xpath":".//*[@id='mainTabContainer']/div[2]/div/form[3]/table/tbody/tr/td/input"
    }
    delete = {
        "locator":"id",
        "id":"del_0"
    }
    name = {
        "locator":"id",
        "id":"NAME_0",
        "value":"cmsprofile"
    }
    description = {
        "locator":"id",
        "id":"DESCRIPTION_0"
    }
    admin_status = {
        "locator":"id",
        "id":"STATUS_OP_0"
    }
    hosts_associated = {
        "locator":"id",
        "id":"assAppliance"
    }
    save = {
        "locator":"xpath",
        "xpath":".//*[@id='buttonSaveCms']/table/tbody/tr/td[1]/input"
    }
    cancel = {
        "locator":"xpath",
        "xpath":".//*[@id='buttonSaveCms']/table/tbody/tr/td[2]/input"
    }
    mandatory_data = [
        name
    ]