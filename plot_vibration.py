import pandas as pd
import matplotlib.pyplot as plt

# โหลดข้อมูล
df = pd.read_csv('results/prediction_results.csv')

# 🔥 ใส่ชื่อไฟล์ (แก้ให้ตรงกับของคุณ)
df['Label'] = [
    'CH-Jun', 'CH-Oct', 'CH-Sep',
    'Pump-Jun', 'Pump-Oct', 'Pump-Sep',
    'Jockey-Jun', 'Jockey-Oct', 'Jockey-Sep'
]

# ฟังก์ชันแบ่ง Zone
def classify_zone(rms):
    if rms < 2.8:
        return 'Zone(Green)'
    elif rms < 7.1:
        return 'Zone(Yellow)'
    elif rms < 18:
        return 'Zone(Orange)'
    else:
        return 'Zone(Red)'

# เพิ่ม Zone
df['Zone'] = df['RMS'].apply(classify_zone)

# สีของแต่ละ Zone
colors = {
    'Zone(Green)': 'green',
    'Zone(Yellow)': 'gold',
    'Zone(Orange)': 'orange',
    'Zone(Red)': 'red'
}

plt.figure()

# 🔥 plot ตามชื่อไฟล์
plt.plot(df['Label'], df['RMS'], marker='o', color='blue', label='RMS')

# จุดสีตาม Zone
for zone in colors:
    subset = df[df['Zone'] == zone]
    plt.scatter(subset['Label'], subset['RMS'],
                color=colors[zone], label=zone)

# เส้นแบ่ง Zone
plt.axhline(y=2.8, linestyle='--', color='green', label='Green/Yellow')
plt.axhline(y=7.1, linestyle='--', color='orange', label='Yellow/Orange')
plt.axhline(y=18.0, linestyle='--', color='red', label='Orange/Red')

# label
plt.xlabel('Machine & Month')
plt.ylabel('RMS')
plt.title('Vibration by Machine and Time')

# หมุนแกน X (สำคัญมาก)
plt.xticks(rotation=45)

plt.legend()
plt.grid()

# save รูป
plt.savefig('vibration_graph.png', bbox_inches='tight')

plt.show()