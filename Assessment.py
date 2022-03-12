import pandas as pd
import matplotlib.pyplot as plt

with open('Overbond Assessment\XICE_Bond_Close2.txt', 'r', encoding='UTF-8') as f:
    final = []
    while True:
        info_block = []
        new_header = f.readline()
        if not new_header:
            break
        info_block.append(new_header.replace('\n', ''))
        for i in range(9):
            new_line = f.readline()
            info_block.append(new_line.replace('\n', ''))

        if all(info_block) == '':
            break
        # print(info_block)

        issurance_date = clean_bid = clean_ask = last_price = None

        if ';DIs' in info_block[6]:
            for i in info_block[6].split(';'):
                if i[0:3] == 'DIs':
                   issurance_date = i 
        # print(issurance_date)

        if 'BPr' in info_block[9]:
            clean_bid = info_block[9].split(';')[7]
        # print(clean_bid)
        
        if 'APl' in info_block[9]:
            for i in info_block[9].split(';'):
                if 'APl' in i:
                    clean_ask = i
        # print(clean_ask)

        if ';Pl' in info_block[9]:
            for i in info_block[9].split(';'):
                if i[0:2] == 'Pl':
                   last_price = i 
        # print(last_price)
        # (info_block)


        issurance_date = int(issurance_date[3:]) if issurance_date else None
        # print(issurance_date)
        clean_bid = float(clean_bid[3:]) if clean_bid else None
        # print(clean_bid)
        clean_ask = float(clean_ask[3:]) if clean_ask else None
        # print(clean_ask)
        last_price = float(last_price[2:]) if last_price else None
        # print(last_price)

        final.append((issurance_date,clean_bid,clean_ask,last_price))
        
    df = pd.DataFrame(final, columns=['IssuanceDate','CleanBid','CleanAsk','LastPrice'])
    print(df)
    plt.scatter(df.IssuanceDate, df.CleanBid, label="CleanBid")
    plt.scatter(df.IssuanceDate, df.CleanAsk, label="CleanAsk")
    plt.scatter(df.IssuanceDate, df.LastPrice, label="LastPrice")
    plt.legend()
    plt.show()