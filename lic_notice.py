import os

for root,  dir, files in os.walk("/home/aksmr/notice_license"):
    for file in files:
        if file.startswith(('LICENSE','Notice')):
            print(f"{root}/{file}")
