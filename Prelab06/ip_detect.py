#!/usr/bin/env python3

import sys
import os
import re

def detect():
    expr1 = r"(\d+)\.(\d+)\.(\d+)\.(\d+)\:(\w+)"
    with open("addys.in") as inputFile:
        content = inputFile.readlines()
        for line in content:
            ip_valid=1
            port_valid=0
            priviledge=0
            matched1 = re.search(expr1,line)
            if matched1:
                for i in range(1,5):
                    if(int(matched1.group(i))>255):
                        ip_valid=0
                if(matched1.group(5).isnumeric() and (int(matched1.group(5)) >=1) and (int(matched1.group(5)) <= 32767)):
                    port_valid=1
                if(port_valid):
                    if(int(matched1.group(5)) <= 1024):
                        priviledge=1

                if not ip_valid:
                    print(matched1.group(0)+" - "+"Invalid IP Address")
                elif ip_valid and not port_valid:
                    print(matched1.group(0)+" - Invalid Port Number")
                elif ip_valid and port_valid:
                    if priviledge:
                        print(matched1.group(0)+" - Valid (root privileges required)")
                    else:
                        print(matched1.group(0)+" - Valid")

    return 0

if __name__ == "__main__":
    detect()

