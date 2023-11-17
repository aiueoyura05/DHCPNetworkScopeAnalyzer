from scapy.all import srp, Ether, IP, UDP, BOOTP, DHCP
import logging

# Disabling Scapy warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def get_dhcp_offer(interface):
    """
    Send a DHCP discover message and receive the offer to get the IP range.
    """

    # Constructing and sending the DHCP Discover packet
    dhcp_discover = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src="0.0.0.0", dst="255.255.255.255") \
                    / UDP(sport=68, dport=67) / BOOTP(op=1, chaddr="1234567890ab") \
                    / DHCP(options=[("message-type", "discover"), "end"])

    # Sending the packet and waiting for a response
    ans, unans = srp(dhcp_discover, iface=interface, multi=True, timeout=10, verbose=False)

    # Parsing the response to find the DHCP Offer ans(送信パケット、応答パケット)

        if DHCP in packet and packet[DHCP].options[0][1] == 2:  # DHCP Offerの確認を行う
            client_ip = packet[BOOTP].yiaddr#クライアントのipアドレス
            subnet_mask = None
            for option in packet[DHCP].options:
                if option[0] == 'subnet_mask':
                    subnet_mask = option[1]
            return client_ip, subnet_mask

    return None, None

# Example usage
interface = "192.168.43.43"  # Replace with your network interface
ip_offer, subnet_mask = get_dhcp_offer(interface)
if ip_offer and subnet_mask:
    print(f"Received DHCP Offer: IP - {ip_offer}, Subnet Mask - {subnet_mask}")
else:
    print("No DHCP Offer received.")


