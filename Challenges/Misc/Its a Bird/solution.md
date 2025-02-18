# It's a Bird!

## Flag
bronco{i<3planes}

## Intended Solution:
The description is riddled with hints. 

You are given an image. It has a file hidden within. 

`steghide extract -sf myBirb.jpg`

You will then get a csv file, called birb.csv. In this, there is a lot of data. 

By searching for and analyzing the data, and also hinted from the title and the description, the data is related to aviation. Specifically, this is SBS-1 BaseStation data. You are to look into the data, and realize what the squawk is.

Here is a good reference. http://woodair.net/sbs/Article/Barebones42_Socket_Data.htm

The squawks that have been listed here are all ASCII values. Translating, you get the flag. 