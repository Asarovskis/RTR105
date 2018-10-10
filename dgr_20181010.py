Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print(123)
123
>>> x=12.2
>>> y=14
>>> x=100
>>> print(x)
100
>>> print(y)
14
>>> spam

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    spam
NameError: name 'spam' is not defined
>>> a=35
>>> b=12.50
>>> c=a*b
>>> print(c)
437.5
>>> x=2
>>> x=x+2
>>> print(x)
4
>>> x=3.9*x*(1-x)
>>> print(x)
-46.8
>>> xx=2
>>> xx=xx+2
>>> print(xx)
4
>>> yy=440*12
>>> print(yy)
5280
>>> zz=yy/1000
>>> print(zz)
5
>>> jj=23
>>> kk=jj%5
>>> print(kk)
3
>>> dd=1+4
>>> print(dd)
5
>>> eee='hello''+ 'there'
SyntaxError: invalid syntax
>>> eee='hello'+ 'there'
>>> print(eee)
hellothere
>>> eee='hello'+ 'there'
>>> eee=eee+1

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    eee=eee+1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type(eee)
<type 'str'>
>>> type('hello')
<type 'str'>
>>> type(1)
<type 'int'>
>>> xx=1
>>> type(xx)
<type 'int'>
>>> temp=98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type(1.0)
<type 'float'>
>>> print(float(99)+100)
199.0
>>> i=42
>>> type(i)
<type 'int'>
>>> f=float(f)

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    f=float(f)
NameError: name 'f' is not defined
>>> f=float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10/2)
5
>>> print(99/100)
0
>>> type(1)
<type 'int'>
>>> print(99/100)
0
>>> sval='123'
>>> type(sval)
<type 'str'>
>>> print(99.0/100)
0.99
>>> type(sval)
<type 'str'>
>>> ype(sval)

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    ype(sval)
NameError: name 'ype' is not defined
>>> type(sval)
<type 'str'>
>>> print(sval+1)

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    print(sval+1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival=int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival+1)
124
>>> nsv='hello bobs'
>>> niv=int(nsv)

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    niv=int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bobs'
>>> inp=input('Ēurope Floor?')
Ēurope Floor?

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    inp=input('Ēurope Floor?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> inp=input('Stāvs?')
Stāvs?usf=int(inp)+1

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    inp=input('Stāvs?')
  File "<string>", line 1
    usf=int(inp)+1
       ^
SyntaxError: invalid syntax
>>> inp=input('Eiropas staavs') usf=int(inp)+1 print('Ūs floor'usf)
SyntaxError: invalid syntax
>>> inp=input('Eiropas staavs') usf=int(inp)+1 print('Ūs floor'usf)
SyntaxError: invalid syntax
>>> inp=input('Eiropas staavs') usf=int(inp)+1 print('Ūs floor'usf)
SyntaxError: invalid syntax
>>> inp=input('Stāvs')
Stāvs

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    inp=input('Stāvs')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> usf=int(inp)+1

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    usf=int(inp)+1
NameError: name 'inp' is not defined
>>> NameError: name 'inp' is not defined
SyntaxError: invalid syntax
>>> 



