# package : pybitcointools (https://pypi.python.org/pypi/bitcoin written by vitalik
import os
import random
import time
import datetime
import hashlib
import bitcoin.main as btc

# secp256k1 domain paramter (order 위수 of G)
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
# CSPRNG : os.urandom(), random() 두함수를 사용하여 hash256()으로 256bit random number 추출
def random_key(): 
    r = str(os.urandom(32)) \
            + str(random.randrange(2**256)) \
            + str(int(time.time() * 1000000))
    encoded_r = r.encode('utf-8')  # 또는 bytes(r, 'utf-8') 사용 가능
    h = hashlib.sha256(encoded_r).digest()
    # 다음은 hex 로 바꾸는 과정을 확인
    print("sha256(encoded_r)'s length=>", hashlib.sha256(encoded_r).digest_size, "bytes")
    print("h type is =>", type(h), "\n""h list is =>", list(h))
    for y in h:
        print("Integer=>", int(y), "Hexadecimal=>""{:02x}".format(y), sep='\t')
    # 확인과정 끝
    key = ''.join('{:02x}'.format(y) for y in h) # convert it to Hex
    return key

while True :
    u_time = time.time()      # UNIX Time : 1970. 1. 1. 0시 0초 이후
    now = datetime.datetime.now()
    print("\nUnix Time:",u_time, ", 일자:",now.year,"년",now.month,"월",now.day,"일")
#    print("{}년 {}월 {}일".format(now.year, now.month, now.day))

    privkey = random_key()
    dPrivKey = btc.decode_privkey(privkey, 'hex')
    if dPrivKey > btc.N:  # secp256k1 의 N 보다 작으면 OK
        print("secp256k1이 N보다 크므로 예외사항입니다.")
        break
    print("\n == privKey Generation (HEX) ==\n", privkey) 
    print("\n == privKey Generation (Decimal) ==\n", int(privkey, 16)) 
    print("\n == PrivKey length =>", len(privkey))

    input_text = input("\n종료하시겠습니까?(y): ")
    if input_text in ["y", "Y"]:
        print("수고하셨습니다.")
        break
    else: 
        pass