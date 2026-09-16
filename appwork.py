from datetime import datetime
import pandas as pd
import streamlit as st

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(
    page_title="FlashJob - Lavoro Last Minute", page_icon="⚡", layout="centered"
)

# --- STILE CSS MOBILE COMPATTO ---
st.markdown(
    """
    <style>
    .main { background-color: #f1f5f9; }
    .block-container { padding-top: 0.5rem !important; padding-bottom: 2rem !important; max-width: 650px; }

    .ios-card {
        background-color: white;
        padding: 15px;
        border-radius: 14px;
        box-shadow: 0 4px 15px -2px rgba(0, 0, 0, 0.05);
        margin-bottom: 12px;
        border: 1px solid #e2e8f0;
    }

    .ios-card-pro {
        background: linear-gradient(135deg, #ffffff 0%, #fffbeb 100%);
        padding: 15px;
        border-radius: 14px;
        box-shadow: 0 4px 15px -2px rgba(234, 179, 8, 0.15);
        margin-bottom: 12px;
        border: 1px solid #fde047;
    }

    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        width: 100%;
        padding: 0.5rem 1rem;
        background-color: #0f172a;
        color: white;
        border: none;
        box-shadow: 0 4px 10px rgba(15, 23, 42, 0.15);
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #1e293b;
        color: white;
        transform: translateY(-1px);
    }

    .stTextInput > div > div > input, .stSelectbox > div > div > div {
        border-radius: 8px;
        border-color: #cbd5e1;
        background-color: #f8fafc;
    }

    h1 { font-size: 1.3rem !important; font-weight: 800 !important; color: #0f172a; }
    h2 { font-size: 1.1rem !important; font-weight: 700 !important; color: #1e293b; }
    
    .badge-free { background-color: #dcfce7; color: #166534; padding: 3px 8px; border-radius: 20px; font-size: 0.7rem; font-weight: 700; display: inline-block; margin-top: 3px; }
    .badge-pro { background-color: #fef08a; color: #854d0e; padding: 3px 8px; border-radius: 20px; font-size: 0.7rem; font-weight: 700; display: inline-block; margin-bottom: 6px; }
    .ad-banner { background-color: #eff6ff; border: 1px dashed #3b82f6; padding: 10px; border-radius: 10px; text-align: center; color: #1e3a8a; font-size: 0.8rem; margin-bottom: 15px; }
    </style>
""",
    unsafe_allow_html=True,
)

# --- MEMORIA DI STATO ---
if "offerte" not in st.session_state:
    st.session_state.offerte = [
        {
            "id": 1,
            "azienda": "The Sanctuary",
            "citta": "Milano",
            "mansione": "Addetto Sala / Bar",
            "data": "2026-06-20",
            "orario": "16:00 - 00:00",
            "compenso": "90€ netti",
            "stato": "Aperta",
            "premium": True,
        }
    ]

if "candidature" not in st.session_state:
    st.session_state.candidature = []

# --- LOGO COMPATTO INTEGRATO ---
logo_html = """
<div style="text-align: center; margin-bottom: 4px;">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 170" width="220" height="68" style="margin: auto; filter: drop-shadow(0px 2px 6px rgba(15,23,42,0.12));">
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
      <rect width="512" height="170" rx="35" fill="url(#bgGrad)" />
      <path d="M 95 25 L 55 95 H 82 L 70 145 L 130 80 H 102 L 115 25 Z" fill="url(#boltGrad)" />
      <text x="165" y="80" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="44" font-weight="900" fill="#ffffff">FlashJob</text>
      <text x="168" y="115" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="600" fill="#94a3b8">Il lavoro a portata di clic</text>
    </svg>
</div>
"""
st.markdown(logo_html, unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center;'><span class='badge-free'>🛡️ 100% Gratuito per i Lavoratori (Zero Commissioni)</span></div>",
    unsafe_allow_html=True,
)
st.divider()

# --- MENU A TENDINA PRINCIPALE ---
ruolo = st.selectbox(
    "Seleziona il tuo profilo di accesso:",
    [
        "👤 Lavoratore (Cerco Turno / Lavoro)",
        "💼 Azienda (Pubblica Turno Urgente)",
        "⭐ Azienda PRO (Abbonamenti & Vetrina)",
    ],
)

# ==========================================
# 👤 AREA LAVORATORE
# ==========================================
if "Lavoratore" in ruolo:
    st.subheader("Bacheca Turni Attivi ⚡")

    citta_filtro = st.selectbox(
        "Filtra per zona:", ["Tutte le città", "Milano", "Roma", "Altro"]
    )

    offerte_aperte = [
        o for o in st.session_state.offerte if o["stato"] == "Aperta"
    ]
    if citta_filtro != "Tutte le città":
        offerte_aperte = [
            o for o in offerte_aperte if o["citta"] == citta_filtro
        ]

    offerte_aperte.sort(key=lambda x: x.get("premium", False), reverse=True)

    if not offerte_aperte:
        st.info("Nessun turno disponibile in questa zona al momento.")
    else:
        nome_utente = st.text_input(
            "Il tuo Nome e Cognome:", placeholder="Es. Mario Rossi"
        )
        telefono_utente = st.text_input(
            "Il tuo WhatsApp / Telefono:", placeholder="Es. 3331234567"
        )

        for offerta in offerte_aperte:
            is_pro = offerta.get("premium", False)
            card_class = "ios-card-pro" if is_pro else "ios-card"
            badge_html = (
                "<span class='badge-pro'>⭐ IN EVIDENZA</span><br>"
                if is_pro
                else ""
            )

            st.markdown(
                f"""
                <div class="{card_class}">
                    {badge_html}
                    <h3 style="margin:0 0 4px 0; color:#0f172a; font-size:1rem;">📍 {offerta['azienda']} <span style="font-size:0.8rem; font-weight:normal; color:#64748b;">({offerta['citta']})</span></h3>
                    <p style="margin:2px 0; font-size:0.9rem; font-weight:600; color:#334155;">Mansione: {offerta['mansione']}</p>
                    <p style="margin:2px 0; color:#475569; font-size:0.8rem;">📅 {offerta['data']} &nbsp;|&nbsp; 🕒 {offerta['orario']}</p>
                    <p style="margin:4px 0 0 0; font-size:1rem; font-weight:700; color:#16a34a;">💰 Compenso: {offerta['compenso']}</p>
                </div>
            """,
                unsafe_allow_html=True,
            )

            if st.button(
                f"🔥 Candidati per {offerta['azienda']}",
                key=f"cand_{offerta['id']}",
            ):
                if not nome_utente or not telefono_utente:
                    st.warning(
                        "⚠️ Inserisci nome e telefono nei campi sopra prima di candidarti!"
                    )
                else:
                    nuova_candidatura = {
                        "id": len(st.session_state.candidature) + 1,
                        "offerta_id": offerta["id"],
                        "nome_lavoratore": nome_utente,
                        "telefono": telefono_utente,
                        "data_candidatura": datetime.now().strftime("%H:%M:%S"),
                    }
                    st.session_state.candidature.append(nuova_candidatura)
                    st.success(
                        f"🎉 Candidatura inviata! L'azienda ti contatterà al numero `{telefono_utente}`."
                    )
                    st.rerun()

# ==========================================
# 💼 AREA AZIENDA (FREE)
# ==========================================
elif "Azienda" in ruolo and "PRO" not in ruolo:
    st.subheader("Pubblica un Turno d'Emergenza")

    st.markdown(
        """
        <div class="ad-banner">
        📢 <b>Spazio Sponsorizzato</b><br>
        <i>Passa a PRO per rimuovere i banner e mettere i turni in cima!</i>
        </div>
    """,
        unsafe_allow_html=True,
    )

    with st.form("form_azienda_free", clear_on_submit=True):
        nome_azienda = st.text_input(
            "Nome Attività", placeholder="Es. Ristorante La Pergola"
        )
        citta = st.selectbox("Città / Zona", ["Milano", "Roma", "Altro"])
        mansione = st.text_input(
            "Mansione richiesta", placeholder="Es. Cameriere / Barista"
        )

        col1, col2 = st.columns(2)
        with col1:
            data_turno = st.date_input("Data del turno")
        with col2:
            orario = st.text_input("Orario", placeholder="Es. 19:00 - 01:00")

        compenso = st.text_input(
            "Compenso Netto", placeholder="Es. 90€ a fine turno"
        )

        pubblica = st.form_submit_button("🚀 Pubblica Subito in Bacheca")
        if pubblica:
            if nome_azienda and mansione and compenso:
                nuova_offerta = {
                    "id": len(st.session_state.offerte) + 1,
                    "azienda": nome_azienda,
                    "citta": citta,
                    "mansione": mansione,
                    "data": str(data_turno),
                    "orario": orario,
                    "compenso": compenso,
                    "stato": "Aperta",
                    "premium": False,
                }
                st.session_state.offerte.append(nuova_offerta)
                st.success("Offerta online!")
                st.rerun()
            else:
                st.warning("Compila tutti i campi.")

    st.divider()
    st.subheader("📋 Candidature Ricevute")

    if not st.session_state.candidature:
        st.info("Nessuna candidatura ricevuta.")
    else:
        for cand in st.session_state.candidature:
            st.markdown(
                f"""
                <div class="ios-card">
                    <p style="margin:0; font-weight:bold; color:#0f172a;">👤 {cand['nome_lavoratore']}</p>
                    <p style="margin:2px 0; color:#334155;">📞 Tel: <b>{cand['telefono']}</b></p>
                </div>
            """,
                unsafe_allow_html=True,
            )

# ==========================================
# ⭐ AREA AZIENDA PRO
# ==========================================
else:
    st.subheader("⭐ FlashJob PRO")
    st.write("Sblocca la massima visibilità per le tue urgenze.")

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown(
            """
        <div class="ios-card">
            <h4>Piano Base</h4>
            <p style="font-size:0.8rem; color:#64748b;">Gratuito</p>
        </div>
    """,
                unsafe_allow_html=True,
        )
    with col_p2:
        st.markdown(
            """
        <div class="ios-card-pro">
            <h4>Piano PRO</h4>
            <p style="font-size:0.8rem; color:#854d0e;"><b>39€ / mese</b></p>
        </div>
    """,
                unsafe_allow_html=True,
        )

    if st.button("Abbonati ora a FlashJob PRO"):
        st.success("🎉 Account aziendale aggiornato a PRO!")