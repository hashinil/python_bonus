files = ["doc.txt", "report.txt"]
contents = ["this is the content of doc file", "this is the content of report file"]

for content, filepath in zip(contents, files):
    file_w = open(f"files/{filepath}", 'w')
    file_w.write(content)
    file_w.close()


