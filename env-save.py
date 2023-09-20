import docker 
import os
import argparse
from utils import filter_container




if __name__ == "__main__":
    
    cmdline = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    cmdline.add_argument('--name', default="")
    cmdline.add_argument('--id', default="")
    flags, unk_args = cmdline.parse_known_args()
    
    f_id, f_name = flags.id, flags.name
    sc = filter_container(f_id,f_name)
    c_id, im_id, im_name = sc['id'],sc['image_id'], sc['image']
    r = input(f"Are you sure you want to overwrite the image {im_id} with tag {im_name} ? [y/N]")
    if r == "y" or r == "Y":
        # do the command
        cmd = f'docker commit {c_id} {im_name}'
        os.popen(cmd)