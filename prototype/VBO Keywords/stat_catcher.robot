*** Settings ***
Library  Selenium2Library
Library  ../Core_Libraries/Application_Utilities/sdputils.py
Library  ../VBO_Objects/sdppo.py
Library  ../VBO_Objects/statCatcherPage.py
Library  ../VBO_Library/lib_files.py


*** Keywords ***
setup_add_new_stat_catcher
    ${SDP} =   BuiltIn.Get Library Instance  sdppo
    open_page  ${driver}  ${SDP.statistics_catcher }
    ${statcatch} =   BuiltIn.Get Library Instance  statCatcherPage
    SET GLOBAL VARIABLE    ${statcatch}

create_stat_catcher
    create_new_stat_catcher  ${driver}