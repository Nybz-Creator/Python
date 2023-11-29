# Lesson: File Handling

# 1. Write to a file:
with open("example.txt", "w") as file:
    file.write("Hello, Python!")
    
# 2. Read from a file:
with open("example.txt", "r") as file:
    content = file.read()
    print(content)