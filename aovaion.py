def main():
    txt = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4"

    n=3
    txt3gram = [txt[i:i+n] for i in range(0, len(txt), n)]
    decode_lst = []

    for i in range(len(txt3gram)):
        decode_lst.append(txt3gram[i][2]+txt3gram[i][0]+txt3gram[i][1])

    print(''.join(decode_lst))


if __name__ == '__main__':
    main()