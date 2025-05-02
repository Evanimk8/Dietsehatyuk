import streamlit as st

st.set_page_config(page_title="Kalkulator Diet Sehat", layout="centered")

st.title("🧮 Kalkulator Diet Sehat")
st.markdown("Hitung kebutuhan kalori harian Anda berdasarkan data pribadi dan aktivitas harian.")

# Input data pengguna
gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
age = st.number_input("Usia (tahun)", min_value=10, max_value=100, value=25)
weight = st.number_input("Berat Badan (kg)", min_value=30.0, max_value=200.0, value=65.0)
height = st.number_input("Tinggi Badan (cm)", min_value=100.0, max_value=250.0, value=170.0)

activity_level = st.selectbox("Tingkat Aktivitas Fisik", [
    "Sedentari (jarang olahraga)",
    "Ringan (1-3 hari/minggu)",
    "Sedang (3-5 hari/minggu)",
    "Berat (6-7 hari/minggu)",
    "Sangat Berat (latihan fisik atau kerja berat)"
])

# Rumus BMR (Mifflin-St Jeor)
def hitung_bmr(gender, weight, height, age):
    if gender == "Laki-laki":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

# Faktor aktivitas
def get_activity_factor(level):
    return {
        "Sedentari (jarang olahraga)": 1.2,
        "Ringan (1-3 hari/minggu)": 1.375,
        "Sedang (3-5 hari/minggu)": 1.55,
        "Berat (6-7 hari/minggu)": 1.725,
        "Sangat Berat (latihan fisik atau kerja berat)": 1.9
    }.get(level, 1.2)

# Kalkulasi saat tombol ditekan
if st.button("Hitung Kalori Harian"):
    bmr = hitung_bmr(gender, weight, height, age)
    aktivitas = get_activity_factor(activity_level)
    kebutuhan_kalori = bmr * aktivitas

    st.success(f"✅ Estimasi kebutuhan kalori harian Anda: **{int(kebutuhan_kalori)} kalori**")
    st.markdown("Gunakan ini sebagai acuan dalam merencanakan diet harian Anda.")

    st.info("""
    📌 **Tips**:
    - Untuk menurunkan berat badan: makan sekitar 500 kalori lebih sedikit dari kebutuhan harian.
    - Untuk menambah berat badan: konsumsi sekitar 500 kalori lebih banyak.
    """)

