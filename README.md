
# Vibration Predictive Maintenance 

โปรเจคนี้เป็นการพัฒนาโมเดล **Predictive Maintenance** สำหรับการวิเคราะห์สภาพเครื่องจักรจากข้อมูล **Vibration Signal (การสั่นสะเทือน)** โดยใช้ **Linear Regression** เพื่อทำนายค่าการสั่นสะเทือน (RMS) และจัดประเภทสภาพเครื่องจักรตามมาตรฐาน **ISO 10816**

---

## วัตถุประสงค์ของโครงงาน

* วิเคราะห์ข้อมูล **Vibration Signal**
* สกัดคุณลักษณะสำคัญของสัญญาณ (Feature Extraction)
* สร้างโมเดล **Machine Learning (Linear Regression)** เพื่อทำนายค่าการสั่นสะเทือน
* จัดประเภทสภาพเครื่องจักรตาม **ISO 10816 Vibration Zone**
* ใช้แนวคิด **Predictive Maintenance** เพื่อช่วยในการวางแผนบำรุงรักษาเครื่องจักร

---

## โครงสร้างโปรเจค

```
vibration-predictive-maintenance
│
├── data
│   ├── raw                # ไฟล์ข้อมูล vibration ดิบ
│   └── processed          # ไฟล์ข้อมูลหลังสกัด feature
│
├── models                 # โมเดล Machine Learning ที่ train แล้ว
│
├── results                # ผลลัพธ์การทำนาย
│
├── src
│   ├── preprocess.py
│   ├── feature_engineering.py
│   └── iso_zone_classifier.py
│
├── extract_features.py    # สกัด Feature จาก vibration signal
├── train_model.py         # สร้างและ train Linear Regression model
├── predict.py             # ทำนายค่า RMS และจัด ISO Zone
│
├── requirements.txt
└── README.md
```

---

## Feature ที่ใช้ในการวิเคราะห์

จากสัญญาณ Vibration จะทำการสกัด Feature ดังนี้

* RMS (Root Mean Square)
* Peak
* Peak-to-Peak
* Kurtosis
* Skewness
* Crest Factor

Feature เหล่านี้เป็นตัวชี้วัดที่ใช้กันทั่วไปในงาน **Vibration Analysis ของเครื่องจักร**

---

## Machine Learning Model

ในโปรเจคนี้ใช้โมเดล

**Linear Regression**

เพื่อทำนายค่า

```
Predicted RMS
```

จาก Feature ของสัญญาณการสั่นสะเทือน

---

## การจัดประเภทสภาพเครื่องจักร (ISO 10816)

หลังจากทำนายค่า RMS แล้ว จะนำไปจัดประเภทตามมาตรฐาน ISO

| Zone         | ความหมาย                     |
| ------------ | ---------------------------- |
| Zone(Green)  | Newly Commissioned Machinery |
| Zone(Yellow) | Unrestricted Operation       |
| Zone(Orange) | Restricted Operation         |
| Zone(Red)    | Damage Occurs                |

---

## ขั้นตอนการใช้งาน

### 1 ติดตั้ง Library

```
pip install -r requirements.txt
```

---

### 2 สกัด Feature จากข้อมูล Vibration

```
python extract_features.py
```

ผลลัพธ์จะถูกบันทึกที่

```
data/processed/features.csv
```

---

### 3 Train โมเดล Machine Learning

```
python train_model.py
```

โมเดลจะถูกบันทึกที่

```
models/linear_regression_model.pkl
```

---

### 4 ทำนายสภาพเครื่องจักร

```
python predict.py
```

ผลลัพธ์จะถูกบันทึกที่

```
results/prediction_results.csv
```

---

## เทคโนโลยีที่ใช้

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib

---

## แนวคิดที่ใช้ในโครงงาน

โปรเจคนี้ใช้แนวคิด **Predictive Maintenance** ซึ่งเป็นการใช้ข้อมูลและ Machine Learning เพื่อคาดการณ์สภาพเครื่องจักรล่วงหน้า ช่วยลดการหยุดเครื่องจักรโดยไม่คาดคิด และเพิ่มประสิทธิภาพในการบำรุงรักษา
