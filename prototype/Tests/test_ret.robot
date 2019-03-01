*** Settings ***
Resource  ../VBO Keywords/common.robot
Resource  ../VBO Keywords/ret.robot
Library  ../Core_Libraries/Test_Data_Pool/data.py
Library  ../VBO_Library/lib_files.py

Suite Setup  Run Keywords  Open sdp  setup_add_new_ret  get_data
Suite Teardown  close sdp
Test Setup  create_ret
Test Teardown  close

*** Variables ***

@{invalid_name}=    {}name1  dkfnksnv+  %fjafaj  =cajkvab

*** Test Cases ***
validate ret name with invalid data

      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_name}
        \   ${ret.retclass.name}  ${data}

validate ret ip address with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_ip}
        \   ${ret.retclass.IP_addr_appliance}  ${data}

validate ret rtcp address with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_ret_rtcp}
        \   ${ret.retclass.RET_RTCP_Service_Port}  ${data}

validate percentage bandwidth with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_perc_bw}
        \   ${ret.retclass.Perc_nominal_Bandwidth_for_RET}  ${data}

validate buffer with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_buffer_size}
        \   ${ret.retclass.Buffer_size}  ${data}
validate rtp payload with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_rtp_payload}
        \   ${ret.retclass.rtp_payload_type}  ${data}
validate threads with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_threads}
        \   ${ret.retclass.number_of_threads}  ${data}

validate concurrent with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_concurrent}
        \   ${ret.retclass.number_of_concurrent}  ${data}
validate bandwidth with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_bw}
        \   ${ret.retclass.total_amt_of_bandwidth}  ${data}
validate sampling period with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_sampling_period}
        \   ${ret.retclass.sampling_period_time}  ${data}
validate no of sample periods with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_no_of_sample_periods}
        \   ${ret.retclass.number_sample_periods}  ${data}
validate debugging port with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_debugging_port}
        \   ${ret.retclass.debugging_port}  ${data}

validate flags with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_ret_input_threads}
        \   ${ret.retclass.operation_flags}  ${data}

validate ret input threads with invalid data
      [Template]  validate_name
        :FOR  ${data}  in  @{invalid_ret_input_threads}
        \   ${ret.retclass.ret_input_threads}  ${data}
*** Keywords ***
get_data
    @{invalid_ip} =  get_invalid_ip
    SET SUITE VARIABLE   @{invalid_ip}

    @{invalid_ret_rtcp} =  get invalid int  1024  65535
    SET SUITE VARIABLE  @{invalid_ret_rtcp}

    @{invalid_perc_bw} =  get invalid int  0  100
    SET SUITE VARIABLE  @{invalid_perc_bw}

    @{invalid_buffer_size} =  get invalid int  0  1000
    SET SUITE VARIABLE  @{invalid_buffer_size}

    @{invalid_rtp_payload} =  get invalid int  99  127
    SET SUITE VARIABLE  @{invalid_rtp_payload}

    @{invalid_threads} =  get invalid int  1  16
    SET SUITE VARIABLE  @{invalid_threads}

    @{invalid_concurrent} =  get invalid int  100  1000
    SET SUITE VARIABLE  @{invalid_concurrent}

    @{invalid_bw} =  get invalid int  0  400
    SET SUITE VARIABLE  @{invalid_bw}

    @{invalid_sampling_period} =  get invalid int  0  999999999
    SET SUITE VARIABLE  @{invalid_sampling_period}

    @{invalid_no_of_sample_periods} =  get invalid int  0  999999999
    SET SUITE VARIABLE  @{invalid_no_of_sample_periods}

    @{invalid_debugging_port} =  get invalid int  1024  65535
    SET SUITE VARIABLE  @{invalid_debugging_port}

    @{invalid_ret_input_threads} =  get invalid int  1  16
    SET SUITE VARIABLE  @{invalid_ret_input_threads}
