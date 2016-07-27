s = input("enter a string:")
alreadyprintanswer=False
for i in s:
    if i.isalnum():
       alreadyprintanswer='True'
       print('True')
       break
if not alreadyprintanswer:
    print('False')
for i in s:
    if i.isalpha():
        alreadyprintanswer = 'True'
        print('True')
        break
if not alreadyprintanswer:
    print('False')
for i in s:
    if i.isdigit():
        alreadyprintanswer = 'True'
        print('True')
        break
if not alreadyprintanswer:
    print('False')
for i in s:
    if i.islower():
        alreadyprintanswer = 'True'
        print('True')
        break
if not alreadyprintanswer:
    print('False')
for i in s:
    if i.isupper():
        alreadyprintanswer = 'True'
        print('True')
        break
if not alreadyprintanswer:
    print('False')







