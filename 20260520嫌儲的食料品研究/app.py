import pandas as pd

def read_csv(path):
    data_list=[]

    df = pd.read_csv(path,encoding='cp932')
    print(df)
    #df.drop(index=[''], inplace=True)
    for idx,i in enumerate(df):
        if idx==0:
            continue
        #print(df[i])
        #print(df[i][1])
        item_name = i
        unit_name = df[i][0]
        price_val = df[i][1]
        print("品目:"+str(item_name))
        print("単位:"+unit_name)
        print("平均価格:"+price_val)

        data_list.append({
            '品目': item_name,
            '単位': unit_name,
            '平均価格': price_val
        })
    return data_list

data_list=read_csv('b002-1.csv')+read_csv('b002-2.csv')

result = pd.DataFrame(data_list)

print(result)
result.to_csv("【嫌儲的分析】主要品目の東京都区部小売価格【2025年4月～2026年4月】.csv")