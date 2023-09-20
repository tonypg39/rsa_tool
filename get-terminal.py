import os
import argparse
from utils import filter_container

img_base = "ur10dev"


if __name__ == "__main__":
    
    cmdline = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    cmdline.add_argument('--name', default="")
    cmdline.add_argument('--id', default="")
    flags, unk_args = cmdline.parse_known_args()
    f_id, f_name = flags.id, flags.name
    sc = filter_container(f_id,f_name)
    if sc is None:
        print("ERR1: No container found with such id or name.")
        exit(1)
    
    sc_id = sc['id']
    cmd = f'gnome-terminal -- bash -c "docker exec -it {sc_id} bash; exec bash"'
    os.popen(cmd)