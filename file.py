import os

for root,dir,files in os.walk("/home/aksmr"):
    for file in files:
        if file.startswith(('LICENSE', 'Notice')):
            with open(root+"/"+file, "r") as fh:
                content=fh.read()
            with open("license_notice_append.txt", "a") as fh1:
                fh1.write("The path of the file:" +root+ "/" + file)
                fh1.write("\nThe corresponding content:"+ content)
            with open("license_append.txt", "r") as fh1:
                 print(fh1.read())
