__author__ = 'vahricmuhtaryan'

# Load requests module to make web api(HTTP) call
import requests
# Load json module to encode/decode json data
import json
# Import Global Variables
from ns_global import *


def netscaller_login(ns_ip, ns_username, ns_password):
    # login credentials
    login_data = {"login": {"username": ns_username, "password": ns_password}}
    # convert login_data to json
    login_data_json = json.dumps(login_data)
    # header what we will send with credentials to get NITRO_AUTH_TOKEN
    headers_data = {"Content-Type": "application/vnd.com.citrix.netscaler.login+json"}

    istek = requests.post(ns_secure + ns_ip + ns_login_path, verify=False,
                          headers=headers_data, data=login_data_json)
    # veya bu sekilde direk json a convert etmedende gonderebilirsiniz
    # or you can send without convert value to json before
    #                  json={"login": {"username": "nsroot", "password": "nsroot"}}, headers=headers)

    # Test Gorelim Ne Donuyor
    # print istek.headers

    # Token i dondurelim
    return istek.cookies['NITRO_AUTH_TOKEN']


def netscaller_get_servers(ns_ip, netscaller_token_def):
    # Kullanici adi ve sifre vermeden Netscaller a login olmak icin
    headers_data = {"Cookie": "NITRO_AUTH_TOKEN=" + netscaller_token_def}

    # Tum Sunucu Listesini Alalim
    istek = requests.get(ns_secure + ns_ip + ns_server_all, verify=False,
                         headers=headers_data)

    # return istek

    # Simdi tum server tanimlarini cekelim
    # HTTP request yapip bunu json() ile pythin dictionary e cevirelim
    get_list_of_servers = istek.json()

    # Birden fazla deger donebileceginden bir liste yapalim
    liste = []
    # Server key i bize gerekli bilgleri verecek , server key in value su array
    for sunucular in get_list_of_servers['server']:
        for sunucubilgileri in sunucular:
            if sunucubilgileri == "name":
                liste.append(sunucular[sunucubilgileri])
                # return sunucular[sunucubilgileri]
    return liste


def netscaller_create_server(ns_ip, netscaller_token_def, serveradi, serveripadresi):

    # Kullanici adi ve sifre vermeden Netscaller a login olmak icin
    headers_data = {"Cookie": "NITRO_AUTH_TOKEN=" + netscaller_token_def,
                    "Content-Type":"application/json"}

    # Sunucu Yaratmak Icin Payload Olusturuyoruz
    create_server_data = {
                            "server":
                            {
                                "name": serveradi,
                                "IPAddress": serveripadresi
                            }
                          }
    print create_server_data
    create_server_data_json = json.dumps(create_server_data)
    print create_server_data_json

    istek = requests.post(ns_secure + ns_ip + ns_server_all, verify=False,
                          headers=headers_data, data=create_server_data_json)
    print istek.url
    return istek