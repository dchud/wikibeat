wikibeat
========

Sonifying wikipulse (http://github.com/edsu/wikipulse), @edsu's 
node.js app showing gauges representing how often wikipedia
pages are changed in different languages.

With an unchanged wikipulse up and running, the script backbeat.py
reads the per-language json feeds wikipulse creates and turns those
into OSC (http://opensoundcontrol.org/) messages.  It sends those
OSC messages to a Pd (http://puredata.info/) application that
sonifies the highest rates of wikipedia changes into something like
a drumbeat.

Installation
============

First install wikipulse using @edsu's exact instructions.  wikibeat
uses wikipulse as-is, without modifications, though you should
probably change the param names in config.json starting with 'irc'.

    - see http://github.com/edsu/wikipulse

You'll know it's working when you visit http://localhost:3000/ and
see a bunch of gauges winding up, showing edit rates.

Second, get this app:

    % git clone https://github.com/dchud/wikibeat.git
    % cd wikibeat

Third, set up a python environment to run the OSC bridge.  We built
this on OSX machines, but it should work fine on your linux of
choice.

    - install virtualenv
    - create a virtualenv in this directory:

        % virtualenv --no-site-packages ENV

    - activate the virtualenv
        
        % source ENV/bin/activate

    - install python dependencies

        % pip install -r requirements.txt

Fourth, download and install Pd.  We used Pd-extended 0.42.5.

    - http://puredata.info/downloads or
    - http://sourceforge.net/projects/pure-data/files/

Run Pd and open wikibeat:

    - File -> open wikibeat-main.pd in this directory
    - in the "Pd-extended" window, check "compute audio"

Run backbeat:

        % python backbeat.py

You'll know it's working when you see a series of numbers print out
on the console once a second.  This is the sorted set of highest-
edit-rate language-specific wikipedias.

Start wikibeat:

    - in the wikibeat-main.pd window, click "bang" near the
      top-left of the patch window.

Turn your speakers up.  You'll know it's working if you hear a 
beat!


Credits
=======

@edsu's wikipulse does the hard work of pulling change data from
the wikipedia IRC channels and making that available easily over a
series of web pages.

Christopher Burns wrote the wikibeat Pd app; Dan Chudnov (@dchud) 
wrote the backbeat OSC thingy.


License
=======

See LICENSE.txt.
