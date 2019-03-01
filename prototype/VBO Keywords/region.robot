*** Settings ***
Library  Selenium2Library
Library  ../Core_Libraries/Application_Utilities/sdputils.py
Library  ../VBO_Objects/sdppo.py
Library  ../VBO_Objects/regionPage.py
Library  ../VBO_Library/lib_files.py

*** Keywords ***
setup_add_new_region
    ${SDP} =   BuiltIn.Get Library Instance  sdppo
    open_page  ${driver}  ${SDP.region}
    ${region} =   BuiltIn.Get Library Instance  regionPage
    SET GLOBAL VARIABLE    ${region}

create_region
    create_new_region  ${driver}