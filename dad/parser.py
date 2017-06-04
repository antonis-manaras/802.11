from __future__ import print_function
import pyshark
from colors import Colors

class Scraper:
    def __init__(self, pcap):
        self.pcap = pcap
        # self.wfilter = wfilter

    def scraper(self):
        dos_pkt_list = []
        targeted_pkt_list = []
        pcap_file = ("data/%s" % self.pcap)
        print ("\n")
        # print Colors.OKGREEN + "===============================" + Colors.ENDC
        # print Colors.OKGREEN + "= Scraping : " + str(pcap_file) + Colors.ENDC
        # print Colors.OKGREEN + "===============================" + Colors.ENDC
        print (Colors.OKGREEN +
        '''
        ===============================
        = Scraping : ''' + str(pcap_file) +
        '''
        ===============================
        ''' + Colors.ENDC )

        # wfilter = "wlan.fc.type_subtype eq 12 && wlan.da != ff:ff:ff:ff:ff:ff"
        print ("Checking for DOS attacs:")
        print ("\n\n")
        wfilter_broadcast = "wlan.fc.type_subtype eq 12 && wlan.da == ff:ff:ff:ff:ff:ff"
        cap = pyshark.FileCapture(pcap_file, display_filter=wfilter_broadcast)

        for pkt in cap:
            try:
                dos_pkt_list.append(pkt)
            except:
                pass # Here should exist proper error handling
        if dos_pkt_list:
            for i, deauth_pkt in enumerate(dos_pkt_list):
                print (Colors.FAIL + str(i+1) + ": Deauth attack on: " + str(deauth_pkt.frame_info.time) + " from : " + str(deauth_pkt.wlan.ta) + " and lasts " + str(deauth_pkt.wlan.duration) + " microseconds." + Colors.ENDC)
            print ("\n\n")
            print (Colors.FAIL + "Total packets detected: " + str(i+1) + ". Possible DOS attack!" + Colors.ENDC)
        else:
            print (Colors.OKGREEN + '''Deauthentication attack not detetected.\nFile is clean!''' + Colors.ENDC)
        print ("\n\n")
        print ("=================================================================")
        print ("\n\n")


        print ("Checking for targeted attacs:")
        print ("\n\n")

        wfilter_targeted = "wlan.fc.type_subtype eq 12 && wlan.da != ff:ff:ff:ff:ff:ff"
        ncap = pyshark.FileCapture(pcap_file, display_filter=wfilter_targeted)

        for npkt in ncap:
            try:
                targeted_pkt_list.append(npkt)
            except:
                pass # Here should exist proper error handling
        if targeted_pkt_list:
            for j, ndeauth_pkt in enumerate(targeted_pkt_list):
                print (Colors.FAIL + str(j+1) + ": Deauth attack on: " + str(ndeauth_pkt.frame_info.time) + " from : " + str(ndeauth_pkt.wlan.ta) + " and lasts " + str(ndeauth_pkt.wlan.duration) + " microseconds." + Colors.ENDC)
            print ("\n\n")
            print (Colors.FAIL + "Total packets detected: " + str(j+1) + Colors.ENDC)
        else:
            print (Colors.OKGREEN + '''Deauthentication attack not detetected.\nFile is clean!''' + Colors.ENDC)
        print ("\n\n")
        print ("=================================================================")
        print ("\n\n")
