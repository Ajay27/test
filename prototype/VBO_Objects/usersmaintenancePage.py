""" This file contains the details of each field of Users Maintenance page
    This (select_cms dict) uses the cms profile named cms_created. Have a cms profile already created where no profile is already associated to it.
"""
import time

class usersmaintclass:
    select = {
        "locator": "id",
        "id": "SELOPTION_USERS"
    }
    create_new_user = {
        "locator":"xpath",
        "xpath":".//*[@id='SELOPTION_USERS']/option[2]"
    }
    username = {
        "locator": "id",
        "id": "NAME_USERS_0",
        "error_message":"Error: User Name cannot contain spaces and the following characters: \ / ` ; > < { } ( ) | ' '' % = +",
        "value": "cms_new_check"
    }

    user_pwd = {
        "locator": "id",
        "id": "PASSWORD_USERS_0",
        "error_message":"Error: The User Password can not be empty",
        "value": "check"
    }

    retype_user_pwd = {
        "locator": "id",
        "id": "PASSWORD1_USERS_0",
        "error_message":"Error: The User Password and the Re-type User Password are not equals",
        "value": "check"
    }

    start_date = {
        "locator": "id",
        "id": "START_DATE_0",
        #"value": 'time.strftime("%Y-%m-%d")'
        "value":"2018-01-31"
    }

    expiry_date = {
        "locator": "id",
        "id": "EXPIRY_DATE_0",
        "value":"2018-12-31"

    }
    reset_attempts = {
        "locator": "id",
        "id": "ATTEMPTS_0"
    }

    select_cms = {
        "locator": "id",
        "id": "CMS_FK_0",
        "value":"cms_created"
    }

    save = {
        "locator": "id",
        "id": "SAVE_USERS"
    }

    cancel = {
        "locator": "id",
        "id": "CANCEL_USERS"
    }
    mandatory_data = [
        username,
        user_pwd,
        retype_user_pwd,
        start_date,
        expiry_date,
        select_cms
    ]