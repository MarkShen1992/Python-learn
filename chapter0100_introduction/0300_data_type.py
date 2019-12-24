# -*- single line comment -*-
# int
a = 10
print(a)

b = 10
c = 10
print(b * c)

d = 17 % 3
print(d)

e = 5 ** 2 # 5的平方
print(e)

# boolean
condition1 = True
print(condition1)

condition2 = False
print(condition2)

# float
f = 8 / 5 # division always returns a floating point number
print(f)

f2 = 8 // 5
print(f2)

# string
string1 = "hello world"
print(string1)

string2 = 'hello world'
print(string2)

string3 = 'doesn\'t'
print(string3)

print("""\
Usage: thingy [OPTIONS]
       -h                        Display this usage message
       -H hostname               Hostname to connect to
""")

string4 = 3 * 'un' + 'ium'
print(string4)

string5 = 'Py' 'thon'
print(string5)

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

# | P | y | t | h | o | n |
# 0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1  0

word = 'Python'
print(word[0])
print(word[-1]) # last character
print(word[-2]) # second-last character
print(word[:2]) # character from the beginning to position 2 -- Py
print(word[2:]) # thon
print('J' + word[1:])

s = 'supercalifragilisticexpialidocious'
print(len(s))

# list
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[-3:])

print(squares + [36, 49, 64, 81, 100])

cubes = [1, 8, 27, 65, 125]  # something's wrong here
print(cubes[3])
cubes[3] = 64  # replace the wrong value
print(cubes[3])
cubes.append(216)
print(cubes)
cubes.append(7 ** 3)
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)

letters = ['a', 'b', 'c', 'd']
print(letters)
g = ['a', 'b', 'c']
n = [1, 2, 3]
x = [g, n]
print(x)