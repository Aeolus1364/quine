import sys
stdout_ = sys.stdout
sys.stdout = open('r.txt', 'w')
import quine
sys.stdout = stdout_
with open("quine.py", "r") as f:
    file = f.read()
with open("r.txt", "r") as f2:
    file2 = f2.read()

print(file == file2)