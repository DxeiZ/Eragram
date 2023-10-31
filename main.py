#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from instagrapi import Client
from ascii_magic import AsciiArt
import requests
import colorama
import shutil
import os
import sys

if sys.platform.startswith('linux'):
    os.system("clear")
else:
    os.system("cls")

colorama.init()

def Header():
    print(colorama.Fore.RED+"""
\033[1;31m
▓█████  ██▀███   ▄▄▄        ▄████  ██▀███   ▄▄▄       ███▄ ▄███▓
▓█   ▀ ▓██ ▒ ██▒▒████▄     ██▒ ▀█▒▓██ ▒ ██▒▒████▄    ▓██▒▀█▀ ██▒
▒███   ▓██ ░▄█ ▒▒██  ▀█▄  ▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▓██    ▓██░
▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██ ░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▒██    ▒██ 
░▒████▒░██▓ ▒██▒ ▓█   ▓██▒░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒▒██▒   ░██▒
░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ░  ░
 ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░░  ░      ░
   ░     ░░   ░   ░   ▒   ░ ░   ░   ░░   ░   ░   ▒   ░      ░   
   ░  ░   ░           ░  ░      ░    ░           ░  ░       ░   
                                                                
                                            \033[1;39mDeveloper by Eratonos\033[1;31m
""")
    print(colorama.Style.RESET_ALL)

ACCOUNT_USERNAME = "ratossoftware"
ACCOUNT_PASSWORD = "guARQ12"

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

Header()

while True:
    TARGET_USERNAME = input(f'\n{colorama.Fore.LIGHTGREEN_EX}İstifadəçi adı >{colorama.Fore.LIGHTYELLOW_EX} ')
    userID = cl.user_id_from_username(TARGET_USERNAME)
    userInfo = cl.user_info(userID)
    
    def download_image(url, file_name, headers):
        if os.path.exists(file_name):
            os.remove(file_name)

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            with open(file_name, "wb") as f:
                f.write(response.content)
        else:
            print(response.status_code)

    if sys.platform.startswith('linux'):
        os.system("clear")
    else:
        os.system("cls")

    if __name__ == "__main__":
        headers = { "User-Agent": "Chrome/51.0.2704.103" }

        url = userInfo.profile_pic_url.replace("HttpUrl('", "").replace("', )", "")
        file_name = "./profile_pic/"+TARGET_USERNAME+".png"

        download_image(url, file_name, headers)
    
    Header()

    # User Info

    my_art = AsciiArt.from_image("./profile_pic/"+TARGET_USERNAME+".png")
    print(my_art.to_ascii(columns=30))
    print(colorama.Style.RESET_ALL)

    key = f"🔐 " if userInfo.is_private else f"🔓 "
    verify = " ☑ " if userInfo.is_verified else ""
    print(f'{colorama.Fore.MAGENTA}İstifadəçi Hakkında Məlumatlar\n'.center(shutil.get_terminal_size().columns))
    
    print(f'{colorama.Fore.RED}⤫ İstifadəçi adı  ⤫ {key}{colorama.Fore.LIGHTYELLOW_EX}{userInfo.username}{verify} ({userInfo.pk})')
    print(f'{colorama.Fore.RED}⤫ Tam adı         ⤫ {colorama.Fore.LIGHTYELLOW_EX}{userInfo.full_name}')
    print(f'{colorama.Fore.RED}⤫ Biografiya      ⤫ {colorama.Fore.LIGHTYELLOW_EX}{userInfo.biography}')
    print(f'{colorama.Fore.RED}⤫ Takip edenler   ⤫ {colorama.Fore.LIGHTYELLOW_EX}{userInfo.follower_count}')
    print(f'{colorama.Fore.RED}⤫ Takip etdikləri ⤫ {colorama.Fore.LIGHTYELLOW_EX}{userInfo.following_count}')
    print(f'{colorama.Fore.RED}⤫ Göndəri sayısı  ⤫ {colorama.Fore.LIGHTYELLOW_EX}{userInfo.media_count}\n')

    # Top 3 post
    print(f'{colorama.Fore.MAGENTA}İstifadəçinin 3 Göndərisi\n'.center(shutil.get_terminal_size().columns))
    userMedia = cl.user_medias(user_id=userID, amount=3)
    if userMedia[0].media_type == 1:
        if __name__ == "__main__":
            url = userMedia[0].thumbnail_url.replace("HttpUrl('", "").replace("', )", "")
            file_name = "./post_pic/"+userMedia[0].id+".png"

            download_image(url, file_name, headers)
        if __name__ == "__main__":
            url = userMedia[1].thumbnail_url.replace("HttpUrl('", "").replace("', )", "")
            file_name = "./post_pic/"+userMedia[1].id+".png"

            download_image(url, file_name, headers)
        if __name__ == "__main__":
            url = userMedia[2].thumbnail_url.replace("HttpUrl('", "").replace("', )", "")
            file_name = "./post_pic/"+userMedia[2].id+".png"

            download_image(url, file_name, headers)

        cap1 = str(userMedia[0].caption_text)[:27]
        cap2 = str(userMedia[1].caption_text)[:27]
        cap3 = str(userMedia[2].caption_text)[:27]
        cap1 += "..."
        cap2 += "..."
        cap3 += "..."

        post1 = AsciiArt.from_image("./post_pic/"+userMedia[0].id+".png")
        post2 = AsciiArt.from_image("./post_pic/"+userMedia[1].id+".png")
        post3 = AsciiArt.from_image("./post_pic/"+userMedia[2].id+".png")
        text="""
\t.·:'''''':·.\t\t\t.·:'''''''''':·.\t\t.·:'''''''''':·.
\t: :  ██╗ : :\t\t\t: : ██████╗  : :\t\t: : ██████╗  : :
\t: : ███║ : :\t\t\t: : ╚════██╗ : :\t\t: : ╚════██╗ : :
\t: : ╚██║ : :\t\t\t: :  █████╔╝ : :\t\t: :  █████╔╝ : :
\t: :  ██║ : :\t\t\t: : ██╔═══╝  : :\t\t: :  ╚═══██╗ : :
\t: :  ██║ : :\t\t\t: : ███████╗ : :\t\t: : ██████╔╝ : :
\t: :  ╚═╝ : :\t\t\t: : ╚══════╝ : :\t\t: : ╚═════╝  : :
\t'·:......:·'\t\t\t'·:..........:·'\t\t'·:..........:·'
"""
        print(f'{colorama.Fore.LIGHTYELLOW_EX}{text}')
        print(f'🤍  💬  🔗\t\t    📌\t🤍  💬  🔗\t\t    📌\t🤍  💬  🔗\t\t    📌\n')
        print(f'\033[1;39m{userMedia[0].comment_count} rəy\t\t\t\t{userMedia[1].comment_count} rəy\t\t\t\t{userMedia[2].comment_count} rəy\033[1;31m')
        print(f'\033[1;39m{userMedia[0].like_count} bəyənmək\t\t\t{userMedia[1].like_count} bəyənmək\t\t\t{userMedia[2].like_count} bəyənmək\033[1;31m')
        print(f'{colorama.Fore.WHITE}{cap1}\t{cap2}\t{cap3}')