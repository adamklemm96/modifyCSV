#!/usr/bin/env python3

import random, os, sys

path1 = sys.argv[1]

descriptions = ["In early 2018, a large dataset of over 1400 individual databases was found online. This leak contained a file named {filename} consisting of email addresses and a combination of hashed and plaintext passwords. About {number} accounts were involved in this particular breach. While the validity of this breach cannot be confirmed, many of the accounts had not been seen in previous data breaches.", "On the hacking forums has appeared the collection of many breaches. {filename} was within this collection. It contains around {number} accounts together with email addresses and passwords. The exact date of this breach is unknown.",
"In 2018 were information from the {filename} publicly shared online. Emails and passwords of {number} users were leaked and sold on the hacking forums."]

def choose_description(list_d):
    import random
    generated_description = list_d[random.randint(0, len(list_d)-1)]
    return generated_description

def decription(path1):
    with open(path1, encoding="latin-1") as f:
        for i, l in enumerate(f):
            pass
        os.system("clear")
        print(descriptions[random.randint(0, len(descriptions)-1)].format(time=2018, filename=path1, number=round(i, -3)))
    return i

print(f"""
Contains:
email addresses and password
Number of rows:
{decription(path1)}
""")

print("=====================")

answer = input("Would you like to upload the file to BT ? [y/n]")

if answer == 'y':
    os.system("mkdir -p done")
    os.system(f"mv {path1} done")
    if len(os.listdir("/opt/spartacus-import-data-breach-ruby/data")) == 0:
        os.system(f"cp done/{path1} /opt/spartacus-import-data-breach-ruby/data")
        print("File is copied to  /opt/spartacus-import-data-breach-ruby/data")
    else:
        print("Directory full copyin to data_2")
        os.system(f"cp done/{path1} /opt/spartacus-import-data-breach-ruby/data_2")
        print("File is copied to  /opt/spartacus-import-data-breach-ruby/data_2")
else:
    exit
