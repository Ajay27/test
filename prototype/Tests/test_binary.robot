*** Settings ***
Library  Selenium2Library
Library  ../Core_Libraries/Test_Data_Pool/data.py
Library  ../VBO_Library/lib_files.py
Library  ../Core_Libraries/Application_Utilities/sdputils.py
Library  ../VBO_Objects/sdppo.py
Library  ../VBO_Objects/binaryPage.py
Library  ../Core_Libraries/Database/database.py
Variables  ../VBO_Objects/properties.py

Suite Setup  setup_add_new_binary
Force Tags  binary_page


*** Variables ***

@{invalid_name}=    {}name1  %fjafaj  =cajkvab'
@{valid_name}=  rew1  rew2  rew3
${sdp.755}=  rewraper-v4
${sdp.756}=  rewrapper-v4
${sdp.753-data}=  l8ym4smw+ye8ZjSaVlCsCi+67fLT29HnjcYrFtWeQv4Hs4Cv0J96WQPIcMdqjgfSmWgwygwr08HkOgCcHoo+ral3jLjc1Q6l+P90qCzzYOISYDj5zCLPJax9pN3oFX+OuPZZw96CRRNNJcwieF+hi+t9xitxiLlZeRYGZ+XVC9E=
${sdp.761-data}=  C:\\\\Users\\\\ajayth\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040100-APP-Services-x86_64\\\\abin\\\\fccret_server_4.1_25
${sdp.760-data}=  fcc-v4
${fcc-path}=  C:\\\\Users\\\\ajayth\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040100-APP-Services-x86_64\\\\abin\\\\fccret_server_4.1_25
${sdp.765-data}=  flow_shaperSP2
${sdp.766-data}=  flow_shaperSP2
${sdp.770-data}=  stats_catcher_54
${sdp.771-data}=  stats_catcher54
${sdp.775-data}=  vsa_monitor-53
${sdp.776-data}=  vsa_monitor-53
${sdp.780-data}=  vsa_managerSP2
${sdp.781-data}=  vsa_managerSP2

*** Test Cases ***

validate binary name with invalid data
      [Template]  validate_check
        :FOR  ${data}  in  @{invalid_name}
        \   ${binary.binaryclass.name}  ${data}

validate binary name with valid data
       [Template]  validate_positive1
        :FOR  ${data}  in  @{paths}
        \   ${binary.binaryclass.browse}  ${data}  binary

sdp.753
    create_binary
    validate  ${driver}  ${binary.binaryclass.signed_digest}  ${sdp.753-data}
sdp.754
     create_binary
     is binary signed  ${driver}
     validate  ${driver}  ${binary.binaryclass.is_binary_signed}
sdp.755
     create_binary
     validate  ${driver}  ${binary.binaryclass.name}  ${sdp.755}
sdp.756
     create_binary
     validate  ${driver}  ${binary.binaryclass.browse}  ${sdp.756}

sdp.757
    HW_Rev  ${driver}  binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\fccret_server54new
    validate  ${driver}  ${binary.binaryclass.hardware_revision}
sdp.758
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\fccret_server54new
    validate  ${driver}  ${binary.binaryclass.signed_digest}  ${sdp.753-data}
sdp.759
     create_binary
     modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\fccret_server54new
     is binary signed  ${driver}
     validate  ${driver}  ${binary.binaryclass.is_binary_signed}
sdp.760
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\fccret_server54new
    validate  ${driver}  ${binary.binaryclass.name}  ${sdp.760-data}
sdp.761
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\fccret_server54new
    validate  ${driver}  ${binary.binaryclass.browse}  ${sdp.761-data}

sdp.762
    HW_Rev  ${driver}  binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\flow_shaper54new
    validate  ${driver}  ${binary.binaryclass.hardware_revision}
sdp.763
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\flow_shaper54new
    validate  ${driver}  ${binary.binaryclass.signed_digest}  ${sdp.753-data}
sdp.764
     create_binary
     modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\flow_shaper54new
     is binary signed  ${driver}
     validate  ${driver}  ${binary.binaryclass.is_binary_signed}
sdp.765
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\flow_shaper54new
    validate  ${driver}  ${binary.binaryclass.name}  ${sdp.765-data}
sdp.766
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\flow_shaper54new
    validate  ${driver}  ${binary.binaryclass.browse}  ${sdp.766-data}

sdp.767
    HW_Rev  ${driver}  binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\stats_catcher54new
    validate  ${driver}  ${binary.binaryclass.hardware_revision}
sdp.768
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\stats_catcher54new
    validate  ${driver}  ${binary.binaryclass.signed_digest}  ${sdp.753-data}
sdp.769
     create_binary
     modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\stats_catcher54new
     is binary signed  ${driver}
     validate  ${driver}  ${binary.binaryclass.is_binary_signed}
sdp.770
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\stats_catcher54new
    validate  ${driver}  ${binary.binaryclass.name}  ${sdp.770-data}
sdp.771
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\stats_catcher54new
    validate  ${driver}  ${binary.binaryclass.browse}  ${sdp.771-data}

sdp.772
    HW_Rev  ${driver}  binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\vsa_monitor54new
    validate  ${driver}  ${binary.binaryclass.hardware_revision}
sdp.773
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\vsa_monitor54new
    validate  ${driver}  ${binary.binaryclass.signed_digest}  ${sdp.753-data}
sdp.774
     create_binary
     modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\vsa_monitor54new
     is binary signed  ${driver}
     validate  ${driver}  ${binary.binaryclass.is_binary_signed}
sdp.775
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\vsa_monitor54new
    validate  ${driver}  ${binary.binaryclass.name}  ${sdp.775-data}
sdp.776
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\vsa_monitor54new
    validate  ${driver}  ${binary.binaryclass.browse}  ${sdp.776-data}

sdp.777
    HW_Rev  ${driver}  binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\vsa_manager54new
    validate  ${driver}  ${binary.binaryclass.hardware_revision}
sdp.778
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\vsa_manager54new
    validate  ${driver}  ${binary.binaryclass.signed_digest}  ${sdp.753-data}
sdp.779
     create_binary
     modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\vsa_manager54new
     is binary signed  ${driver}
     validate  ${driver}  ${binary.binaryclass.is_binary_signed}
sdp.780
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\vsa_manager54new
    validate  ${driver}  ${binary.binaryclass.name}  ${sdp.780-data}
sdp.781
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\4.0\\\\rew-54\\\\NOKIA-VBO-040000-APP-Services-x86_64\\\\abin\\\\vsa_manager54new
    validate  ${driver}  ${binary.binaryclass.browse}  ${sdp.781-data}

sdp.719
    [Documentation]  OS binary creation for 1.3.2
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\132\\\\ALU-VSA-010302-APP-OSinstall-mips64\\\\aos
    modify  ${driver}  ${binary.binaryclass.signed_digest}  TSY1MptC8cXynO45CTgKyn+YO+9a61lDhPV7an9zRop7Wg6lMOlqH2WAhmQhYhw4xTLHqmfss42JM1KTXlkV76EIcPK9q+0tJYRdhaqZb7rdNH7ylRFhbPZX3vfslT339qJ+eLRQblhXFpbnweOiF1IfndTd47eskO4d7QUonVY=
    modify  ${driver}  ${binary.binaryclass.type}  os/Platform RPM
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 1 or 2
    deleteentry  ${driver}  binary  aos
sdp.726
    [Documentation]  OS binary creation for 1.3.2SP1
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\132sp1\\\\ALU-VSA-010302-APP-OSinstall-mips64\\\\aos
    modify  ${driver}  ${binary.binaryclass.signed_digest}  TSY1MptC8cXynO45CTgKyn+YO+9a61lDhPV7an9zRop7Wg6lMOlqH2WAhmQhYhw4xTLHqmfss42JM1KTXlkV76EIcPK9q+0tJYRdhaqZb7rdNH7ylRFhbPZX3vfslT339qJ+eLRQblhXFpbnweOiF1IfndTd47eskO4d7QUonVY=
    modify  ${driver}  ${binary.binaryclass.type}  os/Platform RPM
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 1 or 2
    deleteentry  ${driver}  binary  aos
sdp.733
    [Documentation]  OS binary creation for 3.0
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\30\\\\ALU-VSA-030000SP5-APP-OSinstall-mips64\\\\aos
    modify  ${driver}  ${binary.binaryclass.signed_digest}  ZkreO8+OoVbAdf0S9pVSntk89mQt8kL9/7fjeRFsf/6F6YMFJaI+TtJSoHzYjwScaQY2EzudNsQvLkKZhmqRpXKDm06jE428PTMfk+pxt/mdEm3YvBofD37y6zh3YH0zkjHXPxQuvQZqI7M7/rgNyy05I3xtYwirrREnswOyY6s=
    modify  ${driver}  ${binary.binaryclass.type}  os/Platform RPM
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    deleteentry  ${driver}  binary  aos
sdp.740
    [Documentation]  OS binary creation for 3.1
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\31\\\\NOKIA-VBO-030100SP2-APP-OSinstall-mips64\\\\aos
    modify  ${driver}  ${binary.binaryclass.signed_digest}  UxPHJM4BmA0MZjn8JzPR4FNrU9ZfucDVVGpWyVRz8skrbCYael5eWmkkPJWZfZTS0/Bmz+18eGI2mERrNKK/cKSdONXqeJjZh9SGoXhNoVsFBFL7qbL4AyDj8LWGq/hbAopx/oMF5fBbU+jkjwC9KfoyM/4R2nMT62IJvnFlcTM=
    modify  ${driver}  ${binary.binaryclass.type}  os/Platform RPM
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    deleteentry  ${driver}  binary  aos
sdp.migrated.747
   [Documentation]  OS binary creation for 4.0
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\40\\\\NOKIA-VBO-040000SP1-APP-Platform-x86_64\\\\VBO_Platform-4.0.0SP1-2.x86_64.rpm
    modify  ${driver}  ${binary.binaryclass.signed_digest}  QkYQhVdKAvMbZUPZ87RDXRhvilXaqoeV9q1zitvnVJIY/1YzkQnCDXVd+LJu3e05cHlrzMP1cqaqhkTSd4+DC/EVUq+vRoyZhIE9TJEbIobPOwvt2yEMzLrsaxYT1nM7+g3iDwK3A5I01CtbuDj4fgnFqiEotyiiIKi/wQh9uoE=
    modify  ${driver}  ${binary.binaryclass.type}  os/Platform RPM
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 4
    deleteentry  ${driver}  binary  VBO_Platform-4.0.0SP1-2.x86_64.rpm

sdp.720
    [Documentation]  rewrapper creation for 1.3.2
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\132\\\\ALU-VSA-010302-APP-Services-mips64.tar\\\\ALU-VSA-010302-APP-Services-mips64\\\\arewrapper
    modify  ${driver}  ${binary.binaryclass.signed_digest}  ENgKEcw/KOajPVnIC8b9iGUGfzdqln8/y4ggCJwogZfRHtlSCMrck+miIzgaGpQZBx3NwDmQsEu3qx2zPaZLw/OS0GFvYYb5MXJw6Hfj5OhIgUJjHCXYgH2DETB9yswwImNnTP30zoIJMJHvoZu792yYYCWPliWwbkDXi/PuMZg=
    modify  ${driver}  ${binary.binaryclass.type}  rewrapper
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 1 or 2
    deleteentry  ${driver}  binary  arewrapper
sdp.727
    [Documentation]  rewrapper creation for 1.3.2SP1
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\132sp1\\\\ALU-VSA-010302-SP1-APP-Services-mips64\\\\abin\\\\arewrapper
    modify  ${driver}  ${binary.binaryclass.signed_digest}  oUrfGsG5jFrfZvl48xvV+aZKXFDZzeZwNUkgcE0zIrntYibjnXozzi7Wb2ILjaE8LeSawYOHR0Y96rt4cpUw24c+uxXwmJ8r9jGNcbeS6vs+1UqiosfMV/xj6+eJ8mUs1XaT/JrVIjcg506z28uYsQrF9lmzIlKE/h8IP4r3kBw=
    modify  ${driver}  ${binary.binaryclass.type}  rewrapper
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 1 or 2
    deleteentry  ${driver}  binary  arewrapper
sdp.734
    [Documentation]  rewrapper creation for 3.0
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\30\\\\ALU-VSA-030000SP5-APP-Services-mips64\\\\abin\\\\arewrapper
    modify  ${driver}  ${binary.binaryclass.signed_digest}  vELCXerBXBAGLo96sf1qEsV4Jv3TAb1m3A29fIVbY/U9rpdRI5ab/ZXhoCp54lk5xsqp13GFQAGYnEMBkxEMsqNEOGZdIZlcxK462XZjQwhzUk0lOImQqfAZYCYoW0Q9qJBz25EEC2X1/auq+AzWDC8vcpY7hQUf7FAuUsABnw0=
    modify  ${driver}  ${binary.binaryclass.type}  rewrapper
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    deleteentry  ${driver}  binary  arewrapper
sdp.741
   [Documentation]  rewrapper creation for 3.1
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\31\\\\NOKIA-VBO-030100SP2-APP-Services-mips64\\\\abin\\\\arewrapper\
    modify  ${driver}  ${binary.binaryclass.signed_digest}  Ut9pnTGn37aZg1Qwcb+ccypgYjDRQx3aaRFKvpOZ2Krw0h5zMJ/Z/eZ+RkMSEaDDVrSbKslB/RLPylF50RAAmkGxuQLXjZXlnIOsSHqOkG5eYgqUxhbmR59FphFmvVRQYoxKz0kxF1x6jdptnffTAEXV+3mYf9f8PnWgLp2lT0U=
    modify  ${driver}  ${binary.binaryclass.type}  rewrapper
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    deleteentry  ${driver}  binary  arewrapper
sdp.migrated.748
   [Documentation]  rewrapper creation for 4.0
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\40\\\\NOKIA-VBO-040000SP1-APP-Services-x86_64\\\\abin\\\\arewrapper
    modify  ${driver}  ${binary.binaryclass.signed_digest}  ZDmcmOiQ/DdE7dFjrLFwEm2f00PGmHiIGVyTxbCoCY8rYm6Qkjmdr7x363XpcsExZ1WEohJWcPaVLdHnoO+0aiPxxdrrVnBovFpmhbe1PfYVPEYz5KleaGDudwOlNbriu/KzIF3yPyyDg5zf5O/nLzYdr0PRlZKdgppk1m2vZdQ=
    modify  ${driver}  ${binary.binaryclass.type}  rewrapper
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 4
    deleteentry  ${driver}  binary  arewrapper

sdp.721
    [Documentation]  fccret-server creation for 1.3.2
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\132\\\\ALU-VSA-010302-APP-Services-mips64.tar\\\\ALU-VSA-010302-APP-Services-mips64\\\\afccret_server
    modify  ${driver}  ${binary.binaryclass.signed_digest}  O6CCXC/m8BqYPaOHydVGH08lrCP2ZRx4j4Cocbgu53P9z34bWIvxPczwF44OFOnDPF6k83EsW9w9Zv/aOpuq/ygyoLa67llqCGYUQrkPyfrtdOHMzTpWLjyte4F45n4m54vfIq1x95HoKs8FtpjHkClz62ZD7hzkbwbifS/mK98=
    modify  ${driver}  ${binary.binaryclass.type}  fccret
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 1 or 2
    deleteentry  ${driver}  binary  afccret_server
sdp.728
    [Documentation]  fccret-server creation for 1.3.2SP1
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\132sp1\\\\ALU-VSA-010302-SP1-APP-Services-mips64\\\\abin\\\\afccret_server
    modify  ${driver}  ${binary.binaryclass.signed_digest}  Z5XtYC07DbijCupBClrk6hQMPtX+Tt5woYKVIP0TigF6161x+abUXavi7lj0VPbIFZn4fsN6Jw+7ZsDkbo8JwUh5vdP7+e+AMLIb1mIubY+8z6qNclZEh+0TfhnqTibdfsF63l9742Yu1hlZ0NHumWE6y0cx1P2sQRd4VEh/2m4=
    modify  ${driver}  ${binary.binaryclass.type}  fccret
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 1 or 2
    deleteentry  ${driver}  binary  afccret_server
sdp.735
    [Documentation]  fccret-server creation for 3.0
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\30\\\\ALU-VSA-030000SP5-APP-Services-mips64\\\\abin\\\\afccret_server
    modify  ${driver}  ${binary.binaryclass.signed_digest}  KdX6IpY1C5g2rdKKGmW9V2pHOIbfIEYW6crkZGedTrvzK4GoqG6GbkyQ5hWadfw+60Dgi+X7sRFiEra1gbSLzvz0F0oT53UPXURmLAw4w8tAJx33sEvWlUe0vwzJR4+ddnxswyvLhsY0B+QlUQ6802GTpnJU1ogvk6TzSWGRn+M=
    modify  ${driver}  ${binary.binaryclass.type}  fccret
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    deleteentry  ${driver}  binary  afccret_server
sdp.742
   [Documentation]  fccret-server creation for 3.1
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\31\\\\NOKIA-VBO-030100SP2-APP-Services-mips64\\\\abin\\\\afccret_server
    modify  ${driver}  ${binary.binaryclass.signed_digest}  UMbOiddO8J/HzTWNy918KyG1Al0Z3Yrb9+FG2O6dRGr2y7iiHIHBmq6jjTv4bsYmAGrDHAL1ULQWuO5libh+5tV5wv/Ki4ybStDGhpG4QBFMShM02wF3jVzA/bH8x5nmnlVtL6zsySfDuyAzE555+6j8Lte97IxDX7l4r6/DjFA=
    modify  ${driver}  ${binary.binaryclass.type}  fccret
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    deleteentry  ${driver}  binary  afccret_server
sdp.migrated.749
   [Documentation]  fccret-server creation for 4.0
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\40\\\\NOKIA-VBO-040000SP1-APP-Services-x86_64\\\\abin\\\\afccret_server
    modify  ${driver}  ${binary.binaryclass.signed_digest}  gJUPXsbBtHS7Y/vubAWLDlhRd3MftbeDe/DsA4YJdHll0dRzSpJsSE/OgaaCMnOirz0jPfiRCuzX53FpfXDQm5megnD9Hu5oXDCmR+/2JaZ4biR4nln8u+xfKYSPTKeNZm4zdM9l62fc9s5kDUkC8yGapZnVmttF1Zd9I949DsY=
    modify  ${driver}  ${binary.binaryclass.type}  fccret
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 4
    deleteentry  ${driver}  binary  afccret_server

sdp.722
    [Documentation]  flowshaper creation for 1.3.2
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\132\\\\ALU-VSA-010302-APP-Services-mips64.tar\\\\ALU-VSA-010302-APP-Services-mips64\\\\aflow_shaper
    modify  ${driver}  ${binary.binaryclass.signed_digest}  k3iJJfDNEEsbWsGQWx+rwX2OUHfjvLkKde+GqFikPML6erZT+wh37QClCZ39HOH0VpmFaCcgjX8hahyE/tF5qpwqp0g+zd1iRgCY6ISWwDDmADhbFXwouvz8ogD1YWwewMFFj/geanxW5VZ7l+bDVLB7us6o2n2lrhwhl62/PBw=
    modify  ${driver}  ${binary.binaryclass.type}  flowshaper
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 1 or 2
    deleteentry  ${driver}  binary  aflow_shaper
sdp.729
    [Documentation]  flowshaper creation for 1.3.2sp1
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\132sp1\\\\ALU-VSA-010302-SP1-APP-Services-mips64\\\\abin\\\\aflow_shaper
    modify  ${driver}  ${binary.binaryclass.signed_digest}  JESqwUdk1knP+OrN6OKiqMzl7k8X4aTeKB83MairTY9WKPeitu8mHnb0ne1igjTkvfFg+xP8HS3z092oAWjOHs12ddNZtwg0PqW5pxhz6DvGbPJi+SAhY6XmrzwlIgU2xdZQzNo9ZGx9fb7hQ1hvmj4fZwTvJ5ksdBH6T6ZbEbY=
    modify  ${driver}  ${binary.binaryclass.type}  flowshaper
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 1 or 2
    deleteentry  ${driver}  binary  aflow_shaper
sdp.736
    [Documentation]  flowshaper creation for 3.0
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\30\\\\ALU-VSA-030000SP5-APP-Services-mips64\\\\abin\\\\aflow_shaper
    modify  ${driver}  ${binary.binaryclass.signed_digest}  uPKCfBi+cXkGuE17HmlfrJ5fEU3CE6VVHIzqVk5Oh81IJIdg35nKZqR97dVYr0a0BNfjfW/CV4f/RIw5W1FibDPeEufkpCg2ei6iyC+T7TxIi4izGoZBWEoHOpLxTrlOp77WJOod4fGv23Nsk55zZKluo+BQtarknYBnIeQzBWQ=
    modify  ${driver}  ${binary.binaryclass.type}  flowshaper
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    deleteentry  ${driver}  binary  aflow_shaper
sdp.743
    [Documentation]  flowshaper creation for 3.1
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\31\\\\NOKIA-VBO-030100SP2-APP-Services-mips64\\\\abin\\\\aflow_shaper
    modify  ${driver}  ${binary.binaryclass.signed_digest}  K2AV05hSphLJTbcdNuBJROx9cfgFIY8H1+OflqOznI+IyNTXmaUJvh8MHpO0iL0ptpJOsHO3zuRFWjbCkOMrDiq9nt50ueEs2fX1i7UNkJ1pEIMpy6mZAECr6hTD8DCUmroAjOrzwk+eqZRR0NPGfVF7VDp4NyU5p9lxYH7JR8E=
    modify  ${driver}  ${binary.binaryclass.type}  flowshaper
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    deleteentry  ${driver}  binary  aflow_shaper
sdp.migrated.750
    [Documentation]  flowshaper creation for 4.0
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\40\\\\NOKIA-VBO-040000SP1-APP-Services-x86_64\\\\abin\\\\aflow_shaper
    modify  ${driver}  ${binary.binaryclass.signed_digest}  qziz9c1aupcWRb5Kg2x/ZBui5fmre9PEvHoLQQDGoPg2wPV1AiGuK9zfEmYTTZaYsDVaDHQ+QYKdssMQloBj2fG4blPx1E1PgAX+A5P1ltlYWA3wdb73FEQfSrCCTkNV52Y15keCEzvv/2iNnCAYUhMmC1vIuOyMmC48C1Q4IWU=
    modify  ${driver}  ${binary.binaryclass.type}  flowshaper
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 4
    deleteentry  ${driver}  binary  aflow_shaper

sdp.723
    [Documentation]  flowshaper creation for 1.3.2
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\132\\\\ALU-VSA-010302-APP-Services-mips64.tar\\\\ALU-VSA-010302-APP-Services-mips64\\\\astats_catcher
    modify  ${driver}  ${binary.binaryclass.signed_digest}  yAHbHULZYSUNGwdMUfz8J4GAQAhUdvGlBuRNwH30jp2IP1iYZt08yK0MVimY6AdMlAwfD8PfwQAq7l38jHRCPae8mDgT+3b/Q75lWplN9jsZ7q23yxXK77GJAloFwYn7YWneNnyQbwBWGcttct9xjLc6OulllXW13g2qbvR2ybQ=
    modify  ${driver}  ${binary.binaryclass.type}  statcatcher
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 1 or 2
    deleteentry  ${driver}  binary  astats_catcher
sdp.730
    [Documentation]  flowshaper creation for 1.3.2sp1
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\132sp1\\\\ALU-VSA-010302-SP1-APP-Services-mips64\\\\abin\\\\astats_catcher
    modify  ${driver}  ${binary.binaryclass.signed_digest}  Z5WDHSj/dt3/t9L3OLtVVIRcHHauHhBusfXzXbJjAntBTjZhhAirzeYLjtboO9AklUitdGSp9RokYiwn/zPmQMM2ParXvdvMxCDd6SdfagqLtsYD6Z4K5jH9371afSmmh67DYLai2ZU2qlPN/l7Z2oFOQUNrPwVIWDI1ytbTVSE=
    modify  ${driver}  ${binary.binaryclass.type}  statcatcher
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 1 or 2
    deleteentry  ${driver}  binary  astats_catcher
sdp.737
    [Documentation]  flowshaper creation for 3.0
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\30\\\\ALU-VSA-030000SP5-APP-Services-mips64\\\\abin\\\\astats_catcher
    modify  ${driver}  ${binary.binaryclass.signed_digest}  k1ner1h5aKrbj2vLGXiZFAHpnbwP6/esnqD0rDNEFYQQpcbmChWs+Yh7c1evuhCXfjVCRs+KIU5zmovaPTmP2B9KVapNePaNWJQRfPO7qaxvkz5Kk4T7/S702HxNXpDMKZpEJ5ujX1Ge+z085xCPBkjp6Zl5amqv1VQvvy162kA=
    modify  ${driver}  ${binary.binaryclass.type}  statcatcher
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    deleteentry  ${driver}  binary  astats_catcher
sdp.744
    [Documentation]  flowshaper creation for 3.1
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\31\\\\NOKIA-VBO-030100SP2-APP-Services-mips64\\\\abin\\\\astats_catcher
    modify  ${driver}  ${binary.binaryclass.signed_digest}  ZilgBvuK6pB40BHFiOZGjhuer04qDuxID2fJvs8T2rc9mWOoQ/7otTDpwDu2lOEKEg4x6/v4xl3pn47baI9Pu/FvGYGSUmGrP24V0OeGjMS+/2uC0y0sSFqNrwbKaBt93dATcmori2E4lyZ8TiCJTW3IarH1a05WbewDsIGnhfc=
    modify  ${driver}  ${binary.binaryclass.type}  statcatcher
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    deleteentry  ${driver}  binary  astats_catcher
sdp.migrated.751
    [Documentation]  flowshaper creation for 4.0
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\40\\\\NOKIA-VBO-040000SP1-APP-Services-x86_64\\\\abin\\\\astats_catcher
    modify  ${driver}  ${binary.binaryclass.signed_digest}  R9kukTrweyGc6JAAL0a6XyoKFlXTfuxbh15fe1fM3Lif/rPVpA5MhNb5ZrkRYJ8jR2TU5smjSW5WB/4ZSGVBDRGh1HfV8gvIi/7Rzb1q88OVvXLQVV2kklS2Hjn18oMSI2nYerGm1RKG5qB5/HdMtbVVZeOz3dqU5vWdRcQJ+nw=
    modify  ${driver}  ${binary.binaryclass.type}  statcatcher
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 4
    deleteentry  ${driver}  binary  astats_catcher

sdp.724
    [Documentation]  vsa-monitor creation for 1.3.2
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\132\\\\ALU-VSA-010302-APP-Services-mips64.tar\\\\ALU-VSA-010302-APP-Services-mips64\\\\avsa_monitor
    modify  ${driver}  ${binary.binaryclass.signed_digest}  xVuGf7Fx640bmLtgB1WStVkV8fhrDUyDlU6+Pu96JfQ2m4mpFpQEBGmEkuBF7Pi4f/1fKiEQkx83PreBbZwC4+6rM6lAo2YzxMWBLkF5yslMCRyK3KlQjKTxDQrAQ0DvmsZfKCwL5GM+evqdIfMTbRPkxvWU+e7wfohedq7nQPY=
    modify  ${driver}  ${binary.binaryclass.type}  monitor
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 1 or 2
    deleteentry  ${driver}  binary  avsa_monitor
sdp.731
    [Documentation]  vsa-monitor creation for 1.3.2sp1
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\132sp1\\\\ALU-VSA-010302-SP1-APP-Services-mips64\\\\abin\\\\avsa_monitor
    modify  ${driver}  ${binary.binaryclass.signed_digest}  Hl7L+eLZWYZeE5vC5Dp9JJLLdRgW5W9fxj2f9444MExJk31Mfznzqzfm8SPc828WrRru3i/oHIxwvBBwIvUeIRPMh20qtJbdggz/vkJ9SSS6vx2k46myhTpGL3bdN3Y9iJ8BVlqMmunzuMhO7obc74LK31BHjbrhjDvcbQYMbLM=
    modify  ${driver}  ${binary.binaryclass.type}  monitor
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 1 or 2
    deleteentry  ${driver}  binary  avsa_monitor
sdp.738
    [Documentation]  vsa-monitor creation for 3.0
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\30\\\\ALU-VSA-030000SP5-APP-Services-mips64\\\\abin\\\\avsa_monitor
    modify  ${driver}  ${binary.binaryclass.signed_digest}  XqBkh/ByHa9EEiFPkNHT+2K8ATZDAU+aADbQW/tEuleAo74oKfxr0BT1D72KEbm8CLw2L5xtBvWdavWrCS91Jo/4SiVlVvus4NabKUS0yP/jqiWOBOwrC9BZy86fNmBvqoTpiebfuYFU3WwosVCw/EQmFeJ2DJLhCPhRxdXRcjw=
    modify  ${driver}  ${binary.binaryclass.type}  monitor
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    deleteentry  ${driver}  binary  avsa_monitor
sdp.745
    [Documentation]  vsa-monitor creation for 3.1
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\31\\\\NOKIA-VBO-030100SP2-APP-Services-mips64\\\\abin\\\\avsa_monitor
    modify  ${driver}  ${binary.binaryclass.signed_digest}  YxOlNQTg/EvfJEe/a6ndzdqpmEEFs9GssJNiq9bT7bBaSCcjjT7WFaeZIbr2V9BmhzLMIKmHYhEqjfiEmboBfwJU68th7YrpiCQbGVMX9XFDVrwewEjG5kM90fyrEM67voOGRBoqtDbNnvv9cS8nkVtEG+KUeOheSs73oO5oYI8=
    modify  ${driver}  ${binary.binaryclass.type}  monitor
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    deleteentry  ${driver}  binary  avsa_monitor
sdp.migrated.752
    [Documentation]  vsa-monitor creation for 4.0
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\40\\\\NOKIA-VBO-040000SP1-APP-Services-x86_64\\\\abin\\\\avsa_monitor
    modify  ${driver}  ${binary.binaryclass.signed_digest}  FS4ykSjioPKTaXHZ9/kLX4f+EiOT+gloweFmhCXsrPAtMkxWHXtHUGkzTXZ12B66lldf1oLGzTmnm/ebcPTuhnplGLkd9xWTToD+4SPAu/T6/+y8p6TV2VvGx87WgbrFtzgrpWYGA2N1rIt1ciS+cQnsOFhspAwSUpGmdu+O4sM=
    modify  ${driver}  ${binary.binaryclass.type}  monitor
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 4
    deleteentry  ${driver}  binary  avsa_monitor

sdp.725
    [Documentation]  vsa-manager creation for 1.3.2
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\132\\\\ALU-VSA-010302-APP-Services-mips64.tar\\\\ALU-VSA-010302-APP-Services-mips64\\\\avsa_manager
    modify  ${driver}  ${binary.binaryclass.signed_digest}  lKze8x11lg9t91Qmw+eToxysXTaX7UWs3VWsYDTHzV0sYSFhgES5b4NlK04/uOyDQWlUvhxpLYmd4U365fEjIokRAybe0ODbniUHW5zXtCR6PJ1DvFcW124cjTKeMd3SqfYXeAPDjNOY+BEiq/p/ggWoRvy+zK7/RSYhur8jrMU=
    modify  ${driver}  ${binary.binaryclass.type}  manager
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 1 or 2
    deleteentry  ${driver}  binary  avsa_manager
sdp.732
    [Documentation]  vsa-manager creation for 1.3.2sp1
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\132sp1\\\\ALU-VSA-010302-SP1-APP-Services-mips64\\\\abin\\\\avsa_manager
    modify  ${driver}  ${binary.binaryclass.signed_digest}  Wga4tBJw8AH30t2+UW0A2RcAk2w7AVUXFlMF61vvjJQSIweyPeFvSUydp01IIro7sM94O5h2rHlCu3Aw6QST+XWB8LcW15GGIqTjqeAaG4rc2bpx4K8H123VOV2JllZUjY6lybC0ZtNfRnz3TA9aKsaYzSnx718KflEHHAKJsgQ=
    modify  ${driver}  ${binary.binaryclass.type}  manager
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 1 or 2
    deleteentry  ${driver}  binary  avsa_manager
sdp.739
    [Documentation]  vsa-manager creation for 3.0
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\30\\\\ALU-VSA-030000SP5-APP-Services-mips64\\\\abin\\\\avsa_manager
    modify  ${driver}  ${binary.binaryclass.signed_digest}  CE4HIEUGkFmle9gpfoHahVkDTmPfkJIByajOIpx4NfiBsUMTpmonOtN/LVrr7gYZHBVqVYQOUUhsyMFRz3IqZogtHzhwWM7UJO9/REajtECUr7wFLd+8Cr9B7jAR5oftu/SoFiABxCI+DScHvSx5YWNzlgF3QcE1E72ziH7FnCk=
    modify  ${driver}  ${binary.binaryclass.type}  manager
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    deleteentry  ${driver}  binary  avsa_manager
sdp.746
    [Documentation]  vsa-manager creation for 3.1
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\31\\\\NOKIA-VBO-030100SP2-APP-Services-mips64\\\\abin\\\\avsa_manager
    modify  ${driver}  ${binary.binaryclass.signed_digest}  YCjo60ZNS4JxDOnPNFfSO2fqg5EnIA2z0TTZuTtl8wGOUkyVXQBRxaIPia+1PWk4f/p7AYTCo+nXW4N6PvXmUCW7WXrFF1tuMLrnPtBBhARsjg+hQBjCxBiSMll7daM4c6Afr3ogG4TTn1y+XPRuYAT8nUjCtsLKXbPJNo8Zsm8=
    modify  ${driver}  ${binary.binaryclass.type}  manager
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    deleteentry  ${driver}  binary  avsa_manager
sdp.747
    [Documentation]  os upload without revision type
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\ajayth\\\\Documents\\\\Binary\\\\31\\\\NOKIA-VBO-030100SP2-APP-Services-mips64\\\\aOS
    modify  ${driver}  ${binary.binaryclass.signed_digest}  RjsCwmGGegkhGRABGWNXkTdfZRaoeWLxRQpmiOklTFfeOzkFV6iPBLYieG9H8ZC3AjTe2mouD/TR2iJ4L6yLC7lc8XftsqoTesuDzUt2ozdaFCJrZmIcDmu/w0gHi2D7ujIh24aPRuU5knPWE5K5stL68FgT0E3c3hKraQOlscY=
    modify  ${driver}  ${binary.binaryclass.type}  os/PlatformRPM
    validate  ${driver}  ${binary.binaryclass.hardware_revision}

sdp.748
    [Documentation]  os upload with invalid sign
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\ajayth\\\\Documents\\\\Binary\\\\31\\\\NOKIA-VBO-030100-APP-OSinstall-mips64\\\\aOS
    modify  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    modify  ${driver}  ${binary.binaryclass.type}  os/PlatformRPM
    validate  ${driver}  ${binary.binaryclass.signed_digest}  jsCwmGGegkhGRABGWNXkTdfZRaoeWLxRQpmiOklTFfeOzkFV6iPBLYieG9H8ZC3AjTe2mouD/TR2iJ4L6yLC7lc8XftsqoTesuDzUt2ozdaFCJrZmIcDmu/w0gHi2D7ujIh24aPRuU5knPWE5K5stL68FgT0E3c3hKraQOlscY=

sdp.749
    [Documentation]  os upload without revision type
    create_binary_unsigned
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\ajayth\\\\Documents\\\\Binary\\\\31\\\\NOKIA-VBO-030100-APP-OSinstall-mips64\\\\aOS
    modify  ${driver}  ${binary.binaryclass.signed_digest}  RjsCwmGGegkhGRABGWNXkTdfZRaoeWLxRQpmiOklTFfeOzkFV6iPBLYieG9H8ZC3AjTe2mouD/TR2iJ4L6yLC7lc8XftsqoTesuDzUt2ozdaFCJrZmIcDmu/w0gHi2D7ujIh24aPRuU5knPWE5K5stL68FgT0E3c3hKraQOlscY=
    modify  ${driver}  ${binary.binaryclass.type}  os/PlatformRPM
    modify  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    validate  ${driver}  ${binary.binaryclass.is_binary_signed}

sdp.750
    [Documentation]  os upload without revision type
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\ajayth\\\\Documents\\\\Binary\\\\31\\\\NOKIA-VBO-030100-APP-OSinstall-mips64\\\\aOS
    modify  ${driver}  ${binary.binaryclass.signed_digest}  RjsCwmGGegkhGRABGWNXkTdfZRaoeWLxRQpmiOklTFfeOzkFV6iPBLYieG9H8ZC3AjTe2mouD/TR2iJ4L6yLC7lc8XftsqoTesuDzUt2ozdaFCJrZmIcDmu/w0gHi2D7ujIh24aPRuU5knPWE5K5stL68FgT0E3c3hKraQOlscY=
    modify  ${driver}  ${binary.binaryclass.type}  os/PlatformRPM
    modify  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    save  ${driver}
    get_navigation_page  ${driver}
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\ajayth\\\\Documents\\\\Binary\\\\31\\\\NOKIA-VBO-030100-APP-OSinstall-mips64\\\\aOS
    modify  ${driver}  ${binary.binaryclass.signed_digest}  RjsCwmGGegkhGRABGWNXkTdfZRaoeWLxRQpmiOklTFfeOzkFV6iPBLYieG9H8ZC3AjTe2mouD/TR2iJ4L6yLC7lc8XftsqoTesuDzUt2ozdaFCJrZmIcDmu/w0gHi2D7ujIh24aPRuU5knPWE5K5stL68FgT0E3c3hKraQOlscY=
    modify  ${driver}  ${binary.binaryclass.type}  os/PlatformRPM
    modify  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    validate  ${driver}  ${binary.binaryclass.name}  aOS
    deleteentry  ${driver}  binary  aOS

sdp.751
    [Documentation]  os upload without revision type
    create_binary
    modify  ${driver}  ${binary.binaryclass.name}  aOS
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\ajayth\\\\Documents\\\\Binary\\\\31\\\\NOKIA-VBO-030100-APP-OSinstall-mips64\\\\aOS
    modify  ${driver}  ${binary.binaryclass.signed_digest}  RjsCwmGGegkhGRABGWNXkTdfZRaoeWLxRQpmiOklTFfeOzkFV6iPBLYieG9H8ZC3AjTe2mouD/TR2iJ4L6yLC7lc8XftsqoTesuDzUt2ozdaFCJrZmIcDmu/w0gHi2D7ujIh24aPRuU5knPWE5K5stL68FgT0E3c3hKraQOlscY=
    modify  ${driver}  ${binary.binaryclass.type}  os/PlatformRPM
    modify  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    save  ${driver}
    get_navigation_page  ${driver}
    create_binary
    modify  ${driver}  ${binary.binaryclass.name}  aOS_duplicate
    modify  ${driver}  ${binary.binaryclass.signed_digest}  RjsCwmGGegkhGRABGWNXkTdfZRaoeWLxRQpmiOklTFfeOzkFV6iPBLYieG9H8ZC3AjTe2mouD/TR2iJ4L6yLC7lc8XftsqoTesuDzUt2ozdaFCJrZmIcDmu/w0gHi2D7ujIh24aPRuU5knPWE5K5stL68FgT0E3c3hKraQOlscY=
    modify  ${driver}  ${binary.binaryclass.type}  os/PlatformRPM
    modify  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 3
    validate  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\ajayth\\\\Documents\\\\Binary\\\\31\\\\NOKIA-VBO-030100-APP-OSinstall-mips64\\\\aOS
    deleteentry  ${driver}  binary  aOS


sdp.migrated.753
    [Documentation]  vsa-manager creation for 4.0
    create_binary
    modify  ${driver}  ${binary.binaryclass.browse}  C:\\\\Users\\\\krparama\\\\Documents\\\\Binary\\\\40\\\\NOKIA-VBO-040000SP1-APP-Services-x86_64\\\\abin\\\\avsa_manager
    modify  ${driver}  ${binary.binaryclass.signed_digest}  fYN/DqLCrhg/PqvDCLruYfoawXvNqNeI3JISX2T8yhToJIqEddA1kkU99MVic4ahO7cB71AXLKTZ9lwRs7anP5QqL2ZLltM7MIjuOaTOEebi86blrFKUJ5aUdyqzQk91HqdpMcd66CWnRvk0CwVqKZut9d3nzdvkDv/LNMn7Tm4=
    modify  ${driver}  ${binary.binaryclass.type}  manager
    validate_pos  ${driver}  ${binary.binaryclass.hardware_revision}  Revision 4
    deleteentry  ${driver}  binary  avsa_manager

*** Keywords ***

setup_add_new_binary
    ${SDP} =   BuiltIn.Get Library Instance  sdppo
    open_page  ${driver}  ${SDP.binary }
    ${binary} =   BuiltIn.Get Library Instance  binaryPage
    SET GLOBAL VARIABLE    ${binary}

create_binary
    create_new_  ${driver}  binary
    is binary signed  ${driver}

create_binary_unsigned
    create_new_  ${driver}  binary


validate_check
    [Arguments]  ${field}  ${data}
     log  ${field} ${data}
     create_binary
     validate  ${driver}    ${field}    ${data}


validate_positive1
    [Arguments]  ${field}  ${data}  ${pagename}
    log  ${field} ${data}
    create_binary
    validate_pos  ${driver}  ${field}  ${data}  ${pagename}
    deleteentry  ${driver}  ${pagename}  rewrapper54new