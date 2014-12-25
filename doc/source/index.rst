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

You can further use the RPi with a monitor and keyboard connected or you can use it via ``ssh`` access as one of the small projects explains.


Small Projects with the RPi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Having set up the RPi, you can now move on and implement one or more of the following smaller projects. Ideally, you should **follow them in the sequence as listed below** since later projects assume (at least to some extent) that you have successfully finished earlier ones.

The documentation is structured as follows:

.. toctree::
   :maxdepth: 2

   00_ssh
   01_ipython
   02_web_app
   03_ftp


About the Author
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
