import os
import datetime
import re
import itertools

# Guess this, or add offset at the end
START = datetime.date(2012, 1, 1)
curr_date = START
files_checked = 0
bitstring = ""
folder = "./feelings_journal"
files = [folder + "/" + file for file in os.listdir(folder)]
# Sort files in number
files.sort(key = lambda s: int(re.search(r"\d+", s).group(0)))
while files_checked < len(files):
    ftime = datetime.date.fromtimestamp(os.path.getmtime(files[files_checked]))
    if curr_date == ftime:
        bitstring += "1"
        files_checked += 1
    else:
        bitstring += "0"
    curr_date += datetime.timedelta(days=1)

morseflag = bitstring.replace("111", "-").replace("1", ".").replace("000", " ").replace("0", "")
wordflag = morseflag.replace("--.. . .-. ---", "ZERO").replace("--- -. .", "ONE").replace(" ", "")
binflag = wordflag.replace("ZERO", "0").replace("ONE", "1")
# If you didn't get the start time right, now is when you'd pad binflag
flag = "".join([chr(int(''.join(num), 2)) for num in itertools.batched(binflag, 8)])
print(flag)
