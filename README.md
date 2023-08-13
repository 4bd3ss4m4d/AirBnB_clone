<p align="center">
  <img src="https://github.com/4bd3ss4m4d/AirBnB_clone/blob/main/media/airbnb_project.png" alt="hbnb logo">
</p>

<h1 align="center">AirBnB Clone - Command Line Interface (CLI)</h1>
<p align="center">ALX Africa</p>

## Description of the Project

Welcome to our AirBnB Clone project! This is the initial step towards creating a full-fledged web application inspired by the renowned Airbnb platform. In this project, we've developed a powerful Command Line Interface (CLI) to manage AirBnB objects efficiently.

### Command Line Interface (CLI) - Bridging Vision and Execution

Our Command Line Interface (CLI) serves as the nucleus of interaction with the AirBnB Clone project. It's a dynamic tool that facilitates the seamless communication between developers and the application's core functionalities. At its heart, the CLI empowers developers to effortlessly manage and manipulate AirBnB objects through a series of intuitive commands.

### Streamlining Object Management and Interaction

The CLI isn't just a mere gateway to the application; it's a powerful mechanism that empowers developers to perform a wide array of operations on AirBnB objects:

1. **Creating Objects**: With a single command, developers can instantiate new instances of various AirBnB objects. This initial step lays the foundation for populating our application with data.

2. **Retrieving Objects**: Our CLI is equipped with the capability to retrieve specific objects based on user-defined criteria. This functionality is pivotal for developing advanced search and data retrieval features.

3. **Object Manipulation**: Beyond retrieval, developers can use the CLI to perform an array of operations on objects. From counting and computing statistics to applying updates, the CLI is a versatile toolkit for data manipulation.

4. **Attribute Updation**: The CLI seamlessly facilitates the updating of object attributes. This dynamic feature ensures that our application's data remains current and accurate.

5. **Efficient Object Management**: In situations where objects are no longer needed, the CLI simplifies the process of object destruction, ensuring efficient data management.

## Description of the Command Interpreter

### How to Start the Command Interpreter

The Command Interpreter for the AirBnB project can be initiated using both interactive and non-interactive modes.

#### Interactive Mode

Interactive mode allows you to directly interact with the Command Interpreter within the terminal. To start the interpreter in interactive mode:

1. Open your terminal.
2. Navigate to the root directory of the project.
3. Run the `console.py` script:
```
$ ./console.py
```
4. You will enter the interactive mode prompt indicated by `(hbnb)`.
5. Begin typing your commands, and the interpreter will process and respond to each one.

**Examples:**
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

#### Non-Interactive Mode

Non-interactive mode enables you to run the interpreter with predefined commands provided via standard input. To start the interpreter in non-interactive mode:

1. Open your terminal.
2. Navigate to the root directory of the project.
3. Use the `echo` command to pipe commands into the `console.py` script:
```
$ echo "help" | ./console.py
```
4. The interpreter will execute the provided command(s) and display the results.

**Examples:**
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Console Commands

The AirBnb Interpreter provides several commands for managing instances of classes. These commands allow you to create, show, update, delete, and list instances in a convenient and efficient way.

* ### `create`

The `create` command creates a new instance of a specified class and saves it to the JSON file. It also prints the ID of the newly created instance.

Usage:
$ create <class name>

The `create` command creates a new instance of a specified class and saves it to the JSON file. It also prints the ID of the newly created instance.

Usage:
```
$ create <class name>
```

Example:
```
$ ./console.py
(hbnb) create BaseModel
4d2b8970-e978-4cba-94b3-4e403c5f2443
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.4d2b8970-e978-4cba-94b3-4e403c5f2443": {"id": "4d2b8970-e978-4cba-94b3-4e403c5f2443", "created_at": "2023-08-13T03:53:34.855027", "updated_at": "2023-08-13T03:53:34.855161", "__class__": "BaseModel"}}
```

* ### `show`

The `show` command prints the string representation of an instance based on the class name and ID.

Usage:
```$ show <class> <id>``` or ```$ <class>.show(<id>)```

Example:
```
$ ./console.py
(hbnb) show BaseModel 4d2b8970-e978-4cba-94b3-4e403c5f2443
[BaseModel] (4d2b8970-e978-4cba-94b3-4e403c5f2443) {'id': '4d2b8970-e978-4cba-94b3-4e403c5f2443', 'created_at': datetime.datetime(2023, 8, 13, 3, 53, 34, 855027), 'updated_at': datetime.datetime(2023, 8, 13, 3, 53, 34, 855161)}
(hbnb) BaseModel.show(4d2b8970-e978-4cba-94b3-4e403c5f2443)
[BaseModel] (4d2b8970-e978-4cba-94b3-4e403c5f2443) {'id': '4d2b8970-e978-4cba-94b3-4e403c5f2443', 'created_at': datetime.datetime(2023, 8, 13, 3, 53, 34, 855027), 'updated_at': datetime.datetime(2023, 8, 13, 3, 53, 34, 855161)}
(hbnb)
```

* ### `destroy`

The `destroy` command deletes an instance based on the class name and ID and saves the change to the JSON file.

Usage:
```$ destroy <class> <id>``` or ```$ <class>.destroy(<id>)```

Example:
```
$ ./console.py
(hbnb) destroy BaseModel 4d2b8970-e978-4cba-94b3-4e403c5f2443
(hbnb)
```

* ### `all`

The `all` command prints the string representation of all instances based on the specified class name. If no class name is provided, it prints all instances of all classes.

Usage:
```$ all or all <class>``` or ```$ <class>.all()```

Example:
```
$ ./console.py
(hbnb) all User
["[User] (c5d1ecca-e2d9-46dd-b9d2-51ad37afd162) {'id': 'c5d1ecca-e2d9-46dd-b9d2-51ad37afd162', 'created_at': datetime.datetime(2023, 8, 11, 7, 48, 22, 544915), 'updated_at': datetime.datetime(2023, 8, 11, 7, 48, 22, 544966), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (8047c3c2-f895-4873-a386-384eb2348f43) {'id': '8047c3c2-f895-4873-a386-384eb2348f43', 'created_at': datetime.datetime(2023, 8, 11, 7, 48, 22, 554582), 'updated_at': datetime.datetime(2023, 8, 11, 7, 48, 22, 554605), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}"]
(hbnb) User.all()
["[User] (c5d1ecca-e2d9-46dd-b9d2-51ad37afd162) {'id': 'c5d1ecca-e2d9-46dd-b9d2-51ad37afd162', 'created_at': datetime.datetime(2023, 8, 11, 7, 48, 22, 544915), 'updated_at': datetime.datetime(2023, 8, 11, 7, 48, 22, 544966), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (8047c3c2-f895-4873-a386-384eb2348f43) {'id': '8047c3c2-f895-4873-a386-384eb2348f43', 'created_at': datetime.datetime(2023, 8, 11, 7, 48, 22, 554582), 'updated_at': datetime.datetime(2023, 8, 11, 7, 48, 22, 554605), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}"]
(hbnb)
```

* ### `update`

The `update` command updates an instance's attribute based on the class name and ID. Only one attribute can be updated at a time.

Usage:
```$ update <class> <id> <attribute name> "<attribute value>"``` or ```$ <class>.update(<id>, <attribute name>, <attribute value>)``` or ```$ <class>.update( <id>, <attribute dictionary>)```

Example:
```
$ ./console.py
(hbnb) create User
7149a4e9-273b-4256-b001-fb37174defb4
(hbnb) update User 7149a4e9-273b-4256-b001-fb37174defb4 first_name "Abdessamad"
(hbnb) show User 7149a4e9-273b-4256-b001-fb37174defb4
[User] (7149a4e9-273b-4256-b001-fb37174defb4) {'id': '7149a4e9-273b-4256-b001-fb37174defb4', 'created_at': datetime.datetime(2023, 8, 13, 4, 16, 54, 718478), 'updated_at': datetime.datetime(2023, 8, 13, 4, 16, 54, 727976), 'first_name': 'Abdessamad'}
(hbnb)
```

* ### `count`

The `count` command retrieves the number of instances of a given class.`

Usage:
```$ count <class>``` or ```$ <class>.count()```

Example:
```
(hbnb) create City
9abec432-3890-419b-ae1c-f158121880e5
(hbnb) create City
0247101c-888f-493b-9d26-af3cd05f80a8
(hbnb) create City
84ab6dec-01a2-417c-a6cc-0f48b28293b9
(hbnb) count City
3
(hbnb) City.count()
3
(hbnb)
```

## Testing

The Airbnb project's functionality is thoroughly tested using unit tests, which are defined in the `tests` folder. These tests ensure the correctness and reliability of various components of the project.

### Running Tests

To run the entire test suite simultaneously, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the root directory of the project.
3. Execute the following command:

```
$ python3 -m unittest -m discover tests
```
This command will automatically discover and execute all the unit tests defined in the tests folder, providing you with a comprehensive overview of the project's functionality.

### Running Specific Tests

If you wish to run a specific test file, you can do so by specifying the path to the test file. For example, to run the tests for the console functionality, execute the following command:

```
$ python3 -m unittest -m tests.test_console
```
This command will execute the unit tests defined in the test_console.py file.

### Authors

* **Abdessamad HADDOUCHE** <[4bd3ss4m4d](https://github.com/4bd3ss4m4d)>
* **Imrane ALI LAFKIH** <[imranelaf](https://github.com/imranelaf)>

