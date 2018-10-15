user@epk428-18:~$ firefox&
[1] 2219
user@epk428-18:~$ git clone https://github.com/login/RTR105
Cloning into 'RTR105'...
Username for 'https://github.com': Asarovskis
Password for 'https://Asarovskis@github.com': 
remote: Repository not found.
fatal: repository 'https://github.com/login/RTR105/' not found
user@epk428-18:~$ git clone https://github.com/Asarovskis/RTR105
Cloning into 'RTR105'...
remote: Enumerating objects: 30, done.
remote: Counting objects: 100% (30/30), done.
remote: Compressing objects: 100% (26/26), done.
remote: Total 30 (delta 5), reused 12 (delta 2), pack-reused 0
Unpacking objects: 100% (30/30), done.
Checking connectivity... done.
user@epk428-18:~$ cd RTR105
user@epk428-18:~/RTR105$ python
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> x=5
>>> if x<10
  File "<stdin>", line 1
    if x<10
          ^
SyntaxError: invalid syntax
>>> x=5
>>> if x<10:
... print('Smaller')
  File "<stdin>", line 2
    print('Smaller')
        ^
IndentationError: expected an indented block
>>> x=5
>>> if x<10:
... print('Smaller'):
  File "<stdin>", line 2
    print('Smaller'):
        ^
IndentationError: expected an indented block
>>> x=5
>>> if x<10:
... print('Smaller')
  File "<stdin>", line 2
    print('Smaller')
        ^
IndentationError: expected an indented block
>>> exit()
user@epk428-18:~/RTR105$ ipython


exit()
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 

In [1]: x=5

In [2]: if x<10:
   ...:     print('Smaller')
   ...: if x>20:
   ...:     print('Bigger')
   ...: print('finis')
   ...: 
Smaller
finis

In [3]: x=5

In [4]: if x==5:
   ...:     print('Equals 5')
   ...: if x>4:
   ...:     print('Greater than 4')
   ...: if x>=5:
   ...:     print('Greater than or Equals 5')
   ...: if x<=5:
   ...:     print('Less than or Equals 5')
   ...: if x!=6:
   ...:     print('Not equal 6')
   ...:     
Equals 5
Greater than 4
Greater than or Equals 5
Less than or Equals 5
Not equal 6

In [5]: x=5

In [6]: print('Before 5')
Before 5

In [7]: if x==5:
   ...:     print('Is 5')
   ...:     print('Is still 5')
   ...:     print('Third 5')
   ...: print('Afterwards 5')
   ...: print('Before 6')
   ...: if x==6:
   ...:     print('Is 6')
   ...:     print('Is Still 6')
   ...:     print('Third 6')
   ...: print('Afterwards 6')
   ...: 
Is 5
Is still 5
Third 5
Afterwards 5
Before 6
Afterwards 6

In [8]: 

In [8]: x=5

In [9]: if x>2:
   ...:     print('Bigger than 2')
   ...:     print('Still bigger')
   ...: print('Done with 2')
   ...: 
Bigger than 2
Still bigger
Done with 2

In [10]: for i in range(5):
    ...:     print(i)
    ...:     if i>2:
    ...:         print('Bigger than 2')
    ...:        print('Done with i'i)
  File "<tokenize>", line 5
    print('Done with i'i)
    ^
IndentationError: unindent does not match any outer indentation level


In [11]: x=5

In [12]: if x>2:
    ...:     print('Bigger than 2')
    ...:     print('Still bigger')
    ...:  print('Done with 2')
  File "<tokenize>", line 4
    print('Done with 2')
    ^
IndentationError: unindent does not match any outer indentation level


In [13]: x=5

In [14]: if x>2:
    ...:     print('Bigger than 2')
    ...:     print('Still bigger')
    ...:    print('Done with 2')
  File "<tokenize>", line 4
    print('Done with 2')
    ^
IndentationError: unindent does not match any outer indentation level


In [15]: x
Out[15]: 5

In [16]: done()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-16-2b9763cd6e02> in <module>()
----> 1 done()

NameError: name 'done' is not defined

In [17]: 

In [17]: x
Out[17]: 5

In [18]: x=5

In [19]: if x>2:
    ...:     print('Bigger than 2')
    ...:     print('Still bigger')
    ...: print('Done with 2')
    ...: 
Bigger than 2
Still bigger
Done with 2

In [20]: if x>2:
    ...:     print('Bigger than 2')
    ...:     print('Still bigger')
    ...: print('Done with 2')
    ...: for i in range(5):
    ...:     print(i)
    ...:     if i>2:
    ...:         print('Bigger than 2')
    ...:     print('Done with i'i)
  File "<ipython-input-20-4b46dab0ed22>", line 9
    print('Done with i'i)
                       ^
SyntaxError: invalid syntax


In [21]: if x>2:
    ...:     print('Bigger than 2')
    ...:     print('Still bigger')
    ...: print('Done with 2')
    ...: for i in range(5):
    ...:     print(i)
    ...:     if i>2:
    ...:         print('Bigger than 2')
    ...:     print('Done with i'i)
  File "<ipython-input-21-4b46dab0ed22>", line 9
    print('Done with i'i)
                       ^
SyntaxError: invalid syntax


In [22]: if x>2:
    ...:     print('Bigger than 2')
    ...:     print('Still bigger')
    ...: print('Done with 2')
    ...: for i in range(5):
    ...:     print(i)
    ...:     if i>2:
    ...:         print('Bigger than 2')
    ...:     print('Done with i',i)
    ...: print('All done')
    ...: 
Bigger than 2
Still bigger
Done with 2
0
Done with i 0
1
Done with i 1
2
Done with i 2
3
Bigger than 2
Done with i 3
4
Bigger than 2
Done with i 4
All done

In [23]: x=5

In [24]: if x>2:
    ...:     print('Bigger than 2')
    ...:     print('Still bigger')
    ...: print('Done with 2')
    ...: for i in range(5):
    ...:     print(i)
    ...:     if i>2:
    ...:         print('Bigger than 2')
    ...:     print('Done with i',i)
    ...: print('Done')
    ...: 
Bigger than 2
Still bigger
Done with 2
0
Done with i 0
1
Done with i 1
2
Done with i 2
3
Bigger than 2
Done with i 3
4
Bigger than 2
Done with i 4
Done

In [25]: x=42

In [26]: if x>1:
    ...:     print('More than one')
    ...:     if x<100:
    ...:         print('Less than 100')
    ...: print('All done')
    ...: 
More than one
Less than 100
All done

In [27]: x=4

In [28]: if x>2:
    ...:     print('Bigger')
    ...: else:
    ...:     print('Smaller')
    ...: print('All done')
    ...: 
Bigger
All done

In [29]: x=4

In [30]: if x>2:
    ...:     print('Bigger')
    ...: else:
    ...:     print('Smaller')
    ...: print('All done')
    ...: 
Bigger
All done

In [31]: if x<2:
    ...:     print('small')
    ...: elif x<10:
    ...:     print('Medium')
    ...: else:
    ...:     print('LARGE')
    ...: print('All done')
    ...: 
Medium
All done

In [32]: x=0

In [33]: if x<2:
    ...:     print('small')
    ...: elif x<10:
    ...:     print('Medium')
    ...: else:
    ...:     print('LARGE')
    ...: print('All done')
    ...: 
small
All done

In [34]: x=5

In [35]: x=20

In [36]: if x<2:
    ...:     print('small')
    ...: elif x<10:
    ...:     print('Medium')
    ...: else:
    ...:     print('LARGE')
    ...: print('All done')
    ...: 
LARGE
All done

In [37]: #No else 

In [38]: x=5 

In [39]: if x<2:
    ...:     print('Small')
    ...: elif x<10:
    ...:     print('Medium')
    ...: print('All done')
    ...: 
Medium
All done

In [40]: if x<2:
    ...:     print('Below 2')
    ...: elif x>=2:
    ...:     print('Two or more')
    ...: else:
    ...:     print('Something else')
    ...:      
Two or more

In [41]: astr='Hello Bob'

In [42]: try:
    ...:     instr=int(astr)
    ...: exept:
  File "<ipython-input-42-d606cf598f5c>", line 3
    exept:
        ^
SyntaxError: invalid syntax


In [43]: try:
    ...:     instr=int(astr)
    ...: except:
    ...:     istr=-1
    ...: print('First',istr)
    ...: astr= '123'
    ...: try:
    ...:     istr=int(astr)
    ...: except:
    ...:     istr=-1
    ...: print('Second',istr)
    ...: 
First -1
Second 123

In [44]: astr='Bob'

In [45]: try:
    ...:     print('Hello')
    ...:     istr=int(astr)
    ...:     print('There')
    ...: except:
    ...:     istr=-1
    ...: print('Done',istr)
    ...: 
Hello
Done -1

In [46]:       

