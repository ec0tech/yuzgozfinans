import streamlit as st
import pandas as pd

# ----------------------------------------------------
# SAYFA YAPILANDIRMASI
# ----------------------------------------------------
st.set_page_config(
    page_title="YüzGözFinans",
    page_icon="👁️",
    layout="wide"
)

# ----------------------------------------------------
# ÖZEL CSS
# ----------------------------------------------------
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
    }
    .metric-card {
        background-color: #1E2229;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #2D3748;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 12px;
    }
    .metric-card h4 {
        margin-top: 0;
    }
    h1, h2, h3 {
        color: #FAFAFA !important;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# ÜST BANNER / BAŞLIK ALANI
# ----------------------------------------------------
st.title("👁️ YüzGözFinans")
st.markdown("##### *Parana YüzGöz Ol*")
st.markdown(
    "*Yatırım tavsiyesi değil; dünya gündeminin mekanizması, finansal okuryazarlık "
    "ve veri analitiği.*"
)

st.info(
    "📌 **Bu site gelişim aşamasındadır.** Şu an bir başlangıç (MVP) sürümünü "
    "görüntülüyorsunuz. Önümüzdeki dönemde yeni yazılar, analizler ve araçlar "
    "eklenmeye devam edecek. Sitedeki hiçbir içerik yatırım tavsiyesi değildir; "
    "amaç yalnızca eğitim ve farkındalıktır."
)

st.markdown("---")

# ----------------------------------------------------
# SAYFA SEÇİMİ (session_state ile hafızada tutulur)
# ----------------------------------------------------
SAYFALAR = ["🏠 Ana Sayfa", "📚 Finans 101", "🔎 Gündem Süzgeci", "📊 YüzGözAnaliz"]

if "secim" not in st.session_state:
    st.session_state.secim = "🏠 Ana Sayfa"

# ----------------------------------------------------
# YAN MENÜ (SIDEBAR)
# ----------------------------------------------------
st.sidebar.image("https://img.icons8.com/fluency/96/stocks-growth.png", width=80)
st.sidebar.title("Navigasyon")
st.sidebar.radio(
    "Gitmek istediğin alanı seç:",
    SAYFALAR,
    key="secim"
)

# ----------------------------------------------------
# ANA SAYFA
# ----------------------------------------------------
if st.session_state.secim == "🏠 Ana Sayfa":
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🎯 Projenin Amacı")
        st.info(
            "YüzGözFinans; karmaşık küresel ekonomik olayları arkasındaki "
            "neden-sonuç ilişkileriyle okuyucuya aktaran, tüyolardan arındırılmış "
            "saf bir finansal farkındalık ve eğitim platformudur."
        )
    with col2:
        st.markdown("### 🚀 Öne Çıkan Özellikler")
        st.markdown(
            "- **Manipülasyonsuz eğitim:** Sadece mekanizma öğretir.\n"
            "- **Python destekli:** Gerçek zamanlı veri işleme araçları.\n"
            "- **YüzGözAnaliz:** İnteraktif simülasyonlar ve hesaplayıcılar."
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🧭 Hadi Başlayalım!")

    kutu1, kutu2, kutu3 = st.columns(3)

    with kutu1:
        with st.container(border=True):
            st.markdown("#### 📚 Finans 101")
            st.caption("Temel finans kavramları, sade anlatım.")
            if st.button("Keşfet", key="btn_finans101", use_container_width=True):
                st.session_state.secim = "📚 Finans 101"
                st.rerun()

    with kutu2:
        with st.container(border=True):
            st.markdown("#### 🔎 Gündem Süzgeci")
            st.caption("Dünya ekonomisi, haftalık gündemin nabzı.")
            if st.button("Keşfet", key="btn_gundem", use_container_width=True):
                st.session_state.secim = "🔎 Gündem Süzgeci"
                st.rerun()

    with kutu3:
        with st.container(border=True):
            st.markdown("#### 📊 YüzGözAnaliz")
            st.caption("İnteraktif hesaplayıcılar.")
            if st.button("Keşfet", key="btn_analiz", use_container_width=True):
                st.session_state.secim = "📊 YüzGözAnaliz"
                st.rerun()

# ----------------------------------------------------
# FİNANS 101
# ----------------------------------------------------
elif st.session_state.secim == "📚 Finans 101":
    st.header("📚 Finans 101: Temel Kavramlar")
    st.write("Ekonominin temel taşlarını en sade, anlaşılır dille keşfet.")

    with st.expander("Enflasyon Nedir? Aslında Paramız Neden Erir?", expanded=True):
        st.write(
            "Enflasyon, genel fiyat düzeyinin sürekli artması durumudur. "
            "Satın alma gücünün azalması demektir. Geçen yıl 100 TL ile "
            "aldığınız bir sepet ürün, bu yıl 130 TL'ye çıkıyorsa, paranızın "
            "değeri o oranda erimiş demektir."
        )

    with st.expander("Bileşik Getiri Nedir?"):
        st.write(
            "Bileşik getiri, kazandığınız getirinin de tekrar getiri üretmeye "
            "başlaması prensibidir. Zaman geçtikçe küçük bir başlangıç tutarı "
            "bile katlanarak büyüyebilir. Bu mantık borçlar için de aynı şekilde "
            "işler, bu yüzden erken ödeme her zaman avantajlıdır."
        )

    st.caption("🔜 Bu bölüme yakında yeni kavramlar eklenecek: faiz oranları, bütçe yönetimi, risk ve çeşitlendirme...")

# ----------------------------------------------------
# GÜNDEM SÜZGECİ
# ----------------------------------------------------
elif st.session_state.secim == "🔎 Gündem Süzgeci":
    st.header("🔎 Gündem Süzgeci: Dünya ve Ekonomi")
    st.write(
        "Küresel haberleri olduğu gibi değil, mekanizmasını süzerek aktarıyoruz — "
        "tavsiye vermiyoruz, sadece anlatıyoruz."
    )

    st.markdown("""
        <div class="metric-card">
            <h4>Haftanın Vakası: Çip Krizi ve Otomotiv</h4>
            <p>Uzak Doğu'daki yarı iletken üretim aksamalarının yerel piyasalara ve
            hanehalkı bütçesine zincirleme etkisi nedir?</p>
        </div>
    """, unsafe_allow_html=True)

    st.warning("✍️ Çok yakında yeni süzülmüş analizler burada olacak — takipte kalın!")

# ----------------------------------------------------
# YÜZGÖZANALİZ
# ----------------------------------------------------
elif st.session_state.secim == "📊 YüzGözAnaliz":
    st.header("📊 YüzGözAnaliz: Simülasyon Merkezi")
    st.write("Python altyapısıyla güçlendirilmiş interaktif karar destek araçları.")

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        enflasyon = st.slider("Yıllık Tahmini Enflasyon Oranı (%)", 10, 100, 40)
    with col_b:
        para = st.number_input("Başlangıç Tutarı (TL)", value=10000)
    with col_c:
        yil = st.slider("Süre (Yıl)", 1, 10, 5)

    veri = []
    for y in range(0, yil + 1):
        deger = para / ((1 + enflasyon / 100) ** y)
        veri.append({"Yıl": y, "Reel Alım Gücü (TL)": round(deger, 2)})

    df = pd.DataFrame(veri)
    son_deger = df.iloc[-1]["Reel Alım Gücü (TL)"]
    kayip_yuzde = ((para - son_deger) / para) * 100 if para > 0 else 0

    st.markdown("<br>", unsafe_allow_html=True)
    st.metric(
        label=f"Enflasyon Karşısında {yil} Yıl Sonraki Alım Gücü",
        value=f"{son_deger:,.2f} TL",
        delta=f"-%{kayip_yuzde:.1f} Kayıp",
        delta_color="inverse"
    )

    st.line_chart(df.set_index("Yıl"))

    st.caption(
        "⚠️ Bu hesaplama basitleştirilmiştir; gerçek enflasyon oranları yıldan "
        "yıla değişir. Sonuçlar bilgilendirme amaçlıdır, yatırım tavsiyesi değildir."
    )

# ----------------------------------------------------
# ALT BİLGİ
# ----------------------------------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>YüzGözFinans | Eğitim Amaçlı "
    "Portfolyo Projesidir 🚀</p>",
    unsafe_allow_html=True
)
