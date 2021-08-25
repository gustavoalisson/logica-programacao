import re


mylist = ['* CONSÓRCIO', '* EMPLACAMENTO']
r = re.compile(".* * ")
newlist = list(filter(r.match, mylist)) # Read Note below
print(newlist)
