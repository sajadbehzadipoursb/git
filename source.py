import csv
from statistics import mean 
def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name, "r") as csvreader:
        read = csv.reader(csvreader)
        l3 = []
        for a in read:
            length = len(a)
            l1 = []
            for b in range(1,length):
                l1.append(float(a[b]))
            average = str(mean(l1))
            l2 = []
            l2.append(a[0])
            l2.append(average)
            l3.append(l2)
    with open(output_file_name, "w") as csvwriter:
        csv.writer(csvwriter).writerows(l3)
        csvwriter.close()
def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name, "r") as csvreader:
        read = csv.reader(csvreader)
        dictionary = {}
        sorted_averages = []
        for line in read:
            scores = []
            for a in range(1, len(line)):
                scores.append(float(line[a]))
            average = []
            average = mean(scores)
            sorted_averages.append(average)
            dictionary[line[0]] = str(average)
    averages = list(dictionary.values())
    users = list(dictionary.keys())
    sorted_averages.sort()
    for j in range(0, len(sorted_averages)):
        sorted_averages[j]= str(sorted_averages[j])
    for c in sorted_averages:
        for d in range(1,sorted_averages.count(c)):
            sorted_averages.remove(c)
    final_list = []
    final_users = []
    for char in sorted_averages:
        l1 = []
        count = 0
        for e in range(0,averages.count(char)):
            l1.append(users[averages.index(char, count)])
            average_index = averages.index(char,count)
            count = average_index + 1
        l1.sort()
        final_users.extend(l1)
        for f in range(0, len(l1)):
            semifinal_list = []
            semifinal_list.append(l1[f])
            semifinal_list.append(char)
            final_list.append(semifinal_list)
    with open(output_file_name, "w") as csvwriter:
        csv.writer(csvwriter).writerows(final_list)
        csvwriter.close()
    return(final_users, averages)
def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name, "r") as csvreader:
        read = csv.reader(csvreader)
        dictionary = {}
        sorted_averages = []
        for line in read:
            scores = []
            for a in range(1, len(line)):
                scores.append(float(line[a]))
            average = []
            average = mean(scores)
            sorted_averages.append(average)
            dictionary[line[0]] = str(average)
    averages = list(dictionary.values())
    users = list(dictionary.keys())
    sorted_averages.sort()
    for j in range(0, len(sorted_averages)):
        sorted_averages[j]= str(sorted_averages[j])
    for c in sorted_averages:
        for d in range(1,sorted_averages.count(c)):
            sorted_averages.remove(c)
    final_list = []
    quarterfinal_list = []
    for g in range (1, len(sorted_averages)+1):
        l1 = []
        count = 0
        for e in range(0,averages.count(sorted_averages[-g])):
            l1.append(users[averages.index(sorted_averages[-g], count)])
            average_index = averages.index(sorted_averages[-g],count)
            count = average_index + 1
        l1.sort()
        quarterfinal_list.extend(l1)
    for h in range(0,3):
        semifinal_list = []
        semifinal_list.append(quarterfinal_list[h])
        semifinal_list.append(dictionary[quarterfinal_list[h]])
        final_list.append(semifinal_list)
    with open(output_file_name, "w") as csvwriter:
        csv.writer(csvwriter).writerows(final_list)
        csvwriter.close()
def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name, "r") as csvreader:
        read = csv.reader(csvreader)
        dictionary = {}
        averages = []
        for line in read:
            scores = []
            for a in range(1, len(line)):
                scores.append(float(line[a]))
            average = []
            average = mean(scores)
            averages.append(average)
            dictionary[line[0]] = str(average)
    averages.sort()
    for i in range(0, len(averages)):
        averages[i] = str(averages[i])
    final_list = []
    for f in range(0, 3):
        semifinal_list = []
        semifinal_list.append(averages[f])
        final_list.append(semifinal_list)
    with open(output_file_name, "w") as csvwriter:
        csv.writer(csvwriter).writerows(final_list)
        csvwriter.close()
def calculate_average_of_averages(input_file_name, output_file_name):
    last_calculate = calculate_sorted_averages(input_file_name, output_file_name)
    averages = last_calculate[1]
    final_list = []
    for a in range(0, len(averages)):
        averages[a] = float(averages[a])
    final_average = str(mean(averages))
    final_list.append(final_average)
    with open(output_file_name, "w") as csvwriter:
        csv.writer(csvwriter).writerow(final_list)
        csvwriter.close()