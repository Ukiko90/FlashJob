import streamlit as st

# Configurazione della pagina
st.set_page_config(
    page_title="FlashJob Milano",
    page_icon="⚡",
    layout="centered",
)

# Stile CSS generale
st.markdown(
    """
    <style>
    .stApp {
        background: #f8fafc;
    }
    .hero {
        background: #0f172a;
        color: white;
        padding: 30px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 20px;
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        border: 1px solid #e2e8f0;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Titolo principale
st.markdown(
    """
    <div class="hero">
        <h1 style="color: white; margin-bottom: 10px;">⚡ FlashJob Milano</h1>
        <p style="color: #94a3b8; font-size: 1.1rem;">Trova Personale per il tuo Locale a Milano in 2 Minuti.</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Inizializzazione dati di esempio nello stato se non esistono
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

# Pulsanti di navigazione semplice
scelta = st.radio(
    "Seleziona area:",
    ["🏠 Home / Presentazione", "⭐ Area Aziende (Database)", "👤 Area Lavoratori"],
    horizontal=True,
)

st.markdown("---")

if scelta == "🏠 Home / Presentazione":
  st.subheader("Benvenuto su FlashJob")
  st.write(
      "La piattaforma per connettere rapidamente locali e personale H&R a"
      " Milano."
  )

  col1, col2 = st.columns(2)
  with col1:
    if st.button("SONO UN LOCALE (30€)"):
      st.info("Vai alla sezione Aziende in alto per accedere.")
  with col2:
    if st.button("CERCO LAVORO (Gratis)"):
      st.info("Vai alla sezione Lavoratori in alto per registrarti.")

elif scelta == "⭐ Area Aziende (Database)":
  st.subheader("⭐ Database Lavoratori Disponibili a Milano")
  st.write("Elenco dei profili attivi schedulati:")

  for lav in st.session_state.lavoratori:
    st.markdown(
        f"""
        <div class="card">
            <h4>👤 {lav['nome']}</h4>
            <p><b>Mansione:</b> {lav['mansione']} | <b>Zona:</b> {lav['zona']}</p>
            <p>📞 <b>WhatsApp:</b> <a href="https://wa.me/{lav['tel'].replace(' ', '')}" target="_blank">{lav['tel']}</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

else:
  st.subheader("👤 Registrazione Lavoratore (Gratuita)")
  with st.form("form_lav"):
    nome = st.text_input("Nome e Cognome")
    mansione = st.selectbox(
        "Mansione", ["Cameriere / Sala", "Barista / Bartender", "Cuoco"]
    )
    zona = st.text_input("Zona di Milano")
    tel = st.text_input("Numero WhatsApp")
    invia = st.form_submit_button("Registrati Subito")

    if invia:
      if nome and tel:
        st.session_state.lavoratori.append(
            {"nome": nome, "mansione": mansione, "zona": zona, "tel": tel}
        )
        st.success(
            "Registrazione completata! Adesso compari nel database aziende."
        )
      else:
        st.warning("Inserisci almeno nome e telefono.")