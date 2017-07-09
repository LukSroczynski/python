create_file = open("Sample.txt", "w")  # w - write
create_file.write("Sample Text \nLorem ipsum")
create_file.close()

read_file = open("Sample.txt", "r")  # r - read
print(read_file.read())
read_file.close()

