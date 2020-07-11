
import subprocess
with open("all_ip_list.txt", "w+") as output:
    subprocess.call(["python3", "/root/check.py"], stdout=output);
