from . import models
import sqlite3


# lineid = 'asdf4567'
# name = 'testlinename'
# phone = '001191'
# address = 'Ratchaburi'


def setSellerAddress(lineid='dlineid', name='dname', phone='dphone', address='daddress'):
    seller = models.Seller(lineId=lineid, name=name, phone=phone, address=address)
    seller.save()


def getNearbyAddress():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("select name, address from getridchApp_seller")
    data = c.fetchall()
    for row in data:
        result = result + row[1] + '@' + row[2]
    return result
