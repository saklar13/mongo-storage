import pymongo

DB_NAME = 'test'
COLLECTION_NAME = 'test'
MESSAGE = 'To use program enter:\nstorage-mongo.py --val \
"key1;val1,key2;val2..."'


def main(value):
    doc = {}
    for pair in value.split(','):
        k, v = [x.strip() for x in pair.split(';')]
        doc[k] = v

    client = pymongo.MongoClient()
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    collection.insert_one(doc)


if __name__ == '__main__':
    import sys
    try:
        key, value = sys.argv[1:3]
        if key != '--val':
            raise NameError
    except (IndexError, NameError):
        print(MESSAGE)
        exit()

    main(value)
