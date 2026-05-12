import socket

# Target server configuration
HOST = "127.0.0.1"
PORT = 7777

# Message to send to the TCP server
MESSAGE = "Hello from Python!"

# Create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the TCP server
    client.connect((HOST, PORT))

    # Send the message as bytes
    client.send(MESSAGE.encode())

    print(f"[+] Message sent to {HOST}:{PORT}")

except ConnectionRefusedError:
    print("[-] Connection refused. Start the Netcat listener first.")

finally:
    # Close the connection
    client.close()
  
