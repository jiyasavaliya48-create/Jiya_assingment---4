import os

if os.path.exists("sample.txt"):
    f = open("sample.txt", "r")

    print("Reading file content:")

    line_no = 1
    for line in f:
        print("Line", line_no, ":", line.strip())
        line_no += 1

    f.close()
else:
    print("Error: The file 'sample.txt' was not found.")