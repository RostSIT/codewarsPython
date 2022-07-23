def solution(s):
    new_s = ""

    for i in s:
        if i.islower():
            new_s += i
        else:
            new_s += " " + i

    return new_s


x = solution("camelCasing")
y = solution("identifier")

print(1,x)
print(y)


def solution(s):
    return ''.join(i if i.islower() else " " + i for i in s)


x = solution("camelCasing")
y = solution("identifier")

print(2,x)
print(y)


def solution(s):
    return (i if i.islower() else " " + i for i in s)


x = solution("camelCasing")
y = solution("identifier")

print(3,x)
print(y)

import re


def solution(s):
    return re.sub('([A-Z])', r' \1', s)


x = solution("camelCasing")
y = solution("identifier")

print(4,x)
print(y)
"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""
