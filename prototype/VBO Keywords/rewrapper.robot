*** Settings ***
Library  Selenium2Library
Library  ../Core_Libraries/Application_Utilities/sdputils.py
Library  ../VBO_Objects/sdppo.py
Library  ../VBO_Objects/rewrapperPage.py
Library  ../VBO_Library/lib_files.py
*** Keywords ***
setup_add_new_rewrapper
    ${SDP} =   BuiltIn.Get Library Instance  sdppo
    open_page  ${driver}  ${SDP.rewrapper}
    ${rewrapper} =   BuiltIn.Get Library Instance  rewrapperPage
    SET GLOBAL VARIABLE    ${rewrapper}
create_new_rewrapper
    create_rewrapper  ${driver}





