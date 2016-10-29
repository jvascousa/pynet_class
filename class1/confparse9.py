#!/usr/bin/env python

'''
Use ciscoconfparse library to find the crypto maps.
'''

from ciscoconfparse import CiscoConfParse

def main():
   
    cisco_file = "cisco.cfg"

    cisco_cfg = CiscoConfParse(cisco_file)

    crypto_maps = cisco_cfg.find_objects_w_child(parentspec=r'crypto map CRYPTO',childspec=r'pfs group2')

    print "\nCrypto Maps using PFS group2:"

    for entry in crypto_maps:
        print "   {0}".format(entry.text)


    print



if __name__ == "__main__":
    main()
