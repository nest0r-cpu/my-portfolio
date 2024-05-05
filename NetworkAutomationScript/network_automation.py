from netmiko import ConnectHandler  # Import the ConnectHandler class from Netmiko library

# Define device parameters for SSH connection
device = {
    'device_type': 'cisco_ios',  # Specify the device type (e.g., Cisco IOS)
    'host': '192.168.1.1',        # IP address or hostname of the network device
    'username': 'admin',          # SSH username
    'password': 'password',       # SSH password
}

try:
    # Attempt to establish an SSH connection to the network device
    net_connect = ConnectHandler(**device)
    print("Connected to device.")

    # Send a command to the network device and capture the output
    output = net_connect.send_command("show version")
    print(output)

    # Disconnect from the network device
    net_connect.disconnect()
    print("Disconnected from device.")

except Exception as e:
    # Handle any exceptions that occur during the connection attempt
    print("Failed to connect:", e)
