import csv
from statistics import mean
from collections import OrderedDict
def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as fin, open(output_file_name, 'w', newline='') as fout:
        reader = csv.reader(fin)
        writer = csv.writer(fout)
        for row in reader:
            name = row[0]
            grades = [float(x) for x in row[1:]]
            avg = mean(grades)
            writer.writerow([name, avg])

def calculate_sorted_averages(input_file_name, output_file_name):
    data = []
    with open(input_file_name) as fin:
        reader = csv.reader(fin)
        for row in reader:
            name = row[0]
            grades = [float(x) for x in row[1:]]
            avg = mean(grades)
            data.append((name, avg))
    data.sort(key=lambda x: (x[1], x[0]))
    with open(output_file_name, 'w', newline='') as fout:
        writer = csv.writer(fout)
        for name, avg in data:
            writer.writerow([name, avg])

def calculate_three_best(input_file_name, output_file_name):
    data = []
    with open(input_file_name) as fin:
        reader = csv.reader(fin)
        for row in reader:
            name = row[0]
            grades = [float(x) for x in row[1:]]
            avg = mean(grades)
            data.append((name, avg))
    data.sort(key=lambda x: (-x[1], x[0]))
    top_three = data[:3]
    with open(output_file_name, 'w', newline='') as fout:
        writer = csv.writer(fout)
        for name, avg in top_three:
            writer.writerow([name, avg])

def calculate_three_worst(input_file_name, output_file_name):
    avgs = []
    with open(input_file_name) as fin:
        reader = csv.reader(fin)
        for row in reader:
            grades = [float(x) for x in row[1:]]
            avg = mean(grades)
            avgs.append(avg)
    avgs.sort()
    with open(output_file_name, 'w', newline='') as fout:
        writer = csv.writer(fout)
        for avg in avgs[:3]:
            writer.writerow([avg])

def calculate_average_of_averages(input_file_name, output_file_name):
    avgs = []
    with open(input_file_name) as fin:
        reader = csv.reader(fin)
        for row in reader:
            grades = [float(x) for x in row[1:]]
            avg = mean(grades)
            avgs.append(avg)
    overall_avg = mean(avgs)
    with open(output_file_name, 'w', newline='') as fout:
        writer = csv.writer(fout)
        writer.writerow([overall_avg])