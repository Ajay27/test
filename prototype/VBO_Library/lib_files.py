import sys
import error
import log
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

from Core_Libraries.Application_Utilities.sdputils import get_element, fill_mandatory2, fill_mandatory3, \
    fill_mandatory4, fill_mandatory0
from Core_Libraries.Application_Utilities.sdputils import fill_mandatory
from Core_Libraries.Application_Utilities.sdputils import fill_mandatory1
from Core_Libraries.Application_Utilities.sdputils import insert_value as insert_value
from Core_Libraries.Application_Utilities.sdputils import save as save1
from Core_Libraries.Application_Utilities.sdputils import assertionerror
#from Core_Libraries.Application_Utilities.sdputils import *
from VBO_Objects.sdppo import rewrapper
from VBO_Objects.sdppo import host
from VBO_Objects.sdppo import fcc
from VBO_Objects.sdppo import ret
from VBO_Objects.sdppo import statistics_catcher
from VBO_Objects.sdppo import client_stb
from VBO_Objects.sdppo import area
from VBO_Objects.sdppo import group
from VBO_Objects.sdppo import region
from VBO_Objects.sdppo import system_service_configuration
from VBO_Objects.sdppo import binary
from VBO_Objects.sdppo import users_maintenance
from VBO_Objects.sdppo import sdp_ci
from VBO_Objects.sdppo import sdp_cms
from VBO_Objects.sdppo import channel

from VBO_Objects.rewrapperPage import rewrapperclass
from VBO_Objects.hostPage import hostclass
from VBO_Objects.fccPage import fccclass
from VBO_Objects.retPage import retclass
from VBO_Objects.statCatcherPage import stat_catcherclass as sc
from VBO_Objects.clientSTBPage import clientSTBclass
from VBO_Objects.areaPage import areaclass
from VBO_Objects.groupPage import groupclass
from VBO_Objects.regionPage import regionclass
from VBO_Objects.systemservicesPage import systemserviceclass
from VBO_Objects.binaryPage import binaryclass
from VBO_Objects.usersmaintenancePage import usersmaintclass
from VBO_Objects.sdpciPage import sdpciclass
from VBO_Objects.sdpcmsPage import sdpcmsclass
from VBO_Objects.channelPage import channelclass

import time
def str_to_class(str):
    return getattr(sys.modules[__name__],str)

def get_dict(x):
    if x == "sdpci":
        return sdpciclass, sdp_ci
    if x == "sdpcms":
        return sdpcmsclass, sdp_cms
    if x == "binary":
        return binaryclass, binary
    if x == "channel":
        return channelclass, channel

def click(driver, button):

    locator = button["locator"]
    get_element(driver, locator, button[locator]).click()

class  Is_text_present(object):
    def __init__(self, text):
        self.text = text

    def __call__(self, driver):
        return str(self.text) in driver.page_source

def is_present(driver, field):

    flag = 1
    locator = field["locator"]
    try:
        element = get_element(driver, locator, field[locator])
    except:
        flag = 0

    return flag

def create_rewrapper(driver):
    time.sleep(1)
    get_element(driver,rewrapperclass.add_new_rewrapper["locator"],rewrapperclass.add_new_rewrapper["xpath"]).click()
    fill_mandatory(driver,rewrapper)

def create_new_host(driver):
    get_element(driver,hostclass.add_new["locator"],hostclass.add_new["xpath"]).click()
    select = Select(get_element(driver, hostclass.type1["locator"], hostclass.type1["id"]))
    select.select_by_value('0')
    select1 = Select(get_element(driver, hostclass.Hardware_revision["locator"], hostclass.Hardware_revision["id"]))
    select1.select_by_value('3')
    get_element(driver, hostclass.create_host["locator"], hostclass.create_host["xpath"]).click()
    get_element(driver, hostclass.associated_networks["locator"], hostclass.associated_networks["id"]).click()
    get_element(driver, hostclass.add_network["locator"], hostclass.add_network["id"]).click()
    fill_mandatory(driver,host)
    get_element(driver, hostclass.save_network["locator"], hostclass.save_network["xpath"]).click()
    get_element(driver, hostclass.add_network["locator"], hostclass.add_network["id"]).click()
    fill_mandatory1(driver,host)
    get_element(driver, hostclass.save_network["locator"], hostclass.save_network["xpath"]).click()
    get_element(driver, hostclass.appliance_general_parameters["locator"], hostclass.appliance_general_parameters["id"]).click()
    fill_mandatory2(driver,host)
    time.sleep(6)
    get_element(driver, hostclass.rewrapper_service["locator"], hostclass.rewrapper_service["id"]).click()
    get_element(driver, hostclass.appliance_binaries["locator"], hostclass.appliance_binaries["id"]).click()
    time.sleep(4)
    fill_mandatory3(driver, host)
    time.sleep(4)
    get_element(driver, hostclass.High_Availablity["locator"], hostclass.High_Availablity["id"]).click()
    fill_mandatory4(driver, host)
    get_element(driver, hostclass.save["locator"], hostclass.save["xpath"]).click()

def create_new_fcc(driver):
    time.sleep(1)
    get_element(driver,fccclass.add_new_fcc["locator"],fccclass.add_new_fcc["xpath"]).click()
    time.sleep(1)
    get_element(driver, fccclass.fcc_basics["locator"], fccclass.fcc_basics["id"]).click()
    time.sleep(1)
    get_element(driver, fccclass.fcc_advanced["locator"], fccclass.fcc_advanced["id"]).click()
    fill_mandatory(driver,fcc)


def create_new_ret(driver):
    time.sleep(1)
    get_element(driver,retclass.add_new_ret["locator"],retclass.add_new_ret["xpath"]).click()
    time.sleep(1)
    get_element(driver,retclass.ret_basics["locator"],retclass.ret_basics["id"]).click()
    time.sleep(1)
    get_element(driver,retclass.ret_advanced["locator"],retclass.ret_advanced["id"]).click()
    fill_mandatory(driver,ret)

def create_new_stat_catcher(driver):
    time.sleep(1)
    get_element(driver,sc.add_new_stat_catcher["locator"],sc.add_new_stat_catcher["xpath"]).click()

    fill_mandatory(driver,statistics_catcher)
def create_new_client_stb(driver):
    time.sleep(1)
    get_element(driver,clientSTBclass.add_new_stb_range["locator"],clientSTBclass.add_new_stb_range["xpath"]).click()
    time.sleep(1)
    fill_mandatory(driver,client_stb)

def create_new_group(driver):
    time.sleep(1)
    get_element(driver,groupclass.add_new_group["locator"],groupclass.add_new_group["xpath"]).click()
    time.sleep(1)
    fill_mandatory(driver,group)

def create_new_area(driver):
    time.sleep(1)
    get_element(driver,areaclass.add_new_area["locator"],areaclass.add_new_area["xpath"]).click()
    time.sleep(1)
    fill_mandatory(driver,area)

def create_new_region(driver):
    time.sleep(1)
    get_element(driver,regionclass.add_new_region["locator"],regionclass.add_new_region["xpath"]).click()
    time.sleep(1)
    fill_mandatory(driver,region)

def create_new_systemservices(driver):
    time.sleep(1)
    get_element(driver,systemserviceclass.add_new_service_provider["locator"],systemserviceclass.add_new_service_provider["xpath"]).click()
    time.sleep(1)
    fill_mandatory(driver,system_service_configuration)

def create_new_binary(driver):
    time.sleep(1)
    get_element(driver,binaryclass.add_new_binary["locator"],binaryclass.add_new_binary["xpath"]).click()
    time.sleep(3)
    fill_mandatory(driver,binary)
    get_element(driver,binaryclass.is_binary_signed["locator"],binaryclass.is_binary_signed["xpath"]).click()

#def create_new_binary(driver):
    #time.sleep(1)
    #get_element(driver,binaryclass.add_new_binary["locator"],binaryclass.add_new_binary["xpath"]).click()
    #time.sleep(3)
    #fill_mandatory(driver,binary)
    #get_element(driver,binaryclass.is_binary_signed["locator"],binaryclass.is_binary_signed["xpath"]).click()

def create_new_user_maint(driver):
    time.sleep(1)
    get_element(driver,usersmaintclass.select["locator"],usersmaintclass.select["id"]).click()
    time.sleep(1)
    driver.find_element_by_xpath('//select//option[@value]').send_keys("All")
    time.sleep(1)
    get_element(driver, usersmaintclass.create_new_user["locator"], usersmaintclass.create_new_user["xpath"]).click()
    fill_mandatory(driver,users_maintenance)
    #get_element(driver,binaryclass.is_binary_signed["locator"],binaryclass.is_binary_signed["xpath"]).click()

def search(driver,pagename,item):
    time.sleep(1)
    pagename_string = pagename.encode("utf-8")
    item_string = item.encode("utf-8")
    classname,pagename = get_dict(pagename_string)
    insert_value(driver,classname.search_box,item_string)

    locator = classname.search["locator"]
    get_element(driver, locator, classname.search[locator]).click()
    try:
        link = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, item_string)))
        return link
    except TimeoutException:
        WebDriverWait(driver, 10).until(Is_text_present("Empty search. No row exist with this information"))
        raise error.ItemNotFoundError

def deleteentry(driver,pagename,item):
    try:
        link = search(driver, pagename, item)
    except error.ItemNotFoundError:
        log.info("{a} is not listed in the {b} page".format(a=item, b=pagename))
        return
    link.click()
    time.sleep(1)
    pagename_string = pagename.encode("utf-8")
    classname, pagename = get_dict(pagename_string)
    click(driver,classname.delete)
    save1(driver)
    alert = driver.switch_to_alert()
    alert_text = alert.text
    alert_text_string = alert_text.encode("utf-8")  # Converting unicode into string
    if "Could you confirm to delete?" == alert_text_string:
        alert.accept()
    else:
        raise error.ValidationError
    time.sleep(1)
    if pagename_string == "channel":
        get_element(driver, "xpath", ".// *[ @ id = 'msgconfirmb']").click()
    try:
        WebDriverWait(driver, 30).until(Is_text_present("Data correctly saved in tables"))
    except Exception, e:
        log.info(e.message)
        log.info(e.args)
        raise error.ValidationError
    get_navigation_page(driver)

def create_new_(driver,pagename):

    time.sleep(1)
    pagename_string = pagename.encode("utf-8")
    classname,pagename = get_dict(pagename_string)

    locator = classname.add_new["locator"]
    get_element(driver, locator, classname.add_new[locator]).click()
    time.sleep(1)
    fill_mandatory(driver,pagename)
def HW_Rev(driver,pagename):

    get_element(driver, hostclass.type["locator"]).click()
    time.sleep(1)
    fill_mandatory1(driver,pagename)

def is_binary_signed(driver):
    time.sleep(1)
    get_element(driver, binaryclass.is_binary_signed["locator"], binaryclass.is_binary_signed["xpath"]).click()
def clear_HW_rev(driver):

    elem = driver.find_element_by_id('APPLIANCE_REVISION_0')
    for option in elem.find_elements_by_tag_name('option'):
        if option.text == "":
            break

        else:
            ARROW_DOWN = u'\ue015'
            elem.send_keys(ARROW_DOWN)

def return_to_(driver,classname):
    f = driver.find_element_by_name("mainFrame")
    driver.switch_to.frame(f)

    classname_string = classname.encode("utf-8")
    classname_class = str_to_class(classname_string)

    if is_present(driver, classname_class.return_) == 1:
        click(driver, classname_class.return_)
    else:
        print "return not present"

def post_delete_return_to(driver,classname):
    if type(classname)!= str :
        classname=classname.encode("utf-8")
        classname=str_to_class(classname)
    if is_present(driver, classname.return_) == 1:
        click(driver, classname.return_)
    else:
        print "return not present"

def modify(driver,field,data):
    #data = data["value"]
    data = data.encode("utf-8")
    print "data is ",data
    insert_value(driver,field,data)

def validate(driver,field,data=None):
    if data != None:
        data = data.encode("utf-8")
        print "data is ", data
        insert_value(driver, field, data)
    if data is None:
        insert_value(driver, field, "None")
        #print type(data)

    save1(driver)

    time.sleep(6)

    alert = driver.switch_to_alert()
    alert_text = alert.text
    print "alert accepted"
    print alert_text
    alert.accept()

    alert_text_string = alert_text.encode("utf-8")  # Converting unicode into string
    if field["error_message"] == alert_text_string or "Duplicate entry" in alert_text_string or "must be between" in alert_text_string:
        print "Alert verified"
    else:
        print "Wrong Alert message"
        raise assertionerror
    get_navigation_page(driver)

def validate_pos(driver,field,data,page):
    page = page.encode("utf-8")
    insert_value(driver,field,data)
    save1(driver)
    time.sleep(1)
    if page == "channel":
        get_element(driver,"xpath",".// *[ @ id = 'msgconfirmb']").click()
    try:
        WebDriverWait(driver, 30).until(Is_text_present("Data correctly saved in tables"))
    except Exception, e:
        log.info(e.message)
        log.info(e.args)
        raise error.ValidationError
    get_navigation_page(driver)

def get_navigation_page(driver):
    try:
        driver.find_element_by_class_name("dojoMenuBar2Client")
    except:
        try:
            driver.find_element_by_css_selector('input[value*="Return"][value$="Page"]').click()
        except:
            elements = driver.find_elements_by_css_selector('.boton[value*="Cancel"]')
            for element in elements:
                if element.is_displayed():
                    element.click()
                    break
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "dojoMenuBar2Client")))