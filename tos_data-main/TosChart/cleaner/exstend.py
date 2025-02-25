import os
import chardet

files=os.listdir('/workspaces/tosdata/max_5')
fold='/workspaces/tosdata/max_5/'


try:
    for strat in files:
        with open(fold+strat, 'r', encoding='windows-1252', errors='replace') as rfile:
            old=rfile.readlines()
            fix=old[:-3]

        with open(fold+strat,'w') as wfile:
            wfile.write(''.join(fix))
except:
    print(strat)
    print(old)

'''''
for strat in files:
    with open(fold+strat, 'r', encoding='windows-1252', errors='replace') as rfile:
        old=rfile.read()
        old=old.replace(';',',')

    with open(fold+strat,'w') as wfile:
        wfile.write(old)
'''''

'''
for strat in files:
    with open(fold+strat, 'r', encoding='windows-1252', errors='replace') as rfile:
        old=rfile.readlines()
        copy=old
        for line in old:
            if 'Max' in line or 'Total' in line:
                copy.remove(line)

    with open(fold+strat,'w') as wfile:
        wfile.write(''.join(copy[:-1]))
'''