# Write file
with open("practice.txt", "w") as f:
    f.write("Hy everyone\n we are learning file I/O \n")
    f.write("Using Java \n I like programming in Java ")  # "Jave" ko "Java" kar diya

print("Data written successfully!")

# # Read and Replace Java with Python
# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")
# print("\nUpdated Content:\n")
# print(new_data)

# # Save the updated data back to the file
# with open("practice.txt", "w") as f:
#     f.write(new_data)  # 'data =' hataya
    

# check data if exist in file or not
word = "learning"
line_no = 1
with open("practice.txt","r") as f:
    data = f.read()
    if(word in data):
        print("Found!",line_no)    
    else:
        print("Not Found!")
        
# find which line in our word

word = "pqy"
data = True
line = 1

while data:
    data = f.readline()
    if(word in data):
        print(line)
    line += 1
    
    
    
        