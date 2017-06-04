# -*- coding: utf-8 -*-
from __future__ import print_function
from parser import Scraper
from colors import Colors
import sys

def display_banner():
    print ("\n\n")
    print (Colors.OKBLUE + '''
    ██████╗  █████╗ ██████╗
    ██╔══██╗██╔══██╗██╔══██╗
    ██║  ██║███████║██║  ██║
    ██║  ██║██╔══██║██║  ██║
    ██████╔╝██║  ██║██████╔╝
    ╚═════╝ ╚═╝  ╚═╝╚═════╝    v1.0.1-alpha
    ''' + Colors.ENDC)
    print ("\n\n")
    print (Colors.WARNING + "Deauthentication Attacks Detection - DAD tool" + Colors.ENDC)
    print ("\n\n")

class Menu(Scraper):
    def __init__(self):
        self.choices = {
            "2": self.instructions,
            "1": self.scraper,
            "0": self.quit
        }

    def display_menu(self):
        print ("\n\n")
        print ("Menu")
        print ("============")
        print ("2. Instructions")
        print ("1. Audit .pcap file for Deauthentication Attacks")
        print ("0. Quit")
        print ("\n\n")

    def run(self):
        while True:
            self.display_menu()
            choice = raw_input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print (Colors.FAIL + "Dude.... that is not an option...." + Colors.ENDC)

    def scraper(self):
        pcap1 = raw_input("Enter the name of the first .pcap to audit (I assume it is in data dir): ")
        pcap2 = raw_input("Enter the name of the second .pcap to audit (I assume it is in data dir): ")
        Scraper(pcap1).scraper()
        Scraper(pcap2).scraper()

    def quit(self):
        print ("\n\n")
        print (Colors.FAIL + "Thank you for using DAD tool." + Colors.ENDC)
        print (Colors.FAIL + "Gracefully quiting..." + Colors.ENDC)
        sys.exit(0)

    def instructions(self):
        print ("\n\n")
        print (Colors.WARNING + '''
        Instructions''' + Colors.ENDC + '''
        ================
        This tool checks for Deauthentication Attacks on .pcap files. It assumes that the folder(s) exist in the /data directory.
        e.g. /data/file1.pcap, /data/file2.pcap etc.
        The user has to type just the name of the file (file1.pcap, file2.pcap etc) and make sure they exist in /data directory.
        ''')


if __name__== "__main__":
    display_banner()
    Menu().run()
