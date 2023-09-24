#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 08:02:09 2023

@author: marcelo
"""
import warnings
import qrcode
from PIL import Image, ImageFont, ImageDraw
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

accounts = RWG.getAccounts(host, key)
wlans = RWG.getWlans(host, key)

print('WLANs:')
for wlan in wlans['results']:
    print(wlan['ssid'], wlan['authentication'], )

print()
print('Accounts:')
for account in accounts['results']:
    print(account['login'], account['pre_shared_key'])

print()
print('SSID and DPSK:')

for wlan in wlans['results']:
    if wlan['authentication'] == 'dpsk':
        for account in accounts['results']:
            print(wlan['ssid'], account['pre_shared_key'])
            background = Image.new('RGBA', (550, 650), (255, 255, 255, 255))
            draw = ImageDraw.Draw(background)
            font = ImageFont.truetype('Tahoma.ttf', 24)
            draw.text((105, 580), wlan['ssid'] + ' ' +
                      account['pre_shared_key'], font=font, fill=(0, 0, 0))
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=15,
                border=4,
            )
            qr.add_data("WIFI:S:" + wlan['ssid'] + ";T:WPA2;P:" +
                        account['pre_shared_key'] + ";;")
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(wlan['ssid'] + ' ' +
                     account['pre_shared_key'] + '.png')
            background.paste(img, (0, 30))
            background.show()

RWG.destroyApi_Key(host, ID, key)
