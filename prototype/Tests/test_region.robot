*** Settings ***
Resource  ../VBO Keywords/common.robot
Resource  ../VBO Keywords/region.robot
Library  ../Core_Libraries/Test_Data_Pool/data.py
Library  ../VBO_Library/lib_files.py

Suite Setup  Run Keywords  Open sdp  setup_add_new_region
Suite Teardown  close sdp
Test Setup  create_region
Test Teardown  close

*** Variables ***

@{invalid_name}=    {}name1  dkfnksnv+  %fjafaj   =cajkvab

*** Test Cases ***
validate region name with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_name}
        \   ${region.regionclass.name}  ${data}