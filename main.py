file_path = "C:/Users/Student/Desktop/lesson11.py/leximi.txt"
# file = open(file_path, "r")
# with open (file_path, "r") as file: 
#     line1 = file.readline()
#     print(line1)

# with open (file_path, "w") as file: 
#     file.write("Hello world")

with open(file_path, "w")as file:
    file.seek(20)
    line = file.read()
    print(line)
    