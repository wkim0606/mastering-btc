# Vanity wallet
# using pybitcointools (https://pypi.python.org/pypi/bitcoin) by vitalik

import time
import bitcoin.main as btc

my_string = input("Vanity 주소:초기 2개의 문자열을 입력하세요=>")
while True:
    privKey = btc.random_key()
    pubKey = btc.privkey_to_pubkey(privKey)
    btc_addr = btc.pubkey_to_address(pubKey, 0x00)
    print("\nbitcoin address :\n ", btc_addr, len(pubKey))
    print("\nbitcoin address[0-3] : \n", btc_addr[0:3])
#    time.sleep(1)
#    if btc_addr[0:3] == '1KW':
    if btc_addr[0:2] == my_string[0:2]:
        print("{}....출현 --> vanity address 입니다".format(my_string))
        break

print("\nPrivate Key : \n", privKey)
print("\nPublic Key : \n", pubKey)
print("\nbitcoin address는 {}....로 시작됩니다.".format(my_string))
print("\nwallet address : \n", btc_addr)


input_text = input("\n종료하시겠습니까?(y): ")
if input_text in ["y", "Y"]:
    print("수고하셨습니다.")