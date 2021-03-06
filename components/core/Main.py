#!flask/bin/python

from Server import socketio, server
from ConfReader import check_conf_availability
import logging


def main():
    socketio.run(server, host='0.0.0.0', port=5000)
    # server.run(debug=True)


if __name__ == '__main__':
    logging.basicConfig(filename="./debug-server.log", level=logging.DEBUG)
    logging.warning("INFO: Bassa starting")
    check_conf_availability()
    main()
