# 802.11
802.11 Pentesting repo


## DAD - Deauthentication Attack Detection v.1.0.0-alpha

A tool to detect deauthentication attacks

### How to run the tool
```sh
$ cd dad/
```

Run dad tool

```sh
$ python dad.py
```

### Dependencies
- **pyshark**
Install with ***pip***:
```sh
$ pip install pyshark
```

- Also requires ***Wireshark*** and ***tshark*** (wireshark for terminal) to be installed in the system.

### Notes
- As of now it only reads files from /data
- This tool checks for Deauthentication Attacks on **.pcap** files. It assumes that the folder(s) exist in the ***/data*** directory.e.g. */data/**file1.pcap***, */data/**file2.pcap*** etc.
The user has to type just the name of the file (***file1.pcap***, ***file2.pcap*** etc) and make sure they exist in ***/data*** directory.
