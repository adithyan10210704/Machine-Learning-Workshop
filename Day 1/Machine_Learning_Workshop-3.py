Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======= RESTART: /home/superuser/Desktop/Machine_Learning_Workshop -2.py =======
apple
['cherry', 'date']
>>> 
======= RESTART: /home/superuser/Desktop/Machine_Learning_Workshop -2.py =======
apple
['cherry', 'date']
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/superuser/Desktop/Machine_Learning_Workshop -2.py", line 7, in <module>
    fruits.appennd("mango")
AttributeError: 'list' object has no attribute 'appennd'
>>> 
======= RESTART: /home/superuser/Desktop/Machine_Learning_Workshop -2.py =======
apple
['cherry', 'date']
['date', 'mango']
>>> 
========= RESTART: /home/superuser/Desktop/ML Workshop/Coordinates .py =========
10
>>> 
========= RESTART: /home/superuser/Desktop/ML Workshop/Coordinates .py =========
10
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/superuser/Desktop/ML Workshop/Coordinates .py", line 3, in <module>
    coordinates.append(30)
AttributeError: 'tuple' object has no attribute 'append'
>>> 
========= RESTART: /home/superuser/Desktop/ML Workshop/Coordinates .py =========
10
>>> 
= RESTART: /home/superuser/Desktop/ML Workshop/Student details - dictionary.py =
John
A
>>> 
= RESTART: /home/superuser/Desktop/ML Workshop/Student details - dictionary.py =
John
A
20
>>> 
= RESTART: /home/superuser/Desktop/ML Workshop/Student details - dictionary.py =
John
A
20
name John
courses ['Math', 'Science']
grade A
age 20
>>> 
============= RESTART: /home/superuser/Desktop/ML Workshop/Sets .py ============
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/superuser/Desktop/ML Workshop/Sets .py", line 2, in <module>
    numbers.add(6)
NameError: name 'numbers' is not defined
>>> 
============= RESTART: /home/superuser/Desktop/ML Workshop/Sets .py ============
{2, 4, 6}
>>> 
============= RESTART: /home/superuser/Desktop/ML Workshop/Sets .py ============
{2, 4, 6}
{1, 5}
{1, 2, 4, 5, 6, 8}
>>> 
======== RESTART: /home/superuser/Desktop/ML Workshop/Error Handling .py =======
Traceback (most recent call last):
  File "/home/superuser/Desktop/ML Workshop/Error Handling .py", line 2, in <module>
    result=10/0
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/superuser/Desktop/ML Workshop/Error Handling .py", line 3, in <module>
    except ZeroDivisonError:
NameError: name 'ZeroDivisonError' is not defined
>>> 
======== RESTART: /home/superuser/Desktop/ML Workshop/Error Handling .py =======
You cannot divide by 0
>>> 
==== RESTART: /home/superuser/Desktop/ML Workshop/Multiple_Error_Handling.py ===
You cannot divide by 0
>>> 
======= RESTART: /home/superuser/Desktop/ML Workshop/Error handling -2.py ======
An error occured invalid literal for int() with base 10: 'abc'
>>> 
== RESTART: /home/superuser/Desktop/ML Workshop/Error handling -3 'finally'.py =
The file was not found
>>> 
==== RESTART: /home/superuser/Desktop/ML Workshop/Multiple_Error_Handling.py ===
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/superuser/Desktop/ML Workshop/Multiple_Error_Handling.py", line 2, in <module>
    result=10/a
NameError: name 'a' is not defined
>>> 
==== RESTART: /home/superuser/Desktop/ML Workshop/Multiple_Error_Handling.py ===
>>> 
==== RESTART: /home/superuser/Desktop/ML Workshop/Multiple_Error_Handling.py ===
>>> 
==== RESTART: /home/superuser/Desktop/ML Workshop/Multiple_Error_Handling.py ===
Invalid value
>>> 
==== RESTART: /home/superuser/Desktop/ML Workshop/Multiple_Error_Handling.py ===
>>> 
==== RESTART: /home/superuser/Desktop/ML Workshop/Multiple_Error_Handling.py ===
>>> 
==== RESTART: /home/superuser/Desktop/ML Workshop/Multiple_Error_Handling.py ===
>>> 
==== RESTART: /home/superuser/Desktop/ML Workshop/Multiple_Error_Handling.py ===
You cannot divide by 0
>>> 
= RESTART: /home/superuser/Desktop/ML Workshop/Error handling - Value_Error.py =

>>> 
= RESTART: /home/superuser/Desktop/ML Workshop/Error handling - Value_Error.py =
Cannot divide by zero
>>> 
=== RESTART: /home/superuser/Desktop/ML Workshop/Error handling- arguments.py ==
Result:5.0
Execution completed
Error:Cannot divide by 0!
Execution completed
Error: Both arguments must be numbers
Execution completed
>>> 
==== RESTART: /home/superuser/Desktop/ML Workshop/Multiple_Error_Handling.py ===
Invalid value
>>> 
==== RESTART: /home/superuser/Desktop/ML Workshop/Multiple_Error_Handling.py ===
You cannot divide by 0
>>> 
=========== RESTART: /home/superuser/Desktop/ML Workshop/Avg marks.py ==========
Name of 1st student:?
=========== RESTART: /home/superuser/Desktop/ML Workshop/Avg marks.py ==========
Name of 1st student? XYZ
Math, Science and Computer science marks of  XYZ are 95,58,80 respectively
Name of 2nd student:?ABC
Math, Science and Computer science marks of ABC are 93,84,78 respectively
Average marks of  XYZ is 77.66666666666667
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/superuser/Desktop/ML Workshop/Avg marks.py", line 13, in <module>
    avg_b=(math_b+sci_b+comp+b)/3
NameError: name 'comp' is not defined
>>> 
=========== RESTART: /home/superuser/Desktop/ML Workshop/Avg marks.py ==========
Name of 1st student?xyz
Math, Science and Computer science marks of xyz are 95,58,80 respectively
Name of 2nd student:?abc
Math, Science and Computer science marks of abc are 93,84,78 respectively
Average marks of xyz is 77.66666666666667
Average marks of abc is 85.0
>>> 
== RESTART: /home/superuser/Desktop/ML Workshop/Maximum_and_minimum_in_list.py =
878
12
>>> 
======= RESTART: /home/superuser/Desktop/ML Workshop/No_of_occurences.py =======
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/superuser/Desktop/ML Workshop/No_of_occurences.py", line 7, in <module>
    no_of_times=count_no_of_times(text,word)
NameError: name 'text' is not defined
>>> 
======= RESTART: /home/superuser/Desktop/ML Workshop/No_of_occurences.py =======
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/superuser/Desktop/ML Workshop/No_of_occurences.py", line 7, in <module>
    no_of_times=count_no_of_times(text,word)
NameError: name 'text' is not defined
>>> 
======= RESTART: /home/superuser/Desktop/ML Workshop/No_of_occurences.py =======
The word test occurs 1 times in the line.
>>> 
======= RESTART: /home/superuser/Desktop/ML Workshop/No_of_occurences.py =======
The word test occurs 2 times in the line.
>>> 
======= RESTART: /home/superuser/Desktop/ML Workshop/No_of_occurences.py =======
The word test occurs 3 times in the line.
>>> 
========== RESTART: /home/superuser/Desktop/ML Workshop/Palindrome.py ==========
True
>>> 
========== RESTART: /home/superuser/Desktop/ML Workshop/Palindrome.py ==========
A man a plan a canal Panama is not a palindrome
>>> 
========== RESTART: /home/superuser/Desktop/ML Workshop/Palindrome.py ==========
MALAYALAM is a palindrome
>>> 
=========== RESTART: /home/superuser/Desktop/ML Workshop/Factorial.py ==========
Enter the number5
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/superuser/Desktop/ML Workshop/Factorial.py", line 4, in <module>
    fact=fact*fact(n-1)
TypeError: 'int' object is not callable
>>> 
=========== RESTART: /home/superuser/Desktop/ML Workshop/Factorial.py ==========
Enter the number: 4
24
>>> 
=========== RESTART: /home/superuser/Desktop/ML Workshop/Factorial.py ==========
Enter the number: 10
3628800
>>> 
=========== RESTART: /home/superuser/Desktop/ML Workshop/Factorial.py ==========
Enter the number: 5
120
>>> 