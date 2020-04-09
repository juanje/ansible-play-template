# Playbook template

This is just a simple template for start an [Ansible](https://github.com/ansible/ansible/) playbook.
The aim of this template is to have the minimum functional playbook so you can start to build your own.

The template is configured to run a simple task (install git) and to test if the task has done its job correctly, by using [molecule](https://molecule.readthedocs.io).

**Molecule** is a testing framework for **Ansible**. It also has been configured to use [Testinfra](https://testinfra.readthedocs.io) for the actual tests and [Docker](https://docs.docker.com/get-started/overview/) to run the instances where the tasks and tests will run.

All of this can be changed, but I think it's pretty straightforward configuration to start and it's working **out of the box** here.

## Use it

In order to start with this playbook and use all its power you'll need to install a few things:
* **Ansible**
* **Docker**
* **Molecule**
* **Pytest**
* **Testinfra**
* **Pylint**
* **flake8**

You can disable the linting and avoid installing **pylint** and **flake8**, but I don't recommend it. It's always better to code with style ;-)

If you've **Python** and **Pip** (Python package manager) installed you can install most of this by doing:
```
pip install -r requirements.txt
```

Once you have all the dependencies installed you can play with molecule, to see that everything is OK.
First, let's see the instances we have configured and their status:
```
$ molecule list
Instance Name  Driver Name  Provisioner Name  Scenario Name  Created  Converged
-------------  -----------  ----------------  -------------  -------  -----------
ubuntu1804     docker       ansible           default        false    false
```

Now, let's runs the Ansible tasks and the tests:
```
$ molecule test
```

This should run all the steps that molecule has configured:
* **Lint** (lint all the Ansible files and Python tests)
* **Create** (the instance, the Docker container)
* **Prepare** (make sure Python is installed)
* **Converge** (provision the instance with the Ansible tasks)
* **Verify** (run the **testinfra** tests)
* **Destroy** (stop and remove the Docker container)

## Structure

This is the minimal structure I've found to create a playbook with molecule's tests. You can add more files and directories as you need, but with the current structure you can run the tasks and the tests with no changes.

```
├── hosts
├── LICENSE
├── molecule
│   └── default
│       ├── converge.yml
│       ├── molecule.yml
│       ├── prepare.yml
│       └── tests
│           ├── conftest.py
│           └── test_default.py
├── playbook.yml
└── README.md
```

The important files (the one you want to start editing) are these two:
```
├── molecule
│   └── default
│       └── tests
│           └── test_default.py
├── playbook.yml
```
* `playbook.yml` -> Where you're going to puts your tasks.
* `test_default.py` -> Where you're going to put your tests.

Right now this is configured to run the **tasks** and **tests** on a **Docker** image of **Ubuntu 18.04**. But if can be changed at the file `molecule.yml`:
```
├── molecule
│   └── default
│       ├── molecule.yml

```

## Testing

For the tests you can use different frameworks (Ansible, InSpec, Goss, TestInfra...), but I've configured the project to use **TestInfra**, which is a extension of Pytest to test systems (servers and such).

As an example, there is a simple test that checks if a specific binary file is in the correct place in the system. I think this is a better test than check for specific package to be installed because that way you can be sure that you have that binary available, no matter what distribution you are at or what method you used to install it.

For me, create tests for **playbooks**, **roles** or **collections** should assure some requirements and allow us to **refactor** or change our plays and tasks safely.

In order to test the plays you need to *create* and *converge* the instance, then you can *verify* (run the tests). You can just run `molecule test` each time, but it'll *destroy* and *create* the instance each time, so it takes some time.

I recommend you to run that command once in a while, but you can run just `molecule converge` to run the tasks and the run `molecule verify` each time you make a change.

```
$ molecule converge
.... (It'll run the Ansible tasks)
# Do some changes

$ molecule verify
... (It'll run the tests and see the results)
```

But don't forget to run `molecule converge` to run the Ansible tasks each time you change them, or they won't be reflected at the instance.

## License

|                |                                           |
| -------------- | ----------------------------------------- |
| **Author:**    | Juanje Ojeda (<juanje.ojeda@gmail.com>)   |
| **Copyright:** | Copyright (c) 2020 Juanje Ojeda           |
| **License:**   | Apache License, Version 2.0               |

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
