from datetime import datetime
import pandas as pd
import streamlit as st

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(
    page_title="FlashJob Milano - Personale H&R Immediato",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- STILE CSS CORRETTO (Spaziature e Pulizia UI) ---
st.markdown(
    """
    <style>
    .main { background-color: #f8fafc; }
    .block-container { 
        padding-top: 2rem !important; /* Stacca tutto dal bordo superiore della pagina */
        padding-bottom: 5rem !important; 
        max-width: 720px; 
    }
    div.block-container { padding-left: 1rem; padding-right: 1rem; }

    /* Hero section */
    .hero-container {
        text-align: center;
        padding: 24px 14px;
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        border-radius: 18px;
        color: white;
        margin-bottom: 20px;
        box-shadow: 0 8px 24px -4px rgba(15, 23, 42, 0.2);
    }
    
    /* Card standard */
    .flash-card {
        background-color: #ffffff;
        padding: 18px;
        border-radius: 14px;
        box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.05);
        margin-bottom: 14px;
        border: 1px solid #e2e8f0;
    }

    /* Card in evidenza PRO */
    .flash-card-pro {
        background: linear-gradient(135deg, #ffffff 0%, #fffbeb 100%);
        padding: 20px;
        border-radius: 14px;
        box-shadow: 0 6px 24px -4px rgba(234, 179, 8, 0.15);
        margin-bottom: 18px;
        border: 1.5px solid #fde047;
    }

    /* Box benefici */
    .benefit-box {
        background-color: #ffffff;
        border-left: 4px solid #ca8a04;
        padding: 14px 16px;
        border-radius: 0 10px 10px 0;
        margin-bottom: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.02);
        border-top: 1px solid #f1f5f9;
        border-right: 1px solid #f1f5f9;
        border-bottom: 1px solid #f1f5f9;
    }

    /* Pulsanti personalizzati */
    .stButton > button {
        border-radius: 12px;
        font-weight: 700;
        width: 100%;
        padding: 0.75rem 1rem;
        background-color: #0f172a;
        color: white;
        border: none;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
        transition: all 0.2s ease;
        font-size: 0.95rem;
    }
    .stButton > button:hover {
        background-color: #1e293b;
        color: white;
        transform: translateY(-1px);
    }

    .stTextInput > div > div > input, .stSelectbox > div > div > div {
        border-radius: 8px !important;
        border-color: #cbd5e1 !important;
        background-color: #ffffff !important;
    }

    h1, h2, h3 { color: #0f172a; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }

    .badge-milano { 
        background-color: #eff6ff; 
        color: #1e40af; 
        padding: 6px 14px; 
        border-radius: 20px; 
        font-size: 0.85rem; 
        font-weight: 700; 
        display: inline-flex;
        align-items: center;
        gap: 6px;
        border: 1px solid #bfdbfe;
        margin-top: 10px;
        margin-bottom: 22px;
    }
    .badge-verified {
        background-color: #f0fdf4;
        color: #166534;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 6px;
        border: 1px solid #bbf7d0;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- MEMORIA DI STATO ---
if "lavoratori_schedulati" not in st.session_state:
  st.session_state.lavoratori_schedulati = [
      {
          "id": 1,
          "nome": "Marco R.",
          "mansione": "Cameriere / Sala",
          "esperienza": "Oltre 3 anni",
          "disponibilita": "Serali e Weekend",
          "telefono": "+39 333 1234567",
      },
      {
          "id": 2,
          "nome": "Sara B.",
          "mansione": "Barista / Bartender",
          "esperienza": "1 - 3 anni",
          "disponibilita": "Flessibile",
          "telefono": "+39 340 9876543",
      },
      {
          "id": 3,
          "nome": "Davide L.",
          "mansione": "Cuoco / Aiuto Cuoco",
          "esperienza": "Oltre 3 anni",
          "disponibilita": "Pranzo e Sera",
          "telefono": "+39 347 5551234",
      },
  ]

if "azienda_pro" not in st.session_state:
  st.session_state.azienda_pro = False

if "vista_corrente" not in st.session_state:
  st.session_state.vista_corrente = "Landing Page"

# --- HEADER & LOGO (ABBASSATO E CORRETTO NELLA GRAFICA) ---
logo_html = """
<div style="display: flex; flex-direction: column; align-items: center; width: 100%; margin-top: 15px; margin-bottom: 15px;">
    <div style="width: 100%; max-width: 320px;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 115" style="width: 100%; height: auto; display: block; filter: drop-shadow(0px 6px 16px rgba(15,23,42,0.12));">
          <defs>
            <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#0f172a" />
              <stop offset="100%" stop-color="#1e293b" />
            </linearGradient>
            <linearGradient id="boltGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#fde047" />
              <stop offset="100%" stop-color="#ca8a04" />
            </linearGradient>
          </defs>
          <rect width="512" height="115" rx="24" fill="url(#bgGrad)" />
          <path d="M 70 18 L 38 68 H 58 L 48 98 L 94 56 H 74 L 84 18 Z" fill="url(#boltGrad)" />
          <text x="122" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="42" font-weight="900" fill="#ffffff">FlashJob</text>
          <text x="125" y="83" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="#facc15">MILANO &bull; HOTEL & RESTAURANT HUB</text>
        </svg>
    </div>
    <div style='text-align: center;'>
        <span class='badge-milano'>⚡ Assunzioni rapide nel settore H&R &bull; Solo a Milano</span>
    </div>
</div>
"""
st.markdown(logo_html, unsafe_allow_html=True)

# --- BARRA DI NAVIGAZIONE RAPIDA ---
col_nav1, col_nav2, col_nav3 = st.columns(3)
with col_nav1:
  if st.button("🚀 Home"):
    st.session_state.vista_corrente = "Landing Page"
    st.rerun()
with col_nav2:
  if st.button("⭐ Aziende"):
    st.session_state.vista_corrente = "Area Aziende"
    st.rerun()
with col_nav3:
  if st.button("👤 Lavoratori"):
    st.session_state.vista_corrente = "Area Lavoratori"
    st.rerun()

st.markdown(
    "<hr style='margin: 15px 0; border: none; border-top: 1px solid #e2e8f0;'>",
    unsafe_allow_html=True,
)


# ==========================================
# 🚀 1. LA LANDING PAGE
# ==========================================
if st.session_state.vista_corrente == "Landing Page":

  st.markdown(
      """
        <div class="hero-container">
            <h1 style="color: white; font-size: 1.6rem; margin-bottom: 10px; font-weight: 800; line-height: 1.3;">Trova Personale per il tuo Locale a Milano in 2 Minuti.</h1>
            <p style="color: #94a3b8; font-size: 0.9rem; max-width: 600px; margin: 0 auto 18px auto; line-height: 1.4;">Basta con il caos dei gruppi Telegram. Accedi al primo database di camerieri, baristi e cuochi schedulati e pronti a lavorare.</p>
        </div>
        """,
      unsafe_allow_html=True,
  )

  col_btn1, col_btn2 = st.columns(2)
  with col_btn1:
    if st.button("⭐ SONO UN LOCALE\n(Accedi / 30€)"):
      st.session_state.vista_corrente = "Area Aziende"
      st.rerun()
  with col_btn2:
    if st.button("👤 CERCO LAVORO\n(Registrati Gratis)"):
      st.session_state.vista_corrente = "Area Lavoratori"
      st.rerun()

  st.markdown(
      "<h3 style='text-align: center; margin: 25px 0 15px 0; font-size:"
      " 1.2rem;'>Perché i locali di Milano scelgono FlashJob?</h3>",
      unsafe_allow_html=True,
  )

  st.markdown(
      """
        <div class="benefit-box">
            <b style="color: #0f172a; font-size: 0.95rem;">🚫 Zero confusione, niente perditempo</b>
            <p style="margin: 4px 0 0 0; font-size: 0.85rem; color: #475569;">Nei gruppi social vieni inondato da messaggi disordinati. FlashJob ti offre una rubrica pulita e ordinata.</p>
        </div>
        <div class="benefit-box">
            <b style="color: #0f172a; font-size: 0.95rem;">🔍 Filtri mirati per mansione ed esperienza</b>
            <p style="margin: 4px 0 0 0; font-size: 0.85rem; color: #475569;">Ti serve un bartender con più di 3 anni di esperienza? Filtri con un click e trovi subito chi fa al caso tuo.</p>
        </div>
        <div class="benefit-box">
            <b style="color: #0f172a; font-size: 0.95rem;">📞 Scrivi direttamente su WhatsApp</b>
            <p style="margin: 4px 0 0 0; font-size: 0.85rem; color: #475569;">Nessuna commissione sulle ore. Prendi il numero WhatsApp e accordati direttamente con il candidato.</p>
        </div>
        <div class="benefit-box">
            <b style="color: #0f172a; font-size: 0.95rem;">💰 Un investimento che si ripaga in un turno</b>
            <p style="margin: 4px 0 0 0; font-size: 0.85rem; color: #475569;">Con soli 30€ al mese risolvi le emergenze di personale e salvi le serate di pienone.</p>
        </div>
        """,
      unsafe_allow_html=True,
  )

  st.markdown(
      """
        <div style="background: linear-gradient(135deg, #fef9c3 0%, #fef08a 100%); padding: 20px; border-radius: 14px; text-align: center; margin-top: 25px; border: 1px solid #fde047;">
            <h3 style="color: #713f12; margin-top: 0; font-size: 1.1rem;">Gestisci un bar o un ristorante a Milano?</h3>
            <p style="color: #854d0e; font-size: 0.85rem; margin-bottom: 15px;">Sblocca subito l'accesso completo al database.</p>
        </div>
        """,
      unsafe_allow_html=True,
  )

  st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
  if st.button("⭐ Sblocca Subito il Database Aziende"):
    st.session_state.vista_corrente = "Area Aziende"
    st.rerun()


# ==========================================
# ⭐ 2. AREA AZIENDA PRO
# ==========================================
elif st.session_state.vista_corrente == "Area Aziende":
  st.subheader("⭐ FlashJob PRO - Accesso Aziende (Milano)")

  LINK_PAYPAL_ABBONAMENTO = "https://www.paypal.com/webapps/billing/plans/subscribe?plan_id=INSERISCI_QUI_IL_TUO_ID"

  if not st.session_state.azienda_pro:
    st.markdown(
        """
        <div class="flash-card-pro">
            <h4 style="margin-top:0; color:#854d0e; font-size: 1.1rem;">Sblocca il Database Lavoratori di Milano</h4>
            <p style="font-size:0.85rem; color:#713f12; margin-bottom:12px;">Meno di un'ora di lavoro di un dipendente per risolvere definitivamente le emergenze nel tuo locale.</p>
            <div style="font-size: 1.6rem; font-weight: 800; color: #ca8a04; margin-bottom: 15px;">30 € <span style="font-size: 0.8rem; font-weight: normal; color: #713f12;">/ mese</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div style="text-align: center; margin-bottom: 15px;">
            <a href="{LINK_PAYPAL_ABBONAMENTO}" target="_blank" style="background-color: #0070ba; color: white; padding: 14px 20px; border-radius: 10px; font-weight: 700; text-decoration: none; display: inline-block; box-shadow: 0 4px 12px rgba(0,112,186,0.25); font-size: 0.95rem;">
                💳 Attiva Subito con PayPal (30€/mese)
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("🧪 [Test rapido] Simula Abbonamento Attivo"):
      st.session_state.azienda_pro = True
      st.rerun()

  else:
    st.markdown(
        """
        <div style="background-color: #f0fdf4; border: 1px solid #bbf7d0; padding: 12px 16px; border-radius: 10px; margin-bottom: 20px;">
            <b style="color: #166534;">✅ Abbonamento PRO Attivo (30€/mese)</b><br>
            <span style="font-size: 0.85rem; color: #15803d;">Accesso completo al database e ai contatti diretti di Milano.</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("📋 Database Lavoratori Schedulati (Milano)")

    filtro_mansione = st.selectbox(
        "Filtra per mansione:",
        [
            "Tutte le mansioni",
            "Cameriere / Sala",
            "Barista / Bartender",
            "Cuoco / Aiuto Cuoco",
            "Runner / Facchino",
            "Addetto Pulizie",
        ],
    )

    lavoratori_filtrati = st.session_state.lavoratori_schedulati
    if filtro_mansione != "Tutte le mansioni":
      lavoratori_filtrati = [
          l for l in lavoratori_filtrati if l["mansione"] == filtro_mansione
      ]

    if not lavoratori_filtrati:
      st.info("Nessun lavoratore trovato con questa mansione specifica al momento.")
    else:
      for lav in lavoratori_filtrati:
        st.markdown(
            f"""
            <div class="flash-card">
                <span class="badge-verified">VERIFICATO MILANO</span>
                <h4 style="margin: 0 0 4px 0; color: #0f172a;">👤 {lav['nome']}</h4>
                <p style="margin: 2px 0; font-size: 0.85rem; font-weight: 600; color: #334155;">Mansione: {lav['mansione']}</p>
                <p style="margin: 2px 0; font-size: 0.8rem; color: #475569;">Esperienza: {lav['esperienza']} &bull; Disponibilità: {lav['disponibilita']}</p>
                <hr style="margin: 10px 0; border: none; border-top: 1px solid #f1f5f9;">
                <p style="margin: 0; font-size: 0.9rem; color: #16a34a;">📞 <b>Contatto diretto WhatsApp:</b> {lav['telefono']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
    if st.button("Annulla / Gestisci Abbonamento"):
      st.session_state.azienda_pro = False
      st.rerun()


# ==========================================
# 👤 3. AREA LAVORATORE
# ==========================================
else:
  st.subheader("👤 Registrazione e Schedulazione Profilo")
  st.markdown(
      "<p style='color: #475569; font-size: 0.85rem;'>Il servizio è <b>100% gratuito per i lavoratori</b>. Entra a far parte del database ufficiale di Milano e fatti contattare direttamente su WhatsApp.</p>",
      unsafe_allow_html=True,
  )

  with st.form("form_profilo_lavoratore", clear_on_submit=True):
    nome_lav = st.text_input(
        "Nome e Cognome (o Nome puntato) *", placeholder="Es. Andrea M."
    )
    telefono_lav = st.text_input(
        "Numero WhatsApp / Telefono *", placeholder="Es. 3331234567"
    )

    col_l1, col_l2 = st.columns(2)
    with col_l1:
      mansione_lav = st.selectbox(
          "Mansione Principale *",
          [
              "Cameriere / Sala",
              "Barista / Bartender",
              "Cuoco / Aiuto Cuoco",
              "Runner / Facchino",
              "Addetto Pulizie",
          ],
      )
    with col_l2:
      esperienza_lav = st.selectbox(
          "Anni di Esperienza", ["Meno di 1 anno", "1 - 3 anni", "Oltre 3 anni"]
      )

    disponibilita_lav = st.text_input(
        "Disponibilità (Giorni / Orari)",
        placeholder="Es. Disponibile weekend e serali",
    )

    salva_profilo = st.form_submit_button(
        "🚀 Inserisci Profilo nel Database di Milano"
    )

    if salva_profilo:
      if nome_lav and telefono_lav:
        nuovo_record = {
            "id": len(st.session_state.lavoratori_schedulati) + 1,
            "nome": nome_lav,
            "mansione": mansione_lav,
            "esperienza": esperienza_lav,
            "disponibilita": disponibilita_lav,
            "telefono": telefono_lav,
        }
        st.session_state.lavoratori_schedulati.append(nuovo_record)
        st.success(
            "🎉 Profilo schedulato con successo! Adesso compari nel database"
            " riservato alle aziende di Milano."
        )
      else:
        st.warning(
            "⚠️ Inserisci almeno Nome e Telefono per completare la"
            " schedulazione."
        )

# --- FOOTER ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #94a3b8; font-size: 0.7rem; line-height: 1.4;'>
        <b>FlashJob Milano</b> &bull; Piattaforma tecnologica di directory e bacheca contatti.<br>
        Non gestisce contratti di lavoro o retribuzioni dirette.
    </div>
""",
    unsafe_allow_html=True,
)