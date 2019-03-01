*** Settings ***
Library  Selenium2Library
Library  ../Core_Libraries/Application_Utilities/sdputils.py
Library  ../VBO_Objects/sdppo.py
Library  ../VBO_Objects/sdpcmsPage.py
Library  ../VBO_Library/lib_files.py
Library  ../Core_Libraries/Database/database.py
Variables  ../VBO_Objects/properties.py

Suite Setup  setup_add_new_sdpcms
Force Tags  sdpcmscreation

*** Variables ***

@{invalid_name} =   {}name1  dkfnksnv+  %fjafaj   None
@{valid_name} =  checkcms  cmsprofilic  bidciw
*** Test Cases ***
sdp.413 validate sdpci name with valid data
       [Template]  validate_positive
        :FOR  ${data}  in  @{valid_name}
        \   ${sdpcms.sdpcmsclass.name}  ${data}  sdpci  NAME

sdp.414 validate sdpci name with invalid data
      [Template]  validate_check
        :FOR  ${data}  in  @{invalid_name}
        \   ${sdpcms.sdpcmsclass.name}  ${data}
*** Keywords ***

setup_add_new_sdpcms
    ${SDP} =   BuiltIn.Get Library Instance  sdppo
    open_page  ${driver}  ${SDP.sdp_cms}
    ${sdpcms} =   BuiltIn.Get Library Instance  sdpcmsPage
    SET GLOBAL VARIABLE    ${sdpcms}

validate_check
    [Arguments]  ${field}  ${data}
     log  ${field} ${data}
     create_new_  ${driver}  sdpcms
     validate  ${driver}    ${field}    ${data}
     Click Button    xpath = //input[@value='Cancel']
     sleep  2s

validate_positive
    [Arguments]  ${field}  ${data}  ${tablename}  ${entry}
    log  ${field} ${data}
    create_new_  ${driver}  sdpcms
    validate_pos  ${driver}  ${field}  ${data}
    PAGE SHOULD CONTAIN    text=Data correctly saved in tables
    ${check} =  execute    select * from ${tablename} where ${entry} = "${data}"
    log  ${check}
    sleep  1s
    ${delete} =  deletesql    DELETE from ${tablename} where ${entry} = "${data}"
    return_to_   ${driver}  sdpciclass
