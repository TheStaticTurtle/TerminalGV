# TerminalGV

So I got bored in the train, TerminalGV is a **very** simple client to display stats about your [SNCF](https://en.wikipedia.org/wiki/SNCF) TGV/TER train in your terminal.

The "on-train" api (https://wifi.sncf) runs socket.io, you can join the namespace `/router/api/pepita` and listen for events,
this script listen to theses events: `gps`, `connected_devices` (Network), `internet_link_quality`, `trainDetails` (Stops/Time/Train infos)

Dates are converted to the `Europe/Paris` timezne edit the `ui.py` file to change it

![Screenshot](https://data.thestaticturtle.fr/ShareX/2021/12/22/train.png)
