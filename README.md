# 0x00 AirBnb clone

<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png">

## The Overview

Airbnb is a popular website that is disrupting the hospitality industry by giving people the power to rent out rooms in their homes and/or rent wherever they choose. In other words, Airbnb became the middleman, not hotels. With Airbnb, hosts can list their spaces and book unique accomodations. The prices are determined by the hosts and are often cheaper and much more convenient for many.

Airbnb began in 2008 when two designers hosted three travelers looking for a place to stay. Now, millions of hosts and travelers from all over the world have chosen to use this site as an alternative source of income or a unique way of traveling. The company is successful because it helps make sharing one's space easy and safe. Personal profiles and listings are verified. A smart messaging system is also available so hosts and guests can communicate. It is such a successful platform that Holberton School has decided to create a project out of it!

Here, at Holberton School, our assignment is to clone AirBnb. This is one of five assignments and for this first assignment, our goal is to create the console with Python. The console is important for the overall success of the project because it allows us to create, destroy, show, save, and update our BaseModel, a framework that is inheritable by other classes, aka categories.

## How to use the console

The purpose of the console is to be able to create, show, destroy, save, and update all the classes we need/want. It allows us to start and stop processes when we need to. In other words, we can experiment with the file storage to test what we want and don't want. With our console.py file, here is a short guide on how to use our console:

```
AirBnB_clone$ ./console.py
(hbnb) 
(hbnb) 
(hbnb) all
[]
```

To run our console, simply type in "./console.py". The console will then prompt you with "(hbnb)". If you type all without creating a BaseModel (new class), empty brackets should print to the terminal. However, if class names and instances don't exist, errors should always print out. See example below:

```
(hbnb) all Basemodel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel 121212
** no instance found **
```

To create a new User:

```
(hbnb) User.create()
1bab8a19-a0c7-43ef-956b-b3271bdd684f
(hbnb) User.all()
["[User] (1bab8a19-a0c7-43ef-956b-b3271bdd684f) {'updated_at': datetime.datetime(2017, 10, 4, 18, 21, 27, 164392), 'email': '', 'created_at': datetime.datetime(2017, 10, 4, 18, 21, 27, 164366), 'last_name': '', 'password': '', 'id': '1bab8a19-a0c7-43ef-956b-b3271bdd684f', 'first_name': ''}"]
```

The above example is an advanced feature that allows you to create a new User using ".create". However, you can also create a new User with the regular syntax. For example:

```
(hbnb) create User
777f8007-5aeb-4568-8334-807d507edce0
(hbnb) all User
["[User] (777f8007-5aeb-4568-8334-807d507edce0) {'updated_at': datetime.datetime(2017, 10, 4, 18, 21, 59, 114711), 'email': '', 'created_at': datetime.datetime(2017, 10, 4, 18, 21, 59, 114685), 'last_name': '', 'password': '', 'id': '777f8007-5aeb-4568-8334-807d507edce0', 'first_name': ''}", "[User] (1bab8a19-a0c7-43ef-956b-b3271bdd684f) {'updated_at': datetime.datetime(2017, 10, 4, 18, 21, 27, 164392), 'email': '', 'created_at': datetime.datetime(2017, 10, 4, 18, 21, 27, 164366), 'last_name': '', 'password': '', 'id': '1bab8a19-a0c7-43ef-956b-b3271bdd684f', 'first_name': ''}"]
```

To show a specific User, you'll have to use the "show" command. The show command takes in two arguments - name and id. In the examples, User is the name of all users, but their ids are unique. Please see example below:

```
(hbnb) show User 777f8007-5aeb-4568-8334-807d507edce0
[User] (777f8007-5aeb-4568-8334-807d507edce0) {'updated_at': datetime.datetime(2017, 10, 4, 18, 21, 59, 114711), 'email': '', 'created_at': datetime.datetime(2017, 10, 4, 18, 21, 59, 114685), 'last_name': '', 'password': '', 'id': '777f8007-5aeb-4568-8334-807d507edce0', 'first_name': ''}
```

To destroy a User, use the "destroy" command. The command takes in two arguments - name and id. When successfully implemented, destroy will delete the User from file storage. Please see example below:

```
(hbnb) create User
06505348-0c86-4273-b1c2-68eefcbbab0c
(hbnb) show User 06505348-0c86-4273-b1c2-68eefcbbab0c
[User] (06505348-0c86-4273-b1c2-68eefcbbab0c) {'id': '06505348-0c86-4273-b1c2-68eefcbbab0c', 'last_name': '', 'updated_at': datetime.datetime(2017, 10, 4, 19, 18, 40, 976205), 'email': '', 'created_at': datetime.datetime(2017, 10, 4, 19, 18, 40, 976174), 'password': '', 'first_name': ''}
(hbnb) destroy User 06505348-0c86-4273-b1c2-68eefcbbab0c
(hbnb) show User 06505348-0c86-4273-b1c2-68eefcbbab0c
** no instance found **
```

The "all" command prints all string representation of all instances and the "update" command is used to update the User information. In the example below, the first name is updated to "Betty". Everything can be updated except the id, created and updated datetime.

```
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```

## Requirements for Python scripts

```
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version 1.7.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
```

## Requirements for Python unit tests

```
For this project, you will create unit tests, not doctest:

* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start by test_
* Your file organization in the tests folder should be the same as your project: ex: for models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* We strongly encourage you to work together on test cases, so that you don't miss any edge case
```

### Python Functions and Modules Used

Modules Imported:
```
* cmd
* json
* re
* datetime
```

Functions:
```
* id()
* compile()
* findall()
* format()
* getattr()
* hasattr()
* isinstance()
* join()
* len()
* open()
* setattr()
* split()
* str()
* strip()
* super()
```

### Description of File Structure

0. [AUTHORS](AUTHORS) - Name of the author who wrote the simple shell.
1. [README.md](README.md) - Readme file that gives an overview of how to use the console.
2. [console.py](console.py) - A unit accommodating a set of controls for AirBnb clone.

In the models file:

0. [\_\_init\_\_.py](./models/__init__.py) - file that connects File_storage, console, and Basemodel together.
1. [amenity.py](models/amenity.py) - class amenity that inherits from BaseModel
2. [base_model.py](models/base_model.py) - BaseModel framework that other classes inherit from.
3. [city.py](models/city.py) - class city that inherits from BaseModel
4. [place.py](models/place.py) - class place that inherits from BaseModel
5. [review.py](models/review.py) - class review that inherits from BaseModel
6. [state.py](models/state.py) - class state that inherits from BaseModel
7. [user.py](models/user.py) - class user that inherits from BaseModel

In the engine folder:

0. [file_storage.py](models/engine/file_storage.py) - contains file saving storage information

## Authors
* **Gabriel Ochiba**
