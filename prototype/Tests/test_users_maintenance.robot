*** Settings ***
Library  Selenium2Library
Library  ../Core_Libraries/Application_Utilities/sdputils.py
Library  ../VBO_Objects/sdppo.py
Library  ../VBO_Objects/usersmaintenancePage.py
Library  ../VBO_Library/lib_files.py
Variables  ../VBO_Objects/properties.py

Suite Setup  Run Keywords  Open sdp  setup_add_new_users_maintenance
Force Tags  usersmaintenance
Test Setup  create_users_maintainence
Test Teardown  close

*** Variables ***

@{invalid_name}=   {}name1  dkfnksnv+  %fjafaj   =cajkvab

*** Test Cases ***
validate user name with invalid data
      [Template]  validate_check
        :FOR  ${data}  in  @{invalid_name}
        \   ${user.usersmaintclass.name}  ${data}


*** Keywords ***
Open sdp
    [Documentation]  Login to the application and the driver instance is made as the global variable

    open_browser  ${url}  ff
    ${driver} =  sdp_login
    SET GLOBAL VARIABLE    ${driver}

setup_add_new_users_maintenance
    ${SDP} =   BuiltIn.Get Library Instance  sdppo
    open_page  ${driver}  ${SDP.users_maintenance}
    ${user} =   BuiltIn.Get Library Instance  usersmaintenancePage
    SET GLOBAL VARIABLE    ${user}


create_users_maintainence
    create_new_user_maint  ${driver}

close
    Click Button    xpath = //input[@value='Cancel']
    sleep  2s

validate_check
    [Arguments]  ${field}  ${data}
     validate  ${driver}    ${field}    ${data}


