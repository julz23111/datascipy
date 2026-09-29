tag = '</body>'
try:
    ndx = tag.index('/')
    print (ndx)
except ValueError:
    print ('not found')