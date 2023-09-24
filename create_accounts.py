#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 08:02:09 2023

@author: marcelo
"""
import warnings
from RWG_calls_Q323 import RWG_calls
warnings.filterwarnings("ignore", message="Unverified HTTPS request")
RWG = RWG_calls()

host = 'rwg-fqdn'
username = 'admin'
password = 'password'

apiKey = RWG.genApi_Key(host, username, password)
name = apiKey['name']
key = apiKey['api_key']
ID = RWG.getKeyID_ByName(host, name, key)
print('API KEY details:')
print(ID, name, key, '\n')

firstName = 'Sheldon'
lastName = 'Felino'
login = 'sheldon'
password = '1234'
email = 'marcelo.molinari@gmail.com'
account_group = 80
usage_plan = 86
pre_shared_key = '12345678ABCDEFGH'

account = RWG.createAccount(host, firstName, lastName, login, password,
                            email, account_group, usage_plan,
                            pre_shared_key, key)
print('Account ID and login:')
print(account['id'], account['login'])
RWG.destroyApi_Key(host, ID, key)
