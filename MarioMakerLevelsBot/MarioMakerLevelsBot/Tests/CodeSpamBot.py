import sys
import time
import socket
import random
import threading

from PySide import QtCore

class ChatSpammer(QtCore.QObject):
    """Connects to a Twitch chat channel and sends random Mario Maker-like codes to it.

    Currently assumes the server is the standard Twitch chat.
    """

    HOST = "irc.twitch.tv" # standard Twitch chat server address
    PORT = 6667 # standard Twitch chat server port

    wrong_password = QtCore.Signal()
    connection_failed = QtCore.Signal()
    connection_successful = QtCore.Signal(str)

    def __init__(self, name, oauth, channel, parent=None):
        """Create the ChatListener object.
        """
        super().__init__()
        self.name = name
        self.oauth = oauth
        self.channel = channel
        self.parent = parent
        self.callbacks = []
        self.thread = threading.Thread(target=self._main_listener)
        self.thread.setDaemon(True)

        self.write_thread = threading.Thread(target=self._main_writer)
        self.thread.setDaemon(True)

    def start(self):
        """Start listening to the Twitch chat.

        Runs a separate thread that connects to the Twitch chat, reads messages
        and calls the callbacks for each message.
        """
        try:
            self.thread.start()
            time.sleep(2) # Should wait for connexion to be successful, but let's suppose it'll work after 2 seconds
            self.write_thread.start()
        except RuntimeError: # already started, do nothing
            pass

    def stop(self):
        """Stop listening to the Twitch chat.
        """
        # Stop the current listening thread and create a new one
        try:
            self.thread._stop()
            self.write_thread._stop()
        except:
            pass

        self.thread = threading.Thread(target=self._main)
        self.thread.setDaemon(True)

        self.write_thread = threading.Thread(target=self._main_writer)
        self.thread.setDaemon(True)

    def isAlive(self):
        """Return True if listening is active, False otherwise)."""
        return self.thread.isAlive() and self.write_thread.isAlive()

    def add_callback(self, callback):
        """Add a callback to give messages information to.

        The callback prototype must be compatible with:
        callback(channel, name, tags, message)"""
        if(callback not in self.callbacks):
            self.callbacks.append(callback)

    def remove_callback(self, callback):
        """Remove a callback from the list of callbacks."""
        try:
            self.callbacks.remove(callback)
        except:
            pass

    def reset_callbacks(self):
        """Remove all callbacks"""
        self.callbacks = []


    def _connect(self):
        """Create the connection with Twitch chat server (socket) and initialize the IRC protocol
        """
        try:
            self.socket.close() # closing old socket if it exists
        except:
            pass

        self.socket = socket.socket()

        try:
            self.socket.connect((self.HOST, self.PORT))
        except ConnectionAbortedError:
            self.wrong_password.emit()
            return False
        except OSError as e:
            if(e.winerror == 10056): # Already connected
                return True
            elif(e.winerror == 10053): # Connection aborted, may be due to existing connection
                return False

        # Sending password (Twitch oauth) first
        self.socket.send("PASS {0}\r\n".format(self.oauth).encode())
        # Then the rest of the info
        self.socket.send("NICK {0}\r\n".format(self.name.lower()).encode())
        self.socket.send("USER {0} {1} bla :{2}\r\n".format(
            self.name, self.HOST, self.name + " Bot").encode())

        readbuffer = self.socket.recv(1024).decode()

        if(readbuffer == ""): # Couldn't read anything, connection closed (empty pass?)
            self.wrong_password.emit()
            return False

        # Requesting tags
        self.socket.send("CAP REQ :twitch.tv/tags\r\n".encode())

        # Joining the channel.
        self.socket.send("JOIN #{0}\r\n".format(self.channel.lower().replace("#", "")).encode())

        return True

    def _main_listener(self):
        """Main loop of the listener : connects to the chat and reads
        everything sent by the server.
        """

        if(not self._connect()): # Connection to the Twitch server failed
            return

        readbuffer = "" # Empty buffer

        while(True): # Eternal loop to listen the messages

            try: # Receiving data from IRC
                readbuffer = readbuffer + self.socket.recv(1024).decode()
            except: # Error while reading the socket, try reconnecting
                if(self._connect()): # Reconnecting worked
                    continue
                else: # Reconnecting didn't work
                    break # Getting out of the loop stops the thread

            print(readbuffer.encode(encoding=sys.stdout.encoding, errors='replace').decode())

            if(readbuffer == ""): # Didn't receive anything, connection may be closed
                time.sleep(1) # Waiting a second not to flood with reconnections
                self._connect()
                continue

            temp = str.split(readbuffer, "\r\n")
            readbuffer = temp.pop() # The remainder may be an unfinished message
            
            for line in temp:
                line = str.split(line, " ")

                # IRC checks connectiond with ping.
                # Every ping has to be replied to with a Pong.
                if(line[0] == "PING"):
                    self.socket.send("PONG {0}\r\n".format(line[1]).encode())

    def _main_writer(self):
        """Main loop of the writer: sends random codes to the chat.
        """

        if(not self.socket): # Basic check to see if the socket's there
            return

        while(1):
            code = ("{:04x} " * 4).format(random.randint(0, 0xFFFF),
                                          random.randint(0, 0xFFFF),
                                          random.randint(0, 0xFFFF),
                                          random.randint(0, 0xFFFF)).upper()
            msg = "PRIVMSG #{channel} :{message}\r\n".format(channel=self.channel, message=code)
            self.socket.send(msg.encode())
            time.sleep(5)


if(__name__ == "__main__"):
    name = input("Name? ")
    oauth = input("OAuth? ")
    channel = input("Channel? ")
    bot = ChatSpammer(name, oauth, channel)
    bot.start()
    while(bot.isAlive()):
        time.sleep(10)
