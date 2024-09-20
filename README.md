# tiny-python-tasks
Contains simple python programs


# Lamda
Syntax: lamda param : action(param)
Eg: lamda a,b : a + b
Eg: lamda mark : f"pass with {mark}" if mark > 50
Rules:
    - Only use them once.(onetime annoys function)

# List comprehension

Syntax: list = [item for item in items if condition]

Eg 1: Creating list of vowels in a given word  
list = [letter for letter in words if letter in vowels]

Eg 2: Creating list that contains a score greater than 50%
list = [score for score in scores if score > 50]

Eg 3: Capitalizing each letter in a word 
list = [letter.upper() for letter in words]

Rules:
    - Condition is optional.
    - You can perform an operation on the item    

# Dictionary comprehension

Syntax: dict = {key:value for key, value in dict.items() if condition}

Eg 1: Creating graduated student from all  student list 
graduated_student = { student: score for student,score in all_students.items() if score > 50 }


Rules:
    - Condition is optional.
    - You can perform an operation on the key and value    

# Modules / Packages

- Pandas (To handle table manipulation EXCEL, CSV, SQL database)
  - https://pandas.pydata.org
- pretty table (display a table)
  - https://pypi.org/project/prettytable/
- Turtle (small animations, graphics and games)
  - https://docs.python.org/3/library/turtle.html
- Tkinter (GUI based)
  - https://docs.python.org/3/library/tkinter.html#the-packer
  - http://tcl.tk/man/tcl8.6/TkCmd/pack.htm
- re (for regex string validation)
  - https://www.w3schools.com/python/python_regex.asp
  - https://regex101.com
- SMTP ( to send mail)
  - https://docs.python.org/3/library/smtplib.html
- datetime (works with date and time)
  - https://docs.python.org/3/library/datetime.html


# Services:

To run a python code to run on cloud services for free
    refer: https://www.pythonanywhere.com
