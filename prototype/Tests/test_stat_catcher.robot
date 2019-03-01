*** Settings ***
Resource  ../VBO Keywords/common.robot
Resource  ../VBO Keywords/stat_catcher.robot
Library  ../Core_Libraries/Test_Data_Pool/data.py
Library  ../VBO_Library/lib_files.py

Suite Setup  Run Keywords  Open sdp  setup_add_new_stat_catcher   get_data
Suite Teardown  close sdp
Test Setup  create_stat_catcher
Test Teardown  close

*** Variables ***

@{invalid_name}=    {}name1  dkfnksnv+  %fjafaj   =cajkvab

*** Test Cases ***
validate stat catcher name with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_name}
        \   ${statcatch.stat_catcherclass.name}  ${data}

validate stat catcher IP with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_ip}
        \   ${statcatch.stat_catcherclass.IP_addr_appliance}  ${data}

validate stat catcher port with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_port}
        \   ${statcatch.stat_catcherclass.port_receiving_statistics}  ${data}

validate stat catcher point of presence with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_name}
        \   ${statcatch.stat_catcherclass.point_of_presence}  ${data}

*** Keywords ***
get_data
    @{invalid_ip} =  get_invalid_ip
    SET SUITE VARIABLE   @{invalid_ip}

    @{invalid_port} =  get invalid int  1024  65535
    SET SUITE VARIABLE  @{invalid_port}

