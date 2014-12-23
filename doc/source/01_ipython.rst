
Raspberry Pi for Data Analytics
---------------------------------

This example is about data analytics with Python (cf. http://python.org) and IPython (cf. http://ipython.org) on the RPi. Before we install it, first install the Python PIP installer by::

    sudo apt-get install python-pip python-dev build-essential 

Any serious data analytics effort with Python generally includes to some extent the pandas library (cf. http://pandas.pydata.org). To install it, upgrade the NumPy library first (cf. http://scipy.org)::

    sudo pip install numpy --upgrade

This might take quite a while (1h+) due to the library being pretty large and the RPi not being that quick in compiling it. Then install pandas::

    sudo pip install pandas

This also takes some time (again 1h+). Finally, install the IPython interactive analytics environment::

    sudo pip install ipython

Now start IPython on the shell via::

    ipython

