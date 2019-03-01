*** Settings ***
Library  Selenium2Library
Library  ../Core_Libraries/Application_Utilities/sdputils.py
Library  ../VBO_Objects/sdppo.py
Library  ../VBO_Objects/systemservicesPage.py
Library  ../VBO_Library/lib_files.py


*** Keywords ***
setup_add_new_system_service
    ${SDP} =   BuiltIn.Get Library Instance  sdppo
    open_page  ${driver}  ${SDP.system_service_configuration }
    ${ssc} =   BuiltIn.Get Library Instance  systemservicesPage
    SET GLOBAL VARIABLE    ${ssc}

create_systemsevices
    create_new_systemservices  ${driver}