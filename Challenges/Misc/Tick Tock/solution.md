# Tick Tock

## Flag
bronco{five_minutes_until_midnight}

## Intended Solution:
This image has data hidden inside of it that can be extracted using a program like StegOnline. The time on the clock (11:55) tells us to extract data in the 1 and 5 bits for R, G, and B. This give the following as a result (once spaces are removed):
```
ticktocktocktockticktickticktock ticktocktocktickticktocktocktock ticktocktocktickticktockticktick ticktocktockticktickticktocktock ticktocktocktocktickticktocktick ticktocktocktickticktockticktick ticktocktocktocktockticktocktock ticktocktocktockticktockticktock ticktocktocktocktocktickticktick ticktocktockticktockticktocktock ticktocktocktockticktockticktick ticktockticktocktocktocktocktock ticktocktockticktickticktocktick ticktocktocktocktocktickticktick ticktocktockticktickticktocktock ticktocktockticktockticktocktick ticktocktockticktocktickticktock ticktocktocktockticktockticktick ticktocktockticktocktickticktick ticktockticktocktocktocktocktock ticktocktockticktockticktocktick ticktocktockticktickticktocktock ticktocktockticktocktickticktock ticktocktocktocktocktickticktick ticktocktocktickticktickticktock ticktockticktocktocktocktocktock ticktocktockticktickticktocktick ticktocktocktocktocktickticktick ticktocktocktocktickticktocktock ticktocktockticktickticktocktock ticktocktocktocktocktickticktick ticktocktocktockticktocktocktick ticktocktocktockticktocktocktock ticktocktockticktocktickticktock ticktocktocktocktocktockticktock
```
The repetition of exactly two words indicate that it can be converted into binary, where tick = 0 and tock = 1, and translating the binary to text gives `qgdcrd{uxkt_bxcjith_jcixa_bxscxvwi}`. This in the format of the flag, and a simple ceasar cipher shift converts it to the answer `bronco{five_minutes_until_midnight}`.