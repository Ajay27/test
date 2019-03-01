class regionclass:
    filename = {
        "locator": "xpath",
        "xpath": "//input[@type='Text']"
    }
    search = {
        "locator": "xpath",
        "xpath": "//input[@value='Search']"
    }

    add_new_region = {
        "locator": "xpath",
        "xpath": "//input[@value='Add new Region']"
    }

    list_all_regions = {
        "locator": "xpath",
        "xpath": "//input[@value='List all Regions']"
    }

    delete = {
        "locator": "xpath",
        "xpath": "//input[@disabled='true']"
    }

    name = {
        "locator": "id",
        "name": "NAME_0",
        "id": "NAME_0",
        "tooltip": "Cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +",
        "error_message": "[Description] cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +",
        "value":"region-52"
    }

    period_sending = {
        "locator": "id",
        "name": "DVB_P_XR_PERIOD_0",
        "id": "DVB_P_XR_PERIOD_0",
        "tooltip": "Cannot be empty and must between 60 and 10080 or 0",
        "error_message": "[Period sending Periodic DVB-IPTV XRs (minutes)] cannot be empty and must between 60 and 10080 or 0"
    }

    ip_statistic_catcher = {
        "locator": "id",
        "name": "DVB_P_XR_ADDRESS_0",
        "id": "DVB_P_XR_ADDRESS_0",
        "tooltip": "Cannot be empty and must be a valid IP address but not multicast IP",
        "error_message": "[IP Statistic Catcher Periodic DVB-IPTV XRs] cannot be empty and must be a valid IP address but not multicast IP"
    }

    udp_port = {
        "locator": "id",
        "name": "DVB_P_XR_PORT_0",
        "id": "DVB_P_XR_PORT_0",
        "tooltip": "Cannot be empty and must between 0 and 65535",
        "error_message": "[UDP Port Statistic Catcher Periodic DVB-IPTV XRs] cannot be empty and must between 0 and 65535"
    }

    daily_offset = {
        "locator": "id",
        "name": "XR_DAILY_OFFSET_0",
        "id": "XR_DAILY_OFFSET_0",
        "tooltip": "Cannot be empty and must between -14:00 and +14:00",
        "error_message": "[Daily Offset (hh:mm)] cannot be empty and must between -14:00 and +14:00"
    }

    ip_statistic_catcher_on_demand = {
        "locator": "id",
        "name": "DVB_XR_ADDRESS_0",
        "id": "DVB_XR_ADDRESS_0",
        "tooltip": "Cannot be empty and must be a valid IP address but not multicast IP",
        "error_message": "[IP Statistic Catcher On-Demand DVB-IPTV XRs] cannot be empty and must be a valid IP address but not multicast IP"
    }

    udp_port_statistic_catcher = {
        "locator": "id",
        "name": "DVB_XR_PORT_0",
        "id": "DVB_XR_PORT_0",
        "tooltip": "Cannot be empty and must between 0 and 65535",
        "error_message": "[UDP Port Statistic Catcher On-Demand DVB-IPTV XRs] cannot be empty and must between 0 and 65535"
    }
    scramble_sensitive_data = {
        "locator": "id",
        "name": "XR_SCRAMBLE_0",
        "id": "XR_SCRAMBLE_0",
        "tooltip": "Cannot be empty and must between 0 and 1",
        "error_message": "[Scramble Sensitive Data] cannot be empty and must between 0 and 1"
    }
    send_rtp_data = {
        "locator": "id",
        "name": "RTPDATA_0",
        "id": "RTPDATA_0",
        "tooltip": "Send RTPDATA can not be empty ",
        "error_message": "Send RTPDATA can not be empty"
    }
    mandatory_data = [
        name
    ]
