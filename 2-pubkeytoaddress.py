# private key & public key, public key -> wallet address
# using pybitcointools (https://pypi.python.org/pypi/bitcoin) by vitalik

import bitcoin.main as btc

while True:
    privKey = btc.random_key()
    dPrivKey = btc.decode_privkey(privKey, 'hex')
    if dPrivKey > btc.N:  # secp256k1 의 N 보다 작으면 OK
        print("secp256k1이 N보다 크므로 예외사항입니다.")
        break

    # generating from private key to public key (prefix : 0x04, uncompressed)
    Uncompressed_pubKey = btc.privkey_to_pubkey(privKey)

    # public key => 160bit public key hash
    pubHash160 = btc.hash160(btc.encode_pubkey(Uncompressed_pubKey, 'bin'))

    # from public key to Mainnet wallet address (prefix : 0x00)
    mainnet_address1 = btc.pubkey_to_address(Uncompressed_pubKey, 0x00)

    # 160 bit public key hash => wallet address
    mainnet_address2 = btc.hex_to_b58check(pubHash160, 0x00)

    # public key => Testnet wallet address (prefix : 0x6f)
    testnet_address3 = btc.pubkey_to_address(Uncompressed_pubKey, 0x6f)

    print("\nPrivate key : ", privKey)
    print("\nUncompressed Public key : ", Uncompressed_pubKey)
    print("\nPublickey => 160bit hash : ", pubHash160)
    print("\nprefix 0x00 Mainnet wallet address : ", mainnet_address1)

    print("\nMainnet wallet address : ", mainnet_address2)
    print("\nTestnet address 0x6f : ", testnet_address3)

    input_text = input("\n종료하시겠습니까?(y): ")
    if input_text in ["y", "Y"]:
        print("수고하셨습니다.")
        break
    else:
        pass