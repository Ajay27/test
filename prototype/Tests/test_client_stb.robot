*** Settings ***
Resource  ../VBO Keywords/common.robot
Resource  ../VBO Keywords/client_stb.robot
Library  ../Core_Libraries/Test_Data_Pool/data.py
Library  ../VBO_Library/lib_files.py

Suite Setup  Run Keywords  Open sdp  setup_add_new_clientstb  get_data
Suite Teardown  close sdp
Test Setup  create_client_stb
Test Teardown  close

*** Variables ***

@{invalid_name}=    {}name1  dkfnksnv+  %fjafaj   =cajkvab

*** Test Cases ***
validate stb description with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_name}
        \   ${clientstb.clientSTBclass.description}  ${data}

validate init range with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_ip}
        \   ${clientstb.clientSTBclass.init_range}  ${data}

validate end range with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_ip}
        \   ${clientstb.clientSTBclass.end_range}  ${data}

*** Keywords ***
get_data
    @{invalid_ip} =  get_invalid_ip
    SET SUITE VARIABLE   @{invalid_ip}