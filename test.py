import os

a = "ayoola88"
#b = "0123456789"
c = None

for b in a:
    c = a.translate(None, "0123456789")

print (c)