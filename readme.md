# About

The seperateString microservice is a microservice that receives a string with words seperated witha delimitator of "," and returns a list of seperated strings.


# Usage

There are two important steps to using this microservice. [Request Data](#request-data) and [Receiving Data](#receiving-data). In Request Data you send the string that you wish to split, and then receive the split string in the Receivng Data step.

## Test Case
The test example itself has two batch files that can be used to make it run. The first bvatch file `runMicroService.bat` can be used to launch the microservice which will stay running as long as the command line menu is open. The `runClient.bat` runs once and shows an example call to the server.


## Request Data

To request a split string from the microservice you must send a `utf-8` encoded string to the microservice. First a [python socket](https://docs.python.org/3/library/socket.html) must be setup listening to port 4000. Once setup and connected you must send the string through the socket. See the code example below.

```python
    # String to send over
    stringMessage = "Look at me!, I have a string!, And another one!"

    # Encode string
    encodedString = stringMessage.encode('utf-8')

    # Send the encoded message over the socket
    clientSocket.send(encodedString)
```
## Receiving Data

Receiveing the split string from the microsevice requires the [pickle library](https://docs.python.org/3/library/pickle.html). By default the microservice sends data in less than 1024 increments. Larger strings may require a larger packet size. Just as with requesing data a python socket must be setup listening to port 4000. Once this is setup the code snippet below can be used to receive data.

```python
    # Raw data stream received from socket
    rawData = clientSocket.recv(1024)

    # Pickle to convert raw data stream into a list
    returnedList = pickle.loads(rawData)
```

The microservice will return "Empty Search" if there is only " " sent to it.

# UML

![UML](./Assignment%208.png)