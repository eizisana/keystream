while True:
    print("Keystream Generator")
    n = input("Panjang Key(n) : ")
    key = input("Nilai Key (sebanyak "+ n + ") (1/0) :")
    L = input("Panjang Key(L) : ")
    key1 = key
    key2 = key

    for i in range(2**len(key1)-len(key1)-1):
        key1 += str(int(key1[i])^int(key1[i+3]))
    i = 0
    while(len(key2)<int(L)):
        key2 += str(int(key2[i])^int(key2[i+3]))
        i +=1

    print("\nPanjang Keystream : " + str(2**int(n)-1))
    print("Keystream(n): " + key1)
    print("Keystream(L): " + key2)

    repeat = input("tekan y untuk mengulangi dan n untuk menutup : ")
    print()
    if(repeat == 'n'):
        break

input("Press Enter to exit...")