import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batman')
print(mo.group())

phoneRegex = re.compile(r'\d\d-\d\d\d\d\d\d\d\d\d')
mo = phoneRegex.search('My phone number is 43-999621545')
print(mo.group())


batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo.group())

batRegex = re.compile(r'dinner\?')
mo = batRegex.search('Ready for dinner?')
print(mo.group())
