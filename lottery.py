from hashlib import sha512 as sha
from numpy import loadtxt

list_entries=loadtxt('entries.txt',dtype='str',delimiter=',')
number_entries=len(list_entries)

entries=[]
for i in range(number_entries-1):
	entries.append([list_entries[i+1][1],list_entries[i+1][0],list_entries[i+1][4],list_entries[i+1][5],list_entries[i+1][3]])
max_ticket=int(entries[-1][3])

working_hash=sha('JUNE2020'.encode('ascii'))
entries.sort(key=lambda x:x[0])

for i in range(number_entries-1):
	old_hash=working_hash.hexdigest().encode('ascii')
	working_hash=sha(old_hash+entries[i][0].encode('ascii')+str(entries[i][1]).encode('ascii'))

win_list=str(int(working_hash.hexdigest(),16))
print (win_list)
n_dig,x=len(str(max_ticket)),0

while int(win_list[x:n_dig+x])>max_ticket:
	x+=1
winner=int(win_list[x:n_dig+x])
print (str(winner))

i=0
while int(entries[i][2])<=winner and int(entries[i][3])>=winner:
	i+=1
	if i>len(entries):
		print ('Fail')
		exit()
print ('Winner is '+entries[i-1][4])
