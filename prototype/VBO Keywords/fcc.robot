*** Settings ***
Library  Selenium2Library
Library  ../Core_Libraries/Application_Utilities/sdputils.py
Library  ../VBO_Objects/sdppo.py
Library  ../VBO_Objects/fccPage.py
Library  ../VBO_Library/lib_files.py

*** Keywords ***
setup_add_new_fcc
    ${SDP} =   BuiltIn.Get Library Instance  sdppo
    open_page  ${driver}  ${SDP.fcc}
    ${fcc} =   BuiltIn.Get Library Instance  fccPage
    SET GLOBAL VARIABLE    ${fcc}

create_fcc
    create_new_fcc  ${driver}