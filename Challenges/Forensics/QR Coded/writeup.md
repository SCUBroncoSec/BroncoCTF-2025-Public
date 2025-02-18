# Info
Title: QR Coded
Flag: bronco{th1s_0n3_i5}
# Challenge
This was made using the python script in this folder

Essentially, make two qr codes

# Solution
To solve this challenge, you find extract the LSB bitplanes into their own separate files (for example, use StegOnline)

Then, make the background transparent for each of them.

Finally, overlap them in any image processing software and scan for the flag.
