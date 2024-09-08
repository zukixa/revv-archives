def remove_duplicates(filename, new_filename):
    with open(filename, "r") as f:
        lines = f.readlines()  # Read all lines from the file

    unique_lines = set(lines)  # Use a set to remove duplicate lines

    with open(new_filename, "w") as f:
        f.writelines(unique_lines)  # Write unique lines back to a new file


# Call the function
remove_duplicates("final_mj.txt", "filtered_final_mj.txt")
