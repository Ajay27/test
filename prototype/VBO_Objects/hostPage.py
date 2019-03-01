

class hostclass:
    search_box = {
        "locator": "xpath",
        "xpath": "//input[@name='sMatrixName']"
    }
    search = {
        "locator": "xpath",
        "xpath": "//input[@value='Search']"
    }
    add_new = {
        "locator": "xpath",
        "xpath": "//input[@value='Add new Host']"
    }
    list_all_hosts = {
        "locator": "xpath",
        "xpath": "//input[@value='List all Hosts']"
    }
    type1 = {
        "locator": "id",
        "id": "TYPE_0",
        "value": "Appliance"
    }
    Hardware_revision = {
        "locator": "id",
        "id": "APPLIANCE_REVISION_0",
        "value": "3"
    }
    create_host = {
        "locator": "xpath",
        "xpath":"//input[@value='Create host']"
    }
    cancel={
        "locator":"xpath",
        "xpath":"//input[@value='Cancel']"
    }
    delete={
        "locator":"id",
        "id":"del_0"
    }
    name = {
        "locator": "id",
        "id": "NAME_0",
        "tooltip":"Cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +",
        "error_message":"[NAME] cannot be empty and cannot contain the following characters: \ / ` ; > < { } ( ) | ' '' % = +",
        "value":"test-22"
    }
    description = {
        "locator": "id",
        "id": "DESCRIPTION_0"
    }
    type = {
        "locator": "id",
        "id": "TYPE_0",
        "tooltip":"Cannot be empty"
    }
    hardware_revision = {
        "locator": "id",
        "id": "APPLIANCE_REVISION_0",
        "value": "Revision 3"
    }
    heartbeat_status = {
        "locator": "id",
        "id": 'STATUS_HB_0'
    }
    associated_networks = {
        "locator": "id",
        "id": "Associated Networks"
    }
    add_network = {
        "locator": "id",
        "id": "network_add"
    }
    modify_network = {
        "locator": "id",
        "id": "network_edit"
    }
    delete_network = {
        "locator": "id",
        "id": "network_del"
    }
    network_name = {
        "locator": "id",
        "id": "NETWORK_0",
        "error_message": "[Network Name] cannot be empty and cannot contain the following characters: \ / `; > < {}() | ' '' % = +",
        "value": "Ingress-22"
    }

    network_name1 = {
        "locator": "id",
        "id": "NETWORK_0",
        "error_message": "[Network Name] cannot be empty and cannot contain the following characters: \ / `; > < {}() | ' '' % = +",
        "value": "Egress-22"
    }

    bonding_mode = {
        "locator": "id",
        "id": "BOND_MODE_0"
    }
    interface_name = {
        "locator": "id",
        "id": "DEVICE_0",
        "value":"eth0"
    }
    interface_name1 = {
        "locator": "id",
        "id": "DEVICE_0",
        "value": "eth1"
    }
    boot_protocol = {
        "locator": "id",
        "id": "BOOTPROTO_0"
    }
    ip = {
        "locator": "id",
        "id": "IP_0",
        "value":"10.0.7.22"
    }
    ip1 = {
        "locator": "id",
        "id": "IP_0",
        "value": "10.0.6.22"
    }
    type = {
        "locator": "id",
        "id": "TYPE_NET_0",
        "value": "INGRESS"
    }
    type3 = {
        "locator": "id",
        "id": "TYPE_NET_0",
        "value": "EGRESS"
    }
    network_mask = {
        "locator": "id",
        "id": "NETMASK_0"
    }
    interface_monitor_in = {
        "locator": "id",
        "id":"IFMON_IN_0"
    }
    interface_monitor_out = {
        "locator": "id",
        "id": "IFMON_OUT_0"
    }
    list_of_slaves_1 = {
        "locator": "id",
        "id": "SLAVES1_0"
    }
    list_of_slaves_2 = {
        "locator": "id",
        "id": "SLAVES2_0"
    }
    route_associated = {
        "locator": "id",
        "id": "assnetwork"
    }
    list_of_routes = {
        "locator": "id",
        "id":"mulAvailableNetwork_0"
    }
    save_network = {
        "locator": "xpath",
        "xpath": ".//*[@id='buttonSaveNetwork']/table/tbody/tr/td[1]/input"
    }
    cancel_network ={
        "locator": "xpath",
        "xpath": ".//*[@id='buttonSaveNetwork']/table/tbody/tr/td[2]/input"
    }
    associated_vlan = {
        "locator": "id",
        "id": "Associated Vlan"
    }
    add_vlan = {
        "locator": "id",
        "id": "vlan_add"
    }
    modify_vlan = {
        "locator": "id",
        "id": "vlan_edit"
    }
    delete_vlan = {
        "locator": "id",
        "id": "vlan_del"
    }
    name_of_vlan = {
        "locator": "id",
        "id": "NAME_vlan_0"
    }
    number_of_vlans = {
        "locator": "id",
        "id": "NUM_VLANS_0"
    }
    root_id = {
        "locator": "id",
        "id": "ROOT_ID_0"
    }
    initial_ip = {
        "locator": "id",
        "id": "INITIAL_IP_0"
    }
    bit_mask = {
        "locator": "id",
        "id": "BIT_MASK_0"
    }
    types = {
        "locator": "id",
        "id": "TYPE_vlan_0"
    }
    associated_host_networks = {
        "locator": "id",
        "id": "NETWORK_FK_vlan_0"
    }
    save_vlan = {
        "locator": "xpath",
        "xpath": ".//*[@id='buttonSaveVlan']/table/tbody/tr/td[1]/input"
    }
    cancel_vlan = {
        "locator": "xpath",
        "xpath": ".//*[@id='buttonSaveVlan']/table/tbody/tr/td[2]/input"
    }
    appliance_general_parameters = {
        "locator": "id",
        "id": "Appliance General Parameters"
    }
    SNMP_Agent_listing_interface = {
        "locator": "id",
        "id": "AGENT_ADDRESS_0"
    }
    Storage_location = {
        "locator": "id",
        "id": "SYSLOG_TYPE_0"
    }
    multiple_ingress_interface = {
        "locator": "id",
        "id": "MULTIPLE_INTF_0"
    }
    host_interface_1 = {
        "locator": "id",
        "id": "DEF_INGRESSINTF_0",
        "value": "eth0"
    }
    host_interface_2 = {
        "locator": "id",
        "id": "DEF_INGRESSINTF2_0",
    }
    host_interface_outgoing = {
        "locator": "id",
        "id": "DEF_EGRESSINTF_0",
        "value": "eth1"
    }
    license = {
        "locator": "id",
        "id": "LIC_0",
        "value": "jdsgfgdsfsd"
    }
    Verb_mask = {
        "locator": "id",
        "id": "VERB_MASK_0"
    }
    associated_channels = {
        "locator": "id",
        "id": "Associated Channels"
    }
    RET_client_service = {
        "locator": "id",
        "id": "service_check_RET-Client_0"
    }
    statistics_catcher_service = {
        "locator": "id",
        "id": "service_check_Statistics Catcher_0"
    }
    linear_splicer_service = {
        "locator": "id",
        "id": "service_check_Linear Splicer_0"
    }
    RET_service = {
        "locator": "id",
        "id": "service_check_RET_0"
    }
    rewrapper_service ={
        "locator": "id",
        "id": "service_check_Rewrapper_0"
    }
    FCC_service = {
        "locator": "id",
        "id": "service_check_FCC_0"
    }
    verbosity = {
        "locator": "id",
        "id": "VERBOSITY_0"
    }
    appliance_binaries = {
        "locator": "id",
        "id": "Appliance Binaries"
    }
    rewrapper_binary = {
        "locator": "id",
        "id": "REW_0",
        "value": "rewrapper30"
    }
    monitor_binary = {
        "locator": "id",
        "id": "MON_0",
        "value": "monitor3.0"
    }
    manager_binary = {
        "locator": "id",
        "id": "ADJ_0",
        "value": "manager-3.0"
    }
    flow_shaper_binary = {
        "locator": "id",
        "id": "FLOW_0",
        "value": "flowshaper3.0"
    }
    RET_client_binary = {
        "locator": "id",
        "id": "RETCNT_0"
    }
    FCC_RET_binary = {
        "locator": "id",
        "id": "FCCRET_0"
    }
    OS_binary = {
        "locator": "id",
        "id":'OS_0',
        "value": "os3.0"
    }
    splicer_binary = {
        "locator": "id",
        "id":'SPLICER_0'
    }
    statcatcher_binary = {
        "locator": "id",
        "id": 'STATCATCHER_0'
    }
    High_Availablity = {
        "locator": "id",
        "id":'Redundancy/High Availability'
    }
    HA_mode = {
        "locator": "id",
        "id": 'HA_ROLE_0'
    }
    multicast_addr = {
        "locator": "id",
        "id": 'MONITOR_ADDR_0',
        "value":"239.1.22.1"
    }
    udp_port = {
        "locator": "id",
        "id":'MONITOR_PORT_0'
    }
    multicast_intf_cntl_channel = {
        "locator": "id",
        "id":'MONITOR_INTF_0',
        "value":"10.0.6.22"
    }
    period_ctrl_channel = {
        "locator": "id",
        "id":'TICK_CTRL_0'
    }
    period_between_error_detected_and_switchover ={
        "locator": "id",
        "id":'SWITCHOVER_TOUT_0'
    }
    time_to_wait = {
        "locator": "id",
        "id":'STARTUP_TOUT_0'
    }
    UDP_Port_exchange = {
        "locator": "id",
        "id":'MIRROR_PORT_0'
    }
    Period_consecutive_alarms = {
        "locator": "id",
        "id":'ALARM_PERIOD_0'
    }
    UDP_port_communicate = {
        "locator": "id",
        "id": 'ADJUNCT_PORT_0'
    }
    period_for_monitoring = {
        "locator": "id",
        "id":'ADJUNCT_TICK_0'
    }
    Period_monitoring_manager = {
        "locator": "id",
        "id": 'ADJUNCT_PERIOD_0'
    }
    source_join_timeout = {
        "locator": "id",
        "id": 'SOURCE_JOIN_TOUT_0'
    }
    master_in_pair = {
        "locator": "id",
        "id": 'MASTERCONF_0'
    }
    mated_appliance = {
        "locator": "id",
        "id":'REDUNDANT_FK_0'
    }
    interface_monitor = {
        "locator": "id",
        "id": 'IFMONITOR_0'
    }
    interface_monitor_period = {
        "locator": "id",
        "id": 'IFMON_PERIOD_0'
    }
    appliance_advance_parameters = {
        "locator": "id",
        "id":'Appliance advanced Parameters'
    }
    Timeout_declare_Rewrapper = {
        "locator": "id",
        "id":'APPLICATION_TOUT_0'
    }
    Period_exchange_RTP_seq_numbers = {
        "locator": "id",
        "id":'SYNC_PERIOD_0'
    }
    Period_check_if_configuration = {
        "locator": "id",
        "id":'UPDATE_PERIOD_0'
    }
    Use_Flow_Shaper = {
        "locator": "id",
        "id":'FLSH_CORES_0'
    }
    Flow_Shaper_Buffer_Size = {
        "locator": "id",
        "id": 'FLSH_BUFFER_0'
    }
    memory_percentage = {
        "locator": "id",
        "id": 'MCACHESIZE_0'
    }
    save = {
        "locator": "xpath",
        "xpath": "//input[@type='Submit']"
    }
    cancel = {
        "locator": "xpath",
        "xpath": ".//*[@id='buttonSaveHost']/table/tbody/tr/td[3]/input"
    }
    mandatory_data0 = [
            name
]
    mandatory_data = [
            network_name,
            interface_name,
            ip,
            type,
]
    mandatory_data1 = [
        network_name1,
        interface_name1,
        ip1,
        type3
]
    mandatory_data2 = [
        host_interface_1,
        host_interface_outgoing,
        license
]
    mandatory_data3 = [
        rewrapper_binary,
        monitor_binary,
        manager_binary,
        flow_shaper_binary,
        OS_binary
]
    mandatory_data4 = [
        multicast_addr,
        multicast_intf_cntl_channel
]