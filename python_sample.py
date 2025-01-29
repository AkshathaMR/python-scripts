import random

import sys

import os

print(random.randint(2,5))


for i in range(2,5):
    print(i)

print(sys.argv[0])
print(sys.path)

os.chdir("/home/aksmr")

os.makedirs("Directory", exist_ok=True)
print(os.getcwd())

print(os.listdir("/home/aksmr"))

#print(os.walk("/home/aksmr"))
for path,dir,files in os.walk("/home/aksmr"):
    print(path)
    print(dir)
    print(files)
