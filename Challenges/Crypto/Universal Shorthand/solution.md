# Universal Shorthand

# Flag
bronco{ilov3ph0n3t1cs}

# Solution
This challenge uses a substitution cipher, but is based on phonetics rather than character substitution.
The way to solve the challenge was to use the fact that there was a known plaintext to find out which words corresponded to which encrypted words.
Looking at all of them, it is possible to see that words which start with the same sounds start with the same characters, and words always map onto themselves. This should point users in the direction that it may be phonetic.
After noticing this, users can search for characters in the flag block, find the corresponding sounds, and have the flag read to them at the end.