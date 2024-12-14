# MIT Copyright @Kiarash1NfN1, 2024

## TODO: decode from float
## TODO: color option with --c, base with -b 62 or 36, different bases from -b 10 to 62, 
## TODO: test.py, make it pretty, add float with --f, letters instead of numbers for decimal with --l,
## TODO: help with --h
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

def ReverseString(inp: str) -> str:
    length: int = len(inp)
    st: str = ""
    for i in range(length):
        st += inp[length - i - 1]
    return st

def ConvertToBase(_num: int, base: int) -> str:
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
            return ConvertToBase(int(_num), base)
        _integer: str = ConvertToBase(int(numStr.split('.')[0]), base)
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
        return ConvertToBase(int(_num), base)
    
def decodeFromBase(_inp: str, base: int) -> int:
    pattern = r"[\w.]+"
    if bool(re.fullmatch(pattern, _inp)) == False or _inp.count('.') > 1:
        raise Exception("invalid number")
    if (10 <= base <= 62) == False:
        raise Exception("invalid base")
    isNegative: bool = _inp[0] == '-'
    inp: str = ReverseString(_inp)
    if isNegative:
        inp = ReverseString(_inp[1:])
    __L: list[str] = nums + lettersHigherCase + lettersLowerCase
    L: list[str] = __L[:base]
    num: int = 0
    for ch in range(len(inp)):
        if inp[ch] not in L:
            return "Invalid character"
        num *= len(L)
        num += L.index(inp[ch])
    if isNegative:
        num *= -1
    return num