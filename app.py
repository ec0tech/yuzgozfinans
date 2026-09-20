import streamlit as st
import pandas as pd

# ----------------------------------------------------
# SAYFA AYARLARI
# ----------------------------------------------------
st.set_page_config(
    page_title="YüzGözFinans",
    page_icon="👁️",
    layout="wide",
)

# ----------------------------------------------------
# ÜST BAŞLIK
# ----------------------------------------------------
st.title("👁️ YüzGözFinans")
st.caption("Finansal okuryazarlık için gözünüzü açık tutun.")

st.info(
    "📌 **Bu site gelişim aşamasındadır.** Şu an bir başlangıç (MVP) sürümünü "
    "görüntülüyorsunuz. Önümüzdeki dönemde yeni yazılar, analizler ve araçlar "
    "eklenmeye devam edecek. Sitedeki hiçbir içerik yatırım tavsiyesi değildir; "
    "amaç yalnızca eğitim ve farkındalıktır."
)

# ----------------------------------------------------
# SEKMELER
# ----------------------------------------------------
tab1, tab2, tab3 = st.tabs(["📘 Finans 101", "🧮 Python Köşesi", "🌍 Gündem Analizleri"])

# ==========================================================
# TAB 1 - FİNANS 101
# ==========================================================
with tab1:
    st.header("Finans 101: Temel Kavramlar")
    st.write("Karmaşık finans terimlerini sade bir dille anlatıyoruz.")

    with st.expander("💡 Enflasyon Nedir?", expanded=True):
        st.markdown("""
Enflasyon, bir ekonomideki mal ve hizmetlerin genel fiyat düzeyinin zaman içinde
artması ve buna bağlı olarak paranın satın alma gücünün azalmasıdır.

**Basit bir örnekle düşünelim:**
Geçen yıl 100 TL ile alabildiğiniz bir sepet market ürünü, bu yıl aynı sepeti
almak için 130 TL gerektiriyorsa, yıllık enflasyon oranı yaklaşık %30 demektir.
Aynı 100 TL'niz artık daha az ürün alabiliyor — yani paranızın değeri "eridi".

**Neden önemli?**
- Elinizdeki nakit, hiçbir yere yatırılmadığında enflasyon karşısında zamanla
  değer kaybeder.
- Maaş artışlarının enflasyonun altında kalması, reel olarak daha fakirleşmek
  anlamına gelebilir.
- Merkez bankaları, enflasyonu kontrol altında tutmak için faiz oranlarını
  kullanır (bu konuyu ayrı bir yazıda ele alacağız).

👉 Aşağıdaki **Python Köşesi** sekmesinde, kendi paranızın enflasyon karşısında
ne kadar eridiğini hesaplayabilirsiniz.
        """)

    with st.expander("📈 Bileşik Getiri (Faiz) Nedir?"):
        st.markdown("""
Bileşik getiri, kazandığınız getirinin de tekrar getiri kazanmaya başlaması
prensibidir. Basitçe "paranın parayı kazanması" diyebiliriz.

**Basit bir örnekle düşünelim:**
100 TL'nizi yıllık %10 getiri sağlayan bir yatırıma koyduğunuzu varsayalım.

- 1. yıl sonunda: 100 TL → 110 TL
- 2. yıl sonunda: 110 TL üzerinden %10 kazanırsınız → 121 TL
- 3. yıl sonunda: 121 TL üzerinden %10 kazanırsınız → 133,1 TL

Dikkat ederseniz her yıl kazandığınız miktar biraz daha artıyor, çünkü artık
sadece başlangıç sermayeniz değil, önceki kazancınız da getiri üretiyor.

**Neden önemli?**
- Zaman, bileşik getirinin en güçlü bileşenidir — ne kadar erken başlarsanız
  sonuç o kadar büyür.
- Bu mantık hem birikimler hem de borçlar (örneğin kredi kartı faizi) için
  aynı şekilde işler; borç tarafında ise aleyhinize çalışır.

*Not: Bu anlatım eğitim amaçlıdır, belirli bir yatırım aracını önermez.*
        """)

    st.caption("🔜 Bu bölüme yakında yeni kavramlar eklenecek: faiz oranları, bütçe yönetimi, risk ve çeşitlendirme...")

# ==========================================================
# TAB 2 - PYTHON KÖŞESİ (MINI ARAÇ)
# ==========================================================
with tab2:
    st.header("🧮 Enflasyon Karşısında Paranızın Erime Hesaplayıcısı")
    st.write(
        "Elinizdeki parayı yatırıma koymadan bir kenarda tutarsanız, "
        "enflasyon karşısında satın alma gücünüzün nasıl azaldığını görün."
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        amount = st.number_input("Başlangıç Tutarı (TL)", min_value=0.0, value=10000.0, step=100.0)
    with col2:
        inflation_rate = st.number_input("Yıllık Ortalama Enflasyon Oranı (%)", min_value=0.0, value=35.0, step=0.5)
    with col3:
        years = st.slider("Süre (Yıl)", min_value=1, max_value=20, value=5)

    if st.button("Hesapla", type="primary"):
        data = []
        current_value = amount
        for year in range(0, years + 1):
            real_value = amount / ((1 + inflation_rate / 100) ** year)
            data.append({"Yıl": year, "Reel Satın Alma Gücü (TL)": round(real_value, 2)})

        df = pd.DataFrame(data)

        final_value = df.iloc[-1]["Reel Satın Alma Gücü (TL)"]
        loss_amount = amount - final_value
        loss_percent = (loss_amount / amount) * 100 if amount > 0 else 0

        st.subheader("Sonuç")
        c1, c2, c3 = st.columns(3)
        c1.metric("Başlangıç Değeri", f"{amount:,.0f} TL")
        c2.metric(f"{years} Yıl Sonraki Reel Değer", f"{final_value:,.0f} TL", delta=f"-{loss_amount:,.0f} TL")
        c3.metric("Satın Alma Gücü Kaybı", f"%{loss_percent:.1f}")

        st.line_chart(df.set_index("Yıl"))

        st.caption(
            "⚠️ Bu hesaplama basitleştirilmiştir; gerçek enflasyon oranları yıldan yıla "
            "değişir ve burada sabit kabul edilmiştir. Sonuçlar bilgilendirme amaçlıdır, "
            "yatırım tavsiyesi değildir."
        )

    st.caption("🔜 Bu köşeye yakında yeni interaktif araçlar eklenecek: bileşik getiri hesaplayıcı, temel terimler sözlüğü ve daha fazlası...")

# ==========================================================
# TAB 3 - GÜNDEM ANALİZLERİ (PLACEHOLDER)
# ==========================================================
with tab3:
    st.header("🌍 Gündem Analizleri")
    st.write(
        "Bu bölüm henüz yapım aşamasında. Yakında burada, dünya ekonomisindeki "
        "güncel gelişmelerin (merkez bankası kararları, enerji krizleri, "
        "tedarik zinciri sorunları gibi) **tavsiye vermeden**, sadece "
        "mekanizmasını anlatan haftalık analizler paylaşılacak."
    )
    st.warning("✍️ Çok yakında ilk analiz yazımız burada olacak — takipte kalın!")

# ----------------------------------------------------
# ALT BİLGİ
# ----------------------------------------------------
st.divider()
st.caption(
    "YüzGözFinans — Akbank AI Business School 'Introduction to Python' sertifikası "
    "kapsamında geliştirilen bir portfolyo projesidir. İçerikler zamanla genişletilecektir. "
    "Hiçbir içerik yatırım tavsiyesi teşkil etmez."
)
