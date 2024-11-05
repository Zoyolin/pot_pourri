#! python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import csv
import time
import subprocess
import os
##
# 1) print a serie of PINT / PFLOAT ending with a PEND in c cprogram.
# launch this command to filter the serial output in a tmp file with csv format
#define PFLOAT(x) printf("," #x ",%f,", (x))
#define PINT(x) printf("," #x ",0x%x,", (x))
#define PSTR(str) printf("," #str ",%s,", (str))
#define PEND() printf("\n")

# 2) make sure to adapt the number of matches {3} to the number of PINTs
# idf.py monitor -p /dev/cu.usbmodem11201 | rg --line-buffered -e "^((,.+,([\d\.]+|0x[\dabcdef]+),){3})" > /tmp/424242
# 3) launch this program. Can do hex and floats, no str!
# caveats: relies on the 1st line of the output to be correct.
#          relies on tmp/file to be a valid csv, no extra serie output should wiggle its way in!

def live_filter(nb_y, log_in, backlog, log_out):
    line = (f" tail -n {backlog} -f {log_in} | "
            " rg --line-buffered -e \"^((,.+,([\\d\\.]+|0x[\\dabcdef]+),){" + str(nb_y) + "})\" "
            f" 1>{log_out} "
    )
    print(line)
    # filter_proc = subprocess.Popen(line)
    # yield
    # filter_proc.wait()


def init_csv():
    reader = csv.reader(FILE_POINTER)
    for row in reader:
        print(row)
        for i, col in enumerate(row):
            if col and i-1 not in indexes:
                ys.append([])
                indexes.append(i)
        break
    for col in ys:
        line, = ax.plot([], [])
        lines.append(line)
    print(indexes)

def update_csv():
    reader = csv.reader(FILE_POINTER)
    for row in reader:
        if(len(row) == len(indexes)*3+1):
            for enum, index in enumerate(indexes):
                if row[index+1][:2] == "0x" or row[index+1][:1] == "0X":
                    ys[enum].append(np.float64(int(row[index+1], 16)))
                else:    
                    ys[enum].append(np.float64(row[index+1]))
        else:
            print(f"invalid row {row}")


def init_graph():
    i = len(ys[0])
    imin = max(0, i - WINDOW_SIZE)
    x = np.arange(min(i, WINDOW_SIZE))
    for line, y in zip(lines, ys):
        line.set_data(x,y[imin:i])
    return lines

def animate_graph(i):
    update_csv()
    i = len(ys[0])
    imin = max(0, i - WINDOW_SIZE)
    x = np.arange(min(i, WINDOW_SIZE))
    for line, y in zip(lines, ys):
        line.set_data(x,y[imin:i])
    ax.relim()
    ax.autoscale()
    if YSCALE:
        ax.set(ylim=YSCALE)
    return lines

# cmd line args:
WINDOW_SIZE = 100000
buf_name = "/tmp/lp.csv"
YSCALE = None
# YSCALE = (0, 10)

live_filter(1, "/tmp/monitor.log" ,WINDOW_SIZE, buf_name)

while(not os.path.getsize(buf_name) > 0):
    time.sleep(0.1)

FILE_POINTER = open(buf_name)

indexes = []
lines = []
ys = []
fig, ax = plt.subplots()
ax.margins(0.05)
init_csv()

anim = animation.FuncAnimation(
    fig, animate_graph, init_func=init_graph, 
    interval=10, save_count=WINDOW_SIZE,
    blit=False
)
fig.canvas.manager.full_screen_toggle()
plt.show()


# time.sleep(1000000)
# FILE_POINTER.close()

