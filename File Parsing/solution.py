
from cmath import log
from distutils.log import info


def logSeprate(file):
    try:
        with open(file) as f:
            f = f.readlines()
        if(len(f)==0):
            print("Empty log file passed! Please pass another file.")
            exit()
    except:
        print("No such file exists :(. Try again!")
        exit()

    info_output_file = open(f'{file.split(".")[0]}_info.log', 'w') #info logs file
    debug_output_file = open(f'{file.split(".")[0]}_debug.log', 'w') #debug logs file
    error_output_file = open(f'{file.split(".")[0]}_error.log', 'w') #error logs file

    for line in f:
        lines = line.split('"')
        for j in lines:
            if(j.endswith('HTTP/1.1')):
                ind = lines.index(j)
                break       
        check = int(line.split('"')[ind+1].strip().split(" ")[0]) #retreive the status code through a pattern in web server log files
        if((check>=100) & (check<=199)): #info_log
            info_output_file.write(line)

        elif((check>=400) & (check<=499)): #error log
            error_output_file.write(line)

        elif((check>=300) & (check<=399)): #debug log
            debug_output_file.write(line)
    
    info_output_file.close()
    debug_output_file.close()
    error_output_file.close()
    print("Log sepration done! The 3 new log files corresponding to info, debug & status logs saved.")


if(__name__=="__main__"):
    print("----Log Parser Program----\nLog files available:\n1.access.log 2. w3af.txt 3. empty.log\nEnter any log file name to run the program:")
    #access.log
    #w3af.txt
    #empty.log
    inp = input(str())
    file = inp
    logSeprate(file)
    
