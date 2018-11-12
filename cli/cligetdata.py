#au Filetype python setl et ts=2 sw=2

import os 
import glob
import datetime
import argparse
import skimage

#This code sets up the parser for command line arguments specifying parameters for training.
parser=argparse.ArgumentParser()
parser.add_argument('directories', nargs='+', help='list of directories to read data from')

args=parser.parse_args()

args.directories.sort() #sort directories once, so they will be in the same order when we read images and commands

print(args)

#this loops through the input directories, then through the files in each directory, then through the images in each file
#   to load the images into the image array:
for directory in args.directories:
    imgfiles=glob.glob(os.path.join(directory, '*.png'))
    for imgfile in sorted(imgfiles):
        print(imgfile)

