import os
import subprocess

file_path1 = "./ava.txt"
file_path2 = "./ava_test.txt"
url1 = 'https://s3.amazonaws.com/ava-dataset/trainval/'
url2 = 'https://s3.amazonaws.com/ava-dataset/test/'
with open(file_path1, 'r') as f:
    lines = f.read().splitlines()

for line in lines:
    url = url1 + line
    cmd = 'wget ' + '--no-clobber -q -P ./train_val ' + url
    print(cmd)
    subprocess.call(cmd, shell=True)
