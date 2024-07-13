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
        averages = []
        users = []
        quarterfinal_list = []
        final_list = []
        indexes = []
        dictionary = {}
        dictionary2 = {}
        for line in read:
            # import only numbers
            numbers = line[1:]
            # conver string to float
            float_numbers = []
            for number in numbers:
                float_numbers.append(float(number))
            # import users
            users.append(line[0])
            # computing average
            average = mean(float_numbers)
            averages.append(average)
            # generate dictionary
            dictionary[line[0]] = str(average)
            dictionary2[str(average)] = line[0]
        #  a program for repeat
        repeats = []
        for search in averages:
            if averages.count(search) > 1:
                count = 0
                for repetition in range(0,averages.count(search)):
                    index = averages.index(search,count)
                    repeats.append(users[index])
                    count = index+1
        repeats.sort()
        for char in repeats:
            for a in range(1, repeats.count(char)):
                repeats.remove(char)
        averages.sort()
        for b in range(0,len(averages)):
            averages[b] = str(averages[b])
        for f in repeats:
            indexes.append(averages.index(dictionary[f]))
        numbers_of_c = []
        for g in range(0, len(dictionary)):
            numbers_of_c.append(g)
        for c in numbers_of_c:
            if c in indexes:
                for d in range(0,indexes.count(c)):
                    quarterfinal_list.append(repeats.pop(indexes.index(c)))
                for h in range(c+1, c+indexes.count(c)):
                    numbers_of_c.remove(h)
            else:
                quarterfinal_list.append(dictionary2[averages[c]])
        for i in range(0,len(quarterfinal_list)):
            semifinal_list = []
            semifinal_list.append(quarterfinal_list[i])
            semifinal_list.append(averages[i])
            final_list.append(semifinal_list)
    with open(output_file_name, "w") as csvwriter:
        csv.writer(csvwriter).writerows(final_list)
        csvwriter.close()
    return(quarterfinal_list, averages)
def calculate_three_best(input_file_name, output_file_name):
    last_calculate = calculate_sorted_averages(input_file_name,output_file_name)
    final_list = []
    users = last_calculate[0]
    averages = last_calculate[1]
    count_of_biggest = averages.count(averages[-1])
    for a in range(1, 4):
        semifinal_list = []
        semifinal_list.append(users[-count_of_biggest])
        semifinal_list.append(averages[-count_of_biggest])
        final_list.append(semifinal_list)
        count_of_biggest -= 1
    with open(output_file_name, "w") as csvwriter:
        csv.writer(csvwriter).writerows(final_list)
        csvwriter.close()
def calculate_three_worst(input_file_name, output_file_name):
    last_calculate = calculate_sorted_averages(input_file_name, output_file_name)
    final_list = []
    averages = last_calculate[1]
    for a in range (0,3):
        semifinal_list = []
        semifinal_list.append(averages[a])
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