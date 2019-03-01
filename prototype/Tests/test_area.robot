*** Settings ***
Resource  ../VBO Keywords/common.robot
Resource  ../VBO Keywords/area.robot
Library  ../Core_Libraries/Test_Data_Pool/data.py
Library  ../VBO_Library/lib_files.py

Suite Setup  Run Keywords  Open sdp  setup_add_new_client_stb
Suite Teardown  close sdp
Test Setup  create_area
Test Teardown  close
*** Variables ***

@{invalid_name}=    {}name1  dkfnksnv+  %fjafaj   =cajkvab

*** Test Cases ***
validate area name with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_name}
        \   ${area.areaclass.name}  ${data}