*** Settings ***
Library  Selenium2Library
Library  ../Core_Libraries/Application_Utilities/sdputils.py
Library  ../VBO_Objects/sdppo.py
Library  ../VBO_Objects/binaryPage.py
Library  ../VBO_Library/lib_files.py


*** Keywords ***
setup_add_new_binary
    ${SDP} =   BuiltIn.Get Library Instance  sdppo
    open_page  ${driver}  ${SDP.binary }
    ${binary} =   BuiltIn.Get Library Instance  binaryPage
    SET GLOBAL VARIABLE    ${binary}

create_binary
    create_new_binary  ${driver}