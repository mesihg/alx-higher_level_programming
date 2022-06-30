#!/usr/bin/python3

import sys
sum = 0
for num in range(1, len(sys.argv)):
    sum += int(sys.argv[num])
print(sum)
