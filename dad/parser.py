import pyshark
from colors import Colors

class Scraper:
    def __init__(self, pcap):
        self.pcap = pcap
        # self.wfilter = wfilter

    def scraper(self):
        pkt_list = []
        pcap_file = ("data/%s" % self.pcap)
        print "\n"
        print Colors.OKGREEN + "===============================" + Colors.ENDC
        print Colors.OKGREEN + "= Scraping : " + str(pcap_file) + Colors.ENDC
        print Colors.OKGREEN + "===============================" + Colors.ENDC

        wfilter = "wlan.fc.type_subtype eq 12 && wlan.da != ff:ff:ff:ff:ff:ff"
        cap = pyshark.FileCapture(pcap_file, display_filter=wfilter)

        for pkt in cap:
            try:
                print Colors.FAIL + "Deauth attack on: " + str(pkt.frame_info.time) + " from : " + str(pkt.wlan.ta) + " and lasts " + str(pkt.wlan.duration) + " microseconds." + Colors.ENDC
            except:
                pass
        print "================================================================="
        print "\n\n"
