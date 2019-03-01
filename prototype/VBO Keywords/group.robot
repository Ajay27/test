*** Settings ***
Library  Selenium2Library
Library  ../Core_Libraries/Application_Utilities/sdputils.py
Library  ../VBO_Objects/sdppo.py
Library  ../VBO_Objects/groupPage.py
Library  ../VBO_Library/lib_files.py

*** Keywords ***
setup_add_new_group
    ${SDP} =   BuiltIn.Get Library Instance  sdppo
    open_page  ${driver}  ${SDP.group}
    ${group} =   BuiltIn.Get Library Instance  groupPage
    SET GLOBAL VARIABLE    ${group}

create_group
    create_new_group  ${driver}