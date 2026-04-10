import pandas as pd
from sklearn.preprocessing import MinMaxScaler
df=pd.read_csv("customers_biendoidulieu_dataset_cleaned.csv")

def minMaxNormalization():
    global df
    cols = ["age", "income", "score", "weight", "height", "order_value"]
    for c in cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    scaler = MinMaxScaler(feature_range=(0, 1))
    df[cols] = scaler.fit_transform(df[cols])
def xayDungThuocTinh():
    df['BMI']=(df["weight"]/(df["height"]/100)**2).round(2)
def incomeLevel(x):
    if x<5000000:
        return "Thap"
    elif x<=20000000:
        return "Trung binh"
    else:
        return "Cao"
def chuanHoaTP(city):
    c=str(city).strip().lower()
    if c in df['city']:
        return "HCM"
def tongQuatHoaTP():
    df["city"] = df["city"].apply(chuanHoaTP)

def roiRacHoa():
    df['incomeLevel']=df['income'].apply(incomeLevel)
def main():
    #minMaxNormalization()
    xayDungThuocTinh()
    roiRacHoa()
    #chuanHoaTP()
    print(df)
if __name__=="__main__":
    main()
