
def wash():
    import os

    uncleaned_data_path='/workspaces/TosChart/TosChart/uncleaned_data'
    files=os.listdir(uncleaned_data_path)

    # Loop through each file
    for strat in files:
        try:
            # Read the content of the file
            with open(uncleaned_data_path + '/' + strat, 'r', encoding='windows-1252', errors='replace') as rfile:
                old = rfile.readlines()[1:]  # Skip the first line

                old.pop(1)  # Remove the second line
                sid = old.pop(3)  # Pop the 4th line (index 3)
                old[0] = old[0].replace('\n', ' ')  # Replace newline in the first line
                old[0] += sid  # Append the SID to the first line

            # Now write back to the file
            with open(uncleaned_data_path + '/' + strat, 'w', encoding='windows-1252') as wfile:
                for line in old:
                    if line != '\n':  # Avoid writing empty newlines
                        new_line = line.replace(';', ',')  # Replace semicolons with commas
                        wfile.write(new_line)  # Write the modified line to the file

        except Exception as e:
            print(f"Error processing {strat}: {e}")
            continue


    try:
        for strat in files:
            with open(uncleaned_data_path+'/'+strat, 'r', encoding='windows-1252', errors='replace') as rfile:
                old=rfile.readlines()
                fix=old[:-3]

            with open(uncleaned_data_path+'/'+strat,'w') as wfile:
                wfile.write(''.join(fix))
    except:
        print(strat)
        print(old)
    
if __name__=='__main__':
    wash()