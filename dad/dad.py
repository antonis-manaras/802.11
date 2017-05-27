# -*- coding: utf-8 -*-
from parser import Scraper
from colors import Colors
import sys

class Menu(Scraper):
    def __init__(self):
        self.choices = {
            "1": self.scraper,
            "0": self.quit
        }

    def display_menu(self):
        print "\n\n"
        print Colors.OKBLUE+"██████╗  █████╗ ██████╗" + Colors.ENDC
        print Colors.OKBLUE+"██╔══██╗██╔══██╗██╔══██╗" + Colors.ENDC
        print Colors.OKBLUE+"██║  ██║███████║██║  ██║" + Colors.ENDC
        print Colors.OKBLUE+"██║  ██║██╔══██║██║  ██║" + Colors.ENDC
        print Colors.OKBLUE+"██████╔╝██║  ██║██████╔╝" + Colors.ENDC
        print Colors.OKBLUE+"╚═════╝ ╚═╝  ╚═╝╚═════╝" + "   v1.0.0-alpha" + Colors.ENDC
        print "\n\n"
        print Colors.WARNING + "Deauthentication Attac Detection - DAD tool" + Colors.ENDC
        # print "v1.0.0-alpha"
        print "\n\n"
        print "Menu"
        print "1. Audit .pcap file for Deauthentication Attacks"
        print "0. Quit"

    def run(self):
        while True:
            self.display_menu()
            choice = raw_input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print Colors.FAIL + "Dude.... that is not an option...." + Colors.ENDC

    def scraper(self):
        pcap = raw_input("Enter the name of the .pcap to audit (I assume it is in data dir): ")
        Scraper(pcap).scraper()

    def quit(self):
        print "\n\n"
        print "Thank you for using DAD tool."
        print "Gracefully quiting..."
        sys.exit(0)

if __name__== "__main__":
    Menu().run()
