import shelve

p = [345,232,'asa', True]
s=shelve.open('my.db')
s['p']=p
s.close()