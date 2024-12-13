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