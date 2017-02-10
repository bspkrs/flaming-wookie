from pymongo import MongoClient, ReadPreference

options = {
    "maxPoolSize": 10,
    "socketTimeoutMS": 3600000,
    "connectTimeoutMS": 50000,
    "serverSelectionTimeoutMS": 30000,
    "waitQueueTimeoutMS": None,
    "socketKeepAlive": False,
    "read_preference": ReadPreference.PRIMARY, # of the constants in ReadPreference.PRIMARY, PRIMARY_PREFERRED, SECONDARY, SECONDARY_PREFERRED, NEAREST
    "replicaSet": None # String with the name of the replicaSet
}


def getMongoConnection(host, database, port = 27017, user = None, password = None):
    global options
    client = MongoClient(host=host, port=port, document_class=dict, tz_aware=False, connect=True, **options)
    conn = client[database]
    if len(user) and len(password):
        conn.authenticate(user, password)
#    print("Opened connection to: " + uri)
    return conn


def getMongoConnectionFromInfo(dbInfo):
    user = None
    password = None
    if "user" in dbInfo and "pass" in dbInfo:
        user = dbInfo["user"]
        password = dbInfo["pass"]
    return getMongoConnection(dbInfo["host"], dbInfo["db"], dbInfo["port"], user, password)


def closeMongoConnection(conn):
    conn.client.close()
    #print("Closed connection")


def copyCollection(src, tgt, collection, query):
    tgt[collection].insert_many([doc for doc in src[collection].find(query, {'_id': 0})])


def main():
    src_info = {'host': 'localhost', 'db': 'aerialhub', 'port': 27017, 'user': 'aerialhubUser', 'pass': '12345678', 'authdb': 'aerialhub'}
    tgt_info = {'host': '', 'db': '', 'port': 27017, 'user': '', 'pass': '', 'authdb': ''}
    collection_to_copy = 'MemberMPR'
    query = {}
    copyCollection(getMongoConnectionFromInfo(src_info), getMongoConnectionFromInfo(tgt_info), collection_to_copy, query)


if __name__ == '__main__':
    main()