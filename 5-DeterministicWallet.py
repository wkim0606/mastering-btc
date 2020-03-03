# pybitcointools (https://github.com/vbuterin/pybitcointools)
import bitcoin.main as btc

# Initial Seed
seed = "this is just initial seed value, 이것은 초기 시드 값입니다."

# making Private Key n number
n = 100
error = 0
for i in range(1, (n+1)): # from 1 to 100
    seed += str(i)
    privKey = btc.sha256(seed)
    dPrivKey = btc.decode_privkey(privKey, 'hex')   # hex ==> decimal 로 변환
    if dPrivKey < btc.N:                            # secp256k1 의 N 보다 작으면 OK
        print("Key (%d) : %s" % (i, privKey))
    else:
        error += 1

if error > 0:
    print("initial seed로 private key %d개를 만들지 못했습니다." % n)