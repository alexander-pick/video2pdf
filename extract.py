#!/usr/bin/env python2

import math, operator
from PIL import Image
from PIL import ImageFile
import sys
import os
import glob
import subprocess
import shutil
import datetime
import imagehash

def compare_image_with_hash(image_file_name_1, image_file_name_2, max_dif=10):
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    hash_1 = None
    hash_2 = None
    with open(image_file_name_1, 'rb') as fp:
        hash_1 = imagehash.phash(Image.open(fp))
    with open(image_file_name_2, 'rb') as fp:
        hash_2 = imagehash.phash(Image.open(fp))
    dif = hash_1 - hash_2
    if dif < 0:
        dif = -dif
    if dif <= max_dif:
        return False
    else:
        print dif
        return True

if __name__ == '__main__':

    mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    os.makedirs(mydir)

    if len(sys.argv) < 2:
        sys.exit("Need video file as parameter")
    if not os.path.exists("decomp"):
        os.mkdir("decomp")
    else:
        sys.exit("decomp already exists, exit")

    cmd = ["ffmpeg", "-ss", "00:00:04", "-i", sys.argv[1], "-vf", "fps=fps=1/5'", ''"-vsync", "0", "-f", "image2", "decomp/%09d.png"]

    print "Running ffmpeg: " + " ".join(cmd)

    subprocess.call(cmd)

    print "Done, now eliminating duplicate images and moving unique ones to output folder..."

    filelist = glob.glob(os.path.join("decomp", '*.png'))
    filelist.sort()
    lastvalid = None

    for ii in range(0, len(filelist)):
        if ii < len(filelist) - 1:
            if lastvalid == None:
                head, tail = os.path.split(filelist[ii])
                shutil.copyfile(filelist[ii], mydir + os.path.sep + tail)
                lastvalid = filelist[ii]
            if compare_image_with_hash(filelist[ii], lastvalid):
                print 'Found unique image: ' + filelist[ii]
                lastvalid = filelist[ii]
                head, tail = os.path.split(filelist[ii])
                shutil.copyfile(filelist[ii], mydir + os.path.sep + tail)
        else:
            shutil.copyfile(filelist[ii], mydir + os.path.sep + tail)
    shutil.rmtree("decomp")
