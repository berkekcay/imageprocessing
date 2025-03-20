import streamlit as st

def main():
    st.set_page_config(page_title="AI Destekli Sosyal Medya Optimizasyonu", layout="wide")
    
    # Özel CSS ile renkleri ayarlıyoruz
    st.markdown("""
    <style>
    :root {
        --primary-color: #1DA1F2; /* Mavi */
        --secondary-color: #FFFFFF; /* Beyaz */
        --accent-color: #FF4500; /* Turuncu */
        --background-color: #F5F8FA; /* Açık Gri */
        --text-color: #14171A; /* Koyu Gri */
    }
    
    .stApp {
        background-color: var(--background-color);
        color: var(--text-color);
    }
    
    .stButton>button {
        background-color: var(--primary-color);
        color: var(--secondary-color);
        font-weight: bold;
        border-radius: 8px;
    }
    
    .stFileUploader {
        background-color: var(--secondary-color);
        padding: 10px;
        border-radius: 10px;
    }
    
    .stMetric {
        background-color: var(--accent-color);
        padding: 5px;
        border-radius: 8px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("📸 AI Destekli Sosyal Medya İçerik Optimizasyonu")
    st.subheader("AI destekli analiz ile sosyal medya görsellerinizi optimize edin ve daha fazla etkileşim alın!")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        uploaded_image = st.file_uploader("📤 Bir görsel yükleyin", type=["jpg", "png", "jpeg"])
        st.button("🔍 Analiz Başlat")
    
    if uploaded_image:
        st.image(uploaded_image, caption="Yüklenen Görsel", use_container_width=True)
        st.success("✅ Görsel başarıyla yüklendi!")
    else:
        st.info("Henüz bir görsel yüklenmedi.")
    
    st.markdown("---")
    st.subheader("📊 Analiz Sonuçları")
    
    col3, col4, col5 = st.columns(3)
    with col3:
        st.metric(label="🌟 Parlaklık", value="-", delta="-")
    with col4:
        st.metric(label="🎭 Kontrast", value="-", delta="-")
    with col5:
        st.metric(label="🔍 Netlik", value="-", delta="-")
    
    st.markdown("---")
    st.subheader("💡 Optimizasyon Önerileri")
    st.write("- AI tarafından önerilen optimizasyonlar burada görünecek.")
    
    st.markdown("---")
    st.info("📌 Daha iyi etkileşim almak için AI önerilerini dikkate alın ve içeriğinizi optimize edin!")

if __name__ == "__main__":
    main()
