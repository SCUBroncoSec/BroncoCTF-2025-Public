# Homie Owes Me

## Flag
bronco{y0sh1eth3hom!e8778}

## Intended Solution:
This is a simple password cracking exercise. Using the `intel.txt` provided, we can deduce:

1. The password involves the phrase `yoshiethehomie`
2. There will be some numbers in the phrase - the definition of leetspeak
3. There will be one `!` somewhere in the password, replacing one of the characters
4. There is a 4-digit number at the end of the phrase.
5. The flag format is in the password (part of the hashing process).

Additionally, inspection of the given value should show it is a `SHA-256` hash. (Only the contents after the `:` are the hash; the info is provided in typical John the Ripper `user:pw` format)

John the Ripper or any password cracker is recommended to solve this challenge.
