# Define the paths to your input text files
file1_path = "test_1.txt"
file2_path = "test_0.txt"

# Define the path for the output file
output_path = "combined_test.txt"

# Open the input files for reading
with open(file1_path, "r") as file1, open(file2_path, "r") as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

# Check if the two input files have the same number of lines
if len(lines1) != len(lines2):
    print("Error: The input files have a different number of lines.")
else:
    # Open the output file for writing
    with open(output_path, "w") as output_file:
        # Combine the lines from both input files with a hash symbol
        for line1, line2 in zip(lines1, lines2):
            combined_line = f"<s>{line1.strip()}</s> >>>>>> <p>{line2.strip()}</p>\n"
            output_file.write(combined_line)

print("Combining and writing to the output file is complete.")

