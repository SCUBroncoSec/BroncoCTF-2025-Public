# Info
Title: theflagishere!
Flag: i_am_a_flag

# Challenge

This is a reversing challenge that requires the user to decompile a .pyc file, analyze the code, and determine the flag. This is made harder by the presence of a myriad of "fake" flags, which, despite not being the real flag for the challenge, have a key role to play when it comes to figuring out the solution. Once the user determines the algorithm used to create the flag and recognizes the order in which the characters are listed, the flag is theirs for the taking!

# Solution

For this challenge, I would recommend using an online decompiler such as https://pylingual.io, as it is able to fully decompile the source code and create a human-readable program. Once the user reaches this step, they can either manually figure out what the algorithm being used is and decode the flag by hand, or simply move the source code to a new python program and add a print statement at the end of the code that outputs the flag in the character order listed. Once either of these steps is completed, the flag will be obtained.

# Files

theflagishere.py is the original python source code.
