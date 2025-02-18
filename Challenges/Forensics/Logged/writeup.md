# Info
Title: Logged
Flag: bronco{l0gg1ng_ftw}
# Challenge
This was made by running start.sh on my machine running the X11 window server.

Then, opening vim and spamming keys, and then running motions to fix it in a nonobvious way.

Finally, the log file was edited to make it a little harder to work with.
# Solution
This is an xev dump with critical info removed. It is of a vim typing thing.

Turn it into text, then run the text in vim.

Look at the file it makes, and you are good.

Create something like in solution.py, then run `vim -c "$(python solution.py)"` or something like it.

Or I guess put it all in by hand, but that's a bad idea.
