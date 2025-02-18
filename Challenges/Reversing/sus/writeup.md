# Info
Title: sus
Flag: br4inr0t

# Challenge

This is a reversing challenge that requires readers to determine the meaning of a set of undefined keywords in a C++ program. Once this is completed, the program will be able to execute as normal, succesfully iterating through the algorithms inside and returning a proper flag in the format bronco{}. Until the user assigns a meaning to each keyword, the program will not able to execute, and only the correct assignments will result in correct output.

# Solution

The correct flag is to be determined following an iterative process, but certain knowledge can help expedite the process. To begin with, individuals should aim to determine all keywords that are "obvious", such as recognizing that main() is preceded by int, blocks of code are enclosed in '{}', and more. This process, in theory, should be enough to decode a large chunk of the program, if not all of it. However, some individuals may recognize that the functions rando() and L() are PRNG simulators using the Middle Square Method and a Linear Congruential Generator respectively, which grealy helps with recognizing the keywords within those functions. Once a user works through the entire program, they will be able to execute it and determine the flag.

# Files

sus_original shows the original code used, and sus_solved shows the value of each #define.
