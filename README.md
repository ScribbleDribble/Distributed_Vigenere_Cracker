# Distributed Vigenere Crack

This project utilizes a cluster of machines to crack the vigenere cipher. 
This approach yields around a 50% reduction on cracking time with two servers and one client.

## Dependencies
1. Virtualenv
2. Dispy
3. psutil
4. numpy

2x Raspberry Pi 4B's were used (as servers) alongside one desktop machine (client). 

## Installation 

1 Install virtualenv and then create a virtual environment.

`pip3 install virtualenv`

`python3 -m virtualenv venv_name`

2 Pull repo and install the other dependencies within the virtual environment.

Within venv_name/

`source bin/activate`

`git pull origin master`

`./install`


#### Server

2 Run the server shell script.

`git pull origin master`

`cd server/`

`./start_dispynode.sh`

#### Client

3 Pull repository code and enter into the client directory.

`cd client/`

4 Run controller.py inputting your ciphertext and key length

`python3 controller.py <ciphertext> <key length>`

Info on the additional network configurations needed to be made can be found at: https://projects.raspberrypi.org/en/projects/build-an-octapi/4

## Results
Single node 

![Alt text](images/single_node.png)
----
Multi node

![Alt text](images/multi_node.png)

