
qrserver 
======== 
 
A simple tool to serve a file to a smartphone using a QR code. 
 
Installation
------------

.. code-block:: bash
    
    Install netiface, qrcode, bottle:
    sudo apt-get install python-netifaces python-qrcode python-bottle
    Then simply download qrserver.py

Usage 
----- 

.. code-block:: bash
  
    Help:
    ./qrserver.py -h
    
    Serve a file:
    ./qrserver.py README.rst   


Screenshot 
----------

.. code-block:: bash

    ./qrserver.py README.rst
    
    URL: http://192.168.1.4:8080/README.rst 
                                      
                                      
        █▀▀▀▀▀█ ▀ ▀██▄█▀  █▀▀▀▀▀█     
        █ ███ █ █▀ ▄ █▀▄█ █ ███ █     
        █ ▀▀▀ █ ▀██▄▄█▀ ▄ █ ▀▀▀ █     
        ▀▀▀▀▀▀▀ ▀ ▀▄▀ █ █ ▀▀▀▀▀▀▀     
        ██▀▀ ▄▀▄█▄▀ ▄▀ ▀▀█▄▄▀▀▀▄▀     
         ▄▀▀▄▄▀▀▀ ▄█ █▀▀█▄█  ▄▄       
        ▀ ▀▄▄ ▀█ ▀ ▄▀ ▄ █ ▄ ▄ ▀▀█     
        ▄▀▀██▄▀▄ █▄ ▀▀▀▀▄▄▄▀▀▄▀▀▄     
          ▀▀  ▀▀▄▀█▀█▀▄ █▀▀▀█ █▀█     
        █▀▀▀▀▀█  ▄█▀▄█▄██ ▀ ██ █▀     
        █ ███ █ ▄▀▄ █  ██▀▀██▀▄▀▄     
        █ ▀▀▀ █ ██▄  ▄▄▀▀  ▀▄█▀▀      
        ▀▀▀▀▀▀▀ ▀▀  ▀    ▀▀▀ ▀▀▀▀     
                                      
                                      
    Bottle v0.12.7 server starting up (using WSGIRefServer())... 
    Listening on http://192.168.1.4:8080/ 
    Hit Ctrl-C to quit. 
