import datetime
for i in range(26):
    fname = f"{chr(65+i)}.txt"
    with open(f'pp2\TSIS6\dir-and-files\\task6-txt-generated\{fname}', 'w') as f:
        f.write(f'New file created on {datetime.datetime.now()}')