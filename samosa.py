import os, re, fileinput
from commonMethods import *
from send_sms import *

hostsNameFile = 'names.txt'
'''
Data format in the above file :
"FirstName LastName Email Status"
Status : 0 - Available, 1 - NotAvailable
'''


'''
Reads hostsNameFile and returns all eligible hosts based on respective status
'''
def returnHosts():
    AllPossibleHosts    = []
    file = open(hostsNameFile, 'r')
    for line in file.readlines():
        host            = line.split(' ')
        host_fname      = host[0]
        host_lname      = host[1]
        host_email      = host[2]
        host_status     = host[3].strip('\n')
        if host_status == '0':
            AllPossibleHosts.append(line)
    file.close()
    return AllPossibleHosts

'''
Changes the status of all hosts to 'available' i.e. '0'
'''
def makeAllHostsAvailable():
    for line in fileinput.input(hostsNameFile, inplace=True):
        # This will replace the existing line with the same except the status will be reset i.e. changed to 0
        # this print writes into the file (instead of stdout)
        print line.replace(line,line.split(' ')[0]+' '+line.split(' ')[1]+' '+line.split(' ')[2]+' '+'0')

'''
Updates statuses of 2 hosts who got snacks today
'''
def updateStatusesOfHosts(twoHosts):
    file = open(hostsNameFile, 'r')
    # Syntax : sed -i'' '<lineNum> s/0/1/g' <file-name>
    # line number = index+1
    host_1_index = -1
    host_2_index = -1
    for line in file.readlines():
        host_1_index += 1
        host_2_index += 1
        if line == twoHosts[0]:
            unixFileCmd1 = "sed -i '' \'" + str(host_1_index+1) + " s/0/1/g\' " + hostsNameFile
            os.system(unixFileCmd1)
        if line == twoHosts[1]:
            unixFileCmd2 = "sed -i '' \'" + str(host_2_index+1) + " s/0/1/g\' " + hostsNameFile
            os.system(unixFileCmd2)
    file.flush()
    file.close()

'''
Hosts with status - available
'''
allPossibleHosts = returnHosts()
#print "allPossibleHosts : " , allPossibleHosts

'''
# This is the scenario where the list is about to reset
    # so reset and get the first person from top
'''
if len(allPossibleHosts) < 2:
    # All statuses gets reset to 0
    makeAllHostsAvailable()
    print "#### List reset ####"
    newSetOfAvailableHosts = returnHosts()
    for newHosts in newSetOfAvailableHosts:
        allPossibleHosts.append(newHosts)

twoHosts = allPossibleHosts[0:2]
h1index = 0
h2index = 1
print "Todays hosts are : ", twoHosts

# send message to two hosts
sendMsgTwoHosts(twoHosts, msgBodyString(twoHosts, 'start'))

# Possible Scenarios :
# Both says YES
# One of them says YES
# Both of them says NO

print "Updating status #############"
updateStatusesOfHosts(twoHosts)