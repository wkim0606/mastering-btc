# package : pybitcointools (https://pypi.python.org/pypi/bitcoin written by vitalik
# ECDSA Test

import bitcoin.main as btc

while True:
    d=btc.random_key() # private key => d 
    G=btc.getG()  # generator, Tuple
    Gx,Gy=int(G[0]), int(G[1])
    Q=btc.privkey_to_pubkey(d) # public key => Q =d*G

    print("\n Private Key(d)=> ", d, "\t ==Len(byte)=>", len(d))
    print("\n Gx, Gy의 좌표 =>", tuple(G))
    print("\n ==Public Key Q=d*G => 04xy uncompressed\n", Q,\
        "\t ==Len(byte)=>", len(Q))

    message="ABCD This message is the original document for testing ECDSA."
    en_m=message.encode() # default encoding to utf-8
    print("\n ==The encoded message is =>\n", en_m, "type of en_m =>", type(en_m))
    print("\n -- encoded msg is =>", list(en_m))

    v,r,s=btc.ecdsa_raw_sign(btc.electrum_sig_hash(en_m),d)
    print("\n ==ECDSA raw Signature Result(v)=> \n", v)
    print("\n ==ECDSA raw Signature Result(r)=> \n", r)
    print("\n ==ECDSA Signature Result(s)=> \n", s)

    sig1=btc.encode_sig(v,r,s)
    print("\n ==Signature Result(sig1)=>\n", sig1)

    sig2=btc.ecdsa_sign(en_m,d)  # ecdsa_sign(en_m,d) 함수안에 btc.encode_sig() 존재
    print("\n ==Signature Result(sig2)=>\n", sig2)

    v=btc.ecdsa_verify(en_m,sig2,Q)
    print("\n ==v's Bool=>\t", v)

    print("\nMessage =", en_m.decode())
    if v:
        print("\n Valid Signature")
    else:
        print("\n Invalid Signature") 

    input_text = input("\n종료하시겠습니까?(y): ")
    if input_text in ["y", "Y"]:
        print("수고하셨습니다.")
        break