# constants.py

"""This module defines project-level constants."""

PORT_NUMBERS = [
    1,  # TCP Port Service Multiplexer
    101,  # NIC hostname server
    102,  # ISO-TSAP Class 0
    104,  # ACR-NEMA Digital Imaging and Communications in Medicine
    105,  # CCSO Name Server Protocol
    107,  # Remote Telnet Service
    108,  # SNA Gateway Access Server
    109,  # Post Office Protocol v2
    11,  # Active users
    110,  # Post Office Protocol v3
    111,  # Sun Remote Procedure Call
    113,  # Ident Protocol
    117,  # UUCP Path Service
    118,  # SQL Services
    119,  # Network News Transport Protocol
    1194,  # OpenVPN
    123,  # Network Time Protocol
    1293,  # Internet Protocol Security
    13,  # Daytime
    137,  # NetBios name service
    138,  # NetBios datagram service
    139,  # NetBios session service
    143,  # Interim Mail Access Protocol
    1433,  # Microsoft SQL Server
    1434,  # Microsoft SQL Monitor
    152,  # Background File Transfer Program
    153,  # Simple Gateway Monitoring Protocol
    156,  # SQL Service
    161,  # Simple Network Management Protocol
    162,  # SNMP Traps
    17,  # Quote of the Day
    170,  # Network PostScript
    1701,  # Layer 2 Tunneling Protocol
    1723,  # Microsoft Point-to-Point Tunneling Protocol
    175,  # VMNET
    177,  # X Display Manager Control Protocol
    179,  # Border Gateway Protocol
    18,  # Message Send Protocol
    1812,  # Radius Authentication Protocol
    1813,  # Radius Accounting Protocol
    19,  # Character Generator
    194,  # Internet Relay Chat
    195,  # DNSIX security protocol auditing
    199,  # SNMP Unix Multiplexer
    20,  # FTP data connections
    201,  # AppleTalk Routing Maintenance
    2049,  # Network File System
    209,  # The Quick Mail Transfer Protocol
    21,  # File Transfer Protocol
    210,  # ANSI Z39.50
    2123,  # GPRS Tunneling Protocol Control Data
    213,  # Internetwork Packet Exchange
    2152,  # GPRS Tunneling Protocol User Data
    218,  # Netix Message Posting Protocol
    22,  # Secure Shell Protocol
    220,  # Interactive Mail Access Protocol v3
    23,  # Telnet Protocol
    25,  # Simple Mail Transport Protocol
    259,  # Efficient Short Remote Operations
    264,  # Border Gateway Multicast Protocol
    27,  # NSW User System FE
    280,  # http-mgmt
    29,  # MSG ICP
    311,  # AppleShare IP Web Administration
    318,  # PKIX Timestamp
    319,  # Precision Time Protocol Event
    320,  # Precision Time Protocol General
    33,  # Display Support Protocol
    3386,  # GPRS Tunneling Prime Protocol
    350,  # MATIP Type A
    351,  # MATIP Type B
    366,  # On Demand Mail Retry
    369,  # Rpc2portmap
    37,  # Time
    371,  # Clearcase albd
    3784,  # Bidirectional Forwarding Detection
    3785,  # BFD Echo
    383,  # HP Performance Data Alarm Manager
    384,  # A Remote Network Server System
    387,  # Appletalk Update-Based Routing Protocol
    389,  # Lightweight Directory Access Protocol
    39,  # Resource Location Protocol
    401,  # Uninterruptible Power Supply
    42,  # IEN116 Nameserver Service (obsolete)
    427,  # Server Location Protocol
    43,  # Nicname
    434,  # Mobile IP registration
    443,  # HTTP Secure (HTTPS)
    4432,  # MLAG Protocol
    444,  # Simple Network Paging Protocol
    445,  # Microsoft-DS SMB File Sharing
    4500,  # Internet Security Association and Key Management Protocol
    4532,  # Nat Sync Protocol
    464,  # Kerberos Change/Set Password
    47,  # Generic Routing Encapsulation
    475,  # Aladdin Knowledge Systems Hasp services, TCP/IP version
    49,  # TAC Access Control System
    496,  # PIM Auto-RP
    5,  # Remote Job Entry
    50,  # Remote Mail Checking Protocol
    500,  # Internet Security Association and Key Management Protocol
    50002,  # ARP file transfer server port
    504,  # Citadel
    51,  # IMP Logical Address Maintenance
    512,  # Biff (mail notification, comsat) / Remote Process Execution/Rexec
    513,  # Who service, rwho / Rlogin
    514,  # System Logger / Remote Shell/Rsh
    515,  # Line Printer Daemon
    517,  # Talk
    52,  # XNS (Xerox Network Systems) Time Protocol
    520,  # Extended File Name Server / Routing Information Protocol
    524,  # NetWare Core Protocol
    525,  # Timeserver
    53,  # Domain Name Service
    530,  # Remote Procedure Call
    532,  # Readnews
    533,  # For Emergency Broadcasts
    54,  # XNS (Xerox Network Systems) Clearinghouse
    540,  # Unix-to-Unix Copy Program
    542,  # Commerce Applications
    543,  # Kerberos login
    544,  # Kerberos shell
    546,  # DHCPv6 Client
    547,  # DHCPv6 Server
    548,  # Apple Filing Protocol Over TCP
    55,  # ISI Graphics Language
    550,  # new-who
    554,  # Real Time Streaming Protocol
    556,  # RFS Server
    560,  # Remote Monitord
    561,  # Monitord
    563,  # Network News Transfer Protocol Over TSL/SSH
    58,  # XNS (Xerox Network Systems) Mail
    587,  # Email Message Submission
    591,  # Filemaker, Inc. -HTTP Alternate
    593,  # HTTP RPC Ep Map
    604,  # TUNNEL Profile
    623,  # ASF Remote Management and Control Protocol
    631,  # Internet Printing Protocol
    635,  # RLZ DBase
    636,  # LDAP Over TLS/SSH
    639,  # Multicast Source Discovery Protocol
    641,  # SupportSoft Nexus Remote Command
    646,  # Label Distribution Protocol
    657,  # Remote Monitoring and Control Protocol
    660,  # MacOS Server Admin
    67,  # Bootstrap Protocol (BOOTP) server
    674,  # Application Configuration Access Protocol
    68,  # Bootstrap Protocol (BOOTP) client
    69,  # Trivial File Transfer Protocol
    691,  # MS Exchange Routing
    694,  # Linux-HA Heartbeat
    695,  # IEEE Media Management System Over SSL
    698,  # Optimized Link State Routing
    7,  # Echo
    70,  # Gopher
    700,  # Extensible Provision Protocol
    701,  # Link Management Protocol
    702,  # Internet Registry Information Service Over BEEP
    706,  # Secure Internet Live Conferencing
    71,  # Remote Job Service
    711,  # Cisco Tag Distribution Protocol
    712,  # Topology Broadcast based on Reverse-Path Forwarding Protocol
    72,  # Remote Job Service
    73,  # Remote Job Service
    74,  # Remote Job Service
    749,  # Kerberos Administration
    79,  # Finger
    80,  # World Wide Web (HTTP)
    847,  # DHCP Failover Protocol
    848,  # Group Domain of Interpretation Protocol
    860,  # Internet Small Computers Systems Interface
    873,  # rysnc File Synchronization Protocol
    88,  # Kerberos Authentication System
    9,  # Discard
    989,  # FTPS Protocol (data)
    990,  # FTPS Protocol (control)
    991,  # Netnews Administration System
    993,  # Internet Message Access Protocol over SSL
    995,  # Post Office Protocol 3 over TLS/SSL
]
