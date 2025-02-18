# Bucky's Impossible Obby

## Flag
bronco{n0t_s0_1mp0551bl3_4ft3r_411_w0w!}

## Intended Solution:
You are given a roblox game which is a seemingly innocent and impossible obstacle course.

The obby is technically possible because the wrap-around can be wall-hopped, but beating the obby will not give you any reward.

The first step is to find the test place. The clues are "alternate universe" in the challenge/place description and the italicized letters "test" "place" in the fake winner's popup screen. For the latter, you can also find this hint by downloading the place file (3 dots on the game page) since the place is uncopylocked. Enable the Win object in StarterGui within Roblox Studio to see the fake winner message for more than 5 seconds post-victory-death.

Hunting down the test place involves checking @YoshieTheReverie's roblox places and stumbling upon [bucky-obby-test-place](https://www.roblox.com/games/115403792174655/bucky-obby-test-place). This place is also uncopylocked, meaning you can download it. This version of the obby is actually nerfed, and it is much easier to get to the winpad. Upon touching the winpad in this place, you're given an obviously fake flag. Deeper investigation is necessary.

In the test place, there is a script called FlagCaller which has a line `require(132906055852488)`. This is actually a public module on the roblox creator store, and it is calling its function. This number is also given in the "place version" in the test place's description. Once recognized, the next step is to go to [the module's asset page](https://create.roblox.com/store/asset/132906055852488/Buckys-Flag-Module).

Inspect the script inside the module. Roblox Studio is **required** for this, since the preview tools on the site seem to only appear when Studio is installed, and there is an explicit option to "View in Studio". Inside the `buckysSuperAmazingFlagModule.flaggyflagflags()` function, there are a bunch of variables named `var_####`:

```
        var_0107 = "_is_one_",
        var_0113 = "percent_",
        var_0103 = "his_flag",
        var_0011 = "11_w0w!}",
        var_0127 = "wrong_sr",
        var_0109 = "hundred_",
        var_0005 = "p0551bl3",
        var_0003 = "0t_s0_1m",
        var_0101 = "Boncoo{T",
        var_0002 = "bronco{n",
        var_0007 = "_4ft3r_4",
        var_0131 = "ry_mate}",
```

The variable numbers are actually prime numbers, and the flag module code is returning the concatenation of the prime vars >100 from lowest to highest.

The flag can be reassembled by putting all the <100 prime variables in order. So,

```
        var_0002 = "bronco{n",
        var_0003 = "0t_s0_1m",
        var_0005 = "p0551bl3",
        var_0007 = "_4ft3r_4",
        var_0011 = "11_w0w!}",
```

which yields `bronco{n0t_s0_1mp0551bl3_4ft3r_411_w0w!}`. The module can be repurposed to do this with a few edits, changing some of the constants inside and then running the Lua code; or this can be done by hand.