x = input("Enter text to write to the file: ")
file = open('output.txt','w')
writting = file.write(x + '\n')
print("Data successfully written to output.txt")
file.close()

y = input("Enter additional text to append: ")
file = open('output.txt','a')
appending = file.write(y)
print("Data Successfully appended.")
file.close()

file = open('output.txt','r+')
reading = file.read()
print("Here's what you have stored in the file output.txt: ", reading)
file.close()
