import streamlit as st

# Configurazione della pagina
st.set_page_config(
    page_title="Fla⚡️hJob - H&R Hub",
    page_icon="⚡",
    layout="wide",
)

# Stile CSS personalizzato: Sfondo nero, scritte bianche e logo compatto
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 0rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 100% !important;
    }
    
    /* SFONDO INTERO NERO E TESTO BIANCO */
    .stApp {
        background: #000000;
        color: #f8fafc;
    }

    .content-wrapper {
        max-width: 950px;
        margin: 0 auto;
    }

    /* --- BANNER FULL BLEED CON IMMAGINE --- */
    .hero-full-bleed {
        width: 100vw;
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
        background-image: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.85)), url('https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=1800');
        background-size: cover;
        background-position: center;
        color: white;
        padding: 90px 20px;
        text-align: center;
        margin-bottom: 40px;
        box-shadow: inset 0 0 100px rgba(0,0,0,0.8);
    }

    .hero-content {
        max-width: 900px;
        margin: 0 auto;
    }

    /* Logo compatto con lettere vicine */
    .brand-title {
        color: white;
        margin-bottom: 10px;
        font-size: 3.5rem;
        font-weight: 900;
        letter-spacing: -3px;
    }

    /* CARD CON SFONDO SCURO/ NERO E BORDO ELEGANTE */
    .feature-card {
        background: #111111;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(255,255,255,0.03);
        margin-bottom: 20px;
        border: 1px solid #333333;
        color: #f8fafc;
    }

    .badge-tag {
        background-color: #fef08a;
        color: #713f12;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 10px;
    }

    /* --- GALLERIA FULL BLEED FLUIDA ORIZZONTALE --- */
    .fluid-gallery {
        width: 100vw;
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
        margin-top: 40px;
        margin-bottom: 40px;
        background: #000000;
    }

    .image-strip {
        display: flex;
        overflow-x: auto;
        scroll-snap-type: x mandatory;
        gap: 0px;
        scrollbar-width: thin;
    }

    .image-strip::-webkit-scrollbar {
        height: 8px;
    }
    .image-strip::-webkit-scrollbar-thumb {
        background: #444444;
        border-radius: 4px;
    }

    .fluid-slide {
        flex: 0 0 100vw;
        width: 100vw;
        height: 550px;
        scroll-snap-align: start;
        position: relative;
    }

    .fluid-slide img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }

    .slide-caption {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.95), rgba(0,0,0,0.2));
        color: #f8fafc;
        padding: 30px 20px 20px 20px;
        font-size: 1.15rem;
        font-weight: 600;
        text-align: center;
        letter-spacing: 0.5px;
    }

    .legal-footer {
        background-color: #111111;
        color: #94a3b8;
        padding: 25px;
        border-radius: 14px;
        font-size: 0.75rem;
        line-height: 1.6;
        margin-top: 50px;
        border: 1px solid #333333;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    </style>
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

# ==========================================
# BANNER FULL BLEED CON LOGO COMPATTO (Fla⚡️hJob)
# ==========================================
st.markdown(
    """
    <div class="hero-full-bleed">
        <div class="hero-content">
            <h1 class="brand-title">Fla<span style="margin: 0 -4px;">⚡️</span>hJob</h1>
            <p style="color: #cbd5e1; font-size: 1.25rem; max-width: 650px; margin: 0 auto; font-weight: 400;">Il primo hub digitale che unisce i locali della ristorazione milanese con i migliori professionisti dell'accoglienza in tempo reale.</p>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

# Contenitore centrale per il menu e le sezioni
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# Menu di navigazione
scelta = st.radio(
    "Navigazione rapida:",
    ["🏠 Chi Siamo & Atmosfera", "⭐ Area Aziende (Database)", "👤 Area Lavoratori"],
    horizontal=True,
)

st.markdown("---")
st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 🏠 HOME PAGE: CHI SIAMO, VANTAGGI E GALLERIA FULL BLEED
# ==========================================
if scelta == "🏠 Chi Siamo & Atmosfera":

  st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
  st.markdown("<h3 style='color: white;'>🎯 Chi Siamo e Cosa Facciamo</h3>", unsafe_allow_html=True)
  st.markdown(
      "<p style='color: #cbd5e1;'><b>Fla⚡️hJob</b> nasce per sradicare il caos dei gruppi di"
      " messaggistica disordinati e dare una svolta professionale al mondo"
      " dell'hotellerie e della ristorazione (H&R) sotto la Madonnina. Siamo il"
      " punto di incontro ideale tra i locali milanesi che hanno bisogno di"
      " coprire turni o emergenze all'ultimo minuto e i professionisti del"
      " settore che cercano visibilità e opportunità concrete.</p>",
      unsafe_allow_html=True,
  )

  st.markdown("<br>", unsafe_allow_html=True)

  col_v1, col_v2 = st.columns(2)

  with col_v1:
    st.markdown(
        """
        <div class="feature-card">
            <span class="badge-tag">PER LE AZIENDE 🏢</span>
            <h4 style="color: #ffffff; margin-top:5px;">Perché sceglierci</h4>
            <ul style="padding-left: 18px; color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">
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
            <h4 style="color: #ffffff; margin-top:5px;">I tuoi vantaggi</h4>
            <ul style="padding-left: 18px; color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">
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
  st.markdown("<h3 style='color: white;'>✨ L'atmosfera e lo stile della movida milanese</h3>", unsafe_allow_html=True)
  st.markdown(
      "<p style='color: #cbd5e1;'>Scorri la galleria fotografica per esplorare il livello e lo stile dei"
      " locali in cui operano i nostri professionisti.</p>",
      unsafe_allow_html=True,
  )
  st.markdown("</div>", unsafe_allow_html=True)

  # --- GALLERIA FULL BLEED ORIZZONTALE ---
  st.markdown(
      """
    <div class="fluid-gallery">
        <div class="image-strip">
            <div class="fluid-slide">
                <img src="https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=1600" />
                <div class="slide-caption">🍸 Fla⚡️hJob &bull; Cocktail di ricerca e mixology d'eccellenza</div>
            </div>
            <div class="fluid-slide">
                <img src="https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1600" />
                <div class="slide-caption">🍽️ Fla⚡️hJob &bull; Cura meticolosa della cucina e del servizio</div>
            </div>
            <div class="fluid-slide">
                <img src="https://images.unsplash.com/photo-1574096079513-d8259312b785?w=1600" />
                <div class="slide-caption">🎧 Fla⚡️hJob &bull; Mood serale, eventi e intrattenimento nei locali</div>
            </div>
            <div class="fluid-slide">
                <img src="https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=1600" />
                <div class="slide-caption">🛎️ Fla⚡️hJob &bull; Professionalità e servizio di sala impeccabile</div>
            </div>
            <div class="fluid-slide">
                <img src="https://images.unsplash.com/photo-1543007630-9710e4a00a20?w=1600" />
                <div class="slide-caption">🍷 Fla⚡️hJob &bull; Wine tasting e atmosfere esclusive in centro</div>
            </div>
            <div class="fluid-slide">
                <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1600" />
                <div class="slide-caption">✨ Fla⚡️hJob &bull; Ristoranti, bistrot e design milanese</div>
            </div>
        </div>
    </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
  st.markdown("<br>", unsafe_allow_html=True)
  c1, c2 = st.columns(2)
  with c1:
    if st.button("⭐ ACCEDI AL DATABASE AZIENDE (30€)"):
      st.info("Seleziona 'Area Aziende' dal menu in alto.")
  with c2:
    if st.button("👤 REGISTRATI COME LAVORATORE"):
      st.info("Seleziona 'Area Lavoratori' dal menu in alto.")
  st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# ⭐ AREA AZIENDE
# ==========================================
elif scelta == "⭐ Area Aziende (Database)":
  st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
  st.markdown("<h3 style='color: white;'>⭐ Database Lavoratori Disponibili a Milano</h3>", unsafe_allow_html=True)
  st.markdown(
      "<p style='color: #cbd5e1;'>Accedi ai profili completi di camerieri, baristi e cuochi"
      " schedulati.</p>",
      unsafe_allow_html=True,
  )

  for lav in st.session_state.lavoratori:
    st.markdown(
        f"""
        <div class="feature-card">
            <h4 style="color: white; margin-top:0;">👤 {lav['nome']}</h4>
            <p style="margin: 4px 0; color: #cbd5e1;"><b>Mansione:</b> {lav['mansione']} | <b>Zona:</b> {lav['zona']}</p>
            <p style="margin: 4px 0;">📞 <b>WhatsApp diretto:</b> <a href="https://wa.me/{lav['tel'].replace(' ', '')}" target="_blank" style="color: #4ade80; font-weight: 600;">{lav['tel']}</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
  st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 👤 AREA LAVORATORI
# ==========================================
else:
  st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
  st.markdown("<h3 style='color: white;'>👤 Registrazione Gratuita Lavoratore</h3>", unsafe_allow_html=True)
  st.markdown(
      "<p style='color: #cbd5e1;'>Inserisci i tuoi dati per entrare nel database ufficiale di"
      " Milano.</p>",
      unsafe_allow_html=True,
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
            "Per favore inserisci almeno il nome e il telefono di contatto."
        )
  st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# ⚖️ TERMINI LEGALI E NOTE IN FONDO ALLA PAGINA
# ==========================================
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="legal-footer">
        <b style="color: #ffffff; font-size: 0.85rem;">⚖️ Note Legali e Condizioni di Utilizzo - Fla⚡️hJob</b><br><br>
        <b>1. Natura del Servizio:</b> Fla⚡️hJob opera esclusivamente come bacheca digitale e directory di contatto B2B/B2C per il settore Hotellerie & Restaurant (H&R). La piattaforma non costituisce un'agenzia di somministrazione di lavoro di cui al D.Lgs. 276/2003, né agisce in qualità di intermediario o datore di lavoro.<br><br>
        <b>2. Autonomia delle Parti:</b> Tutti gli accordi lavorativi, contrattuali, di ingaggio o di corresponsione economica avvengono direttamente e autonomamente tra i locali/aziende e i singoli lavoratori. Fla⚡️hJob è totalmente estranea ai rapporti contrattuali instaurati e declina ogni responsabilità civile e penale derivante dalle prestazioni lavorative.<br><br>
        <b>3. Trattamento Dati e Privacy:</b> I dati inseriti volontariamente dagli utenti vengono trattati nel pieno rispetto del GDPR (Regolamento UE 2016/679). La pubblicazione dei contatti all'interno dell'area riservata è subordinata all'accettazione delle presenti condizioni d'uso.
    </div>
""",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)