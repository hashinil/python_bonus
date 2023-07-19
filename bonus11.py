def get_average():
    with open("files/temp.txt", 'r') as temp_file:
        data = temp_file.readlines()

    values = data[1:]
    values = [float(val) for val in values]

    average = sum(values)/len(values)
    return average

avg = get_average()
print(avg)