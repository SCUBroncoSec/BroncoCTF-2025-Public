import os
import shutil
import datetime

# Create the bitflag, with 1s representing days which have an entry
flag = "bronco{bl4st_fr0m_th3_pa5t}"
binflag = ''.join(format(ord(x), '08b') for x in flag)
wordflag = binflag.replace("0", "zero").replace("1", "one")
morseflag = wordflag.replace("zero", "--.. . .-. --- ").replace("one", "--- -. . ").strip()
bitflag = morseflag.replace(".", "10").replace("-", "1110").replace(" ", "00")[:-1]

# Start date
START = datetime.date(2012, 1, 1)
curr_date = START
onecount = 1
name = "how_im_feeling_today"
for bit in bitflag:
    if bit == "1":
        target = f"./feels/{name}_{onecount}.jpg"
        shutil.copyfile("./smiling.jpg", target)
        unix_time = int(curr_date.strftime('%s'))
        times = (unix_time, unix_time)
        os.utime(target, times)
        onecount += 1

    # Get next day
    curr_date += datetime.timedelta(days=1)

print(onecount)
