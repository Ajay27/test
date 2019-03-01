
""" This file contains the information about the binary page """
class binaryclass :

    search_box = {
        "locator": "xpath",
        "xpath": ".//*[@id='mainTabContainer']/div[2]/div/form[1]/table/tbody/tr[1]/td/input[1]"
        }
    search = {
        "locator":"xpath",
        "xpath":".//*[@id='mainTabContainer']/div[2]/div/form[1]/table/tbody/tr[4]/td/input"
    }

    add_new = {
        "locator": "xpath",
        "xpath": "// input[ @ value = 'Add new Binary']"
        }

    list_all_binaries = {
        "locator": "xpath",
        "xpath": "//input[@value='List all Binaries']"
        }

    delete = {
        "locator": "id",
        "id": "del_0"
        }

    is_binary_signed = {
        "locator": "xpath",
        "xpath" : "//input[@id='ISSIGNED_0']",
        "error_message":"Problem with the MD5 value | Invalid MD5 Value"
    }

    name = {
        "locator": "id",
        "id": "NAME_0",
        "tooltip": """Cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = + """,
        "error_message": """[Name] cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +""",
        "value":""
    }

    browse = {
        "locator": "xpath",
        "xpath": "//input[@type='file']",
        "tooltip": "Can not empty and must be smaller than 50M. if need to modify the upload file limit,Please see I&C manual!",
        "error_message": "[File Name] can not empty and must be smaller than 50M. if need to modify the upload file limit, Please see I&C manual!",
        "value":"C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\rewrapper54new"
    }
    fccpath ={
        "value":"C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\fccret_server54new"
    }
    version = {
        "locator": "xpath",
        "xpath": "//input[@id='VERSION_0']",
        "tooltip": "Cannot be empty and cannot contain special characters",
        "error_message": "[Version] cannot be empty and cannot contain special characters",
        "value":"4.0"
    }

    signed_digest = {
        "locator": "xpath",
        "xpath": "//textarea[@align='right']",
        "tooltip": "Cannot be empty",
        "error_message": "Problem with the Signature.",
        "value":"fr9irf48rbvajwQiHPio/9zHusom10EhipJMVs2GKj07jJxc8g/6aEJBs0U7RIkco2vAEUUsVAJysbddP9A8Z0cRT2Ux92bs0jrWMoEEddilJeeLbqqiLYO0XF+FftP9cFiw66OFyGmU8pnJ2plwR2gh2RG1lidmhE1PoT9yoVQ="
    }

    type ={
        "locator": "xpath",
        "xpath": "//select[@id='BINTYPE_0']",
        "tooltip": "Cannot be empty",
        "error_message": "[Type] cannot be empty",
        "value" : "rewrapper"
    }

    hardware_revision = {
        "locator": "xpath",
        "xpath": "//select[@id='APPLIANCE_REVISION_0']",
        "tooltip": "Cannot be empty",
        "error_message": "[Hardware Revision] cannot be empty",
        "value": ""
    }

    return_ = {
        "location": "xpath",
        "xpath": "html/body/form/table[3]/tbody/tr/td/input"
    }

    mandatory_data = [
        name,
        browse,
        version,
        signed_digest,
        type,
        hardware_revision
    ]
    mandatory_data_without_HW_rev = [
        name,
        browse,
        version,
        signed_digest,
        type
    ]
