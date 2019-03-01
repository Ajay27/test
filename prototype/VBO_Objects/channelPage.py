""" This file contains the information about the channel page
    Automation for scrambling related parameters can be taken up later.
    It has not been done yet
"""

class channelclass:
    search_box = {
        "locator": "xpath",
        "xpath": "//input[@name='sMatrixName']"
    }
    channel_number_box ={
        "locator": "xpath",
        "xpath": "//input[@name='sMatrixNumber']"
    }
    ingress_or_egress_multicast_address_box={
        "locator": "xpath",
        "xpath": "// input[ @ name = 'sMatrixAddr']"
    }
    search={
        "locator": "xpath",
        "xpath": "//input[@value='Search']"
    }
    import_and_export = {
        "locator": "xpath",
        "xpath": "//input[contains(@value,'Import and Export')]"
    }
    add_new={
        "locator": "xpath",
        "xpath": "//input[@value='Add New Channels']"
    }
    list_all_channels = {
        "locator": "xpath",
        "xpath": "//input[@value='List All Channels']"
    }
    delete ={
        "locator": "id",
        "id": "del_0"
    }
    channel_name={
        "locator": "id",
        "name": "NAME_0",
        "id": "NAME_0",
        "tooltip": "Cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % =",
        "error_message": "[Channel Name] cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % =",
        "value":"test-33001"
    }
    channel_number={
        "locator": "id",
        "name": "ASSET_0",
        "id": "ASSET_0",
        "tooltip": "Cannot be empty and must between 0 and 65535",
        "error_message": "[Channel Number] cannot be empty and must be between 0 and 65535",
        "value":"33001"
    }
    source_multicast_value={
        "locator": "id",
        "name": "INGRESS_URL_IP_0",
        "id": "INGRESS_URL_IP_0",
        "tooltip": "Cannot be empty and must be a multicast IP address",
        "error_message": "[Source Multicast value] cannot be empty and must be a multicast IP address",
        "value":"229.10.187.75"
    }
    source_port_value={
        "locator": "id",
        "name": "INGRESS_URL_PORT_0",
        "id": "INGRESS_URL_PORT_0",
        "tooltip": "Cannot be empty and must between 0 and 65535",
        "error_message": "[Source Port value] cannot be empty and must between 0 and 65535",
        "value":"11010"
    }
    rewrapper_source_interface1={
        "locator": "id",
        "name": "INGRESS_INTF_0",
        "id": "INGRESS_INTF_0",
        "tooltip": "Must between eth0 and eth7 or bond0 and bond3 or xaui0 and xaui1 or eth0-7.X or bond0-3.X or xaui0-1.X X is number between 1 and 4094",
        "error_message": "[Rewrapper Source Interface 1] must be between eth0 and eth7 or bond0 and bond3 or xaui0 and xaui1"
    }
    rewrapper_source_interface2={
        "locator": "id",
        "name": "INGRESS_INTF2_0",
        "id": "INGRESS_INTF2_0",
        "tooltip": "Must between eth0 and eth7 or bond0 and bond3 or xaui0 and xaui1 or eth0-7.X or bond0-3.X or xaui0-1.X X is number between 1 and 4094",
        "error_message":"[Rewrapper Source Interface 2] must be between eth0 and eth7 or bond0 and bond3 or xaui0 and xaui1"
    }
    destination_multicast_value={
        "locator": "id",
        "name": "EGRESS_URL_IP_0",
        "id": "EGRESS_URL_IP_0",
        "tooltip": "Cannot be empty and must be a multicast IP address",
        "error_message": "[Destination Multicast value] cannot be empty and must be a multicast IP address",
        "value":"229.11.187.75"
    }
    destination_port_value={
        "locator": "id",
        "name": "EGRESS_URL_PORT_0",
        "id": "EGRESS_URL_PORT_0",
        "tooltip": "Cannot be empty and must between 0 and 65535",
        "error_message": "[Destination Port value] cannot be empty and must between 0 and 65535",
        "value":"11010"
    }
    Rewrapper_Destination_interface={
        "locator": "id",
        "name": "EGRESS_INTF_0",
        "id": "EGRESS_INTF_0",
        "tooltip": "Must between eth0 and eth7 or bond0 and bond3 or xaui0 and xaui1 or eth0-7.X or bond0-3.X or xaui0-1.X X is number between 1 and 4094",
        "error_message":"[Rewrapper Destination interface] must between eth0 and eth7 or bond0 and bond3 or xaui0 and xaui1 or eth0-7.X or bond0-3.X or xaui0-1.X X is number between 1 and 4094"
    }
    Source_Identifier_for_RTP = {
        "locator": "id",
        "name": "SSRC_0",
        "id": "SSRC_0",
        "tooltip": "Cannot be empty and must be a number",
        "error_message": "[Source Identifier for RTP] cannot be empty and must be a number",
        "value": "33001"

    }
    RET_Buffer_size = {
        "locator": "id",
        "name": "RETBUFSIZE_0",
        "id": "RETBUFSIZE_0",
        "tooltip": "Must between 0 and 999999999",
        "error_message": "[RET Buffer Size] must between 0 and 999999999"
    }
    Generation_of_ext_headers = {
        "locator": "id",
        "name": "SCT35RTP_0",
        "id": "SCT35RTP_0"
    }
    input_protocol = {
        "locator": "id",
        "name": "IN_PROTO_0",
        "id": "IN_PROTO_0",
        "value": ""
    }
    output_protocol = {
        "locator": "id",
        "name": "OUT_PROTO_0",
        "id": "OUT_PROTO_0"
    }
    IGMP_v3_parameters={
        "locator": "xpath",
        "xpath": "//input[@value='IGMPv3 Parameters']"
    }
    ingress_source_1={
        "locator": "id",
        "name": "INGRESS_SOURCE_IP_0",
        "id": "INGRESS_SOURCE_IP_0",
        "tooltip": "Must be a valid IP address but not Multicast IP",
        "error_message": "[Ingress Source 1] must be a valid IP address but not Multicast IP"
    }
    ingress_source_2={
        "locator": "id",
        "name": "INGRESS_SOURCE_IP2_0",
        "id": "INGRESS_SOURCE_IP2_0",
        "tooltip": "Must be a valid IP address but not Multicast IP",
        "error_message": "[Ingress Source 2] must be a valid IP address but not Multicast IP"
    }
    source_rewrapper={
        "locator": "id",
        "name": "FCCRET_SOURCE_REW_0",
        "id": "FCCRET_SOURCE_REW_0"
    }
    adaptive_fcc_parameters={
        "locator": "id",
        "name": "INGRESS_SOURCE_IP2_0",
        "id": "// input[ @ value = 'Adaptative FCC Parameters']"
    }
    fcc_mode={
        "locator": "id",
        "name": "MODE_0",
        "id": "MODE_0"
    }
    fec_parameters={
        "locator": "xpath",
        "xpath": "//input[@value='FEC Parameters']"
    }
    enable_fec_generation={
        "locator": "id",
        "name": "FEC_0",
        "id": "FEC_0"
    }
    DRM_Encryption={
        "locator" : "xpath",
        "xpath" : "// input[ @ value = 'DRM Encryption']"
    }
    DRM_Encryption_percentage={
        "locator" : "id",
        "name": "DRM_MULTICAST_0",
        "id" : "DRM_MULTICAST_0"
    }
    Ingress_ECM_Address={
        "locator" : "id",
        "name" : "INGRESS_ECM_ADDRESS_0",
        "id" : "INGRESS_ECM_ADDRESS_0"
    }
    Ingress_ECM_Port={
        "locator" : "id",
        "name" :"INGRESS_ECM_PORT_0",
        "id" : "INGRESS_ECM_PORT_0"
    }
    Egress_ECM_Address={
        "locator": "id",
        "name": "EGRESS_ECM_ADDRESS_0",
        "id": "EGRESS_ECM_ADDRESS_0"
    }
    Egress_ECM_Port={
        "locator": "id",
        "name": "EGRESS_ECM_PORT_0",
        "id": "EGRESS_ECM_PORT_0"
    }
    scrambling_simulcrypt_parameters={
      #""unable to find the ID of this field"
        "locator":"xpath",
        "xpath":".//*[@id='channelDiv']/table[7]/tbody/tr/td/input"
    }
    enable_scrambling_simulcrypt={
        "locator": "id",
        "name": "ENABLE_SIMULCRYPT_0",
        "id": "ENABLE_SIMULCRYPT_0"
    }
    scrambling_profile={
        "locator": "id",
        "name": "SCRAMBLING_PROFILE_ID_0",
        "id": "SCRAMBLING_PROFILE_ID_0"
    }
    content_CAS={
     #unable to find ID for this parameter. Under this many fields are present. Didnt find the ID for all this parameters also
        "locator":"xpath",
        "xpath":".//*[@id='scramblingDiv']/table[1]/tbody[2]/tr/td[3]/input"
    }
    access_criteria={
        "locator":"id",
        "id":"acc_crit_0"
    }
    ecm_id={
        "locator":"id",
        "id":"ecm_id_0"
    }
    ecm_pid={
        "locator":"id",
        "id":" ecm_pid_0"
    }
    #List of CAS associated and Save button is not yet written under this
    enable_EMM={
        "locator": "id",
        "name": "ENABLE_EMMMUX_0",
        "id":"ENABLE_EMMMUX_0"
    }
    EMM_PAT_interval={
        "locator": "id",
        "name": "EMM_PAT_INTERVAL_0",
        "id": "EMM_PAT_INTERVAL_0"
    }
    EMM_CAT_interval={
        "locator": "id",
        "name": "EMM_CAT_INTERVAL_0",
        "id": "EMM_CAT_INTERVAL_0"
    }
    EMM_Transport_stream_identifier={
        "locator": "id",
        "name": "EMM_TS_ID_0",
        "id":"EMM_TS_ID_0"
    }
    EMM_PMT_PID={
        "locator": "id",
        "name": "EMM_PMT_PID_0",
        "id":"EMM_PMT_PID_0"
    }
    EMM_PCR_PID={
        "locator": "id",
        "name": "EMM_PCR_PID_0",
        "id":"EMM_PCR_PID_0"
    }
    EMM_PAT_Program_Id={
        "locator": "id",
        "name":"EMM_PAT_PROGRAM_ID_0",
        "id":"EMM_PAT_PROGRAM_ID_0"
    }
    EMM_Video_PID={
        "locator": "id",
        "name": "EMM_VIDEO_PID_0",
        "id":"EMM_VIDEO_PID_0"
    }
    associated_emm_mux={

    #Proper ID for this is not present
        "locator":"xpath",
        "xpath":".//*[@id='scramblingDiv']/table[2]/tbody[2]/tr/td[9]/input"
    }

    # The parameters for this has not yet been uploaded
    RTP_Data={
    #ID for this is different.
        "locator":"xpath",
        "xpath":".//*[@id='channelDiv']/table[8]/tbody/tr/td/input"
        }

    Force_RTPDATA_Header_Format={
        "locator": "id",
        "name": "FORCE_RTPDATA_0",
        "id":"FORCE_RTPDATA_0"
    }
    RET_Server_virtual_IP_address={
        "locator": "id",
        "name": "RET_ADDR_0",
        "id": "RET_ADDR_0"
    }
    RET_Server_virtual_port={
        "locator": "id",
        "name": "RET_PORT_0",
        "id": "RET_PORT_0"
    }
    FCC_Server_Virtual_IP_Address={
            "locator": "id",
            "name": "FCC_ADDR_0",
            "id": "FCC_ADDR_0"
    }
    FCC_Server_Virtual_Port={
        "locator": "id",
        "name": "FCC_PORT_0",
        "id":"FCC_PORT_0"
    }
    splicer_parameters={
        #not proper ID
        "locator":"xpath",
        "xpath":".//*[@id='channelDiv']/table[9]/tbody/tr/td/input"
    }
    splice_zone={
        "locator": "id",
        "name": "SPLICEZONE_0",
        "id":"SPLICEZONE_0"
    }
    advanced_parameters={
        #ID is not known
        "locator":"xpath",
        "xpath":".//*[@id='channelDiv']/table[10]/tbody/tr/td/input"
    }
    TS_packets_size_buffer={
        "locator": "id",
        "name": "BUF_0",
        "id": "BUF_0"
    }
    Payload_type_for_RTP_Headers={
        "locator": "id",
        "name": "PTYPE_0",
        "id": "PTYPE_0"
    }
    no_flow_control_when_sending={
        "locator": "id",
        "name": "NOPUMP_0",
        "id": "NOPUMP_0"
    }
    add_null_TS_packet={
        "locator": "id",
        "name": "TSPADD_0",
        "id": "TSPADD_0"
    }
    countdown_start_in_cdown={
        "locator": "id",
        "name": "CDOWN_0",
        "id": "CDOWN_0"
    }
    countdown_start={
        "locator": "id",
        "name": "CDOWNMS_0",
        "id": "CDOWNMS_0"
    }
    do_not_split={
        "locator": "id",
        "name": "NOSPLIT_0",
        "id": "NOSPLIT_0"
    }
    does_not_rewrap={
        "locator": "id",
        "name": "NOREWRAP_0",
        "id":"NOREWRAP_0"
    }
    do_not_add_any_TS={
        "locator": "id",
        "name": "NOADD_0",
        "id":"NOADD_0"
    }
    direct_sending={
        "locator": "id",
        "name": "DIRECT_0",
        "id":"DIRECT_0"
    }
    filter_out_on_output={
       "locator": "id",
       "name": "FILTER_0",
        "id":"FILTER_0"
    }
    fill_the_DSCP_bits={
        "locator": "id",
        "name": "DSCP_0",
        "id":"DSCP_0"
    }
    video_stream_verbosity={
        "locator": "id",
        "name": "VINFO_0",
        "id":"VINFO_0"
    }
    print_PLL_info={
        "locator": "id",
        "name": "PLLINFO_0",
        "id":"PLLINFO_0"
    }
    force_a_drift_in_wall={
        "locator": "id",
        "name": "CKFACTOR_0",
        "id":"CKFACTOR_0"
    }
    disable_the_PLL={
        "locator": "id",
        "name": "NOPLL_0",
        "id":"NOPLL_0"
    }
    force_errors_rate={
        "locator":"id",
        "name":"BER_0",
        "id":"BER_0"
    }
    insert_a_DVB_TDT_table={
        "locator": "id",
        "name": "TDT_0",
        "id":"TDT_0"
    }
    RTP_sequence_number={
        "locator": "id",
        "name": "RTPSEQ_0",
        "id":"RTPSEQ_0"
    }
    dataIn_Port={
        "locator": "id",
        "name": "DATAIN_PORT_0",
        "id":"DATAIN_PORT_0"
    }
    Time_to_delay_network={
        "locator":"id",
        "name":"TIMESHIFT_0",
        "id":"TIMESHIFT_0"
    }
    use_only_TS_level={
        "locator": "id",
        "name": "TSONLY_0",
        "id":"TSONLY_0"
    }
    advance_audio_sending={
        "locator": "id",
        "name": "AUDADV_0",
        "id":"AUDADV_0"
    }
    minimizes_the_input={
        "locator": "id",
        "name": "MINDELAY_0",
        "id":"MINDELAY_0"
    }
    add_offset_to_PCR_values={
        "locator": "id",
        "name": "PCROFFSET_0",
        "id":"PCROFFSET_0"
    }
    Insert_a_TDEC_RTP_Header={
        "locator": "id",
        "name": "TDEC_PRIO_0",
        "id":"TDEC_PRIO_0"
    }
    RTP_exended_headers={
        "locator": "id",
        "name": "CRTP_0",
        "id":"CRTP_0"
    }
    RTP_Header_size={
        "locator": "id",
        "name": "RTPHEADERSIZE_0",
        "id":"RTPHEADERSIZE_0"
    }
    Advertisement_parameters={
#ID is not found in this case
        "locator":"xpath",
        "xpath":".//*[@id='channelDiv']/table[11]/tbody/tr/td/input"
    }
    configurable={
        "locator": "id",
        "name": "CONFIGURABLE_0",
        "id":"CONFIGURABLE_0"
    }
    CCMS_id={
        "locator": "id",
        "name": "CCMSID_0",
        "id":"CCMSID_0"
    }
    splicer_FTP_upload={
        "locator": "id",
        "name": "SPLFTP_UP_0",
        "id":"SPLFTP_UP_0"
    }
    splicer_FTP_download={
        "locator": "id",
        "name": "SPLFTP_DOWN_0",
        "id":"SPLFTP_DOWN_0"
    }
    SAR_FTP_upload={
        "locator": "id",
        "name": "SARFTP_UP_0",
        "id":"SARFTP_UP_0"
    }
    SAR_HTTP_Download={
        "locator": "id",
        "name": "SARHTTP_DOWN_0",
        "id":"SARHTTP_DOWN_0"
    }
    VRS_FTP_Upload={
        "locator": "id",
        "name": "VRSFTP_UP_0",
        "id":"VRSFTP_UP_0"
    }
    VRS_FTP_Download={
        "locator": "id",
        "name": "VRSFTP_DOWN_0",
        "id":"VRSFTP_DOWN_0"
    }
    VRS_HTTP={
        "locator": "id",
        "name": "VRSHTTP_0",
        "id":"VRSHTTP_0"
    }

    mandatory_data = [
        channel_name,
        channel_number,
        source_multicast_value,
        source_port_value,
        destination_multicast_value,
        destination_port_value,
        Source_Identifier_for_RTP
    ]
