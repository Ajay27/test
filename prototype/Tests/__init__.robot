*** Settings ***

Library  Selenium2Library
Library  ../Core_Libraries/Application_Utilities/sdputils.py
Variables  ../VBO_Objects/properties.py


Documentation  This suite tests the SDP GUI
Suite Setup  Open sdp
Suite Teardown  close sdp

*** Keywords ***
Open sdp
    [Documentation]  Login to the application and the driver instance is made as the global variable

    open browser  ${url}  ff
    ${driver}=  sdp_login
    SET GLOBAL VARIABLE    ${driver}

close sdp
    [Documentation]  Closes the sdp application after the process is over.
    close browser