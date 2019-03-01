"""This file contains link to different pages in sdp"""
from ConfigurationInfopage import ConfigurationInfopage
from hostPage import hostclass
from rewrapperPage import rewrapperclass
from fccPage import fccclass
from retPage import retclass
from statCatcherPage import stat_catcherclass
from clientSTBPage import clientSTBclass
from areaPage import areaclass
from groupPage import groupclass
from regionPage import regionclass
from systemservicesPage import systemserviceclass
from binaryPage import binaryclass
from channelPage import channelclass
from usersmaintenancePage import usersmaintclass
from sdpciPage import sdpciclass
from sdpcmsPage import sdpcmsclass

global_configuration = "//span[contains(.,'Global Configuration')]"

configuration_info = (global_configuration, "//td[contains(.,'Configuration Info')]", ConfigurationInfopage)
users_maintenance = (global_configuration,"//td[contains(.,'Users Maintenance')]", usersmaintclass)
sdp_cms = (global_configuration,"//td[contains(.,'SDP-CMS')]",sdpcmsclass)
syslog_gui = (global_configuration,"//td[contains(.,'Syslog GUI')]")
sdp_ci = (global_configuration,"// td[contains(., 'SDP-CI')]",sdpciclass)

appliance_configuration = "//span[contains(.,'Appliance Configuration')]"

host = (appliance_configuration,  "//td[contains(.,'Host')]",hostclass)
network = (appliance_configuration,  "//td[contains(.,'Network')]")
route = (appliance_configuration, "//td[contains(.,'Route')]")
vlan = (appliance_configuration, "//td[contains(.,'VLAN')]")
system_service_configuration =  (appliance_configuration, "//td[contains(.,'System Service Configuration')]",systemserviceclass)
binary = (appliance_configuration, "//td[contains(.,'Binary')]",binaryclass)
channel = (appliance_configuration, "//td[contains(.,'Channel')]",channelclass)

appliance_services = "//span[contains(.,'Appliance Services')]"

rewrapper = (appliance_services, "//td[contains(.,'Rewrapper')]", rewrapperclass)
fcc = (appliance_services, "//td[contains(.,'FCC')]", fccclass)
ret = (appliance_services, "//td[contains(.,'RET')]",retclass)
ret_client = (appliance_services, "//td[contains(.,'RET Client')]")
linear_splicer = (appliance_services, "//td[contains(.,'Linear Splicer')]")
statistics_catcher = (appliance_services, "//td[contains(.,'Statistics Catcher')]",stat_catcherclass)

topology="//span[contains(.,'Topology')]"

client_stb = (topology, "//td[contains(.,'Client STB')]", clientSTBclass)
area = (topology,"//td[contains(.,'Area')]", areaclass)
region = (topology,"//td[contains(.,'Region')]",regionclass)
group = (topology,"//td[contains(.,'Group')]",groupclass)