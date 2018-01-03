from pymongo import MongoClient

from Web_Craw_RB import RedesB

if __name__ == '__main__':
    client = MongoClient('mongodb://user:password@ds151279.mlab.com:51279/ucuenca')
    db = client.ucuenca

    red = RedesB('http://wwww.heroku.com', 1000000)
    red.run(db)
