*** Settings ***
Library  Selenium2Library
Library  ../Core_Libraries/Test_Data_Pool/data.py
Library  ../VBO_Library/lib_files.py
Library  ../Core_Libraries/Application_Utilities/sdputils.py
Library  ../VBO_Objects/sdppo.py
Library  ../VBO_Objects/channelPage.py
Library  ../Core_Libraries/Database/database.py
Variables  ../VBO_Objects/properties.py

Suite Setup  setup_add_new_channel
Force Tags  channel
*** Variables ***

@{invalid_name}=    {}name1  %fjafaj  =cajkvab'
@{valid_name}=  chann-33011  ch33001  sample33011
@{invalid_ch_num}=  -1  65536  @Fefwmlf  fdfq72y8diow
@{valid_ch_num}=  33001  33062  33040
@{invalid_source}=  1.1.1.1  9.0vj24b28  223.255.255.255  240.0.0.0
@{valid_source}=  226.0.10.1  239.1.1.1  229.8.9.10
@{invalid_source_interface1}=  bond0.11
@{valid_source_interface1}=  eth0
@{invalid_source_interface2}=  bond1.2323
@{invalid_source_interface2}=  bond2.2234
@{valid_source_interface2}=  eth1
@{invalid_destination_multicast}=  255.255.0.0  10.0.0.0
@{valid_destination_multicast}=  230.19.122.1  224.1.12.1  225.12.1.3
@{invalid_destination_port}=  12.12  11.d  123.23  !!213
@{valid_destination_port}=  11010  8433  1111
@{invalid_destination_interface}=  eth0.1  bond0.2  xaui1.9
@{valid_destination_interface}=  bond3  eth9  eth10
@{invalid_Source_Identifier}=  fdjksf  1!@!@@  127jdkhf
@{valid_Source_Identifier}=  12323  1333  1222
@{invalid_RET_Buffer}=  122.3  12d.f  0.2234
@{valid_RET_Buffer}=  350  450  650
@{invalid_input_proto}=  "-1"
*** Test Cases ***

sdp.791
      [Template]  validate_check
        :FOR  ${data}  in  @{invalid_name}
        \   ${channel.channelclass.channel_name}  ${data}
sdp.792
       [Template]  validate_positive1
        :FOR  ${data}  in  @{valid_name}
        \   ${channel.channelclass.channel_name}  ${data}  channel
sdp.793
      [Template]  validate_check
        :FOR  ${data}  in  @{invalid_ch_num}
        \   ${channel.channelclass.channel_number}  ${data}
sdp.794
       [Template]  validate_positive
        :FOR  ${data}  in  @{valid_ch_num}
        \   ${channel.channelclass.channel_number}  ${data}  channel
sdp.795
      [Template]  validate_check
        :FOR  ${data}  in  @{invalid_source}
        \   ${channel.channelclass.source_multicast_value}  ${data}
sdp.796
       [Template]  validate_positive
        :FOR  ${data}  in  @{valid_source}
        \   ${channel.channelclass.source_multicast_value}  ${data}  channel
sdp.797
       [Template]  validate_check
        :FOR  ${data}  in  @{invalid_source_interface1}
        \   ${channel.channelclass.rewrapper_source_interface1}  ${data}
sdp.798
       [Template]  validate_positive
        :FOR  ${data}  in  @{valid_source_interface1}
        \   ${channel.channelclass.rewrapper_source_interface1}  ${data}  channel
sdp.799
       [Template]  validate_check
        :FOR  ${data}  in  @{invalid_source_interface2}
        \   ${channel.channelclass.rewrapper_source_interface2}  ${data}
sdp.800
       [Template]  validate_positive
        :FOR  ${data}  in  @{valid_source_interface2}
        \   ${channel.channelclass.rewrapper_source_interface2}  ${data}  channel
sdp.801
       [Template]  validate_check
        :FOR  ${data}  in  @{invalid_destination_multicast}
        \   ${channel.channelclass.destination_multicast_value}  ${data}
sdp.802
       [Template]  validate_positive
        :FOR  ${data}  in  @{valid_destination_multicast}
        \   ${channel.channelclass.destination_multicast_value}  ${data}  channel
sdp.803
       [Template]  validate_check
        :FOR  ${data}  in  @{invalid_destination_port}
        \   ${channel.channelclass.destination_port_value}  ${data}
sdp.804
       [Template]  validate_positive
        :FOR  ${data}  in  @{valid_destination_port}
        \   ${channel.channelclass.destination_port_value}  ${data}  channel
sdp.805
       [Template]  validate_check
        :FOR  ${data}  in  @{invalid_destination_interface}
        \   ${channel.channelclass.Rewrapper_Destination_interface}  ${data}
sdp.806
       [Template]  validate_positive
        :FOR  ${data}  in  @{valid_destination_interface}
        \   ${channel.channelclass.Rewrapper_Destination_interface}  ${data}  channel
sdp.807
       [Template]  validate_check
        :FOR  ${data}  in  @{invalid_Source_Identifier}
        \   ${channel.channelclass.Source_Identifier_for_RTP}  ${data}
sdp.808
       [Template]  validate_positive
        :FOR  ${data}  in  @{valid_Source_Identifier}
        \   ${channel.channelclass.Source_Identifier_for_RTP}  ${data}  channel
sdp.809
       [Template]  validate_check
        :FOR  ${data}  in  @{invalid_RET_Buffer}
        \   ${channel.channelclass.RET_Buffer_size}  ${data}
sdp.810
       [Template]  validate_positive
        :FOR  ${data}  in  @{valid_RET_Buffer}
        \   ${channel.channelclass.RET_Buffer_size}  ${data}  channel
sdp.811
       [Template]  validate_check
        :FOR  ${data}  in  @{invalid_input_proto}
        \   ${channel.channelclass.input_protocol}  ${data}
*** Keywords ***

setup_add_new_channel
    ${SDP} =   BuiltIn.Get Library Instance  sdppo
    open_page  ${driver}  ${SDP.channel }
    ${channel} =   BuiltIn.Get Library Instance  channelPage
    SET GLOBAL VARIABLE    ${channel}

validate_check
    [Arguments]  ${field}  ${data}
     log  ${field} ${data}
     create_new_  ${driver}  channel
     validate  ${driver}    ${field}    ${data}

validate_positive1
    [Arguments]  ${field}  ${data}  ${pagename}
    log  ${field} ${data}
    create_new_  ${driver}  channel
    validate_pos  ${driver}  ${field}  ${data}  ${pagename}
    deleteentry  ${driver}  ${pagename}  ${data}

validate_positive
    [Arguments]  ${field}  ${data}  ${pagename}
    log  ${field} ${data}
    create_new_  ${driver}  channel
    validate_pos  ${driver}  ${field}  ${data}  ${pagename}
    deleteentry  ${driver}  ${pagename}  test-33001