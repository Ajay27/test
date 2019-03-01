*** Settings ***
Resource  ../VBO Keywords/common.robot
Resource  ../VBO Keywords/hbip.robot
Library  ../Core_Libraries/Test_Data_Pool/data.py



Suite Setup   Open sdp
Suite Teardown  close sdp
Test Setup  setup configurationInfo

*** Variables ***
@{invalid_heartbeat_ip}=   256.256.256.256  235.256.234.253  asad  -23.-23.-12.-34   224.0.0.0   239.255.255.255
*** Test Cases ***
validate heartbeat ip with invalid data
      [Template]  validate
        :FOR  ${data}  in  @{invalid_heartbeat_ip}
        \   ${configInfo.ConfigurationInfo.heartbeat_ip}  ${data}

