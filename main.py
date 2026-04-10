import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
#dung thu vien
def priori1(data,sup,con):

    te=TransactionEncoder()
    te_ary = te.fit(data).transform(data)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    #tim tap pho bien
    frequent_itemsets = apriori(df, min_support=sup, use_colnames=True)

    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=con)

    print("--- Các tập mục phổ biến ---")
    print(frequent_itemsets)
    print("\n--- Luật kết hợp tìm được ---")
    print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

def main():
    data=[
        ["Facebook","Messenger"],
        ["Facebook","Youtube"],
        ["Facebook","Messenger","Youtube"],
        ["Youtube","Tiktok"],
        ["Facebook","Messenger"]
    ]
    sup=numberInput("Nhap nguong support: ")
    con=numberInput("Nhap nguong confidence: ")
    priori1(data,sup,con)

if __name__=="__main__":
    main()