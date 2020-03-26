import json
import datetime
from access_token.AccessTokenURI import getAccessToken

class Info(object):
    def __init__(self, access_token: str, time:str):
        self.access_token = access_token
        self.time = time
    def toJson(self):
        return json.dumps(self.__dict__)


def readInfo():
    try:
        with open('access_token/info.json') as info:
            data = json.load(info)
        return json.loads(data)
    except ValueError:
        return None

def updateInfo(info: Info):
    with open('access_token/info.json', 'w') as json_file:
        json.dump(info.toJson(), json_file)

def generateNewAccessToken():
    old = readInfo()
    if ( old is not None ):
        datetime_obj = datetime.datetime.strptime(old['time'], '%m/%d/%Y')
        newdate = datetime.date.today()
        if(newdate == datetime_obj.date()):
            info = readInfo()
            return info['access_token']
    access = getAccessToken()
    test  = datetime.datetime.now().strftime("%m/%d/%Y")
    info = Info(access, test)
    updateInfo(info)
    return access

def regenerateAccessToken():
    access = getAccessToken()
    test = datetime.datetime.now().strftime("%m/%d/%Y")
    info = Info(access, test)
    updateInfo(info)
    return
