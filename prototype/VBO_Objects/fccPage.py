""" This file contains the details of each field of rewrapper page"""

class fccclass:
    filename = {
        "locator": "xpath",
        "xpath": "//input[@type='Text']"
    }

    search = {
        "locator": "xpath",
        "xpath": "//input[@value='Search']"
    }

    add_new_fcc = {
        "locator": "xpath",
        "xpath": "//input[@value='Add new FCC Service ']"
    }

    list_all_fcc = {
        "locator": "xpath",
        "xpath": "//input[@value='List all FCC Service']"
    }

    delete = {
        "locator": "xpath",
        "xpath": "//input[@disabled='true']"
    }

    host_associated = {
        "locator": "id",
        "name": "HOST_FK_0",
        "id": "HOST_FK_0",
        "tooltip": "Cannot be empty",
        "error_message": "[Host Associated] cannot be empty",
        "value": "App-52"
    }
    name = {
        "locator": "id",
        "name": "NAME_0",
        "id": "NAME_0",
        "tooltip": """Cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = + """,
        "error_message": "[Name] cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +",
        "value": "Fcc-52"
    }

    fcc_basics = {
        "locator":"id",
        "id": "basicBtn"
    }

    IP_addr_appliance = {
        "locator": "id",
        "name": "FCC_INTF_0",
        "id": "FCC_INTF_0",
        "tooltip": """Cannot be empty and must be a valid IP address but not multicast IP """,
        "error_message": "[IP Addr. Appliance Intf. delivering FCC Service] cannot be empty and must be a valid IP address but not multicast IP",
        "value": "127.0.0.1"
    }

    FCC_RTCP_Service_Port_Number = {
        "locator": "id",
        "name": "FCC_PORT_0",
        "id": "FCC_PORT_0",
        "tooltip": """ Cannot be empty and must between 1024 and 65535 """,
        "error_message": "[FCC RTCP Service Port Number] cannot be empty and must be between 1024 and 65535",
        "value": "4096"
    }

    FCC_Mode ={
        "locator": "id",
        "name": "MODE_0",
        "id": "MODE_0",
        "tooltip": """Cannot be empty """,
        "error_message": "[FCC Mode] cannot be empty"
    }

    Perc_nominal_Bandwidth_used_to_catchup ={
        "locator": "id",
        "name": "E0_0",
        "id": "E0_0",
        "tooltip": """Cannot be empty and must between 0 and 400 """,
        "error_message": "[Perc. nominal Bandwidth used to catch up to multi. stream] cannot be empty and must be between 0 and 400"
    }

    Perc_nominal_Bandwidth_used_for_handover = {
        "locator": "id",
        "name": "E1_0",
        "id": "E1_0",
        "tooltip": """Cannot be empty and must between 0 and 400 """,
        "error_message": "[Perc. nominal Bandwidth used for handover to multi. stream] cannot be empty and must be between 0 and 400"
    }

    fcc_advanced = {
        "locator" : "id",
        "id" : "advancedBtn"
    }
    number_of_threads = {
        "locator" : "id",
        "name":"FCC_THREAD_0",
        "id":"FCC_THREAD_0",
        "tooltip" : "Cannot be empty and must between 1 and 16",
        "error_message" : "[Number of threads to use in FCC Service] cannot be empty and must be between 1 and 16"
    }

    number_of_concurrent = {
        "locator" : "id",
        "name": "FCC_CLIENT_0",
        "id": "FCC_CLIENT_0",
        "tooltip" : "Cannot be empty and must between 100 and 1000",
        "error_message" : "[Number concurrent Clients in FCC Service] cannot be empty and must be between 100 and 1000"
    }

    total_amt_of_bandwidth = {
        "locator": "id",
        "name": "FCC_BW_0",
        "id": "FCC_BW_0",
        "tooltip": "Cannot be empty and must between 0 and 4000",
        "error_message": "[Total amount of Bandwidth (in Mbps) for FCC Service] cannot be empty and must be between 0 and 4000"
    }

    fcc_time_max_igmp_join ={
        "locator": "id",
        "name": "JMAX_0",
        "id": "JMAX_0",
        "tooltip": "Cannot be empty and must between 0 and 300",
        "error_message": "[FCC Time Max IGMP Join (in ms)] cannot be empty and must be between 0 and 300"
    }
    fcc_time_min_igmp_join = {
        "locator": "id",
        "name": "JMIN_0",
        "id": "JMIN_0",
        "tooltip": "Cannot be empty and must between 0 and 999999999",
        "error_message": "[FCC Time Min IGMP Join (in ms)] cannot be empty and must be between 0 and 999999999"
    }
    fcc_time_max_igmp_leave = {
        "locator": "id",
        "name": "LMAX_0",
        "id": "LMAX_0",
        "tooltip": "Cannot be empty and must between 0 and 999999999",
        "error_message": "[FCC Time Max IGMP Leave (in ms)] cannot be empty and must be between 0 and 999999999"
    }

    fcc_time_client = {
        "locator": "id",
        "name": "DELAY_0",
        "id": "DELAY_0",
        "tooltip": "Cannot be empty and must between 0 and 999999999",
        "error_message": "[FCC Time client will buffer content before (in ms)] cannot be empty and must be between 0 and 999999999"
    }

    fcc_time_difference = {
        "locator": "id",
        "name": "MCDIFF_0",
        "id": "MCDIFF_0",
        "tooltip": "Cannot be empty and must between 0 and 999999999",
        "error_message": "[FCC Time Diff. bw multicast arrival at Server and Client (in ms)] cannot be empty and must be between 0 and 999999999"
    }

    fcc_max_video = {
        "locator": "id",
        "name": "DENT_MAX_0",
        "id": "DENT_MAX_0",
        "tooltip": "Cannot be empty and must between 0 and 999999999",
        "error_message": "[FCC Max Video Frames to drop during catch up] cannot be empty and must be between 0 and 999999999"
    }

    time_allowed_to_complete = {
        "locator": "id",
        "name": "FCC_TIMEOUT_MSEC_0",
        "id": "FCC_TIMEOUT_MSEC_0",
        "tooltip": "Cannot be empty and must between 1000 and 999999999",
        "error_message": "[Time allowed to complete the FCC transaction (in ms)] cannot be empty and must be between 1000 and 999999999"
    }

    debugging_port = {
        "locator": "id",
        "name": "FCC_DEBUG_0",
        "id": "FCC_DEBUG_0",
        "tooltip": "Must between 1024 and 65535 or 0",
        "error_message": "[Debugging Port] must be between 1024 and 65535 or 0"
    }

    operation_flags = {
        "locator": "id",
        "name": "FCC_FLAGS_0",
        "id": "FCC_FLAGS_0",
        "tooltip": "Must between 0x0000 and 0xFFFF",
        "error_message": "[Operation Flags] must be between 0x0000 and 0xFFFF"
    }

    fcc_input_threads = {
        "locator": "id",
        "name": "FCC_IN_THREAD_0",
        "id": "FCC_IN_THREAD_0",
        "tooltip": "Must between 1 and 16",
        "error_message": "[FCC Input Threads] must be between 1 and 16"
    }

    mandatory_data = [
            host_associated,
            name
    ]