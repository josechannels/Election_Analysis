# Create a filename variable to a direct or indirect path to the file.
file_to_save = "Analysis\election_analysis.txt"

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")

    # Write three counties to the file.
    txt_file.write("Counties in the Election \n----------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")