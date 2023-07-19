filenames = ["1.test.txt", "2.data.txt", "3.names.txt"]

for file in filenames:
    file = file.replace('.', '-', 1)
    print(file)