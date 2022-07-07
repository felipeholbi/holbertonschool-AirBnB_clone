# The Console 🔧

![Screenshot from 2022-07-06 21-57-10](https://user-images.githubusercontent.com/98775024/177681066-d4a85ac7-d5b1-4d43-9475-4355494bdfc7.png)


## Description. 📝

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

### Fucionalities. 🧰

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Files. 🗂️

| Name | Description |
| ------------------------------ | -------------------------------------------- |
| AUTHORS | Contributors in this repository.|
| console.py | Command line interpreter. file. |
| models/ | Package with the base classes. |
| amenity.py | Class Amenity. |
| base_model.py | defines all common attributes/methods for other classes. |
| city.py | Class City. |
| place.py | Class Place. |
| review.py | Class Review. |
| state.py | Class State. |
| user.py | Class User. |
| models/engine | Package with in storage file. |
| file_storage.py | Class FileStorage. serializes/deserializes instances to a JSON file. |
| tests/ | Directory with class tests. |
|  |  |
| | |

## Console description. 📋

* ```quit``` - exits console
* ```create``` - Creates a new instance of ```BaseModel```, saves it (to the JSON file) and prints the id.

* ```destroy``` - Deletes an instance based on the class name and id (save the change into the JSON file).
* ```show``` - Prints the string representation of an instance based on the class name and id.
* ```all``` - Prints all string representation of all instances based or not on the class name.
* ```update``` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).


## Requeriments. ⚙️

All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)

## Install. 💾

* Clone https://github.com/alejuran/holbertonschool-    AirBnB_clone.git


## Usage. 💿

* Run the interactive mode: ```./console.py```
* Run the non-interactive mode: ```echo "help" | ./console.py```


### Examples. 🖇️

* **Run console in interactive mode:**

```$ 
./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

* **Run console in Non-interactive mode:**

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

## Authors.

<a href = 'https://www.github.com/Crisgrva'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/github.svg"/></a> [@alejuran](https://github.com/alejuran) | [@felipeholbi](https://github.com/felipeholbi)

<a href = 'https://www.twitter.com/crisgrvc'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/twitter.svg"/></a> [@alejuran](https://twitter.com/alejuran) | [@FelipelosRg](https://twitter.com/@FelipelosRg)
