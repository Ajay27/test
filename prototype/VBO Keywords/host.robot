*** Settings ***
Library  Selenium2Library
Library  ../Core_Libraries/Application_Utilities/sdputils.py
Library  ../VBO_Objects/sdppo.py
Library  ../VBO_Objects/hostPage.py
Library  ../VBO_Library/lib_files.py
*** Keywords ***
setup_add_new_host
    ${SDP} =   BuiltIn.Get Library Instance  sdppo
    open_page  ${driver}  ${SDP.host}
    ${host} =   BuiltIn.Get Library Instance  hostPage
    SET GLOBAL VARIABLE    ${host}
create_new_rewrapper
    create_rewrapper  ${driver}