import requests,json,os
from colorama import Fore

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(Fore.GREEN + """
 ██▓███   ▄▄▄       ██▀███   ▄▄▄        ██████  ██▓▄▄▄█████▓▓█████ 
▓██░  ██▒▒████▄    ▓██ ▒ ██▒▒████▄    ▒██    ▒ ▓██▒▓  ██▒ ▓▒▓█   ▀ 
▓██░ ██▓▒▒██  ▀█▄  ▓██ ░▄█ ▒▒██  ▀█▄  ░ ▓██▄   ▒██▒▒ ▓██░ ▒░▒███   
▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██▀▀█▄  ░██▄▄▄▄██   ▒   ██▒░██░░ ▓██▓ ░ ▒▓█  ▄ 
▒██▒ ░  ░ ▓█   ▓██▒░██▓ ▒██▒ ▓█   ▓██▒▒██████▒▒░██░  ▒██▒ ░ ░▒████▒
▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░▓    ▒ ░░   ░░ ▒░ ░
░▒ ░       ▒   ▒▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░    ░     ░ ░  ░
░░         ░   ▒     ░░   ░   ░   ▒   ░  ░  ░   ▒ ░  ░         ░   
               ░  ░   ░           ░  ░      ░   ░              ░  ░
                                                   
                                                   Tool made by alenify#3808 
                                                   if you find any bugs feel free to dm!
                                                   fuck anyone who skids this shit.
                                                   
                                                                                                 
    """ + Fore.GREEN)   

clear()

self_avatar = ""
base_url = "https://discord.com/api/webhooks/WEBHOOK_ID/WEBHOOK_TOKEN"
url = ""

while True:
    option2 = input("""select your option:
[1] through url.
[2] coming soon

""")
    if option2=="1":
        url = input(Fore.GREEN+"webhook url > "+Fore.WHITE)
        break
        print(Fore.RED+"invalid option: "+option2+Fore.WHITE)

# check webhook
rq = requests.get(url)
if rq.status_code == 200:
    clear()
    print(Fore.GREEN+"session started"+Fore.WHITE)
    print()
else:
    print(Fore.RED+f" {rq.status_code}. token or id might be invalid. program will commit suicide.."+Fore.WHITE)
    exit(0) #this was some old shit i wrote, too lazy to change it back.



while True:
    option=input(f"""options:
{Fore.GREEN}[1] chat using the webhook, can ping everyone
{Fore.GREEN}[2] edit the webhook 
{Fore.RED}[3] kill the webhook {Fore.GREEN}
""")
    if option == "1":
        clear()
        print(Fore.RED+"session started (\'exit\' to exit)")
        while True:
            inp = input(Fore.RED+'> '+Fore.WHITE)
            if inp == "exit":
                clear()
                break
            data = {"content": inp}
            if self_avatar!="":
                data['avatar_url']=self_avatar

            x=requests.post(url, data=json.dumps(data), headers={ "Content-Type": "application/json"})
            if x.status_code == 204:
                print(Fore.RED+"msg sent"+Fore.WHITE)
            else:
                print(Fore.RED+f" {x.status_code}: action failed"+Fore.WHITE)
    elif option == "2":
        print(Fore.RED + "enter blank for default"+Fore.WHITE)
        name = input(Fore.RED+"custom name > "+Fore.WHITE)
        avatar = input(Fore.RED+"custom avatar url > "+Fore.WHITE)
        data = {"name":name,"avatar":avatar}
        self_avatar=avatar
        x = requests.patch(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
        if x.status_code == 200:
            clear()
            print(Fore.RED+"message sent"+Fore.WHITE)
        else:
            print(Fore.RED+f" {x.status_code}: possibly failed"+Fore.WHITE)
    elif option == "3":
        clear()
        yn = input(Fore.RED+"are you sure? (y/n) > "+Fore.WHITE)
        if yn == "y":
            inp = input(Fore.RED+"any last words (leave blank for none) > "+Fore.WHITE)
            if inp != "":
                data = {"content": inp}
                x = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
                if x.status_code == 204:
                    print(Fore.GREEN + "succes" + Fore.WHITE)
                else:
                    print(Fore.YELLOW + f" {x.status_code}: failed" + Fore.WHITE)
            print()
            rq = requests.delete(url)
            if rq.status_code == 204:
                print(Fore.GREEN+"hook is deleted closing the program."+Fore.WHITE)
            else:
                print(Fore.YELLOW+f" {rq.status_code}:action failed closing down."+Fore.WHITE)
            exit(0)
        else:
            clear()

    else:
        print(Fore.YELLOW+f"invalid option: {option}\n"+Fore.WHITE)
