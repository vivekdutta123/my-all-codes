#filename = input("Enter the filename: ")
#fh = open(filename)

# Loop through each line in the file
##for line in fh:
    # Check if the line starts with "Hellow"
    #if line.startswith("Hellow"):
        #print(line.strip())  # .strip() removes leading/trailing whitespace

# Close the file after processing
#fh.close()
filename = input("Enter the filename: ")
fh = open(filename)
count=0
# Loop through each line in the file
for line in fh:
    count=count+1
    # Check if the line starts with "Hellow"
    if line.startswith("Hellow"):
        print(line.strip())  # .strip() removes leading/trailing whitespace

# Close the file after processing
fh.close()
