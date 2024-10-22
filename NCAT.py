from netmiko import ConnectHandler

# Device details (Change these to match your actual router)
router = {
    'device_type': 'cisco_ios',  # Cisco IOS router
    'ip': '192.168.1.1',  # IP of the router
    'username': 'admin',  # SSH username
    'password': 'password',  # SSH password
}

# Commands to configure the router
commands = [
    # Set default gateway
    'ip route 0.0.0.0 0.0.0.0 192.168.5.5',  # Default route to 192.168.5.5

    # Configure DHCP (for a subnet of 192.168.5.0/24)
    'ip dhcp pool my-dhcp-pool',
    'network 192.168.5.0 255.255.255.0',  # Define the network
    'default-router 192.168.5.5',  # Default gateway for clients
    'lease 1',  # Lease duration of 1 day
    'dns-server 8.8.8.8',  # Assign Google DNS to DHCP clients

    # Enable STP (Spanning Tree Protocol)
    'spanning-tree mode pvst',  # Enable Per-VLAN STP (or change mode if needed)

    # Basic Firewall configuration
    'access-list 100 permit ip any any',  # Allow all traffic (simple rule example)
    'access-list 101 deny ip 192.168.5.0 0.0.0.255 any',  # Deny traffic from specific network
    'access-list 102 permit ip any any',  # Permit all other traffic

    # Apply access-lists to interfaces
    'interface GigabitEthernet0/0',  # Specify your interface
    'ip access-group 101 in',  # Apply the firewall rule to incoming traffic
    'exit',

    # Save the configuration
    'write memory'
]

# Connect to the router and apply the configuration
def configure_router(router, commands):
    try:
        # Establish SSH connection to the device
        net_connect = ConnectHandler(**router)
        
        # Send configuration commands
        output = net_connect.send_config_set(commands)
        print("Configuration Output:\n", output)
        
        # Disconnect from the device
        net_connect.disconnect()
    except Exception as e:
        print(f"Failed to configure the router: {e}")

if __name__ == "__main__":
    configure_router(router, commands)