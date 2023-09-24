#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 08:02:09 2023.

@author: marcelo
"""

import requests


class RWG_calls:

    def genApi_Key(self, host, username, password):
        url = 'https://' + host + '/api/login'
        body = {'username': username, 'password': password}
        r = requests.post(url, json=body, verify=False)
        return r.json()

    def getApi_Keys(self, host, api_key):
        url = 'https://' + host + '/api/api_keys/' + '?api_key=' + api_key
        r = requests.get(url, verify=False)
        return r.json()

    def getKeyID_ByName(self, host, name, api_key):
        url = 'https://' + host + '/api/api_keys/' + '?api_key=' + api_key
        keyList = requests.get(url, verify=False).json()['results']
        for key in keyList:
            if key['name'] == name:
                return key['id']
        return

    def destroyApi_Key(self, host, ID, api_key):
        url = 'https://' + host + '/api/api_keys/' + str(ID) + '?api_key=' + \
            api_key
        requests.delete(url, verify=False)
        return

    def getAccounts(self, host, api_key):
        url = 'https://' + host + '/api/accounts/' + '?api_key=' + api_key
        r = requests.get(url, verify=False)
        return r.json()

    def getWlans(self, host, api_key):
        url = 'https://' + host + '/api/wlans/' + '?api_key=' + api_key
        r = requests.get(url, verify=False)
        return r.json()

    def createAccount(self, host, firstName, lastName, login, password, email,
                      account_group, usage_plan, pre_shared_key, api_key):
        url = 'https://' + host + '/api/accounts' + '?api_key=' + api_key
        body = {
            'first_name': firstName,
            'last_name': lastName,
            'login': login,
            'password': password,
            'password_confirmation': password,
            'email': email,
            'account_group': account_group,
            'usage_plan': usage_plan,
            'pre_shared_key': pre_shared_key,
            'unlimited_devices': True,
            'unlimited_usage_minutes': True,
            'unlimited_usage_mb_up': True,
            'unlimited_usage_mb_down': True,
            'no_usage_expiration': True,
            'automatic_login': True
            }
        r = requests.post(url, json=body, verify=False)
        return r.json()
