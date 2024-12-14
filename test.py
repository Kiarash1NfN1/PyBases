import getopt, sys

argumentList = sys.argv[1:]

def Print(message: str) -> None:
    if colorized:
        st: str = ""
        indx: int = 0
        canColor: bool = True
        OnNote: bool = False
        for i in message:
            if i == '!':
                canColor = canColor == False
                continue
            if i == '%':
                OnNote = OnNote == False
                continue
            if OnNote:
                st += bcolors.FAIL + i + bcolors.ENDC
                continue
            if canColor == False:
                st += i
                continue
            if i == '.':
                st += bcolors.WARNING + i + bcolors.ENDC
                indx += 1
                continue
            if i == ':':
                st += bcolors.OKBLUE + i + bcolors.ENDC
                continue
            if i == '-':
                IsNegative: bool = True
                if (indx != 0 and message[indx - 1] == '-') or (indx != len(message) - 1 and message[indx + 1] == '-'):
                    IsNegative = False
                if IsNegative == False:
                    st += bcolors.OKGREEN + i + bcolors.ENDC
                else:
                    st += bcolors.FAIL + i + bcolors.ENDC
                indx += 1
                continue
            st += bcolors.OKCYAN + i + bcolors.ENDC
            indx += 1
        print(st)
        return
    print(message)

long_options = ["help", "decode", "encode", "lettersdecimal", "colored"]

def PrintHelp():
    Print("[              !HELP!              ]")
    Print("-c: !colorize terminal!.")
    Print("-d: !you want to decode your number!.")
    Print("-e: !you want to encode your number!.")
    Print("-n: !your number!.")
    Print("-b: !your target base!.")
    Print("-l: !use letters for decimal parts!.")
    Print("------------------------------------")
    Print(f"Long options: !{long_options}!")
    Print(f"!example!: test.py --colored -e -n 24 -b 10")
    Print("%IMPORTANT NOTE%: !you should use options before entering the number and the base!.")
    Print("%IMPORTANT NOTE%: you can't use both -e and -d.")

if len(argumentList) == 0:
    PrintHelp()
    exit(0)

if '-c' in argumentList:
    argumentList.insert(argumentList.index("-c") + 1, "True")
if '-d' in argumentList:
    argumentList.insert(argumentList.index("-d") + 1, "True")
if '-e' in argumentList:
    argumentList.insert(argumentList.index("-e") + 1, "True")

if '-l' in argumentList:
    argumentList.insert(argumentList.index("-l") + 1, "True")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

options = "hdenblc:"

colorized: bool = False
letterDecimal: bool = False
specifiedNum: bool = False
Base: int = 36
decode: bool = False
encode: bool = False
_num: str = "NaN"



try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
    colorized = "c" in arguments
    
    for currentArgument, currentValue in arguments:

        if currentArgument in ("-d", "--decode"):
            decode = True
        if currentArgument in ("-e", "--encode"):
            encode = True
        if currentArgument in ("-c", "--colored"):
            colorized = True
        if currentArgument in ("-h", "--help"):
            PrintHelp()
            exit(0)
        if currentArgument in ("-l", "--lettersdecimal"):
            letterDecimal = True
        if currentArgument in ("-b", "--base"):
            Base = int(argumentList[argumentList.index(currentArgument) + 1])
            if (10 <= Base <= 62) == False:
                Print("Not a valid base! Base should be between 10 and 62")
                exit(0)
        if currentArgument in ("-n", "--number"):
            specifiedNum = True
            _num = argumentList[argumentList.index(currentArgument) + 1]
    if '-b' in argumentList:
        Base = argumentList[argumentList.index('-b')+1]
    if '--base' in argumentList:
        Base = argumentList[argumentList.index('--base')+1]
    if '-n' in argumentList:
        _num = argumentList[argumentList.index('-n')+1]
    if '--number' in argumentList:
        _num = argumentList[argumentList.index('--number')+1]
except getopt.error as err:
    print (str(err))
    exit(0)

print(f"result: c_{colorized}, letter_{letterDecimal}, speci_{specifiedNum}, b_{Base}, dCode_{decode}, eCode: {encode}, num: {_num}")
# colorized: bool = False
# letterDecimal: bool = False
# specifiedNum: bool = False
# Base: int = 36
# decode: bool = False
# encode: bool = False
# _num: str = "NaN"

#base -b [n], letter decimal --l, help --h, num -n (loop if not), ! break,