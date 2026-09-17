import streamlit as st

# Configurazione della pagina
st.set_page_config(
    page_title="FlashJob Milano - H&R Hub",
    page_icon="⚡",
    layout="centered",
)

# Stile CSS avanzato con sfondi e grafica curata
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
        transition: transform 0.2s ease;
    }
    .feature-card:hover {
        transform: translateY(-2px);
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
    </style>
""",
    unsafe_allow_html=True,
)

# Header principale con grafica
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
    ["🏠 Chi Siamo & Vantaggi", "⭐ Area Aziende (Database)", "👤 Area Lavoratori"],
    horizontal=True,
)

st.markdown("---")

# ==========================================
# 🏠 HOME PAGE: CHI SIAMO, COSA FACCIAMO E VANTAGGI
# ==========================================
if scelta == "🏠 Chi Siamo & Vantaggi":

  st.markdown("### 🎯 Chi Siamo e Cosa Facciamo")
  st.write(
      "**FlashJob Milano** nasce per risolvere il problema numero uno della"
      " ristorazione e dell'hotellerie milanese: trovare o offrire personale"
      " qualificato **subito**, senza perdite di tempo, intermediari"
      " farraginosi o il caos dei gruppi social."
  )
  st.write(
      "Mettiamo a disposizione una piattaforma pulita, immediata e strutturata"
      " dove i locali possono attingere a un database profilato di camerieri,"
      " baristi e cuochi pronti a lavorare in città."
  )

  st.markdown("<br>", unsafe_allow_html=True)

  col_v1, col_v2 = st.columns(2)

  with col_v1:
    st.markdown(
        """
        <div class="feature-card">
            <span class="badge-tag">PER LE AZIENDE 🏢</span>
            <h4 style="color: #0f172a; margin-top:5px;">Risolvi le emergenze in 2 minuti</h4>
            <ul style="padding-left: 18px; color: #475569; font-size: 0.9rem; line-height: 1.6;">
                <li><b>Zero commissioni</b> sulle ore lavorate.</li>
                <li><b>Contatto diretto WhatsApp</b> immediato con il candidato.</li>
                <li><b>Filtri avanzati</b> per mansione, zona ed esperienza.</li>
                <li><b>Copertura rapida</b> dei turni di sala, bar e cucina.</li>
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
            <h4 style="color: #0f172a; margin-top:5px;">Il tuo lavoro a Milano senza filtri</h4>
            <ul style="padding-left: 18px; color: #475569; font-size: 0.9rem; line-height: 1.6;">
                <li><b>100% Gratuito</b> per chi cerca lavoro.</li>
                <li><b>Visibilità massima</b> davanti ai migliori locali milanesi.</li>
                <li><b>Gestione autonoma</b> delle tue disponibilità orarie.</li>
                <li><b>Contatti diretti</b> gestiti in totale autonomia.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

  st.markdown("<br>", unsafe_allow_html=True)
  c1, c2 = st.columns(2)
  with c1:
    if st.button("⭐ VAI AL DATABASE AZIENDE (30€)"):
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