import pymongo
import prov.model
import datetime
import uuid

exec(open('../pymongo_dm.py').read())

client = pymongo.MongoClient()
repo = client.repo

f = open("auth.json").read()
auth = loads(f)
user = auth['user']
repo.authenticate(user, user)


startTime = datetime.datetime.now()

##########




###########

endTime = datetime.datetime.now()

repo.logout()