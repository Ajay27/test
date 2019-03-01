*** Settings ***
Library  Selenium2Library
Library  ../Core_Libraries/Application_Utilities/sdputils.py
Library  ../VBO_Library/lib_files.py
Variables  ../VBO_Objects/properties.py

*** Keywords ***
Open sdp
    Open Browser  ${url}  ff
    ${driver}=  sdp_login
    SET GLOBAL VARIABLE    ${driver}


close sdp
    # Click Button  xpath=//input[@value='Log out']
    Close Browser

close
    Click Button    xpath = //input[@value='Cancel']
    sleep  2s

validate_name
    [Arguments]  ${field}  ${data}
     validate  ${driver}    ${field}    ${data}