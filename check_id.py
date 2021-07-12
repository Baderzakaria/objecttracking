import os
import csv
import subprocess
from subprocess import Popen
def check_id():
    var =0 
    filename = "id.csv"
    if os.path.exists(filename) :
        with open(filename, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    var=row[0]
    else:      
        with open(filename,"w") as f:
            writer=csv.writer(f)
            var=raw_input("enter id")
            writer.writerow(var)

    cmd = "google-chrome --start-fullscreen --app=https://ads.store.utrender.com/panel_images.php?id="+str(var)
    #os.system(cmd)
    proc = Popen([cmd], shell=True,stdin=True, stdout=True, stderr=None, close_fds=True)
    return var