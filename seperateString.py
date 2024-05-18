import socket
import pickle


# Server settings
SERVERPORT = 4000
SERVERADDRESS = "127.0.0.1"


# Main function
def main():

    # Setup socket
    msSocket = socket.socket()
    msSocket.bind((SERVERADDRESS, SERVERPORT))
    msSocket.listen(0)
    print(f"Listening to {SERVERADDRESS}:{SERVERPORT}")

    # Main socket loop
    while True:

        # Accept socket connection
        returnedClient, address = msSocket.accept()
        print(f"Accepted connection from: {address[0]}:{address[1]}")

        # Decode string
        sentString = returnedClient.recv(1024).decode('utf-8')

        # Check if string is "empty"
        if sentString == " ":
            # Send back an "Empty Search" error
            rawData = pickle.dumps("Empty Search")
            returnedClient.send(rawData)
            
            # Print error and close connection. Continue to next while loop
            returnedClient.close()
            print("Empty list detected, sent error back to client")
            continue
        

        splitString = sentString.split(",")

        # Convert list into data stream
        rawData = pickle.dumps(splitString)

        # Return data stream and close connection
        returnedClient.send(rawData)
        returnedClient.close()

        print("Converted list sent back to client")


if __name__ =='__main__':
    main()