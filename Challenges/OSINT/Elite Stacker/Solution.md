# Elite Stacker

## Flag
bronco{The Laboratory}

## Intended Solution:
This is an OSINT challenge contained within TETR.IO, a free-to-win modern yet familiar online stacker. (Basically free online Tetris that I really enjoy)

The first challenge is dealing with the `.ttr` file. This is a TETR.IO replay file which can be opened in the site "TETR.IO" - note that this might take some forensics work to uncover/unpack. The hints about stacking, sprint, and T-Spins should eliminate other possibilities of `.ttr` and hint people towards TETR.IO.

When the user realizes they must go to `TETR.IO`, they can enter as an anonymous user (leave the name blank) to pass the login screen and enter the main menu. Now, the replay file can be opened either by:

1. By dragging and dropping the file into the window once past the login screen.
2. Going to TETRA CHANNEL and entering the ID located at the end of the replay file's name. 

This will open up YOSHIE878's most recent 40 Lines personal best run (insane attempt btw, just playing for the sake of this challenge). Click on YOSHIE878's name on the bottom to be taken to open up their account briefing, and select VIEW FULL PROFILE.

Then, you should end up at https://ch.tetr.io/u/yoshie878 - yoshie's TETR.IO profile. The goal is to find the "highest floor Yoshie has climbed to in the Zenith Tower." This might require some research:

- The Zenith Tower is Quick Play mode.
- In Quick Play, your goal is to achieve the highest altitude by sending lines and eliminating other players in a persistent free-for-all lobby.
- Altitude ranges are divided in to sections called "Floors," each of which have their own name.

The QUICK PLAY section has yoshie's career best altitude - 1,015.8m. This is the altitude we are looking for!

Additionally, the ACHIEVEMENTS section contains the ZENITH EXPLORER achievement: it states that Floor 7 is the highest floor yoshie has discovered. 

Now, we need to translate this to the actual name of the floor. Here are 2 options:

1. Watch someone play Quick Play and pay attention to the board. Even in replay mode, every time a player reaches a new floor, text will flash with `FLOOR #` and `FLOOR NAME` whenever they reach a new floor. There is also a floor indicator on the replay seek bar. There are endless QUICK PLAY replays to use for this purpose in the TETRA CHANNEL.
2. Find a source that maps the Quick Play floor names to their numbers, such as https://tetris.wiki/TETR.IO/Quick_Play 

Floor 7 is `The Laboratory`, and that is the answer to the floor portion. (Note: This part could be brute-forced with a list of the floor names)

Wrap both parts it in `bronco{}` and submit!


P.S. this challenge not sponsored by this TETR.IO or its developer osk. I just really like this game!