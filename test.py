import getopt, sys

argumentList = sys.argv[1:]

options = "hmo:"

long_options = ["Help", "My_file", "Output="]

colorized: bool = False
numbase: int = 36
letterDecimal: bool = False

def Print(message: str) -> None:
    if colorized:
        print()
        # colorized
    print(str)

def PrintHelp():
    print("h")

try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
    if '-c' in arguments or '--colored' in arguments:
        colorized = True
    if '-h' in arguments or '--help' in arguments:
        PrintHelp()
        exit(0)
    
    for currentArgument, currentValue in arguments:

        if currentArgument in ("-h", "--Help"):
            print ("Displaying Help")
            
        elif currentArgument in ("-m", "--My_file"):
            print ("Displaying file_name:", sys.argv[0])
            
        elif currentArgument in ("-o", "--Output"):
            print (("Enabling special output mode (% s)") % (currentValue))
            
except getopt.error as err:
    print (str(err))

#color --c, base -b [n], letter decimal --l, help --h, num -n (loop if not), ! break,