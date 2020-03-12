# split method for string
# s = "ram is a good boy.ram"
# # print((s.split(" ")))
# lst = []
# str1 = ""
# for char in s:
#     if char == " ":
#         lst.append(str1)
#         str1 = " "
#     else:
#         str1 = str1 + char
#
# print(lst)

import re

# a = "abc3abc4abc5"
# print(re.findall('abc', a))
# print(len(re.findall('abc', a)))
# b = re.finditer('abc', a)
# for i in b:
#     print(i)
# print(re.fullmatch('abc',a))
# print(re.fullmatch('abc3abc4abc5',a))
# results = []
# pattern = 'Ram'
# flag = 0
# string = ''
# for i in a:
#     if (pattern[0] == i):
#         string = string + i
#         flag = 1
#     elif (flag == 1):
#         pass
# print(results)
# s = ''
# finalResult = []
# for i in results:
#     if s == pattern:
#         finalResult.append(s)
#         s = ''
#     s = s + i
# finalResult.append(s)
# print(finalResult)
# print(re.findall('Ram', a))

# s = input("enter the string: ")
# s2 = re.sub(r'[A-Z a-z][0-9]', '*', s)  # r stands for the pattern compilation
# print(s2)
#
# re.sub
# print("--------")
# a = re.sub(r'[ad]', '*', 'abcdef')
# print(a)
#
# b = re.sub(r'[abc][123]', '*', 'a1 + b2 + c5 + x2')
# print(b)
#
# print("---------")
# c1 = re.sub(r'A.B', '*', 'A2B AxB AxxB A$B')
# print(c1)
# c2 = re.sub(r'A.B', '*', 'A2B AxB AxxB A$B A\nB')
# print(c2)
#
# print("---------")
# d = re.sub(r'AB+', '*', 'ABC ABB ABBBBC AC')
# print(d)
# d = re.sub(r'AB+', '*', 'ABC ABB ABBBBC AC')
# print(d)
#
e = re.sub(r'AB{3,6}', '*', 'ABB ABBB ABBBB ABBBBBBBBB')
print(e)
#
# f = re.sub(r'abc|xyz', '*', 'abcdefxyz123abc')
# print(f)
#
# g = re.sub('^abc', '*', 'abcdefgabc')  # here ^  is used for starts with
# print(g)
#
# h = re.sub('abc$', '*', 'abcdefgabc')  # here $ is use for ends with
# print(h)
#
# i = re.sub(r'AB\+', '*', 'AB+C')
# print(i)
#
# print("-------")
#
# j = re.sub(r'\d', '*', '3 + 14 = 17')  # here \d is used to replace the digits
# print(j)
#
# k = re.sub(r'\D', '*', '3 + 14 = 17')  # here \D is used to replace evrything except digits
# print(k)
#
# l = re.sub(r'\w', '*', 'This is a test. Or i?')  # \w is used to replace words or text except spaces and  special char
# print(l)
#
# m = re.sub(r'\W', '*', 'This is a test. Or is it?')  # here \W is used to replace the whitespaces and the special char
# print(m)
#
# n = re.sub(r'\s', '*', 'This is a test. Or is it?')  # here \s is used to replace the everything
# # but keeps the string and special char
# print(n)
#
# o = re.sub(r'\S', '*', 'This is a test. Or is it?')  # here \S is used to replace string but keeps the spaces
# print(o)

# print("----re.findall----")

# re.findall

# a = re.findall(r'[ad]', 'abcdef')
# print(a)
#
# b = re.findall(r'[abcx][1234]', 'a1 + b2 + c5 + x2')
# print(b)
#
# print("---------")
# c1 = re.findall(r'A.B', 'A2B AxB AxxB A$B')
# print(c1)
#
#
# i = re.findall(r'AB\+|ab\+', 'AB+Cab+dsfjaassaab+dfjhab+fdkjAB+')  #escape sequence is used to print special character
# print(i)

print("-------")

j = re.findall(r'\d', '3 + 14 = 17')  # here \d is used to finf the digits
print(j)
x = re.findall(r'\d{10}', "7609947483 8015295125 2035006370 6154817037 7608440455 7609947483@vtext.com 8015295125@sms.mycricket.com")
print(x)
# this forward slash(\) is used when we wnat to print the special symbols
y = re.findall(r'\d{4} \d{7}|\d{3} \d{8}', " 0511 4405222  021 87888822 ")
print(y)
z = re.findall(r'\(\d{4}\) \d{7}|\(\d{3}\) \d{8}', " (0511) 4405222  (021) 87888822 ")
print(z)


# k = re.findall(r'\D', '3 + 14 = 17')  # here \D is used to find evrything except digits
# print(k)
#
# l = re.findall(r'\w', 'This is a test. Or i?')  # here \w is used to find text
# print(l)
#
# m = re.findall(r'\W', 'This is a test. Or is it?')  # here \W is used to find the whitespaces and the special char
# print(m)
#
# print("-------------")
# n = re.findall(r'\s', 'This is a test. Or is it?')
# print(n)
# o = re.findall(r'\S', 'This is a test. Or is it?')  # here \S is used to replace string but keeps the spaces
# print(o)
# print('abc\abc')
