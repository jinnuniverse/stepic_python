#x =[1,2,3]

#x.append(4)
#x.append(5)

#print(x)

#top = x.pop()
#print(top)
#print(x)

#top = x.pop()
#print(top)
#print(x)

#x = print(4)
#print(type(x))

def closest_mod_5(x):
    y = x

    if str(type(y)) == "<class 'int'>":

        while y % 5 != 0:
            y += 1

        if y >= x:
            return y
    return 0

#print(closest_mod_5(28))

def printab(a, b, *args):
    print(a)
    print(b)
    for arg in args:
        print(arg)

#printab(5, 8, -45, 14, 390)

def printab(a, b, **kwargs):
    print(a)
    print(b)
    for key in kwargs:
        print(key, kwargs[key])

#printab(5, 8, v = -45, test = 14, mood = 390)

def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res

s(0,0, 31)


