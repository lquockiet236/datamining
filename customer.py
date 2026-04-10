import pandas as pd
df=pd.read_csv("customer_data.csv")


#xu li du lieu khong nhat quan
mapping={
    '8tr':8,
    'nam':'Nam',
    'male':'Nam',
    'nữ':'Nữ',  
}
df['Gioi tinh']=df['Gioi tinh'].str.lower().replace(mapping)
df['Luong (trieu)']=df['Luong (trieu)'].replace(mapping)

#xu li du lieu thieu
#df['Tuoi']=df['Tuoi'].fillna(df['Tuoi'].mode()[0], inplace=True) 
df.fillna({'Tuoi':df['Tuoi'].mode()[0]},inplace=True)
df = df.drop(df[(df['SDT'].isna()) | (df['SDT'] == 0)].index)
df['SDT'] = df['SDT'].astype(int)

#xu li du lieu nhieu
medianTuoi=df['Tuoi'].median()
df.loc[df['Tuoi'] >100, 'Tuoi'] = medianTuoi
df['Luong (trieu)'] = df['Luong (trieu)'].astype(int)
medianLuong=df['Luong (trieu)'].median()
df.loc[df['Luong (trieu)']<0,'Luong (trieu)']=medianLuong

#xu li du lieu ngoai lai
Q1 = df['Luong (trieu)'].quantile(0.25) 
Q3 = df['Luong (trieu)'].quantile(0.75) 
IQR = Q3 - Q1 
lower = Q1 - 1.5 * IQR 
upper = Q3 + 1.5 * IQR 
outliers = df[(df['Luong (trieu)'] < lower) | (df['Luong (trieu)'] > upper)]

#xu li du lieu trung lap
df.drop_duplicates(subset=['SDT'], inplace=True) 

df.to_csv('customer_data_cleaned.csv', index=False) 
print(df)
print(outliers)