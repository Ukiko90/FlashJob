from datetime import datetime
import pandas as pd
import streamlit as st

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(
    page_title="FlashJob Milano - Profili Lavoratori",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- STILE CSS PROFESSIONALE (UI/UX) ---
st.markdown(
    """
    <style>
    .main { background-color: #f1f5f9; }
    .block-container { 
        padding-top: 1rem !important; 
        padding-bottom: 5rem !important; 
        max-width: 720px; 
    }
    div.block-container { padding-left: 1rem; padding-right: 1rem; }

    /* Card standard */
    .flash-card {
        background-color: #ffffff;
        padding: 22px;
        border-radius: 14px;
        box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.05);
        margin-bottom: 16px;
        border: 1px solid #e2e8f0;
    }

    /* Card in evidenza PRO (30€/mese) */
    .flash-card-pro {
        background: linear-gradient(135deg, #ffffff 0%, #fffbeb 100%);
        padding: 22px;
        border-radius: 14px;
        box-shadow: 0 6px 24px -4px rgba(234, 179, 8, 0.15);
        margin-bottom: 16px;
        border: 1.5px solid #fde047;
    }

    /* Pulsanti personalizzati */
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        width: 100%;
        padding: 0.6rem 1rem;
        background-color: #0f172a;
        color: white;
        border: none;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.12);
        transition: all 0.2s ease;
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
        padding: 5px 12px; 
        border-radius: 20px; 
        font-size: 0.8rem; 
        font-weight: 700; 
        display: inline-flex;
        align-items: center;
        gap: 6px;
        border: 1px solid #bfdbfe;
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
  ]

if "azienda_pro" not in st.session_state:
  st.session_state.azienda_pro = False  # Stato abbonamento azienda

# --- HEADER & LOGO ---
logo_html = """
<div style="display: flex; justify-content: center; align-items: center; width: 100%; margin-bottom: 8px;">
    <div style="width: 100%; max-width: 360px;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 115" style="width: 100%; height: auto; display: block; filter: drop-shadow(0px 4px 12px rgba(15,23,42,0.08));">
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
          <text x="125" y="83" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="500" fill="#94a3b8">Milano Talent Hub</text>
        </svg>
    </div>
</div>
"""
st.markdown(logo_html, unsafe_allow_html=True)

st.markdown(
    """
    <div style='text-align: center; margin-bottom: 22px;'>
        <span class='badge-milano'>📍 Esclusivamente attivo su MILANO &bull; Pool Lavoratori Verificati</span>
    </div>
""",
    unsafe_allow_html=True,
)

# --- MENU A TENDINA PRINCIPALE ---
ruolo = st.selectbox(
    "Seleziona la tua area d'accesso:",
    [
        "👤 Profilo Lavoratore (Registrazione & Schedulazione)",
        "⭐ Area Azienda PRO (Abbonamento 30€/mese & Database Lavoratori)",
    ],
)

st.markdown(
    "<hr style='margin: 20px 0; border: none; border-top: 1px solid"
    " #e2e8f0;'>",
    unsafe_allow_html=True,
)

# ==========================================
# 👤 AREA PROFILO LAVORATORE
# ==========================================
if "Lavoratore" in ruolo:
  st.subheader("👤 Registrazione e Schedulazione Profilo")
  st.markdown(
      "<p style='color: #475569; font-size: 0.9rem;'>Entra a far parte del database ufficiale dei lavoratori disponibili a Milano. Le aziende locali potranno contattarti direttamente per esigenze lavorative.</p>",
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

    st.markdown(
        "<div style='margin-top: 5px; font-size:0.8rem;"
        " color:#64748b;'>*Campi obbligatori per la schedulazione</div>",
        unsafe_allow_html=True,
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

  st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
  st.info(
      "💡 **Nota per i lavoratori:** Il servizio è 100% gratuito per voi. Le"
      " aziende vi contatteranno direttamente tramite il vostro numero"
      " WhatsApp."
  )

# ==========================================
# ⭐ AREA AZIENDA PRO (ABBONAMENTO 30€/MESE)
# ==========================================
else:
  st.subheader("⭐ FlashJob PRO - Accesso Aziende (Milano)")

  if not st.session_state.azienda_pro:
    # Se l'azienda non è abbonata, mostra la schermata di vendita dell'abbonamento
    st.markdown(
        """
        <div class="flash-card-pro">
            <h4 style="margin-top:0; color:#854d0e;">Sblocca il Database Lavoratori di Milano</h4>
            <p style="font-size:0.9rem; color:#713f12; margin-bottom:15px;">Accedi illimitatamente ai contatti diretti di camerieri, baristi e personale di sala schedulati nella tua zona per coprire ogni emergenza.</p>
            <div style="font-size: 1.6rem; font-weight: 800; color: #ca8a04; margin-bottom: 15px;">30 € <span style="font-size: 0.85rem; font-weight: normal; color: #713f12;">/ mese</span></div>
            <ul style="font-size: 0.88rem; color: #713f12; padding-left: 20px; margin-bottom: 0;">
                <li><b>Contatti WhatsApp diretti</b> di tutti i lavoratori schedulati</li>
                <li>Filtri per mansione ed esperienza</li>
                <li>Disdetta possibile in qualsiasi momento</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("💳 Attiva Abbonamento Azienda (30€ / mese)"):
      st.session_state.azienda_pro = True
      st.success(
          "🎉 Abbonamento attivato con successo! Benvenuto in FlashJob PRO."
      )
      st.rerun()

  else:
    # Se l'azienda è abbonata, mostra la rubrica/database dei lavoratori con i numeri visibili
    st.markdown(
        """
        <div style="background-color: #f0fdf4; border: 1px solid #bbf7d0; padding: 12px 16px; border-radius: 10px; margin-bottom: 20px;">
            <b style="color: #166534;">✅ Abbonamento PRO Attivo (30€/mese)</b><br>
            <span style="font-size: 0.85rem; color: #15803d;">Hai accesso completo ai contatti diretti del personale schedulato a Milano.</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("📋 Database Lavoratori Schedulati (Milano)")

    filtro_mansione = st.selectbox(
        "Filtra per mansione:",
        ["Tutte le mansioni", "Cameriere / Sala", "Barista / Bartender", "Cuoco / Aiuto Cuoco", "Runner / Facchino", "Addetto Pulizie"]
    )

    lavoratori_filtrati = st.session_state.lavoratori_schedulati
    if filtro_mansione != "Tutte le mansioni":
      lavoratori_filtrati = [l for l in lavoratori_filtrati if l["mansione"] == filtro_mansione]

    if not lavoratori_filtrati:
      st.info("Nessun lavoratore trovato con questa mansione specifica al momento.")
    else:
      for lav in lavoratori_filtrati:
        st.markdown(
            f"""
            <div class="flash-card">
                <span class="badge-verified">VERIFICATO MILANO</span>
                <h4 style="margin: 0 0 4px 0; color: #0f172a;">👤 {lav['nome']}</h4>
                <p style="margin: 2px 0; font-size: 0.9rem; font-weight: 600; color: #334155;">Mansione: {lav['mansione']}</p>
                <p style="margin: 2px 0; font-size: 0.85rem; color: #475569;">Esperienza: {lav['esperienze'] if 'esperienze' in lav else lav['esperienza']} &bull; Disponibilità: {lav['disponibilita']}</p>
                <hr style="margin: 10px 0; border: none; border-top: 1px solid #f1f5f9;">
                <p style="margin: 0; font-size: 0.95rem; color: #16a34a;">📞 <b>Contatto diretto WhatsApp:</b> {lav['telefono']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
    if st.button("Annulla / Gestisci Abbonamento"):
      st.session_state.azienda_pro = False
      st.rerun()

# --- FOOTER / NOTE LEGALI ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #94a3b8; font-size: 0.75rem; line-height: 1.4;'>
        <b>FlashJob Milano</b> è esclusivamente una piattaforma tecnologica di directory e bacheca contatti.<br>
        Non gestisce contratti di lavoro, retribuzioni o pagamenti diretti tra le parti.<br>
        Consulta i <a href="https://github.com/TuoNomeUtente/TuoRepo/blob/main/TERMINI.md" target="_blank" style="color: #64748b; text-decoration: underline;">Termini e Condizioni Legali</a>.
    </div>
""",
    unsafe_allow_html=True,
)