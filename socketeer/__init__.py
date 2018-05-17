"""socket testing utility"""
import logging
import sys
import socket

# pylint: disable=locally-disabled, invalid-name
logger = logging.getLogger('socketeer')
logging.basicConfig(
    level=logging.DEBUG,
    format='%(process)s %(asctime)-15s %(levelname)7s: %(message)s',
    stream=sys.stdout,
)


class SocketeerException(Exception):
    """Socketeer Base Error"""
    pass


class Socketeer:
    """ the socketeer client and server"""

    def __init__(self, args):
        """
        start  client or server
        default to server
        """
        # Create a TCP/IP socket
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if args.mode == "client":
            self._socketeer_client(args.server_name, args.port)
        else:
            self._socketeer_server(args.server_name, args.port)

    def _socketeer_server(self, server_name, port=80):
        """
        create a server
        :return:
        """
        logger.info("Socketeer: I am in server mode.")
        self._sock.bind((server_name, int(port)))
        self._sock.listen(1)

        while True:
            logger.info('Waiting for a connection')
            connection, client_address = self._sock.accept()
            try:
                logger.info("Client connected:{}".format(client_address))
                while True:
                    try:
                        data = connection.recv(16)
                    except ConnectionResetError as connection_error:
                        logger.debug("The network hates me {}!".format(connection_error))
                        connection, client_address = self._sock.accept()
                    logger.info('Received "%s"' % data)
                    if data:
                        connection.sendall(data)
                    else:
                        break
            finally:
                connection.close()

    def _socketeer_client(self, server_name, port=80):
        """
        create a client
        :return:
        """
        logger.info("Socketeer: I am in client mode.")
        self._sock.connect((server_name, int(port)))
        message = 'This is your captain speaking, network turbulence expected'
        logger.info("Sending: %s" % message)
        while True:
            try:
                self._sock.sendall(message.encode('utf-8'))
                amount_received = 0
                amount_expected = len(message)
                while amount_received < amount_expected:
                    data = self._sock.recv(16)
                    amount_received += len(data)
                    logger.info("Received: %s" % data)
            except:
                logger.debug("Something went boom!")
        self._sock.close()


if __name__ == "__main__":
    s = Socketeer()