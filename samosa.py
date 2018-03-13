import os

def returnHosts():
    AllPossibleHosts    = []
    file = open('names.txt', 'r+')
    for line in file.readlines():
        host            = line.split(' ')
        host_fname      = host[0]
        host_lname      = host[1]
        host_email      = host[2]
        host_status     = host[3].strip('\n')
        if host_status == '0':
            AllPossibleHosts.append(line)

    return AllPossibleHosts

allPossibleHosts = returnHosts()
if len(allPossibleHosts) < 2:
    file = open('names.txt', 'r+')

    # This is the scenario where the list is about to reset after this turn
    # Consider the 1st person in the line as the 2nd host
    allPossibleHosts.append(file.readline())

twoHosts = allPossibleHosts[0:2]
print twoHosts

# send message to two hosts