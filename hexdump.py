import sys

def hexdump(command):
    if len(command) < 1:
        return
    line_word = ""
    command = " ".join([i for i in command.split(" ") if i != ''])
    command = command.replace("\n ", "\n")
    for i in range(0, len(command)):
        if (i % 16 == 0):
            print(str(hex(i))[2:].zfill(8), end = "   ")
        print(str(hex(ord(command[i])))[2:].zfill(2), end=" ")
        line_word += command[i]
        if (i % 16 == 15 or i == len(command)-1):
            print("   " * (16 - len(line_word)), end="")
            line_word = line_word.replace('\n', '.')
            print("|" + line_word + '|\n')
            line_word = ""
    print(str(hex(len(command)))[2:].zfill(8))

n = len(sys.argv)

if (n != 2):
    print("Usage: python3 hexdump.py <file>")
    sys.exit()

try:
    file = open(sys.argv[1], "r", encoding="utf-8")
except:
    print("Unable to read file... closing")
    sys.exit()
    
file_contents = file.read()

hexdump(file_contents)

file.close()