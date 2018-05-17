# Socketeer

#Virtualenv

virtualenv -p python3 env

source env/bin/activate

./run.py -m <client|server> -p <port number> -s <server_name> 


#Fun and profit

    Usage: run.py [-h] [-m MODE] [-p PORT] [-s SERVER_NAME]
    
    optional arguments:
      -h, --help            show this help message and exit
      -m MODE, --mode MODE  Client or Server
      -p PORT, --port PORT  Change the default port
      -s SERVER_NAME, --server_name SERVER_NAME
                            Server name
