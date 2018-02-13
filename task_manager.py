# using paramiko, ssh into clients to exec shell commands
import paramiko
import json
from threading import Thread, Lock

def run_tasks(client, queue, lock):
    # loop over queue
    while len(queue) > 0:
        # grab the next element
        with lock:
            task = queue.pop()
        task = process(task)

        stdin,stdout,stderr = client.exec_command(task)
        print("EXECUTED: ", stdout.readlines())

def process(task):
    # do something to build it from a json object
    # right now tasks are just string forms of commands
    return task

def build_clients(config):
    ssh_clients = [] 
    for client in config:
        print(client)
        ssh_client = paramiko.SSHClient()
        ssh_client.load_system_host_keys()
        ssh_client.connect(hostname=client['hostname'], 
                           username=client['username'], 
                           password=client['password'])       # and other things as needed
        ssh_clients.append(ssh_client)
    return ssh_clients

if __name__ == '__main__':
    # read config file for clients
    clients_cfg = json.load(open("clients.json"))

    # list of ssh clients instead
    clients = build_clients(clients_cfg)
    print("connected to clients")

    # read task queue file
    queue = json.load(open("queue.json"))
    print(queue)

    # create a lock for the queue to prevent race conditions
    lock = Lock()

    # create a list to store all the threads
    threads = []

    # start each client to execute tasks from the queue
    for client in clients:
        threads.append(Thread(target=run_tasks, args=(client, queue, lock)))

    # start all threads, and then wait for them to all finish
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    print("finished all work")

