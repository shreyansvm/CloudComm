import os, re, fileinput

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
    print "Todays hosts are : ", twoHosts

    updateHost_1 = twoHosts[0].split(' ')[0] + ' ' \
                   + twoHosts[0].split(' ')[1] + ' ' \
                    + twoHosts[0].split(' ')[2] + ' ' + '1'

    updateHost_2 = twoHosts[1].split(' ')[0] + ' ' \
                   + twoHosts[1].split(' ')[1] + ' ' \
                   + twoHosts[1].split(' ')[2] + ' ' + '1'

    # for line in fileinput.input(hostsNameFile, inplace=True):
    #     print line.replace(twoHosts[0], updateHost_1)
    #     print line.replace(twoHosts[1], updateHost_2)

allPossibleHosts = returnHosts()
#print "allPossibleHosts : " , allPossibleHosts

if len(allPossibleHosts) < 2:
    # This is the scenario where the list is about to reset
    # so reset and get the first person from top
    '''All statuses gets reset to 0'''
    makeAllHostsAvailable()
    print "List reset #############"
    newSetOfAvailableHosts = returnHosts()
    for newHosts in newSetOfAvailableHosts:
        allPossibleHosts.append(newHosts)

twoHosts = allPossibleHosts[0:2]
h1index = 0
h2index = 1
print twoHosts

updateFile = open(hostsNameFile, 'r+')
for s in updateFile.readlines():
    if s == 'Shreyans Mulkutkar Shreyans.Mulkutkar@alcatel-lucent.com 0\n':
        print '\t*** Found Shreyans'
        #updateFile.write(s.replace(s,'Shreyans Mulkutkar Shreyans.Mulkutkar@alcatel-lucent.com 0\n'))
updateFile.close()

print "Updating status #############"
updateStatusesOfHosts(twoHosts)

# Scenarios :
# send message to two hosts
# Both says YES
# One of them says YES
# Both of them says NO