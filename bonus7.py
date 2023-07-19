filenames = ["1.data", "2.report"]

filenames = [filename.replace('.', '_')+'.txt' for filename in filenames]

print(filenames)
