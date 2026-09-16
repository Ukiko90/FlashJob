from datetime import datetime
import pandas as pd
import streamlit as st

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(
    page_title="FlashJob - Lavoro Last Minute", page_icon="⚡", layout="centered"
)

# --- STILE CSS PROFESSIONALE (UI/UX) ---
st.markdown(
    """
    <style>
    /* Sfondo generale e container principale */
    .main { background-color: #f8fafc; }
    .block-container { 
        padding-top: 1.5rem !important; 
        padding-bottom: 4rem !important; 
        max-width: 680px; 
    }

    /* Card standard per i turni */
    .flash-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 4px 16px -4px rgba(15, 23, 42, 0.08);
        margin-bottom: 16px;
        border: 1px solid #e2e8f0;
        transition: transform 0.2s ease;
    }
    .flash-card:hover {
        border-color: #cbd5e1;
    }

    /* Card in evidenza PRO */
    .flash-card-pro {
        background: linear-gradient(145deg, #ffffff 0%, #fffdf4 100%);
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 6px 20px -4px rgba(234, 179, 8, 0.15);
        margin-bottom: 16px;
        border: 1.5px solid #fde047;
    }

    /* Pulsanti personalizzati */
    .stButton > button {
        border-radius: 12px;
        font-weight: 600;
        width: 100%;
        padding: 0.65rem 1rem;
        background-color: #0f172a;
        color: white;
        border: none;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #1e293b;
        color: white;
        transform: translateY(-1px);
    }

    /* Campi di input */
    .stTextInput > div > div > input, .stSelectbox > div > div > div {
        border-radius: 10px !important;
        border-color: #cbd5e1 !important;
        background-color: #ffffff !important;
        padding: 0.4rem;
    }

    /* Tipografia */
    h1 { font-size: 1.5rem !important; font-weight: 800 !important; color: #0f172a; }
    h2, h3 { color: #1e293b; }

    /* Badge e Tag */
    .badge-free { 
        background-color: #f0fdf4; 
        color: #166534; 
        padding: 6px 14px; 
        border-radius: 30px; 
        font-size: 0.8rem; 
        font-weight: 700; 
        display: inline-flex;
        align-items: center;
        gap: 6px;
        border: 1px solid #bbf7d0;
    }
    .badge-pro { 
        background-color: #fef08a; 
        color: #854d0e; 
        padding: 4px 10px; 
        border-radius: 20px; 
        font-size: 0.75rem; 
        font-weight: 700; 
        display: inline-block; 
        margin-bottom: 8px; 
    }
    .ad-banner { 
        background-color: #eff6ff; 
        border: 1px dashed #3b82f6; 
        padding: 14px; 
        border-radius: 12px; 
        text-align: center; 
        color: #1e3a8a; 
        font-size: 0.85rem; 
        margin-bottom: 20px; 
    }
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

# --- LOGO DESIGN PULITO E PROPORZIONATO ---
logo_html = """
<div style="display: flex; justify-content: center; align-items: center; width: 100%; margin-bottom: 12px;">
    <div style="width: 100%; max-width: 380px;">
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
          <rect width="512" height="115" rx="26" fill="url(#bgGrad)" />
          <path d="M 70 18 L 38 68 H 58 L 48 98 L 94 56 H 74 L 84 18 Z" fill="url(#boltGrad)" />
          <text x="122" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="42" font-weight="900" fill="#ffffff">FlashJob</text>
          <text x="125" y="83" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="500" fill="#94a3b8">Il lavoro a portata di clic</text>
        </svg>
    </div>
</div>
"""
st.markdown(logo_html, unsafe_allow_html=True)

# Badge di garanzia centrato
st.markdown(
    """
    <div style='text-align: center; margin-bottom: 24px;'>
        <span class='badge-free'>🛡️ 100% Gratuito per i Lavoratori &bull; Zero Commissioni</span>
    </div>
""",
    unsafe_allow_html=True,
)

# --- MENU A TENDINA PRINCIPALE ---
ruolo = st.selectbox(
    "Seleziona il tuo profilo di accesso:",
    [
        "👤 Lavoratore (Cerco Turno / Lavoro)",
        "💼 Azienda (Pubblica Turno Urgente)",
        "⭐ Azienda PRO (Abbonamenti & Vetrina)",
    ],
)

st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

# ==========================================
# 👤 AREA LAVORATORE
# ==========================================
if "Lavoratore" in ruolo:
  st.subheader("Bacheca Turni Attivi ⚡")

  citta_filtro = st.selectbox(
      "Filtra per zona:", ["Tutte le città", "Milano", "Roma", "Altro"]
  )

  offerte_aperte = [o for o in st.session_state.offerte if o["stato"] == "Aperta"]
  if citta_filtro != "Tutte le città":
    offerte_aperte = [o for o in offerte_aperte if o["citta"] == citta_filtro]

  offerte_aperte.sort(key=lambda x: x.get("premium", False), reverse=True)

  if not offerte_aperte:
    st.info("Nessun turno disponibile in questa zona al momento.")
  else:
    st.markdown(
        "<p style='color: #64748b; font-size: 0.9rem; margin-bottom:"
        " 12px;'>Inserisci i tuoi dati una sola volta per candidarti"
        " rapidamente ai turni:</p>",
        unsafe_allow_html=True,
    )

    nome_utente = st.text_input(
        "Il tuo Nome e Cognome:", placeholder="Es. Mario Rossi"
    )
    telefono_utente = st.text_input(
        "Il tuo WhatsApp / Telefono:", placeholder="Es. 3331234567"
    )

    st.markdown(
        "<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True
    )

    for offerta in offerte_aperte:
      is_pro = offerta.get("premium", False)
      card_class = "flash-card-pro" if is_pro else "flash-card"
      badge_html = (
          "<span class='badge-pro'>⭐ IN EVIDENZA</span><br>" if is_pro else ""
      )

      st.markdown(
          f"""
            <div class="{card_class}">
                {badge_html}
                <h3 style="margin:0 0 6px 0; color:#0f172a; font-size:1.1rem;">📍 {offerta['azienda']} <span style="font-size:0.85rem; font-weight:normal; color:#64748b;">({offerta['citta']})</span></h3>
                <p style="margin:4px 0; font-size:0.95rem; font-weight:600; color:#334155;">Mansione: {offerta['mansione']}</p>
                <p style="margin:4px 0; color:#475569; font-size:0.85rem;">📅 {offerta['data']} &nbsp;|&nbsp; 🕒 {offerta['orario']}</p>
                <p style="margin:8px 0 0 0; font-size:1.1rem; font-weight:700; color:#16a34a;">💰 Compenso: {offerta['compenso']}</p>
            </div>
        """,
          unsafe_allow_html=True,
      )

      if st.button(
          f"🔥 Candidati per {offerta['azienda']}", key=f"cand_{offerta['id']}"
      ):
        if not nome_utente or not telefono_utente:
          st.warning(
              "⚠️ Inserisci nome e telefono nei campi sopra prima di"
              " candidarti!"
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
              f"🎉 Candidatura inviata! L'azienda ti contatterà al numero"
              f" `{telefono_utente}`."
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
        <i>Passa a PRO per rimuovere i limiti e posizionare i turni in cima alla bacheca!</i>
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

    compenso = st.text_input("Compenso Netto", placeholder="Es. 90€ a fine turno")

    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
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
        st.success("Offerta pubblicata con successo!")
        st.rerun()
      else:
        st.warning("Compila tutti i campi obbligatori.")

  st.divider()
  st.subheader("📋 Candidature Ricevute")

  if not st.session_state.candidature:
    st.info("Nessuna candidatura ricevuta al momento.")
  else:
    for cand in st.session_state.candidature:
      st.markdown(
          f"""
            <div class="flash-card">
                <p style="margin:0; font-weight:bold; color:#0f172a;">👤 {cand['nome_lavoratore']}</p>
                <p style="margin:4px 0 0 0; color:#334155;">📞 Telefono: <b style="color:#0f172a;">{cand['telefono']}</b></p>
            </div>
        """,
          unsafe_allow_html=True,
      )

# ==========================================
# ⭐ AREA AZIENDA PRO
# ==========================================
else:
  st.subheader("⭐ FlashJob PRO")
  st.write("Sblocca la massima visibilità per le tue urgenze di personale.")

  st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

  col_p1, col_p2 = st.columns(2)
  with col_p1:
    st.markdown(
        """
        <div class="flash-card" style="text-align: center;">
            <h4 style="margin-bottom:5px;">Piano Base</h4>
            <p style="font-size:0.85rem; color:#64748b; margin-bottom:0;">Gratuito</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
  with col_p2:
    st.markdown(
        """
        <div class="flash-card-pro" style="text-align: center;">
            <h4 style="margin-bottom:5px; color:#854d0e;">Piano PRO</h4>
            <p style="font-size:0.85rem; color:#854d0e; margin-bottom:0;"><b>39€ / mese</b></p>
        </div>
    """,
        unsafe_allow_html=True,
    )

  st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

  if st.button("Abbonati ora a FlashJob PRO"):
    st.success("🎉 Account aziendale aggiornato a PRO con successo!")

# --- FOOTER / NOTE LEGALI (TUTELA PIATTAFORMA) ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #94a3b8; font-size: 0.75rem; line-height: 1.4;'>
        <b>FlashJob</b> è esclusivamente una piattaforma tecnologica di comunicazione e bacheca annunci.<br>
        Non gestisce contratti di lavoro, retribuzioni o pagamenti tra le parti.<br>
        Consulta i <a href="https://github.com/TuoNomeUtente/TuoRepo/blob/main/TERMINI.md" target="_blank" style="color: #64748b; text-decoration: underline;">Termini e Condizioni Legali</a>.
    </div>
""",
    unsafe_allow_html=True,
)