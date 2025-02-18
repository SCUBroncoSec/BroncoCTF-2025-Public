# Wordlands

## Flag
bronco{i_love_admiring_beautiful_landscapes}

## Intended Solution:
This challenge is a reference to the mobile game "Wordscapes." (They are actually heavy spenders when it comes to mobile advertisements, so the lore is warranted!)

In the game, you connect letters given in a ring to spell out words. Normally, you can only use letters once, and the goal is to spell out all the designated words in each "landscape."

The image given breaks all these rules:

1. Letters are used multiple times, as we see the selection lines going to letters more than once
2. The selection line goes outside the ring to hit an "underscore" character
3. There's only one "word" being spelled, instead of the typical crossword puzzle in Wordscapes

One's intuition might prompt them to just start with "bronco{" (beginning of the flag) and try to follow the selection lines to spell out the flag. However, this is impractical with how thick the selection line is and how many characters (51) the flag is. The lines cross so much and letters are repeated several times such that following the selection line becomes incredibly difficult, if not impossible.

This is a forensics challenge, namely a steganography challenge, so the real approach is to figure out what is hiding within this file. In fact, hidden inside the PNG's least significant bits is a PSD (Photoshop) file! It is a super-shrinked version of the photoshop file used to make this image. While over 7x smaller than the original picture, having access to a PSD is still incredibly valuable. We get to see the layers of the image, and it turns out the selection lines are stacked in the order of the flag.

With the ability to isolate the selection lines via the layers, we no longer have to be overwhelemed by all 50 lines causing lots of ambiguities. Either hide all the lines and show one at a time, or select each line to highlight it. Whichever strategy is used to provide better clarity for the selection lines, follow the lines one-by-one and write out the flag.

If looking for a program to open PSDs, [photopea.com](photopea.com) is a great free option.