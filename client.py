import socket
import pickle


# Server settings
SERVERPORT = 4000
SERVERADDRESS = "127.0.0.1"

def callServer():

    # Setup socket and connect to server
    clientSocket = socket.socket()
    clientSocket.connect((SERVERADDRESS, SERVERPORT))

    # Message to split
    emptyMessage = " "

    stringMessage = "Look at me!, I have a string!, And another one!"

    # Send the message as a string
    clientSocket.send(stringMessage.encode('utf-8'))

    # Take the raw data from the server and convert it back into a list
    rawData = clientSocket.recv(1024)
    data = pickle.loads(rawData)

    # Print the data and close the server
    print("Returned Data:")
    print(data)
    clientSocket.close()



if __name__ =='__main__':
    callServer()