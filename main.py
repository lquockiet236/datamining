import numpy as np
from sklearn.neighbors import KNeighborsClassifier
def knn():
    print("--- Chương trình dự đoán k-NN đơn giản ---")
    
    # 1. Nhập dữ liệu huấn luyện (Training Data)
    try:
        n_points = int(input("Nhập số lượng mẫu dữ liệu huấn luyện: "))
        n_features = int(input("Nhập số đặc trưng (ví dụ: Chiều cao, Cân nặng -> 2): "))
        
        X_train = []
        y_train = []
        
        for i in range(n_points):
            print(f"\nNhập dữ liệu cho mẫu thứ {i+1}:")
            features = [float(x) for x in input(f"  Nhập {n_features} giá trị đặc trưng (cách nhau bởi dấu cách): ").split()]
            label = input("  Nhập nhãn của mẫu này (ví dụ: 'Thấp', 'Cao' hoặc 0, 1): ")
            X_train.append(features)
            y_train.append(label)

        # 2. Khởi tạo mô hình
        k = int(input("\nNhập số lượng láng giềng k (thường là số lẻ, ví dụ: 3): "))
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, y_train)

        # 3. Nhập điểm cần dự đoán
        print("\n--- Dự đoán mẫu mới ---")
        x_new = [float(x) for x in input(f"Nhập {n_features} giá trị của mẫu cần dự đoán: ").split()]
        
        # Dự đoán
        prediction = model.predict([x_new])
        
        print("-" * 30)
        print(f"Kết quả dự đoán: Nhãn của mẫu mới là: {prediction[0]}")
        print("-" * 30)

    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập số hợp lệ.")

def main():
    pass
if __name__ == "__main__":
    main()