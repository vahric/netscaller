__author__ = 'vahricmuhtaryan'

from netscaller1 import *

#Netscaller login olup token i alalim

netscaller_token = netscaller_login("10.111.34.220","nsroot","nsroot")


#netscaller_sunucular = netscaller_get_servers("10.111.34.220",netscaller_token)

"""
#Listelemek icin donguye alalim
for i in netscaller_sunucular:
    print i
"""

netscaller_create_server("10.111.34.220",netscaller_token,"vahric02","10.7.7.7")




