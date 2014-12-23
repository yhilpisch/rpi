.. Raspberry Pi for Serious Things master file, created by
   (c) Dr. Yves J. Hilpisch.
   The Python Quants GmbH

   This documentation is about setting up the Raspberry Pi
   for certain "useful" things.

Raspberry Pi for Serious Things
-------------------------------

This Web site and tutorial is about setting up and using the Raspberry Pi for some serious things. Among others, it covers:

* using the RPi as a Python calculator
* using the RPi as ftp server
* using the RPi with a Webcam for security applications

I assume that you have bought a RPi and all the equipment necessary to use it (power plug, etc.). It is recommended to start using the RPi connected to the Web via an Ethernet cable (for convenience and speed).

Setting up the RPi
~~~~~~~~~~~~~~~~~~~~

The first step is to build a bootable SD card for the RPi. We will use a **Raspbian Debian Wheezy** image in the  following which you can download here: http://www.raspberrypi.org/downloads/.

Using a Mac, you can do the following to write the downloaded image to the  SD card. First, insert the SD card. On the shell type::

    diskutil list

Using Linux (eg Ubuntu), type::

    df -h

This gives you a list of all disk drives. Identify the SD card with a name like ``diskX``.

Then unmount the SD card on the Mac as follows::

    diskutil unmountDisk /dev/diskX

Under Linux do::

    umount /dev/diskX

The next step is to write the OS image to the SD card::

    sudo dd bs=1m if=os-image.img of=/dev/diskX

Here, replace the image name and the disk name with those that apply for you.

Booting the RPi
~~~~~~~~~~~~~~~~~

You should connect a monitor via a HDMI cable to the RPi and a keyboard via USB (I am using a keyboard and mouse, both connected via the same USB token). Put the SD card into the RPi and connect it to the power plug. It should now boot.

You will be directed to an options screen where you can do different things, like for example:

* expand the file system to use the full capacity of your SD card (which you should do)
* change the root/pi password (which I assume in the following you do not do)
* enable SSH access (via Advanced Options, which you should do)

After finishing the options setting procedure, the RPi has to re-boot. Once rebooted, you should login as user ``pi`` with password ``raspberry`` (if not changed before). The type::

    sudo apt-get update

This might  take a while. After that, upgrade you system with::

    sudo apt-get upgrade

You can further use the RPi with a monitor and keyboard connected or you can use it via ``ssh`` access as the next section explains.

Access via SSH
~~~~~~~~~~~~~~~~~

When the RPi boots, being connected via Ethernet cable to a router, it shows at the end of the boot output the **IP address** under which it is connected. Alternatively, for example, using your admin access to your router, identify the IP address under which the RPi is connected. Then using another computer connected to the local network, open the shell and ``ssh`` to the RPi as follows::

    ssh pi@192.168.178.xx

Here, replace the IP address that applies for you. After you are prompted for it, type in the password ``raspberry``. You should now be connected with the RPi.

Using ``screen``
^^^^^^^^^^^^^^^^^

A really helpful tool when working via ``ssh`` access is ``screen`` (cf. http://ss64.com/bash/screen.html). It allows you to have multiple shells running at the same time, to disconnect from them and later reconnect. Install it via::

    sudo apt-get install screen

To start it, type::

    screen

A new screen is created by ``ctrl+a`` then ``c``. You switch to the next screen with ``ctrl+a`` and then ``n`` (more commands are found under the above link).

Later when you reconnect via ``ssh`` to the RPi you can reattach to your screen session via::

    screen -r

Fixed IP Address
^^^^^^^^^^^^^^^^^

A fixed IP address for the RPi is helpful for a number of reasons. I have configured the router such that the RPi always gets the same IP address, say 192.168.178.xx. For the RPi type the following to edit the respective settings::

    sudo nano /etc/network/interfaces

Replace the following line::

    iface eth0 inet dhcp

by these lines::

    iface eth0 inet static
    address 192.168.178.xx
    netmask 255.255.255.0
    gateway 192.168.178.1

Exit the editor with ``ctrl+x`` saving the changes. Finally, re-start the network service by::

    sudo /etc/init.d/networking restart

Henceforth, the RPi should be reachable under 192.168.178.xx.

Public IP address
^^^^^^^^^^^^^^^^^^

Using a service like http://whatismyipaddress.com/, you can figure out what your public router IP address is (depending on your router this might change regularly; modern ones at least keep their addresses until the next re-boot).

Say you have figured out that the address is xx.yy.zz.100. Configuring your router to make the IP address of your RPi 192.168.178.xx an "exposed host", should enable you to access the RPi from anywhere via::

    ssh pi@xx.yy.zz.100

Knowing you public IP you can also set an A record (cf. http://support.dnsimple.com/articles/a-record/) of one of your domains to access the RPi, like http://rpi.mydomain.net (which should have an A record equal to the public IP xx.yy.zz.100). 

Using Public Keys
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connecting to the RPi via ``ssh`` generally asks for a password. However, you can also generate RSA keys and copy the public key to the RPi which then allows you the ``ssh`` to the RPi without typing your password again and again (when using the same machine and/or keys). Generate keys (if you haven't yet) via::

    ssh-keygen -t rsa

Then copy the public key via (Linux)::

    ssh-copy-id pi@192.168.178.xx

On the Mac see, for example, https://github.com/beautifulcode/ssh-copy-id-for-OSX.

Small Projects with the RPi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Having set up the RPi (in particular for ``ssh`` access), you can now move on and implement one or more of the following smaller projects:

The documentation is structured as follows:

.. toctree::
   :maxdepth: 2

   ftp


About the author
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yves Hilpisch is managing partner of The Python Quants GmbH (Germany) and co-founder of The Python Quants LLC (New York City). The Python Quants provide, among others, the **Python Quant Platform** as a solution for browser-based, interactive, collaborative financial analytics (cf. http://quant-platform.com). On this platform (for which free trials are available) you can also immediately try our open source financial analytics library DX Analytics (http://dx-analytics.com).
   

.. Indices and tables
.. ------------------

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

Copyright & Disclaimer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

© Dr. Yves J. Hilpisch \| The Python Quants GmbH

This Web site comes with no representations or warranties, to the extent
permitted by applicable law.

http://www.pythonquants.com \| rpi@pythonquants.com \|
http://twitter.com/dyjh

**Python Quant Platform** \| http://quant-platform.com

**Derivatives Analytics with Python (Wiley Finance)** \|
http://derivatives-analytics-with-python.com

**Python for Finance (O'Reilly)** \|
http://shop.oreilly.com/product/0636920032441.do
