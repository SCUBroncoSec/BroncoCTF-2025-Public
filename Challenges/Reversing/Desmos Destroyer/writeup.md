# Info
Title: Desmos Destroyer
Flag: /bronco{g,g,c,l,(dl|ld),a,u,u,u,(ur|ru),a,f,f,f,f,(dr|rd),(dr|rd),d,d,d,(dr|rd),(dr|rd),a}/
Notes: This is a regex flag
# Challenge
This is a Desmos reversing challenge. It is meant to be hard.
You are supposed to hit various challenges, then fix them the only way possible and move on to the next one.

Generally, here is the solution:
- Somehow fix the food problem
- Do the glitch for infinite tiredness.
- Rush to a specific space which can be fortified (exploit zombie pathing not taking into account slowing areas).
- Fortify twice, which allows for the zombies to be defeated.
- Pass through the corner of the zombie wall.
- To get around the kill screen, do the special action of hide in a cave space to be “invulnerable” for a turn.

# Solution
The correct flag is meant to be found by solving all of the following problems
## Problem: Food
You will run out of food very fast. The way around this is to send people out to get it.
The only way this doesn't kill you is to send out 2 or 3 of them.
Sending out 3 takes too long, so it is not an option.
## Problem: Energy
You can't really do anything with the amount of energy you have.
So, you exploit a glitch to get unlimited energy.
This glitch can be found by looking into the equations, and is obviously a massive issue that has to be fixed.
## Problem: Zombie
The Zombie will catch you eventually. Plus, they need to die for you to win.
The only way to do this is exploit the fact that while fortifying only boosts you once, it boosts the mountain bonus a lot.
In order to get enough, you can calculate that it takes a certain amount of them to kill the zombie.
The only way to get this many is to guide the zombie through a swamp.
## Problem: Zombie Wall
The zombie wall has no corners.
This means that you have 4 options to get through, but only 1 will get you to the next spot in time.
## Problem: Kill Wall
The hard kill wall has only 1 thing that can stop it: cave action.
There is only 1 cave, and coming from the spot where you HAD to stop the zombie, you get there just in time if you map optimally.
## Putting it all together
Once you work through all of that, you have the flag.
Wrap it in the flag format, and you will be done.
