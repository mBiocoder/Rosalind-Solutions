#!/usr/python3

import sys
#When using commandline arguments
#filename = sys.argv[1]

with open("C:\Bachelor Bioinformatik\Bachelor Bioinformatik\ProPra\RosalindPythonProblems\File.txt") as f1, \
        open("C:\Bachelor Bioinformatik\Bachelor Bioinformatik\ProPra\RosalindPythonProblems\Fileoutput.txt", "w") as f3:
            count = 0
            for line in f1:
                count = count + 1
                if count % 2 == 0:
                    print(line.strip())
                    f3.write(line.strip() + '\n')

