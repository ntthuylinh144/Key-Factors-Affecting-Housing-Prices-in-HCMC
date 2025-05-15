## 📊 Dự đoán giá căn hộ tại TP.HCM

### 🏨 1. Giới thiệu dự án

Dự án này tập trung khai thác, phân tích và dự đoán **giá bán căn hộ/chung cư tại TP.HCM** dựa trên các đặc điểm liên quan đến vị trí, pháp lý, diện tích và loại hình bất động sản. Dữ liệu được thu thập từ các bài đăng rao bán trên trang **Chợ Tốt** vào tháng 09/2024.
- Data source: https://www.chotot.com/
- Icon source: https://www.flaticon.com/
### 📆 2. Mô tả bộ dữ liệu

* Số mẫu: **5181**
* Số biến: **15**

| Biến                    | Mô tả                         |
| ----------------------- | ----------------------------- |
| `square`                | Diện tích (m²)                |
| `property-status`       | Trạng thái bàn giao           |
| `number-of-bedrooms`    | Phòng ngủ                     |
| `number-of-bathrooms`   | Phòng tắm                     |
| `apartment-type`        | Loại hình chung cư            |
| `legal-documents`       | Pháp lý                       |
| `interior-status`       | Nội thất                      |
| `ownership_status`      | Sở hữu                        |
| `corner_apartment`      | Căn góc (1/0)                 |
| `district`              | Quận                          |
| `view`                  | View sông / view / không view |
| `latitude`, `longitude` | Vĩ độ, Kinh độ                |
| `ty/m2`                 | Giá theo tỷ/m²                |
| `price`                 | Giá bán (tỷ VND)              |

### 🧹 3. Xử lý dữ liệu

* Dọn dữ liệu: missing value, encoding, scaling
* Loại bỏ outlier (IQR đối với biến số, còn biến phân loại- dựa vào quan sát số lượng, giá trung bình và kiểm định T-test giữa các nhóm)
* Phân tích tương quan giữa các biến
* Trực quan hóa: hist, bar chart, boxplot.

### 🧠 4. Huấn luyện mô hình

So sánh 4 mô hình dự đoán giá căn hộ:

| Mô hình           | MSE        | RMSE       | MAPE       | R²         |
| ----------------- | ---------- | ---------- | ---------- | ---------- |
| Linear Regression | 0.4835     | 0.6953     | 0.1788     | 0.8180     |
| XGBoost           | 0.4074     | 0.6382     | 0.1587     | 0.8467     |
| Random Forest     | **0.3702** | **0.6084** | **0.1427** | **0.8607** |
| LightGBM          | 0.3923     | 0.6264     | 0.1571     | 0.8523     |

### 📂 5. Khai thác dữ liệu với SQL

* Tính trung bình giá / m²
* Liệt kê quận theo giá trung bình
* Tính số lượng bài đăng theo loại hình

### 📊 6. Trực quan hóa bằng Power BI

* Biểu đồ giá trung bình theo quận
* Biểu đồ phân phố giá theo view, loại hình, cơ sở vật chất
* Dashboard tương tác

### 🔧 7. Công nghệ sử dụng

* Python: pandas, seaborn, scikit-learn, xgboost, lightgbm
* SQL: MySQL
* Power BI
* Jupyter Notebook

### 🔖 8. Kết luận

* Dự án đã xây dựng mô hình Random Forest hiệu quả cao
* Hỗ trợ người mua nhà, nhà đầu tư và phát triển bất động sản

### 📄 9. Cấu trúc thư mục

```
.

├── Analysis.ipynb
│── Modeling.py
├── Queries.sql
├── Apartment_Sales_Dashboard.pbix
├── Queries_result.docx
│── Model_result.csv
│── regression_plot
│── icons
│── README.md
```

---

> Dự án học máy - Dự đoán giá bất động sản
> TP.HCM, 09/2024
