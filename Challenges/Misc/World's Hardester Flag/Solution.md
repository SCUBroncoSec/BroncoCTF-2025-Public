# World's Hardester Flag

## Flag
bronco{n0th1ng_1s_2oo_h4rd_4_m3!}

## Intended Solution:
You're presented with an unimaginably difficult 2D obstacle course.

Last year, you could try to beat the game, but with the new final room - "OG4 Hell" - you are NOT beating this new course legit.

The intended way to solve the challenge is to abuse the Lua terminal the creator left in. While there are new restrictions - with three banned words `Position, Humanoid, Destroy, Name` that INSTANTLY KILL the player upon detection in the player's submission - it is still very much breakable.

Here are some ideas:

1. Glitch a teleporter. In the room before the impossible final room, "OG4 Hall," there is a suspiciously placed ClearPad that teleports players to the checkpoint in this room. It has an attribute, `Destination`, which is the part in the world that the ClearPad teleports the players to upon touch. Using the terminal, edit this attribute to be the WinPad. The path to the WinPad can be obtained by mousing over the WinPad, a new debug tool added this year.

2. Noclip through the walls/enemies. While changing the Name of an object will instantly kill you, changing other properties will not. One of the best ones is `CanCollide`, which allows your Roblox character to phase through a part and also not die to Dehnemy-s due to how the hit detection works. Phase out of the map in "OG4 Hell", walk along the baseplate, and phase into the right wall to make contact with the WinPad. Or, disable every single Dehnemy by in "OG4 Hell" (and the other levels) by setting every Dehnemy's CanCollide to False.

The challenge is open-ended and other ways of solving it are possible, too.
