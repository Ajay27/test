*** Settings ***
Library  Selenium2Library
Library  ../Core_Libraries/Application_Utilities/sdputils.py
Library  ../VBO_Objects/sdppo.py
Library  ../VBO_Objects/areaPage.py
Library  ../VBO_Library/lib_files.py

*** Keywords ***
setup_add_new_area
    ${SDP} =   BuiltIn.Get Library Instance  sdppo
    open_page  ${driver}  ${SDP.area}
    ${area} =   BuiltIn.Get Library Instance  areaPage
    SET GLOBAL VARIABLE    ${area}

create_area
    create_new_area  ${driver}