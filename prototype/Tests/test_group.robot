*** Settings ***
Resource  ../VBO Keywords/common.robot
Resource  ../VBO Keywords/group.robot
Library  ../Core_Libraries/Test_Data_Pool/data.py
Library  ../VBO_Library/lib_files.py

Suite Setup  Run Keywords  Open sdp  setup_add_new_group
Test Setup  create_group
Test Teardown  close

*** Variables ***

@{invalid_name}=    {}name1

*** Test Cases ***
validate group name with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_name}
        \   ${group.groupclass.name}  ${data}