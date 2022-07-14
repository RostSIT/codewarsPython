p = 'xdOXo'
c = 'xdoo'
u = 'ffddss'


def xo(s):
    s.lower()
    x = 0
    o = 0
    for i in s:
        if i == 'x':
            x += 1
        if i == 'o':
            o += 1
    if x == o or x == 0 and o == 0:
        return True
    else:
        return False


y = xo(p)
z = xo(c)
v = xo(u)

print(y)
print(z)
print(v)


def xo(s):
    return s.lower().count('x') == s.lower().count('o')

"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""
