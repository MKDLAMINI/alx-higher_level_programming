#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    tally_sum = 0
    for i in range(1, len(argv)):
        tally_sum += int(argv[i])
    print("{}".format(tally_sum))
