*** Settings ***
Library  ../Core_Libraries/Test_Data_Pool/data.py
Library  ../Core_Libraries/Database/database.py
Library  Selenium2Library
Library  ../Core_Libraries/Application_Utilities/sdputils.py
Library  ../VBO_Objects/sdppo.py
Library  ../VBO_Objects/ConfigurationInfopage.py



*** Keywords ***
setup configurationInfo
    ${SDP} =   BuiltIn.Get Library Instance  sdppo
    open_page  ${driver}  ${SDP.configuration_info}
    fill mandatory  ${driver}  ${SDP.configuration_info}
    ${configInfo} =   BuiltIn.Get Library Instance  ConfigurationInfopage
    SET GLOBAL VARIABLE    ${configInfo}
get_invalid_ip
    invalid_ip

validate
    [Arguments]  ${field}  ${data}
    log  ${field} ${data}
    insert_value    ${driver}    ${field}    ${data}
    save    ${driver}
    alert should be present    text=[Heartbeat IP] cannot be empty and must be a valid IP address but not multicast IP
    ${hbip}=    execute    select HBIP from configuration
    should not be equal    ${hbip)    ${data}
