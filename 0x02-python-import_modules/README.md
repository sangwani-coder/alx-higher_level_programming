# Python Import & Modules
## General
- Why Python programming is awesome
- Howe to import functions from another file
- How to use importted functions
- How to create a module
- How to use the built-in function dir()
- How to prevent code in the script from being executed when imported
- How to use command line arguments with Python programs
## Requirements
### General
- Alllowed editors: vi, vim, emacs
- All the files will be interpreted/compiled on Ubuntu 20.04 LTS using python3(version 3.8.5)
- All files should end with a new line
- The first line of every file should be #!/usr/bin/python3
- A README.md file, at the root of this folder of the project
- The code should use the pycodestyle(version2.7.*)
- All the files should be executable
- The length of the files will be tested using wc
## Tasks 0. Import a simple function from a simple file
### filename: 0-add.py
Imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3.
- The print function should be usued with string format to display integers
- the asteric * should not be used for imporint of __import__
- The code should not be executed when imported -by using __import__
## Task 1. My first toolbox
### filename: 1-calculation.py
Imports functions from the file calculator_1.py, does some Maths, and prints the result
- Do not use the print() more than four times.
- The code should not be executed when imported by using __import__
## Task 2. How to make a script dynamic
### filename: 2-args.py
Prints the number of and the list of arguments to the program.
- The code should not be executed when imported.
