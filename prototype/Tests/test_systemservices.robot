*** Settings ***
Resource  ../VBO Keywords/common.robot
Resource  ../VBO Keywords/systemservices.robot
Library  ../Core_Libraries/Test_Data_Pool/data.py
Library  ../VBO_Library/lib_files.py

Suite Setup  Run Keywords  Open sdp  setup_add_new_system_service  get_data
Suite Teardown  close sdp
Test Setup  create_systemsevices
Test Teardown  close
*** Variables ***

@{invalid_name}=    {}name1  dkfnksnv+  %fjafaj   =cajkvab

*** Test Cases ***
validate systemservices name with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_name}
        \   ${ssc.systemserviceclass.name}  ${data}

validate systemservices ip with invalid data
      [Tags]  smoke
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_ip}
        \   ${ssc.systemserviceclass.ip}  ${data}

*** Keywords ***
get_data
    @{invalid_ip} =  get_invalid_ip
    SET SUITE VARIABLE   @{invalid_ip}