In [1]: noraade_uz_failu=open('texts.txt','r')

In [2]: fhand=open('texts.txt','r')

In [3]: fhand=open('textx.txt')
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-3-523cbaae43b9> in <module>()
----> 1 fhand=open('textx.txt')

FileNotFoundError: [Errno 2] No such file or directory: 'textx.txt'

In [4]: fhand=open('texts.txt')

In [5]: print(fhand)
<_io.TextIOWrapper name='texts.txt' mode='r' encoding='UTF-8'>

In [6]: texts.read()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-6-5d59c8606e89> in <module>()
----> 1 texts.read()

NameError: name 'texts' is not defined

In [7]: fhand.read()
Out[7]: 'mans fails 1\n'

In [8]: stuff='Hello\nWorld'

In [9]: stuff
Out[9]: 'Hello\nWorld'

In [10]: print(fhand)
<_io.TextIOWrapper name='texts.txt' mode='r' encoding='UTF-8'>

In [11]: print(stuff)
Hello
World

In [12]: stuff='X\nY'

In [13]: print(stuff)
X
Y

In [14]: len(stuff)
Out[14]: 3

In [15]: xfile=open('texts.txt')

In [16]: for cheese in xfile:
    ...:     print(cheese)
    ...:     
mans fails 1


In [17]: fhand=open('texts.txt')

In [18]: count=0

In [19]: for line in fhand:
    ...:     count=count+1
    ...: print('Line count:',count)
    ...: 
Line count: 1

In [20]: fhand=open('texts.txt')

In [21]: inp=hand.read()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-21-f57db996a91b> in <module>()
----> 1 inp=hand.read()

NameError: name 'hand' is not defined

In [22]: fhand=open('texts.txt')

In [23]: inp=fhand.read()

In [24]: print(len(inp))
13

In [25]: print(inp[:20])
mans fails 1


In [26]: fhand=open('texts.txt')

In [27]: for line in fhand:
    ...:     if line.startswith('From')
  File "<ipython-input-27-968858b53d75>", line 2
    if line.startswith('From')
                              ^
SyntaxError: invalid syntax


In [28]: fhand=open('texts.txt')

In [29]: for line in fhand:
    ...:     if line.startswith('From'):
    ...:         print(line)
    ...:         

In [30]: fhand=open('texts.txt')

In [31]: for line in fhand:
    ...:     line=line.rstrip()
    ...:     if line.startswith('From'):
    ...:         continue
    ...:     print(line)
    ...:     
    ...:         
    ...:         
mans fails 1

In [32]: fname=input('Enter the file name:')
Enter the file name:

In [33]: fhand=open(fname)
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-33-547ea7252a02> in <module>()
----> 1 fhand=open(fname)

FileNotFoundError: [Errno 2] No such file or directory: ''

In [34]: fname=input('Enter the file name:')
Enter the file name:

In [35]: fhand=open(fname)
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-35-547ea7252a02> in <module>()
----> 1 fhand=open(fname)

FileNotFoundError: [Errno 2] No such file or directory: ''

In [36]: fname=input('Enter the file name: ')
Enter the file name:  zxs

In [37]: fhand=open(fname)
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-37-547ea7252a02> in <module>()
----> 1 fhand=open(fname)

FileNotFoundError: [Errno 2] No such file or directory: ' zxs'

In [38]: fname=input('Enter the file name: ')
    ...: fhand=open(fname)
    ...: count=0
    ...: for linein fhand:
  File "<ipython-input-38-c32a13fa2475>", line 4
    for linein fhand:
                   ^
SyntaxError: invalid syntax


In [39]: fname=input('Enter the file name: ')
    ...: fhand=open(fname)
    ...: count=0
    ...: for line in fhand:
    ...:     if line.startswith('mans'):
    ...:         count=count+1
    ...: print('There were',count,'subject lines in',fname)
    ...: 
Enter the file name: texts.txt
There were 1 subject lines in texts.txt

In [40]: fname=input('Enter the file name: ')
Enter the file name:                         

In [41]: fname=input('Enter the file name: ')
    ...: try:
    ...:     fhand=open(fname)
    ...: exept:
    ...:     print('File can not be opened:',fname)
    ...:     quit()
    ...: 
    ...: 
  File "<ipython-input-41-8dbc1dda9111>", line 4
    exept:
        ^
SyntaxError: invalid syntax


In [42]: fname=input('Enter the file name: ')
    ...: try:
    ...:     fhand=open(fname)
    ...: except:
    ...:     print('File can not be opened:',fname)
    ...:     quit()
    ...:     
    ...: 
    ...: 
Enter the file name: texts.txt   

In [43]: 

In [43]: fname=input('Enter the file name: ')
    ...: try:
    ...:     fhand=open(fname)
    ...: except:
    ...:     print('File can not be opened:',fname)
    ...:     quit()
    ...:     
    ...: 
    ...: 
Enter the file name: sasfa
File can not be opened: sasfa

