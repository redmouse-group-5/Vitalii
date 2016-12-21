import shelve

s=shelve.open('my.db')
p=s['p']
print(p)
s['p']=(True, True)
s.close()