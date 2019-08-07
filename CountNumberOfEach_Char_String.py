# Please write a program which count the numbers of each character in a string input by console.

#--Solution:

dic = {}

s=input()

for item in s:

    dic[item] = dic.get(item,0)+1

print ('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))

#-----------Hints

#Use dict to store key/value pairs.
#Use dict.get() method to lookup a key with default value.
