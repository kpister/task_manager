# Task Manager

clients.json contains a list of client objects. Each object has a hostname, username, password.

We can add additional properties in the future as needed.

queue.json contains a list of shell commands which should be executed. These are not buildable right now, but in the future they will be objects as well.

task\_manager.py is annotated well within itself.

## Usage:

Run `pip install paramiko` to setup the environment.

Update clients.json with your available computers.

Update queue.json with the work you want distributed.

Run `python task_manager.py`

## Work to be done:

[ ] - Error handling

[ ] - Allow more config options on clients

[ ] - Allow more config options on jobs

[ ] - More testing

# Work done for Calit2 by Kaiser Pister 2018
