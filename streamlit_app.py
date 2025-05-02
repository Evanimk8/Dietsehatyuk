import streamlit as st

st.set_page_config(page_title="Menu Diet Sehat Harian", layout="centered")

st.title("🥗 Rekomendasi Menu Diet Sehat Harian")
st.markdown("Pilih kategori diet dan waktu makan untuk mendapatkan ide menu sehat yang sesuai.")

# Pilihan kategori diet
kategori = st.selectbox("Pilih Kategori Diet", [
    "Rendah Karbohidrat",
    "Tinggi Protein",
    "Vegetarian",
    "Rendah Lemak",
    "Detoks Harian"
])

# Pilihan waktu makan
waktu = st.selectbox("Pilih Waktu Makan", ["Pagi", "Siang", "Malam"])

# Database menu diet
menu_diet = {
    "Rendah Karbohidrat": {
        "Pagi": ["Omelet bayam + alpukat", "Greek yogurt + biji chia"],
        "Siang": ["Dada ayam panggang + salad sayur", "Ikan kukus + brokoli"],
        "Malam": ["Sup ayam bening + telur rebus", "Tumis tahu + sayuran hijau"]
    },
    "Tinggi Protein": {
        "Pagi": ["Telur rebus + susu rendah lemak", "Smoothie protein + pisang"],
        "Siang": ["Dada ayam + nasi merah + sayur", "Tuna salad + quinoa"],
        "Malam": ["Tahu panggang + kacang panjang", "Telur dadar + sayur rebus"]
    },
    "Vegetarian": {
        "Pagi": ["Oatmeal + buah potong", "Roti gandum + selai kacang"],
        "Siang": ["Tumis tahu + tempe + sayur", "Nasi merah + sup bayam"],
        "Malam": ["Sup labu + roti gandum", "Salad sayur + kentang rebus"]
    },
    "Rendah Lemak": {
        "Pagi": ["Smoothie buah + oat", "Roti gandum + putih telur"],
        "Siang": ["Sayur kukus + ayam rebus", "Sup bening + nasi merah"],
        "Malam": ["Tahu rebus + brokoli kukus", "Sup sayur + telur rebus"]
    },
    "Detoks Harian": {
        "Pagi": ["Infused water + buah segar", "Jus seledri + apel hijau"],
        "Siang": ["Salad sayur + lemon dressing", "Jus bit + wortel"],
        "Malam": ["Sup sayur ringan", "Smoothie sayur hijau"]
    }
}

if st.button("Tampilkan Menu"):
    st.subheader(f"🍽️ Menu Diet {kategori} - Waktu Makan: {waktu}")
    menu_list = menu_diet.get(kategori, {}).get(waktu, ["Menu tidak tersedia"])
    for item in menu_list:
        st.markdown(f"- {item}")
