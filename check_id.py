import os
import csv
import sys
import platform
import subprocess
from subprocess import Popen


def check_id():
    var = 0
    filename = "id.csv"
    if os.path.exists(filename):
        with open(filename , "r") as f:
            reader = csv.reader(f)
            for row in reader:
                var = row[ 0 ]
    else:
        with open(filename , "w") as f:
            writer = csv.writer(f)
            var = input("enter id")
            writer.writerow(var)
    if platform.system() == 'Linux':
        cmd = "google-chrome --start-fullscreen --app=https://campaign.utrender.com/panel_images.php?id=" + str(var)
    else:
        cmd = "chromium-browser --start-fullscreen --app=https://campaign.utrender.com/panel_images.php?id=" + str(var)
    # chromium-browser
    # os.system(cmd)
    proc = Popen([ cmd ] , shell=True , stdin=True , stdout=True , stderr=None , close_fds=True)
    return var
