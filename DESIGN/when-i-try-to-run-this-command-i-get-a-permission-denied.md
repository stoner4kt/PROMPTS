# When I try to run this command, I get a permission denied

When I try to run this command, I get a permission denied error ( <(curl -Ls https://bit.ly/udroid-installer) udroid install jammy:xfce4)

---

I want to run these commands now after installing the Ubuntu pkg install x11-repo -y pkg install termux-x11-nightly -y termux-x11 :1 -ac &
 udroid login jammy:xfce4 export DISPLAY=:1 startxfce4 & and I get these errors : ~/fs-manager-udroid $ pkg install x11-repo -y pkg install termux-x11-nightly -y termux-x11 :1 -ac & udroid login jammy:xfce4 export DISPLAY=:1 startxfce4 & curl -fsSL https://ollama.com/install.sh | sh ollama serve
[2] 31867
[3] 31868
sh: 0: cannot open ollama: No such file
> LOGIN jammy:xfce4
No mirror or mirror group selected. You might want to select one by running 'termux-change-repo'
Checking availability of current mirror:
[*] https://termux.cdn.lumito.net/termux-main: ok
E: Command line option 'a' [from -ac] is not understood in combination with the other options.
curl: (23) Failure writing output to destination, passed 1378 returned 0
[1]   Exit 100                   pkg install x11-repo -y pkg install termux-x11-nightly -y termux-x11 :1 -ac
[2]-  Exit 100                   pkg install x11-repo -y pkg install termux-x11-nightly -y termux-x11 :1 -ac
[3]+  Done                       udroid login jammy:xfce4 export DISPLAY=:1 startxfce4

---

Do i need to download the x11 app separately outside of termux

---

OK I have the app, when I run the commands this is what I get : termux-x11 :1 -xstartup "udroid login jammy:xfce4 -- /bin/bash -c 'export DISPLAY=:1 && startxfce4'" &
[1] 9361
~ $ _XSERVTransSocketUNIXCreateListener: ...SocketCreateListener() failed
_XSERVTransMakeAllCOTSServerListeners: server already running
(EE)
Fatal server error:
(EE) Cannot establish any listening sockets - Make sure an X server isn't already running(EE)
~ $ -udroid login jammy:xfce4
-udroid: command not found
[1]+  Exit 1                     termux-x11 :1 -xstartup "udroid login jammy:xfce4 -- /bin/bash -c 'export DISPLAY=:1 && startxfce4'"

---

So if i want to close down the machine and stop it from running, I can just logout in th x11 app ui and then kill - for Termux-x11

---

What alternatives are there and can I use this setup on a device to host a server/remote desktop/ Claude code/Gemini Cli / vps for Agent

---

So if i delete termux and x11 this whole setup deletes aswell right
