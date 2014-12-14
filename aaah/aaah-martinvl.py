from sys import stdin

lines = stdin.readlines()
marius = lines[0]
doctor = lines[1]

if len(marius) >= len(doctor):
    print("go")
else:
    print("no")