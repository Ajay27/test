""" This file contains the details of each field of rewrapper page"""

class retclass :
    filename = {
        "locator": "xpath",
        "xpath": "//input[@type='Text']"
    }

    search = {
        "locator": "xpath",
        "xpath": "//input[@value='Search']"
    }

    add_new_ret = {
        "locator": "xpath",
        "xpath": "//input[@value='Add new RET Service ']"
    }

    list_all_ret = {
        "locator": "xpath",
        "xpath": "//input[@value='List all RET Service']"
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
        "error_message": "[Associated Host] cannot be empty",
        "value":"App-52"
    }

    name = {
        "locator": "id",
        "name": "NAME_0",
        "id": "NAME_0",
        "tooltip": """Cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = + """,
        "error_message": "[Name] cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +",
        "value":"RET-52"
    }

    ret_basics = {
        "locator":"id",
        "id": "basicBtn"
    }

    IP_addr_appliance = {
        "locator": "id",
        "name": "RET_INTF_0",
        "id": "RET_INTF_0",
        "tooltip": """Cannot be empty and must be a valid IP address but not multicast IP """,
        "error_message": "[IP Addr. Appliance Intf. delivering RET] cannot be empty and must be a valid IP address but not multicast IP",
        "value": "127.0.0.1"
    }

    RET_RTCP_Service_Port = {
        "locator": "id",
        "name": "RET_PORT_0",
        "id": "RET_PORT_0",
        "tooltip": """ Cannot be empty and must between 1024 and 65535 """,
        "error_message": "[RET RTCP service Port] cannot be empty and must be between 1024 and 65535",
        "value": "4098"
    }

    Perc_nominal_Bandwidth_for_RET ={
        "locator": "id",
        "name": "PERCENT_0",
        "id": "PERCENT_0",
        "tooltip": """Cannot be empty and must between 0 and 100 """,
        "error_message": "[Percentage nominal bandwidth for RET] cannot be empty and must be between 0 and 100",
        "value" : "20"
    }

    Buffer_size = {
        "locator": "id",
        "name": "BUFFER_0",
        "id": "BUFFER_0",
        "tooltip": """Cannot be empty and must between 0 and 1000 """,
        "error_message": "[Buffer size (in ms)] cannot be empty and must be between 0 and 1000",
        "value": "350"
    }

    ret_advanced = {
        "locator" : "id",
        "id" : "advancedBtn"
    }
    rtp_payload_type ={
        "locator": "id",
        "name": "RTP_TYPE_0",
        "id": "RTP_TYPE_0",
        "tooltip": """Cannot be empty and must between 99 and 127 or 33""",
        "error_message": "[RTP Payload Type] cannot be empty and must be between 99 and 127 or 33",
        "value": "99"
    }

    number_of_threads = {
        "locator" : "id",
        "name":"RET_THREAD_0",
        "id":"RET_THREAD_0",
        "tooltip" : "Cannot be empty and must between 1 and 16 ",
        "error_message" : "[Number of threads to use for RET] cannot be empty and must be between 1 and 16",
        "value":"4"
    }

    number_of_concurrent = {
        "locator" : "id",
        "name": "RET_CLIENT_0",
        "id": "RET_CLIENT_0",
        "tooltip" : "Cannot be empty and must between 100 and 1000",
        "error_message" : "[Number of concurrent clients] cannot be empty and must be between 100 and 1000",
        "value":"500"
    }

    total_amt_of_bandwidth = {
        "locator": "id",
        "name": "RET_BW_0",
        "id": "RET_BW_0",
        "tooltip": "Cannot be empty and must between 0 and 400",
        "error_message": "[Total amount of bandwidth for RET (in ms)] cannot be empty and must be between 0 and 400",
        "value" : "400"
    }

    sampling_period_time = {
        "locator": "id",
        "name": "SAMPLE_0",
        "id": "SAMPLE_0",
        "tooltip": "Cannot be empty and must between 0 and 999999999",
        "error_message": "[Sampling Period Time (in ms)] cannot be empty and must be between 0 and 999999999",
        "value" : "20"
    }

    number_sample_periods ={
        "locator": "id",
        "name": "RETRY_0",
        "id": "RETRY_0",
        "tooltip": "Cannot be empty and must between 0 and 999999999",
        "error_message": "[Num. sample periods bef. Retry RET] cannot be empty and must be between 0 and 999999999",
        "value" : "5"
    }

    debugging_port = {
        "locator": "id",
        "name": "RET_DEBUG_0",
        "id": "RET_DEBUG_0",
        "tooltip": "Must between 1024 and 65535 or 0",
        "error_message": "[Debugging Port] must be between 1024 and 65535 or 0",
        "value" : "0"
    }

    operation_flags = {
        "locator": "id",
        "name": "RET_FLAGS_0",
        "id": "RET_FLAGS_0",
        "tooltip": "Must between 0x0000 and 0xFFFF",
        "error_message": "[Operation Flags] must be between 0x0000 and 0xFFFF",
        "value" : "0x0000"
    }

    ret_input_threads = {
        "locator": "id",
        "name": "RET_IN_THREAD_0",
        "id": "RET_IN_THREAD_0",
        "tooltip": "Must between 1 and 16",
        "error_message": "[RET Input Threads] must be between 1 and 16",
        "value" : "12"
    }

    mandatory_data = [
            host_associated,
            name
    ]
