*** Settings ***
Library  Selenium2Library
Library  ../Core_Libraries/Application_Utilities/sdputils.py
Library  ../VBO_Objects/sdppo.py
Library  ../VBO_Objects/sdpciPage.py
Library  ../VBO_Library/lib_files.py
Library  ../Core_Libraries/Database/database.py
Variables  ../VBO_Objects/properties.py

Suite Setup  setup_add_new_sdpci
Force Tags  sdpcicreation


*** Variables ***

@{invalid_name} =   {}name1  dkfnksnv+  %fjafaj   None
@{valid_name} =  check
@{valid_host} =  heartbeat
@{search}=  sdpci
*** Test Cases ***

sdp.411 validate sdpci host_associated with valid data
       [Template]  validate_positive1
        :FOR  ${data}  in  @{valid_host}
        \   ${sdpci.sdpciclass.host_associated}  ${data}  sdpci

sdp.413 validate sdpci name with valid data
       [Template]  validate_positive
        :FOR  ${data}  in  @{valid_name}
        \   ${sdpci.sdpciclass.name}  ${data}  sdpci  NAME

sdp.414 validate sdpci name with invalid data
      [Template]  validate_check
        :FOR  ${data}  in  @{invalid_name}
        \   ${sdpci.sdpciclass.name}  ${data}

sdp.418 validate search function
        search  ${driver}  sdpci  sdpci
        return to  ${driver}  sdpciclass

*** Keywords ***

setup_add_new_sdpci
    ${SDP} =   BuiltIn.Get Library Instance  sdppo
    open_page  ${driver}  ${SDP.sdp_ci}
    ${sdpci} =   BuiltIn.Get Library Instance  sdpciPage
    SET GLOBAL VARIABLE    ${sdpci}


create_sdpci
    create_new_  ${driver}  sdpci

close
    Click Button    xpath = //input[@value='Cancel']
    sleep  2s

validate_check
    [Arguments]  ${field}  ${data}
     log  ${field} ${data}
     create_sdpci
     validate  ${driver}    ${field}    ${data}
     close

validate_positive
    [Arguments]  ${field}  ${data}  ${tablename}  ${entry}
    log  ${field} ${data}
    create_sdpci
    validate_pos  ${driver}  ${field}  ${data}
    PAGE SHOULD CONTAIN    text=Data correctly saved in tables
    ${check} =  execute    select * from ${tablename} where ${entry} = "${data}"
    log  ${check}
    sleep  1s
    ${delete} =  deletesql    DELETE from ${tablename} where ${entry} = "${data}"
    return_to_   ${driver}  sdpciclass

validate_positive1
    [Arguments]  ${field}  ${data}  ${pagename}
    log  ${field} ${data}
    create_sdpci
    validate_pos  ${driver}  ${field}  ${data}
    return_to_   ${driver}  binaryclass
    deleteentry  ${driver}  ${pagename}  ${data}