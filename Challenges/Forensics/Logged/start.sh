echo "Click the window you wish to record"
xev -1 -id $(xwininfo | rg "Window id: (.+?) " -or '$1') | tee keys.log
