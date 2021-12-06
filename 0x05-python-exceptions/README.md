# Python -Exceptions
In this project we are required to:
* know the difference between errors nad exceptions
* What execeptions are and how to use them
* When to use exceptions
* How to correclty handle an exceptions
* Whats the purpose of catching exceptions
* How to raise a builtin exception
* When do we need to implement a clean-up action after an exceptions
## Requirements
*  Allowed editors: vi , vim, emacs
* All files will be interpreted/compiled on ubuntu 20.04 LTS using python3 (version 3.8.5)
* All files should end with a new line
* The first line of all the files should be #!/usr/bin/python3
* Yhe code should use th pycodestyle (version 2.7.*)
*  All the files must be executable
# TASKS
### 0.Safe list printing
write a function that prints x elements of a list
* prototype: _def safe_print_list(my_list=[], x=0):_
* my_list can contain any type (int, str, etc)
* All elements must be printed on the same line followed by a new line
* x represents the number of elements to print
* x can be bigger than length of my_list
* Returns the real number of elements printed
* Use the try: / except:
* Importing of modules is not allowed
* The use of the len() is not allowed
### file
0-safe_print_list.py
### test file
0-main.py
### 1.Safe printing of integers list
Write a functiond that prints an integer with "{:d}".format().
* Prototype: def safe_print_integer(value):
* value can be any type(int, str, etc)
* The integer should be printed followed by a new line
* Returns True if value has been correctly printed (it means the value is an int)
* Otherwise, returns False
* Use ty: / except:
* Use "{:d}".format() to print as integer
* Importing of modules is not allowed
* The use of the type() is not allowed
### file
1-safe_print_integer.py
### test file
1-main.py
### 2.Print and count integers
Write a funciton that prints the first x elements of a list and only integers
* Prototype __def safe_print_list_integers(my_list=[], x=0):
* my_list can contain any type(in, str, etc)
* All integers have to be printed on the same line followed by a new line -
	other type of value in the list must be skipped
* x represents the number of elements to access in my_list
* x can be bigger than the length of my_list - if its the case, an exception is expected to occur
* Returns the real number of integers printed
* Use try: / except:
use "{:d}".format() to print an integer
* Importing of modules is not allowed
* The use of the len() is not allowed
### file
2-safe_print_list_integers.py
### test file
2-main.py
### 3.Integers division with debug
Write a function that divides 2 integers and prints the result.
* Prototype: def __safe_print_division(a, b):__
* Assume and and b are integers
* The result of the division should print on the finally: section preceded by Inside result:
* returns the value of the division, otheriwse None
* Use try: / except: / finally:
* use "{:d}".format() to print the result
* Importing of any modules is not allowed
### files
3-safe_print_division.py
### test file
3-main.py
