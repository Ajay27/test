*** Settings ***
Resource  ../VBO Keywords/common.robot
Resource  ../VBO Keywords/fcc.robot
Library  ../Core_Libraries/Test_Data_Pool/data.py
Library  ../VBO_Library/lib_files.py


Suite Setup  Run Keywords  Open sdp  setup_add_new_fcc  get_data
Suite Teardown  close sdp
Test Setup  create_fcc
Test Teardown  close

*** Variables ***
@{invalid_name}=    fcc-1{}  fcc-2+  %;fcc-3

@{invalid_rtcp} =  1023  65536  @jjvn{}  -1323  0

@{invalid_threads}=    0  17  -11  @dnqsjn
@{invalid_concurrent}=  99  1001  -502  @#209
@{invalid_bw}=  -1  4001  @#!356  ()2678
@{invalid_igmp_join_max}=  -1  301  sjonodqow  @cw289
@{invalid_range}=  -1  1000000000  $%#%68798  ()797990  ?<>$%#7787000
@{invalid_time}=  999  1000000000  $%#wd68798  bksckw@#797990  ?<>":{}}#E7787000
@{invalid_debugging}=  1023  65536  -789  @#$!25345
@{invalid_flags}=  0!@xdnlkc  @#ABAB  0xFFFFF  00FA4E
@{invalid_input_threads}=  0  17  -5  ()7  @!9


*** Test Cases ***
validate fcc name with valid data
      [Tags]  smoke
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_name}
        \   ${fcc.fccclass.name}  ${data}

validate fcc ip with valid address
    [Tags]  smoke
    [Template]  validate_name
        :FOR  ${data}  in  @{invalid_ip}
        \   ${fcc.fccclass.IP_addr_appliance}  ${data}
validate fcc rtcp with valid data
    [Tags]  smoke
    [Template]  validate_name
        :FOR  ${data}  in  @{invalid_rtcp}
        \   ${fcc.fccclass.FCC_RTCP_Service_Port_Number}  ${data}

validate perc.nominal - catchup with valid data
   [Tags]  smoke
   [Template]  validate_name
        :FOR  ${data}  in  @{invalid_perc}
        \   ${fcc.fccclass.Perc_nominal_Bandwidth_used_to_catchup}  ${data}

validate perc.nominal - handover with valid data
    [Tags]  smoke
    [Template]  validate_name
        :FOR  ${data}  in  @{invalid_perc}
        \   ${fcc.fccclass.Perc_nominal_Bandwidth_used_for_handover}  ${data}

validate threads with valid data
    [Template]  validate_name
        :FOR  ${data}  in  @{invalid_threads}
        \   ${fcc.fccclass.number_of_threads}  ${data}
validate concurrent with valid data
    [Template]  validate_name
        :FOR  ${data}  in  @{invalid_concurrent}
        \   ${fcc.fccclass.number_of_concurrent}  ${data}
validate bandwidth with valid data
    [Template]  validate_name
        :FOR  ${data}  in  @{invalid_bw}
        \   ${fcc.fccclass.total_amt_of_bandwidth}  ${data}
validate IGMP join max with valid data
    [Template]  validate_name
        :FOR  ${data}  in  @{invalid_igmp_join_max}
        \   ${fcc.fccclass.fcc_time_max_igmp_join}  ${data}
validate IGMP join min with valid data
    [Template]  validate_name
        :FOR  ${data}  in  @{invalid_range}
        \   ${fcc.fccclass.fcc_time_min_igmp_join}  ${data}
validate IGMP leave max with valid data
    [Template]  validate_name
        :FOR  ${data}  in  @{invalid_range}
        \   ${fcc.fccclass.fcc_time_max_igmp_leave }  ${data}
validate time client with valid data
    [Template]  validate_name
        :FOR  ${data}  in  @{invalid_range}
        \   ${fcc.fccclass.fcc_time_client}  ${data}
validate time difference with valid data
    [Template]  validate_name
        :FOR  ${data}  in  @{invalid_range}
        \   ${fcc.fccclass.fcc_time_difference}  ${data}
validate max video with valid data
    [Template]  validate_name
        :FOR  ${data}  in  @{invalid_range}
        \   ${fcc.fccclass.fcc_max_video}  ${data}
validate time allowed with valid data
    [Template]  validate_name
        :FOR  ${data}  in  @{invalid_time}
        \   ${fcc.fccclass.time_allowed_to_complete}  ${data}
validate debugging port with valid data
    [Template]  validate_name
        :FOR  ${data}  in  @{invalid_debugging}
        \   ${fcc.fccclass.debugging_port}  ${data}
validate operation flags with valid data
   [Template]  validate_name
        :FOR  ${data}  in  @{invalid_flags}
        \   ${fcc.fccclass.operation_flags}  ${data}
validate input threads with valid data
    [Template]  validate_name
        :FOR  ${data}  in  @{invalid_input_threads}
        \   ${fcc.fccclass.fcc_input_threads}  ${data}


*** Keywords ***
get_data
    @{invalid_ip} =  get_invalid_ip
    SET SUITE VARIABLE   @{invalid_ip}

    @{invalid_perc} =  get invalid int  0  400
    SET SUITE VARIABLE  @{invalid_perc}