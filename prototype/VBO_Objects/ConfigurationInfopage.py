""" This file contains the details of each field of configuration info page"""


class ConfigurationInfopage:
    heartbeat_ip = {
        "locator": "id",
        "name": "HBIP_0",
        "id": "HBIP_0",
        "tooltip": "Cannot be empty and must be a valid IP address but not multicast IP",
        "error_message": "[Heartbeat IP]cannot be empty and must be a valid IP address but not multicast IP",
        "value": "10.92.10.176"

    }

    heartbeat_port = {
        "locator": "id",
        "id": "HBPORT_0",
        "tooltip": "Cannot be empty and must between 0 and 65535",
        "error_message": "[Heartbeat Port] cannot be empty and must between 0 and 65535",
        "value": "8090"
    }

    heartbeat_limit = {
        "locator": "id",
        "id": "HBLIMIT_0",
        "tooltip": "Cannot be empty and must between 0 and 99999",
        "error_message": "[Heartbeat Limit] cannot be empty and must between 0 and 99999",
        "value": "50"
    }

    heartbeat_period = {
        "locator": "id",
        "id": "HBPERIOD_0",
        "tooltip": "Cannot be empty and must between 0 and 99999",
        "error_message": "[Heartbeat Period (in seconds)] cannot be empty and must between 0 and 99999",
        "value": "4"
    }

    syslog_ip = {
        "locator": "id",
        "id": "SYSLOGIP_0",
        "tooltip": "Cannot be empty and must be a valid IP address but not multicast IP",
        "error_message": "[Syslog IP]cannot be empty and must be a valid IP address but not multicast IP",
        "value": "10.92.10.176"
    }

    sdp_ip_address = {
        "locator": "id",
        "id": "SDP_SERVER_0",
        "tooltip": "Cannot be empty and must be a valid IP address but not multicast IP",
        "error_message": "[SDP IP Address]cannot be empty and must be a valid IP address but not multicast IP",
        "value": "10.92.10.181"
    }

    sdp_port = {
        "locator": "id",
        "id": "SDP_PORT_0",
        "tooltip": "Cannot be empty and must between 0 and 65535",
        "error_message": "[SDP Port] cannot be empty and must between 0 and 65535",
        "value": "8080"
    }

    local_timezone = {
        "locator": "id",
        "id": "TIMEZONE_0",
        "tooltip": "Cannot be empty",
        "error_message": "[Local Timezone] cannot be empty",
        "value": "Europe/Madrid"
    }

    banner_displayed = {
        "locator": "id",
        "id": "BANNER_LOGIN_0",
        "tooltip": "Cannot be empty",
        "error_message": "[Banner Displayed] cannot be empty",
        "value": "ALCATEL-LUCENT - Unathorized access is forbidden"
    }

    # it is a dropdown list
    igmp_protocol = {
        "locator": "id",
        "id": "IGMP_0",
        "tooltip": "Cannot be empty",
        "error_message": "[IGMP Protocol] cannot be empty",
        "value": "3"
    }

    delay_bw_asset_restart = {
        "locator": "id",
        "id": "DLY_BW_RESTART_REW_0",
        "tooltip": "Cannot be empty and must between 2000 and 30000",
        "error_message": "[Delay Between Asset Restart (in ms)] cannot be empty and must between 2000 and 30000",
        "value": "2000"
    }

    delay_bw_switching_sources = {
        "locator": "id",
        "id": "DLY_BW_SRC_FLIP_0",
        "tooltip": "Cannot be empty and must between 1 and 30",
        "error_message": "[Delay Between Switching Sources For The Same Asset "
                         "(in minutes)] cannot be empty and must between 1 and 30",
        "value": "5"
    }

    rtp_data = {
        "locator": "id",
        "id": "RTPDATA_0",
        "tooltip": "Must be a url",
        "error_message": "[RTP DATA] must be a url",
        "value": "http://10.92.10.184:80/appliance/rwstb/config"
    }

    # it is a dropdown list
    send_rtp_ranges = {
        "locator": "id",
        "id": "RTPRANGES_0",
        "tooltip": None,
        "error_message": None,
        "value": "Send"
    }

    # it is a checkbox
    rewrapper_ping = {
        "locator": "id",
        "id": "ICMP_DYNAMIC_DISABLE_0",
        "tooltip": None,
        "error_message": None

    }

    ip_statistic_catcher_periodic = {
        "locator": "id",
        "id": "DVB_P_XR_ADDRESS_0",
        "tooltip": "Cannot be empty and must be a valid IP address but not multicast IP",
        "error_message": "[IP Statistic Catcher Periodic DVB-IPTV XRs]"
                         "cannot be empty and must be a valid IP address but not multicast IP",
        "value": "10.92.10.220"
    }

    udp_port_statistic_catcher_periodic = {
        "locator": "id",
        "id": "DVB_P_XR_PORT_0",
        "tooltip": "Cannot be empty and must between 0 and 65535",
        "error_message": "[UDP Port Statistic Catcher Periodic DVB-IPTV XRs] cannot be empty"
                         " and must between 0 and 65535",
        "value": "4094"
    }

    ip_statistic_catcher_on_demand = {
        "locator": "id",
        "id": "DVB_XR_ADDRESS_0",
        "tooltip": "Cannot be empty and must be a valid IP address but not multicast IP",
        "error_message": "[IP Statistic Catcher On-Demand DVB-IPTV XRs] cannot be empty "
                         "and must be a valid IP address but not multicast IP",
        "value": "10.92.10.220"
    }

    udp_port_statistic_catcher_on_demand = {
        "locator": "id",
        "id": "DVB_XR_PORT_0",
        "tooltip": "Cannot be empty and must between 0 and 65535",
        "error_message": "[UDP Port Statistic Catcher On-Demand DVB-IPTV XRs] cannot be empty"
                         " and must between 0 and 65535",
        "value": "4094"
    }

    ip_statistic_catcher = {
        "locator": "id",
        "id": "STATS_CATCHER_ADDRESS_0",
        "tooltip": "Must be a valid IP address",
        "error_message": "[IP of the statistics catcher] must be a valid IP address",
        "value": "10.92.10.220"
    }

    port_statistic_catcher = {
        "locator": "id",
        "id": "STATS_CATCHER_PORT_0",
        "tooltip": "Cannot be empty and must between 1024 and 65535 or 0",
        "error_message": "[Port of the statistics catcher] cannot be empty"
                         " and must between 1024 and 65535 or 0",
        "value": "4094"
    }

    period_sending_statistics_values = {
        "locator": "id",
        "id": "STATS_PERIOD_0",
        "tooltip": "Cannot be empty and must between 0 and 65535",
        "error_message": "[Period for sending statistics values (in seconds)]"
                         " cannot be empty and must between 0 and 65535",
        "value": "60"
    }

    # STB Client profile parameters starts from here...visible only if "STB Client profile parameters" button is pressed.
    Timeout_option_fcc = {
        "locator": "id",
        "id": "FCCTIMEOUT_0",
        "tooltip": "Must be a number",
        "error_message": "[Period for sending statistics values (in seconds)] "
                         "cannot be empty and must between 0 and 65535",

    }

    unicast_timeout_option_ = {
        "locator": "id",
        "id": "UNICAST_TIMEOUT_0",
        "tooltip": "Must be a number",
        "error_message": "[Unicast Timeout for the option FCC (in ms)] must be a number",

    }

    ret_max_period = {
        "locator": "id",
        "id": "RET_MAXREQ_0",
        "tooltip": "Must be a number",
        "error_message": "[RET Max Packets per period] must be a number",

    }

    ret_sample_period = {
        "locator": "id",
        "id": "RET_PERIOD_0",
        "tooltip": "Must be a number",
        "error_message": "[RET sample period (in seconds)] must be a number",

    }

    ret_blackout_period = {
        "locator": "id",
        "id": "RET_BLACKOUT_0",
        "tooltip": "Must be a number",
        "error_message": "[RET blackout period (in seconds)] must be a number",
        # "value" : ""
    }

    mode_option_fcc_client_stb = {
        "locator": "id",
        "id": "FCCMODE_0",
        "tooltip": "Must be a number",
        "error_message": "[Mode for the option FCC for Client STB] must be a number",
        # "value" : ""
    }

    time_delay_option_fcc = {
        "locator": "id",
        "id": "FCCDELAY_0",
        "tooltip": "Must be a number",
        "error_message": "[Time for delay for the option FCC (in ms)] must be a number",
        # "value" : ""
    }

    fcc_max_video_frames = {
        "locator": "id",
        "id": "FCCDENTMAX_0",
        "tooltip": "Must be a number",
        "error_message": "[FCC Max Video Frames] must be a number",
        # "value" : ""
    }

    fcc_time_max_igmp_join = {
        "locator": "id",
        "id": "FCCJMAX_0",
        "tooltip": "Must be a number",
        "error_message": "[FCC Time Max IGMP Join (in ms)] must be a number",
        # "value" : ""
    }

    fcc_time_min_igmp_join = {
        "locator": "id",
        "id": "FCCJMIN_0",
        "tooltip": "Must be a number",
        "error_message": "[FCC Time Min IGMP Join (in ms)] must be a number",
        # "value" : ""
    }

    fcc_time_max_igmp_leave = {
        "locator": "id",
        "id": "FCCLMAX_0",
        "tooltip": "Must be a number",
        "error_message": "[FCC Time Max IGMP Leave (in ms)] must be a number",
        # "value" : ""
    }

    ret_payload_type = {
        "locator": "id",
        "id": "RETRTPTYPE_0",
        "tooltip": "Must be a number",
        "error_message": "[RET Payload Type] must be a number",
        # "value" : ""
    }

    ret_buffer_size = {
        "locator": "id",
        "id": "RETBUFSIZE_0",
        "tooltip": "Must be a number",
        "error_message": "[RET Buffer Size (in ms)] must be a number",
        # "value" : ""
    }

    sample = {
        "locator": "id",
        "id": "RETSAMPLE_0",
        "tooltip": "Cannot be empty and must between 0 and 65535",
        "error_message": "[SAMPLE] cannot be empty and must between 0 and 65535",
        # "value" : ""
    }

    retry = {
        "locator": "id",
        "id": "RETRETRY_0",
        "tooltip": "Cannot be empty and must between 0 and 65535",
        "error_message": "[RETRY] cannot be empty and must between 0 and 65535",
        # "value" : ""
    }

    stb_client_profile_parameters = {
        "locator": "xpath",
        "xpath": "//input[@value='STB Client profile parameters']",
        # "value" : ""
    }

    license_management = {
        "locator": "xpath",
        "xpath": "//input[@value='License Management']",
        # "value" : ""
    }

    browse = {
        "locator": "id",
        "id": "LicenseFileName_BIN_0",
        # "value" : ""
    }

    save = {
        "locator": "xpath",
        "xpath": "//input[@type='Submit']",
        # "value" : ""
    }

    save_download = {
        "locator": "id",
        "id": "saveDownload",
        # "value" : ""
    }

    cancel = {
        "locator": "xpath",
        "id": "//input[@value='Cancel']",
        # "value" : ""
    }

    mandatory_data = [
        heartbeat_ip,
        heartbeat_port,
        heartbeat_limit,
        heartbeat_period,
        syslog_ip,
        sdp_ip_address,
        sdp_port,
        local_timezone,
        banner_displayed,
        igmp_protocol,
        delay_bw_asset_restart,
        delay_bw_switching_sources,
        ip_statistic_catcher_periodic,
        udp_port_statistic_catcher_periodic,
        ip_statistic_catcher_on_demand,
        udp_port_statistic_catcher_on_demand,
        ip_statistic_catcher,
        port_statistic_catcher,
        period_sending_statistics_values
    ]
