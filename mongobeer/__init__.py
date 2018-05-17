"""socket testing utility"""
import logging
from pymongo import MongoClient
from pymongo.errors import  ConnectionFailure
import sys
import time

# pylint: disable=locally-disabled, invalid-name
logger = logging.getLogger('mongobeer')
logging.basicConfig(
    level=logging.DEBUG,
    format='%(process)s %(asctime)-15s %(levelname)7s: %(message)s',
    stream=sys.stdout,
)


class MongobeerException(Exception):
    """mongobeer Base Error"""
    pass


class Mongobeer:
    """ the mongobeer client and server"""

    def __init__(self, args):
        """
        start  client or server
        default to server
        """
        # Create a TCP/IP socket
        try:
            self._client = MongoClient(args.connection_string, maxPoolSize=1)
        except ConnectionFailure as conn_error:
            logger.info("Conection error: {}".format(conn_error))

        self._mongobeer_one(args.collection)

    def _mongobeer_one(self, collection):
        """
        create a client
        :return:
        """
        logger.info("mongobeer: I am in client mode.")
        db = self._client[collection]
        while True:
            db.collection.find_one()
            logger.info("find one")
            time.sleep(5)


if __name__ == "__main__":
    m = Mongobeer()