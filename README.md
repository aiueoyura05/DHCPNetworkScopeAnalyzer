DHCPNetworkScopeAnalyzer
scapyを用いて、ネットワークアドレスの範囲を取得する。

DHCPdiscoverを構築し、DHCPOfferの解析を行う。

解析した内容からネットワーク規模を示す。(wip for portscannig tool)

![Uploading image.png…]()
![image](https://github.com/aiueoyura05/DHCPNetworkScopeAnalyzer/assets/104673838/9e704490-3219-4266-86b7-13ba33d54213)# 
by https://infocenter.nokia.com/public/7750SR227R1A/index.jsp?topic=%2Fcom.nokia.Triple_Play_Service_Delivery_Architecture_Guide%2Fdhcp_principles-ai9jxkmatx.html

[参考]
scapy/layers/dhcp.py
メモ
>DHCPのオプション
>
>
DHCPOptions = {

    0: "pad",
    
    1: IPField("subnet_mask", "0.0.0.0"),
    
    2: IntField("time_zone", 500),
    3: IPField("router", "0.0.0.0"),
    4: IPField("time_server", "0.0.0.0"),
    5: IPField("IEN_name_server", "0.0.0.0"),
    6: IPField("name_server", "0.0.0.0"),
    7: IPField("log_server", "0.0.0.0"),
    8: IPField("cookie_server", "0.0.0.0"),
    9: IPField("lpr_server", "0.0.0.0"),
    10: IPField("impress-servers", "0.0.0.0"),
    11: IPField("resource-location-servers", "0.0.0.0"),
    12: "hostname",
    13: ShortField("boot-size", 1000),
    14: "dump_path",
    15: "domain",
    16: IPField("swap-server", "0.0.0.0"),
    17: "root_disk_path",
    18: "extensions-path",
    19: ByteField("ip-forwarding", 0),
    20: ByteField("non-local-source-routing", 0),
    21: IPField("policy-filter", "0.0.0.0"),
    22: ShortField("max_dgram_reass_size", 300),
    23: ByteField("default_ttl", 50),
    24: IntField("pmtu_timeout", 1000),
    25: ShortField("path-mtu-plateau-table", 1000),
    26: ShortField("interface-mtu", 50),
    27: ByteField("all-subnets-local", 0),
    28: IPField("broadcast_address", "0.0.0.0"),
    29: ByteField("perform-mask-discovery", 0),
    30: ByteField("mask-supplier", 0),
    31: ByteField("router-discovery", 0),
    32: IPField("router-solicitation-address", "0.0.0.0"),
    33: IPField("static-routes", "0.0.0.0"),
    34: ByteField("trailer-encapsulation", 0),
    35: IntField("arp_cache_timeout", 1000),
    36: ByteField("ieee802-3-encapsulation", 0),
    37: ByteField("tcp_ttl", 100),
    38: IntField("tcp_keepalive_interval", 1000),
    39: ByteField("tcp_keepalive_garbage", 0),
    40: StrField("NIS_domain", "www.example.com"),
    41: IPField("NIS_server", "0.0.0.0"),
    42: IPField("NTP_server", "0.0.0.0"),
    43: "vendor_specific",
    44: IPField("NetBIOS_server", "0.0.0.0"),
    45: IPField("NetBIOS_dist_server", "0.0.0.0"),
    46: ByteField("NetBIOS_node_type", 100),
    47: "netbios-scope",
    48: IPField("font-servers", "0.0.0.0"),
    49: IPField("x-display-manager", "0.0.0.0"),
    50: IPField("requested_addr", "0.0.0.0"),
    51: IntField("lease_time", 43200),
    52: ByteField("dhcp-option-overload", 100),
    53: ByteEnumField("message-type", 1, DHCPTypes),
    54: IPField("server_id", "0.0.0.0"),
    55: _DHCPParamReqFieldListField(
        "param_req_list", [],
        ByteField("opcode", 0)),
    56: "error_message",
    57: ShortField("max_dhcp_size", 1500),
    58: IntField("renewal_time", 21600),
    59: IntField("rebinding_time", 37800),
    60: StrField("vendor_class_id", "id"),
    61: StrField("client_id", ""),
    62: "nwip-domain-name",
    64: "NISplus_domain",
    65: IPField("NISplus_server", "0.0.0.0"),
    66: "tftp_server_name",
    67: StrField("boot-file-name", ""),
    68: IPField("mobile-ip-home-agent", "0.0.0.0"),
    69: IPField("SMTP_server", "0.0.0.0"),
    70: IPField("POP3_server", "0.0.0.0"),
    71: IPField("NNTP_server", "0.0.0.0"),
    72: IPField("WWW_server", "0.0.0.0"),
    73: IPField("Finger_server", "0.0.0.0"),
    74: IPField("IRC_server", "0.0.0.0"),
    75: IPField("StreetTalk_server", "0.0.0.0"),
    76: IPField("StreetTalk_Dir_Assistance", "0.0.0.0"),
    77: "user_class",
    78: "slp_service_agent",
    79: "slp_service_scope",
    80: "rapid_commit",
    81: "client_FQDN",
    82: "relay_agent_information",
    85: IPField("nds-server", "0.0.0.0"),
    86: StrField("nds-tree-name", ""),
    87: StrField("nds-context", ""),
    88: "bcms-controller-namesi",
    89: IPField("bcms-controller-address", "0.0.0.0"),
    91: IntField("client-last-transaction-time", 1000),
    92: IPField("associated-ip", "0.0.0.0"),
    93: "pxe_client_architecture",
    94: "pxe_client_network_interface",
    97: "pxe_client_machine_identifier",
    98: StrField("uap-servers", ""),
    100: StrField("pcode", ""),
    101: StrField("tcode", ""),
    108: IntField("ipv6-only-preferred", 0),
    112: IPField("netinfo-server-address", "0.0.0.0"),
    113: StrField("netinfo-server-tag", ""),
    114: StrField("captive-portal", ""),
    116: ByteField("auto-config", 0),
    117: ShortField("name-service-search", 0,),
    118: IPField("subnet-selection", "0.0.0.0"),
    121: ClasslessFieldListField(
        "classless_static_routes",
        [],
        ClasslessStaticRoutesField("route", 0)),
    124: "vendor_class",
    125: "vendor_specific_information",
    128: IPField("tftp_server_ip_address", "0.0.0.0"),
    136: IPField("pana-agent", "0.0.0.0"),
    137: "v4-lost",
    138: IPField("capwap-ac-v4", "0.0.0.0"),
    141: "sip_ua_service_domains",
    146: "rdnss-selection",
    150: IPField("tftp_server_address", "0.0.0.0"),
    159: "v4-portparams",
    160: StrField("v4-captive-portal", ""),
    161: StrField("mud-url", ""),
    208: "pxelinux_magic",
    209: "pxelinux_configuration_file",
    210: "pxelinux_path_prefix",
    211: "pxelinux_reboot_time",
    212: "option-6rd",
    213: "v4-access-domain",
    255: "end"
}


>DHCPとBOOTPの継承関係

class BOOTP(Packet):

    name = "BOOTP"　
    
    fields_desc = [　
    
        ByteEnumField("op", 1, {1: "BOOTREQUEST", 2: "BOOTREPLY"}),　
        ByteEnumField("htype", 1, HARDWARE_TYPES),　
        ByteField("hlen", 6),　
        ByteField("hops", 0),　
        XIntField("xid", 0),　
        ShortField("secs", 0),　
        FlagsField("flags", 0, 16, "???????????????B"),　
        IPField("ciaddr", "0.0.0.0"),　
        IPField("yiaddr", "0.0.0.0"),　
        IPField("siaddr", "0.0.0.0"),　
        IPField("giaddr", "0.0.0.0"),　　
        _BOOTP_chaddr("chaddr", b"", length=16),　
        StrFixedLenField("sname", b"", length=64),　　
        StrFixedLenField("file", b"", length=128),　　　
        StrEnumField("options", b"", {dhcpmagic: "DHCP magic"})]　　
