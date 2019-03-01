import logging
import time

from VBO_Objects.loginpo import Login
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class assertionerror(Exception):
    pass


def get_element(driver, identifier, value):
    if identifier == "id":
        element = driver.find_element_by_id(value)
    if identifier == "xpath":
        element = driver.find_element_by_xpath(value)

        # write the remaining possibilities here

    return element


def insert_value(driver, field, value="None1"):
    """ This function inserts given value to given field in the given browser page(driver)
         driver - selenium webdriver instance which has the given field
         field - dictionary of the field which has it's properties
         vlaue - string that has to be inserted to the field"""
    logging.info(field)
    logging.info(value)
    locator = field["locator"]
    element = get_element(driver, locator, field[locator])
    try:
     element.clear()
    except:
        pass
    if value == "None1":
        value = field["value"]
    element.send_keys(value)
    if value == "None":
        element.send_keys(Keys.DELETE)
        #element.select_by_value("")

def save(driver):

    #get_element(driver, "xpath", "// input[ @ value = 'Save']").click()
    get_element(driver,"xpath",".// *[ @ id = 'buttonSaveChannel'] / table / tbody / tr / td[1] / input").click()
    #get_element(driver, "xpath", "// input[ @ value = 'Save']").click()
def open_page(driver, page):

    f = driver.find_element_by_name("mainFrame")
    driver.switch_to.frame(f)
    g = driver.find_element_by_xpath(page[0])
    hover = ActionChains(driver).move_to_element(g)
    hover.perform()
    time.sleep(1)
    driver.find_element_by_xpath(page[1]).click()
    time.sleep(2)

def fill_mandatory0(driver, page):
    mandatory_fields0 =  page[2].mandatory_data0
    for field in mandatory_fields0:
        insert_value(driver, field)
def fill_mandatory(driver, page):
    mandatory_fields =  page[2].mandatory_data
    for field in mandatory_fields:
        insert_value(driver, field)
def fill_mandatory1(driver, page):
    mandatory_fields1 =  page[2].mandatory_data1
    for field in mandatory_fields1:
        insert_value(driver, field)
def fill_mandatory2(driver, page):
    mandatory_fields2 =  page[2].mandatory_data2
    for field in mandatory_fields2:
        insert_value(driver, field)
def fill_mandatory3(driver, page):
    mandatory_fields3 =  page[2].mandatory_data3
    for field in mandatory_fields3:
        insert_value(driver, field)
def fill_mandatory4(driver, page):
    mandatory_fields4 =  page[2].mandatory_data4
    for field in mandatory_fields4:
        insert_value(driver, field)

def sdp_login(user="sdp", password="sdp"):
    """This method can be used for login into sdp system. If username and password
            is not provided it will be considered as "sdp" and "sdp" respectively"""
    # for accessing the driver opened using selenium2library
    se2lib = BuiltIn().get_library_instance('Selenium2Library')
    time.sleep(3)
    driver = se2lib._current_browser()

    insert_value(driver, Login.user, user)
    insert_value(driver,Login.password, password)
    locator = Login.enter["locator"]
    get_element(driver, locator, Login.enter[locator]).click()
    return driver