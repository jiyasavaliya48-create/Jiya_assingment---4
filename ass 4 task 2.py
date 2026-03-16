import os

text = input("Enter text to write to the file: ")

f = open("output.txt", "w")
f.write(text + "\n")
f.close()

print("Data successfully written to output.txt.")

more_text = input("Enter additional text to append: ")

f = open("output.txt", "a")
f.write(more_text + "\n")
f.close()

print("Data successfully appended.")


if os.path.exists("output.txt"):
    f = open("output.txt", "r")
    print("\nFinal content of output.txt:")

    for line in f:
        print(line.strip())

    f.close()
else:
    print("Error: File not found.")