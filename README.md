# diy-shell-tools
Welcome to `diy-shell-tools`, a project where you can build and customise your own command-line utilities!
    
## Table of contents

+ [About](#about)
+ [Built With](#built-with)
+ [Getting Started](#getting-started)
+ [tools](#tools)
+ [Inspiration](#inspiration)

## About
This project aims to provide a command line interface for running customised shell commands, 
inspiring by [Coding Challenges by John Crickett](https://codingchallenges.fyi/challenges).
The main purpose of the project is to build several shell commands like wc, grep, cat, etc
using python and following the best practices of software development and TDD.

## Built With

- Python (3.10)

## Getting Started
<details>

<summary> To initialize local environment </summary>

```
pip install virtualenv
virtualenv .penv --python=python3.10
. .penv/bin/activate
```
</details>
<details>
<summary>To run the project, find the details below</summary>

- The project main script is located at [run_command.py](src/main/run_command.py)
- Usage:
```
Usage: python run_command.py <command> -- [<options>] <input_file>
```
Note: Argsparse expects to have `--` to separate the command and the options from the input file.

</details>
<details>
<summary> To run formatter </summary>

```
tox -e formatter
```
</details>
<details>
<summary> To run lint </summary>

```
tox -e lint
```
</details>
<details>
<summary> To run the tests </summary>

```
tox
```
</details>

## Tools
To read more about the tools, click on the links below:
- [ccwc](src/main/tools/ccwc/readme.md)

## Inspiration
- [Coding Challenges by John Crickett](https://codingchallenges.fyi/challenges)



