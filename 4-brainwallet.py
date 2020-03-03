# Brain wallet
# using pybitcointools (https://pypi.python.org/pypi/bitcoin) by vitalik
# brainwallet 은 사용자가 선택한 단어로 구성되며, Mnemonic code words는 지갑에서 무작위로 
# 단어열을 생성해서 제시 (hangul/english 입력 가능)

import bitcoin.main as btc

passphrase = "" 

while True : 

    passphrase = input("\n\n당신의 Mnemonic Code를 입력=> ")

    if (passphrase.isdigit()) : 
        break

    privKey = btc.sha256(passphrase)
    dPrivKey = btc.decode_privkey(privKey, 'hex') # hexadecimal code를 decimal code 로 변환 
    if dPrivKey > btc.N:  # secp256k1 의 N 보다 작으면 OK
        print("secp256k1이 N보다 크므로 예외사항입니다.")
        break

    # generating from private key to public key (prefix: 0x04, uncompressed) 
    pubKey = btc.privkey_to_pubkey(privKey)

    # from public key to Mainnet wallet address (prefix : 0x00)
    main_btc_addr = btc.pubkey_to_address(pubKey, 0x00)

    # public key => Testnet wallet address (prefix : 0x6f)
    test_btc_addr = btc.pubkey_to_address(pubKey, 0x6f)

    print("\npassphrase \n ", passphrase)
    print("\nprivate key to use passphrase:\n ", privKey, len(privKey))
    print("\npublic key : uncompressed 0x04 \n ", pubKey, len(pubKey))
    print("\nMainnet wallet address : prefix 0x00 \n ", main_btc_addr, len(main_btc_addr))
    print("\nTestnet address : prefix 0x6f \n ", test_btc_addr, len(test_btc_addr))

    input_text = input("\n종료하시겠습니까?(y): ")
    if input_text in ["y", "Y"]:
        print("수고하셨습니다.")
        break