import csv
import hashlib
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    cracked = []
    with open(input_file_name) as fin:
        reader = csv.reader(fin)
        hashed_list = list(reader)
    rainbow_table = OrderedDict()
    for i in range(10000):
        pwd = str(i).zfill(4)
        hashed = hashlib.sha256(pwd.encode()).hexdigest()
        rainbow_table[hashed] = pwd
    for name, hash_value in hashed_list:
        if hash_value in rainbow_table:
            cracked.append((name, rainbow_table[hash_value]))
    with open(output_file_name, 'w', newline='') as fout:
        writer = csv.writer(fout)
        for name, password in cracked:
            writer.writerow([name, password])