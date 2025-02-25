import os

# List all the files in the target folder
files = os.listdir('/workspaces/tosdata/max_5')
fold = '/workspaces/tosdata/max_5/'

# Loop through each file
for strat in files:
    try:
        # Read the content of the file
        with open(fold + strat, 'r', encoding='windows-1252', errors='replace') as rfile:
            old = rfile.readlines()[1:]  # Skip the first line

            old.pop(1)  # Remove the second line
            sid = old.pop(3)  # Pop the 4th line (index 3)
            old[0] = old[0].replace('\n', ' ')  # Replace newline in the first line
            old[0] += sid  # Append the SID to the first line

        # Now write back to the file
        with open(fold + strat, 'w', encoding='windows-1252') as wfile:
            for line in old:
                if line != '\n':  # Avoid writing empty newlines
                    new_line = line.replace(';', ',')  # Replace semicolons with commas
                    wfile.write(new_line)  # Write the modified line to the file

    except Exception as e:
        print(f"Error processing {strat}: {e}")
        continue
