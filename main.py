#!/usr/bin/env python
# coding: utf-8

# In[21]:


import os
import time
from colorama import init, Fore
import paramiko
import json
import time


# In[22]:


green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW
blue = Fore.BLUE
purple = Fore.MAGENTA
reset = Fore.RESET


# In[23]:


def error(mode, string):
    if mode == 'p':
        string = red + string + reset
        print(string)
        return string
    if mode == 'i':
        string = red + string + reset
        opt = input(string)
        return opt
    
def success(mode, string):
    if mode == 'p':
        string = green + string + reset
        print(string)
        return string
    if mode == 'i':
        string = green + string + reset
        opt = input(string)
        return opt

def message(mode, string):
    if mode == 'p':
        string = blue + string + reset
        print(string)
        return string
    if mode == 'i':
        string = blue + string + reset
        opt = input(string)
        return opt


# In[24]:


def is_open(host, usr, passwd):
    client = paramiko.SSHClient()
    
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(host, username=usr, password=passwd, timeout = 5)
        success('p', 'Success: \nusername = {} \npassword = {}'.format(usr, passwd))
        client.close()
        return True
    except paramiko.AuthenticationException:
        error('p', 'Connection refused\nusername = {}\npasswords = {}'.format(usr, passwd))
        return False


# In[25]:


connections = {}
default_file = {'hosts': [], 'usrs': [], 'passwds': []}


# In[26]:


if not os.path.exists('hosts.json'):
    with open('hosts.json', 'w') as f:
        json.dump(default_file, f)
        error('p', 'hosts.json not exists. Creating one...')
        message('p', 'Insert values in hosts.json and restart.')
        exit()
else:
    with open('hosts.json', 'r') as f:
        connections = json.load(f)
        if connections == default_file:
            error('p', 'Insert data in hosts.json')
            exit()
        else:
            for i in connections:
                if len(connections[i]) == 0:
                    error('p', 'Insert {}'.format(i))
                    exit()
                else:
                    message('p', 'Found {} {}'.format(len(connections[i]), i))
            hosts = connections['hosts']
            usrs = connections['usrs']
            passwds = connections['passwds']


# In[27]:


for host in hosts:
    for usr in usrs:
        for passwd in passwds:
            if is_open(host, usr, passwd):
                pass
                time.spleep(1)


# In[ ]:




