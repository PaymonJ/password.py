import random
import sys
from functions import isInt, validateInput

reqs = {
    "noNum": False,
    "noSym": False,
    "noUp": False,
    "noLow": False
}

validateInput(sys.argv, reqs)

if all(value == True for value in reqs.values()):
    print("ERROR Password must containg one of the following: Numbers, Symbols, Lowercase Letters, or Uppercase Letters.\n")
    sys.exit()

secureRand = random.SystemRandom()
setChar = 0
chars = []

if isInt(sys.argv[1]):
    length = int(sys.argv[1])
else:
    length = 12

arrASCII = list(range(33, 126+1))

numASCII = list(range(48, 57+1))
upASCII = list(range(65, 90+1))
lowASCII = list(range(97, 122+1))
symASCII = list(range(33, 47+1)) + list(range(58, 64+1)) + list(range(91, 96+1)) + list(range(123, 126+1))

if reqs["noNum"]:
    for i in range(48, 57+1):
        arrASCII.remove(i)
else:
    chars.append(chr(secureRand.choice(numASCII)))
    setChar += 1

if reqs["noSym"]:
    for i in range(33, 47+1):
        arrASCII.remove(i)
    for i in range(58, 64+1):
        arrASCII.remove(i)
    for i in range(91, 96+1):
        arrASCII.remove(i)
    for i in range(123, 126+1):
        arrASCII.remove(i)
else:
    chars.append(chr(secureRand.choice(symASCII)))
    setChar += 1

if reqs["noUp"]:
    for i in range(65, 90+1):
        arrASCII.remove(i)
else:
    chars.append(chr(secureRand.choice(upASCII)))
    setChar += 1

if reqs["noLow"]:
    for i in range(97, 122+1):
        arrASCII.remove(i)
else:
    chars.append(chr(secureRand.choice(lowASCII)))
    setChar += 1

for i in range(0, length-setChar):
    chars.append(chr(secureRand.choice(arrASCII)))

random.shuffle(chars)
password = ''.join(chars)

print(password)