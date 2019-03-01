*** Settings ***
Library  Selenium2Library
Library  ../Core_Libraries/Application_Utilities/sdputils.py
Library  ../VBO_Objects/sdppo.py
Library  ../VBO_Objects/clientSTBPage.py
Library  ../VBO_Library/lib_files.py

*** Keywords ***
setup_add_new_client_stb
    ${SDP} =   BuiltIn.Get Library Instance  sdppo
    open_page  ${driver}  ${SDP.client_stb}
    ${clientstb} =   BuiltIn.Get Library Instance  clientSTBPage
    SET GLOBAL VARIABLE    ${clientstb}

create_client_stb
    create_new_client_stb  ${driver}