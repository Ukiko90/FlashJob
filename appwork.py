import streamlit as st

# Configurazione della pagina
st.set_page_config(
    page_title="FlashJob Milano - H&R Hub",
    page_icon="⚡",
    layout="centered",
)

# Stile CSS avanzato per l'interfaccia
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
    }
    .hero-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: white;
        padding: 35px 25px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(15, 23, 42, 0.15);
        border: 1px solid #334155;
    }
    .feature-card {
        background: white;
        padding: 22px;
        border-radius: 16px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.04);
        margin-bottom: 18px;
        border: 1px solid #e2e8f0;
    }
    .badge-tag {
        background-color: #fef08a;
        color: #713f12;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 8px;
    }
    .gallery-img {
        width: 100%;
        border-radius: 16px;
        margin-bottom: 15px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        object-fit: cover;
        max-height: 450px;
    }
    .legal-footer {
        background-color: #1e293b;
        color: #94a3b8;
        padding: 20px;
        border-radius: 14px;
        font-size: 0.75rem;
        line-height: 1.5;
        margin-top: 40px;
        border: 1px solid #334155;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Header principale
st.markdown(
    """
    <div class="hero-box">
        <div style="font-size: 2.5rem; margin-bottom: 10px;">⚡ 🍸 🍳 🛎️</div>
        <h1 style="color: white; margin-bottom: 8px; font-weight: 800;">FlashJob Milano</h1>
        <p style="color: #94a3b8; font-size: 1.1rem; max-width: 550px; margin: 0 auto;">Il primo hub digitale che unisce i locali della ristorazione milanese con i migliori professionisti dell'accoglienza in tempo reale.</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Inizializzazione dati
if "lavoratori" not in st.session_state:
  st.session_state.lavoratori = [
      {
          "nome": "Marco R.",
          "mansione": "Cameriere / Sala",
          "zona": "Navigli",
          "tel": "+39 333 1234567",
      },
      {
          "nome": "Sara B.",
          "mansione": "Barista / Bartender",
          "zona": "Porta Romana",
          "tel": "+39 340 9876543",
      },
  ]

# Menu di navigazione
scelta = st.radio(
    "Navigazione rapida:",
    ["🏠 Chi Siamo & Atmosfera", "⭐ Area Aziende (Database)", "👤 Area Lavoratori"],
    horizontal=True,
)

st.markdown("---")

# ==========================================
# 🏠 HOME PAGE: CHI SIAMO, VANTAGGI E FOTO VERTICALI
# ==========================================
if scelta == "🏠 Chi Siamo & Atmosfera":

  st.markdown("### 🎯 Chi Siamo e Cosa Facciamo")
  st.write(
      "**FlashJob Milano** nasce per sradicare il caos dei gruppi di messaggistica"
      " disordinati e dare una svolta professionale al mondo dell'hotellerie e"
      " della ristorazione (H&R) sotto la Madonnina. Siamo il punto di incontro"
      " ideale tra i locali milanesi che hanno bisogno di coprire turni o"
      " emergenze all'ultimo minuto e i professionisti del settore che cercano"
      " visibilità e opportunità concrete."
  )

  st.markdown("<br>", unsafe_allow_html=True)

  col_v1, col_v2 = st.columns(2)

  with col_v1:
    st.markdown(
        """
        <div class="feature-card">
            <span class="badge-tag">PER LE AZIENDE 🏢</span>
            <h4 style="color: #0f172a; margin-top:5px;">Perché sceglierci</h4>
            <ul style="padding-left: 18px; color: #475569; font-size: 0.9rem; line-height: 1.6;">
                <li><b>Zero commissioni</b> sulle ore lavorate o sulle selezioni.</li>
                <li><b>Contatto diretto immediato</b> via WhatsApp con i candidati.</li>
                <li><b>Filtri mirati</b> per mansione, zona ed esperienza specifica.</li>
                <li><b>Copertura rapida</b> dei turni di sala, bar e cucina in 2 minuti.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

  with col_v2:
    st.markdown(
        """
        <div class="feature-card">
            <span class="badge-tag" style="background-color: #bbf7d0; color: #166534;">PER I LAVORATORI 👤</span>
            <h4 style="color: #0f172a; margin-top:5px;">I tuoi vantaggi</h4>
            <ul style="padding-left: 18px; color: #475569; font-size: 0.9rem; line-height: 1.6;">
                <li><b>100% Gratuito</b> per camerieri, baristi, cuochi e staff.</li>
                <li><b>Vetrina d'eccellenza</b> davanti ai migliori locali di Milano.</li>
                <li><b>Gestione autonoma</b> delle proprie disponibilità e turni.</li>
                <li><b>Zero intermediari</b>, gestisci il colloquio direttamente tu.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

  st.markdown("<br>", unsafe_allow_html=True)
  st.markdown(
      "### ✨ L'atmosfera e la qualità della ristorazione milanese"
  )
  st.write(
      "Ecco un assaggio del contesto in cui operiamo: locali di alto livello,"
      " drink ricercati, cura dei dettagli e professionisti appassionati."
  )

  # Galleria fotografica verticale (le immagini caricate)
  st.image(
      "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800",
      caption="FlashJob Milano - Cocktail e pairing di qualità",
      use_container_width=True,
  )
  st.image(
      "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=800",
      caption=(
          "FlashJob Milano - Cura meticolosa della cucina e del servizio"
      ),
      use_container_width=True,
  )
  st.image(
      "https://images.unsplash.com/photo-1574096079513-d8259312b785?w=800",
      caption="FlashJob Milano - Mood serale e intrattenimento nei locali",
      use_container_width=True,
  )
  st.image(
      "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=800",
      caption="FlashJob Milano - Professionalità e servizio di sala impeccabile",
      use_container_width=True,
  )

  st.markdown("<br>", unsafe_allow_html=True)
  c1, c2 = st.columns(2)
  with c1:
    if st.button("⭐ ACCEDI AL DATABASE AZIENDE (30€)"):
      st.info("Seleziona 'Area Aziende' dal menu in alto.")
  with c2:
    if st.button("👤 REGISTRATI COME LAVORATORE"):
      st.info("Seleziona 'Area Lavoratori' dal menu in alto.")

# ==========================================
# ⭐ AREA AZIENDE
# ==========================================
elif scelta == "⭐ Area Aziende (Database)":
  st.subheader("⭐ Database Lavoratori Disponibili a Milano")
  st.write(
      "Accedi ai profili completi di camerieri, baristi e cuochi schedulati."
  )

  for lav in st.session_state.lavoratori:
    st.markdown(
        f"""
        <div class="feature-card">
            <h4>👤 {lav['nome']}</h4>
            <p style="margin: 4px 0;"><b>Mansione:</b> {lav['mansione']} | <b>Zona:</b> {lav['zona']}</p>
            <p style="margin: 4px 0;">📞 <b>WhatsApp diretto:</b> <a href="https://wa.me/{lav['tel'].replace(' ', '')}" target="_blank" style="color: #16a34a; font-weight: 600;">{lav['tel']}</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ==========================================
# 👤 AREA LAVORATORI
# ==========================================
else:
  st.subheader("👤 Registrazione Gratuita Lavoratore")
  st.write(
      "Inserisci i tuoi dati per entrare nel database ufficiale di Milano."
  )

  with st.form("form_lav"):
    nome = st.text_input("Nome e Cognome / Nome d'arte")
    mansione = st.selectbox(
        "Mansione Principale",
        ["Cameriere / Sala", "Barista / Bartender", "Cuoco / Aiuto Cuoco"],
    )
    zona = st.text_input("Zona di Milano (es. Navigli, Brera, Duomo)")
    tel = st.text_input("Numero WhatsApp (es. 3331234567)")
    invia = st.form_submit_button("🚀 Registrati Subito (Gratis)")

    if invia:
      if nome and tel:
        st.session_state.lavoratori.append(
            {"nome": nome, "mansione": mansione, "zona": zona, "tel": tel}
        )
        st.success(
            "Registrazione completata con successo! Ora compari nel database"
            " per i locali di Milano."
        )
      else:
        st.warning(
            "Per favore inserisci almeno il nome e il numero di telefono."
        )

# ==========================================
# ⚖️ TERMINI LEGALI E NOTE IN FONDO ALLA PAGINA
# ==========================================
st.markdown(
    """
    <div class="legal-footer">
        <b style="color: #f8fafc; font-size: 0.8rem;">⚖️ Note Legali e Condizioni di Utilizzo - FlashJob Milano</b><br><br>
        <b>1. Natura del Servizio:</b> FlashJob Milano opera esclusivamente come bacheca digitale e directory di contatto B2B/B2C per il settore Hotellerie & Restaurant (H&R). La piattaforma non costituisce un'agenzia di somministrazione di lavoro di cui al D.Lgs. 276/2003, né agisce in qualità di intermediario o datore di lavoro.<br><br>
        <b>2. Autonomia delle Parti:</b> Tutti gli accordi lavorativi, contrattuali, di ingaggio o di corresponsione economica avvengono direttamente e autonomamente tra i locali/aziende e i singoli lavoratori. FlashJob Milano è totalmente estranea ai rapporti contrattuali instaurati e declina ogni responsabilità civile e penale derivante dalle prestazioni lavorative.<br><br>
        <b>3. Trattamento Dati e Privacy:</b> I dati inseriti volontariamente dagli utenti vengono trattati nel pieno rispetto del GDPR (Regolamento UE 2016/679). La pubblicazione dei contatti all'interno dell'area riservata è subordinata all'accettazione delle presenti condizioni d'uso.
    </div>
""",
    unsafe_allow_html=True,
)