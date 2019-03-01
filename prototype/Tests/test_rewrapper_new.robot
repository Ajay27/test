*** Settings ***
Resource  ../VBO Keywords/common.robot
Resource  ../VBO Keywords/rewrapper.robot
Library  ../Core_Libraries/Test_Data_Pool/data.py
Library  ../VBO_Library/lib_files.py


#Suite Setup   Run Keywords  Open sdp  setup_add_new_rewrapper
#Suite Teardown  close sdp
Suite Setup  setup_add_new_rewrapper
Force Tags  rewrapper1
Test Setup  create_rewrapper
Test Teardown  close

*** Variables ***
@{invalid_name}=    {}name1  dkfnksnv+  %fjafaj   =cajkvab

@{invalid_ttl}=  -1  256  89797  @qxkn
@{invalid_delay_between_asset_restart} =  0  150  40000  -1  asdinnk  !@#  1999  30001
@{invalid_delay_between_switching_sources} =   0  -31  77348  31  afa  @!!
*** Test Cases ***
#validate rewrapper name with invalid data
#      [Template]  validate_name
#        :FOR  ${data}  in  @{invalid_name}
#        \   ${rewrapper.rewrapperclass.name}  ${data}


#validate rewrapper host associated with invalid host
#      [Template]  validate_host_asso
#        :FOR  ${data}  in  @{invalid_host}
#        \   ${rewrapper.rewrapperclass.host_associated}  ${data}
sdp.900
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_ttl}
        \   ${rewrapper.rewrapperclass.ttl_for_multicast_sending}  ${data}


validate rewrapper with invalid delay between asset restart
    [Template]  validate_name
        :FOR  ${data}  in  @{invalid_delay_between_asset_restart}
        \   ${rewrapper.rewrapperclass.delay_between_asset_restart}  ${data}

validate rewrapper with invalid delay between switching sources
    [Template]  validate_name
        :FOR  ${data}  in  @{invalid_delay_between_switching_sources}
        \   ${rewrapper.rewrapperclass.delay_between_switching}  ${data}


