# This came from a database. Name and phonenumber are
# seperated by a colon

dbRecord = "Fred Flinstone:041234567"
colonPosn = dbRecord.find(":")
print (colonPosn)
name = dbRecord[:colonPosn]
print(name)
phoneNum = dbRecord[colonPosn+1:]
print (phoneNum)