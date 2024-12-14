# MIT Copyright @Kiarash1NfN1, 2024 

## TODO: letters instead of numbers for decimal with --l,
## TODO: add proper comments and documentations
## TODO: release on pip, return strs into exceptions

import math
import re

nums: list[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
lettersLowerCase: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lettersHigherCase: list[str] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def abs(number: int | float) -> int | float:
    """returns the absolute of 'number'"""
    if number < 0:
        return -number
    return number

def IsValidNum(inp: str) -> bool:
    for j in inp:
        if j == '.' or j == '-':
            continue
        if j.lower() not in (nums + lettersLowerCase):
            return False
    return True

def ReverseString(inp: str) -> str:
    length: int = len(inp)
    st: str = ""
    for i in range(length):
        st += inp[length - i - 1]
    return st

def IntToBase(_num: int, base: int) -> str:
    if (10 <= base <= 62) == False:
        raise Exception("invalid number")
    if _num == 0:
        return "0"
    isNegative = _num < 0
    num: int = abs(_num)
    __L: list[str] = nums + lettersHigherCase + lettersLowerCase
    L: list[str] = __L[:base]
    lim: int = len(L)
    res: str = ""
    b = 0
    t = 0
    while True:
        if num < math.pow(lim, t):
            t -= 1
            break
        t += 1
    tmp = num
    for i in range(t):
        j = t - i
        res += L[tmp // int(math.pow(lim,j))]
        tmp -= int(math.pow(lim, j))
    if isNegative:
        res = "-" + res
    return res + L[num % lim]

def Base10ToBase(_num: str, base: int, lettersForDecimal: bool = False) -> str:
    pattern = r"[\w.]+"
    if bool(re.fullmatch(pattern, _num)) == False or _num.count('.') > 1:
        raise Exception("invalid number")
    if float(_num) == 0:
        return "0"
    if (10 <= base <= 62) == False:
        raise Exception("invalid base")
    __L: list[str] = nums + lettersHigherCase + lettersLowerCase
    L: list[str] = __L[:base]
    if '.' in _num:
        #float
        isNegative: bool = float(_num) < 0
        num: float = abs(float(_num))
        numStr: str = str(num)
        if len(numStr.split('.')) <=  1:
            return IntToBase(int(_num), base)
        _integer: str = IntToBase(int(numStr.split('.')[0]), base)
        decimalSplit: str = numStr.split('.')[1]
        decimalStr: str = ""
        if lettersForDecimal:
            for i in range(len(decimalSplit)):
                decimalStr += lettersHigherCase[int(decimalSplit[i])]
        else:
            decimalStr = decimalSplit
        if (isNegative):
            return (-1.0) * (_integer + "." + decimalStr)
        return _integer + "." + decimalStr
    else:
        return IntToBase(int(_num), base)

def decodeFromInt(_inp: str, base: int) -> int:
    isNegative: bool = _inp[0] == '-'
    inp: str = ReverseString(_inp)
    if isNegative:
        inp = ReverseString(_inp[1:])
    _L: list[str] = nums + lettersHigherCase + lettersHigherCase
    L: list[str] = _L[:base]
    num: int = 0
    for ch in range(len(inp)):
        if inp[ch] not in L:
            return "Invalid character"
        num *= len(L)
        num += L.index(inp[ch])
    if isNegative:
        num *= -1
    return num

def decodeFromBase(_inp: str, base: int) -> int | float:
    if ('.' not in _inp) or (len(_inp.split('.')) <= 1):
        result = decodeFromInt(ReverseString(_inp), base)
        if result != "Invalid character":
            return float(result)
        return result
    isNegative: bool = _inp[0] == '-'
    integer: int
    if isNegative:
        integer = decodeFromInt(ReverseString(_inp.split('.')[0][1:]), base)
    else:
        integer = decodeFromInt(ReverseString(_inp.split('.')[0]), base)
    if integer == "Invalid character":
        return "Invalid character"
    decimal: str = _inp.split('.')[1]
    hasAnyLetters: bool = False
    _inpLower: str = _inp.lower()
    for c in lettersLowerCase:
        if c in _inpLower:
            hasAnyLetters = True
            break
    if hasAnyLetters == False:
        if isNegative:
            return (-1.0) * (float(abs(integer)) + float('0.' + decimal))
        return float(integer) + float('0.' + decimal)
    decimalStr: str = "0."
    indx: int = 0
    for j in decimal:
        if j in nums:
            decimalStr += j
            continue
        if lettersLowerCase.index(j.lower()) > 9:
            raise Exception('invalid decimal on decimal part character: ' + str(indx))
        decimalStr += str(lettersLowerCase.index(j.lower()))
        indx += 1
    if isNegative:
        # Why doesn't python have condition operator? so stupid lol
        return (-1.0) * (float(integer) + float(decimalStr))
    return float(integer) + float(decimalStr)

#print(decodeFromBase('-1.2', 36))
#print(decodeFromBase('-10', 36) + 80)
#print(decodeFromBase('-10.3', 36))
#print(decodeFromBase('-1A.B', 36))
while True:
    # _Input = input("enter to encode: ")
    # print(Base10ToBase(_Input, 36, True))
    # print(Base10ToBase(_Input, 36, False))

    _Input = input("enter to decode: ")
    print(decodeFromBase(_Input, 36))