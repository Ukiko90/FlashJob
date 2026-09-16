from datetime import datetime
import pandas as pd
import streamlit as st

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(
    page_title="FlashJob Milano - Turni Last Minute",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- STILE CSS PROFESSIONALE (UI/UX REFRESH) ---
st.markdown(
    """
    <style>
    /* Sfondo generale e container principale */
    .main { background-color: #f1f5f9; }
    .block-container { 
        padding-top: 1rem !important; 
        padding-bottom: 5rem !important; 
        max-width: 720px; 
    }

    /* Rimozione padding extra di Streamlit */
    div.block-container { padding-left: 1rem; padding-right: 1rem; }

    /* Card standard per i turni */
    .flash-card {
        background-color: #ffffff;
        padding: 22px;
        border-radius: 14px;
        box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.05);
        margin-bottom: 16px;
        border: 1px solid #e2e8f0;
        transition: all 0.2s ease;
    }
    .flash-card:hover {
        border-color: #cbd5e1;
        box-shadow: 0 6px 24px -2px rgba(15, 23, 42, 0.08);
    }

    /* Card in evidenza PRO (5€/mese) */
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

    /* Campi di input */
    .stTextInput > div > div > input, .stSelectbox > div > div > div, .stDateInput > div > div > input {
        border-radius: 8px !important;
        border-color: #cbd5e1 !important;
        background-color: #ffffff !important;
    }

    /* Tipografia pulita */
    h1, h2, h3 { color: #0f172a; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }

    /* Badge e Tag */
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
    .badge-pro { 
        background-color: #fef08a; 
        color: #854d0e; 
        padding: 3px 10px; 
        border-radius: 12px; 
        font-size: 0.7rem; 
        font-weight: 700; 
        display: inline-block; 
        margin-bottom: 8px; 
    }
    
    /* Box Informativi / Sezioni */
    .info-box {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 18px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- MEMORIA DI STATO (SESSION STATE) ---
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
      },
      {
          "id": 2,
          "azienda": "Panino Giusto - Duomo",
          "citta": "Milano",
          "mansione": "Cameriere di Sala",
          "data": "2026-06-21",
          "orario": "12:00 - 16:00",
          "compenso": "50€ netti",
          "stato": "Aperta",
          "premium": False,
      },
  ]

if "lavoratori_registrati" not in st.session_state:
  # Database locale simulato dei lavoratori schedulati
  st.session_state.lavoratori_registrati = []

if "candidature" not in st.session_state:
  st.session_state.candidature = []

if "utente_corrente" not in st.session_state:
  st.session_state.utente_corrente = None  # Telefono del lavoratore loggato

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
          <text x="125" y="83" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="500" fill="#94a3b8">Milano Last-Minute Hub</text>
        </svg>
    </div>
</div>
"""
st.markdown(logo_html, unsafe_allow_html=True)

# Badge Città
st.markdown(
    """
    <div style='text-align: center; margin-bottom: 22px;'>
        <span class='badge-milano'>📍 Esclusivamente attivo su MILANO &bull; Turni Verificati</span>
    </div>
""",
    unsafe_allow_html=True,
)

# --- MENU A TENDINA PRINCIPALE (LAYOUT PULITO) ---
ruolo = st.selectbox(
    "Seleziona la tua area d'accesso:",
    [
        "👤 Lavoratore (Schedulazione & Bacheca Turni)",
        "💼 Azienda (Pubblica Turno Urgente)",
        "⭐ Azienda PRO (Abbonamento 5€/mese)",
    ],
)

st.markdown(
    "<hr style='margin: 20px 0; border: none; border-top: 1px solid"
    " #e2e8f0;'>",
    unsafe_allow_html=True,
)

# ==========================================
# 👤 AREA LAVORATORE & SCHEDULAZIONE
# ==========================================
if "Lavoratore" in ruolo:
  st.subheader("👤 Profilo & Schedulazione Lavoratore")

  # Verifica se l'utente è già schedulato (memorizzato in sessione)
  if st.session_state.utente_corrente is None:
    st.markdown(
        """
        <div class="info-box">
            <h4 style="margin-top:0; color:#0f172a; font-size:1rem;">Benvenuto in FlashJob Milano!</h4>
            <p style="font-size:0.88rem; color:#475569; margin-bottom:0;">Per accedere alla bacheca dei turni e candidarti con 1 solo click, effettua la schedulazione iniziale del tuo profilo. Ti bastano 30 secondi.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("form_schedulazione"):
      col_s1, col_s2 = st.columns(2)
      with col_s1:
        nome = st.text_input(
            "Nome e Cognome *", placeholder="Es. Marco Rossi"
        )
      with col_s2:
        telefono = st.text_input(
            "WhatsApp / Telefono *", placeholder="Es. 3331234567"
        )

      col_s3, col_s4 = st.columns(2)
      with col_s3:
        mansione_principale = st.selectbox(
            "Mansione Principale *",
            [
                "Cameriere / Sala",
                "Barista / Bartender",
                "Cuoco / Aiuto Cuoco",
                "Runner / Facchino",
                "Altro",
            ],
        )
      with col_s4:
        esperienza = st.selectbox(
            "Esperienza nel settore",
            ["Meno di 1 anno", "1 - 3 anni", "Oltre 3 anni"],
        )

      note_disponibilita = st.text_input(
          "Disponibilità oraria / giorni",
          placeholder="Es. Disponibile la sera e nei weekend",
      )

      btn_schedula = st.form_submit_button(
          "✅ Schedula Profilo e Accedi ai Turni"
      )

      if btn_schedula:
        if not nome or not telefono:
          st.error(
              "⚠️ Compila i campi obbligatori (Nome e Telefono) per completare"
              " la schedulazione."
          )
        else:
          # Salva o aggiorna nel database dei lavoratori schedulati
          nuovo_lavoratore = {
              "nome": nome,
              "telefono": telefono,
              "mansione": mansione_principale,
              "esperienza": esperienza,
              "disponibilita": note_disponibilita,
              "registrato_il": datetime.now().strftime("%Y-%m-%d %H:%M"),
          }
          st.session_state.lavoratori_registrati.append(nuovo_lavoratore)
          st.session_state.utente_corrente = telefono
          st.success("🎉 Profilo schedulato con successo! Accesso consentito.")
          st.rerun()

  else:
    # Utente già schedulato: Mostra badge benvenuto e bacheca turni
    lavoratore_info = next(
        (
            l
            for l in st.session_state.lavoratori_registrati
            if l["telefono"] == st.session_state.utente_corrente
        ),
        {"nome": "Utente", "mansione": "Generico"},
    )

    st.markdown(
        f"""
        <div style="background-color: #f8fafc; border: 1px solid #cbd5e1; padding: 12px 16px; border-radius: 10px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <div>
                <span style="font-size: 0.85rem; color: #64748b;">Profilo Schedulato:</span><br>
                <b style="color: #0f172a; font-size: 1rem;">👤 {lavoratore_info['nome']} ({lavoratore_info['mansione']})</b>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("⚡ Bacheca Turni Attivi a Milano")

    offerte_aperte = [
        o for o in st.session_state.offerte if o["stato"] == "Aperta"
    ]
    # Ordinamento: Prima i PRO in evidenza
    offerte_aperte.sort(key=lambda x: x.get("premium", False), reverse=True)

    if not offerte_aperte:
      st.info(
          "Nessun turno disponibile a Milano in questo momento. Torna a"
          " controllare a breve!"
      )
    else:
      for offerta in offerte_aperte:
        is_pro = offerta.get("premium", False)
        card_class = "flash-card-pro" if is_pro else "flash-card"
        badge_html = (
            "<span class='badge-pro'>⭐ TURNO IN EVIDENZA</span><br>"
            if is_pro
            else ""
        )

        st.markdown(
            f"""
                <div class="{card_class}">
                    {badge_html}
                    <h3 style="margin:0 0 6px 0; color:#0f172a; font-size:1.1rem;">📍 {offerta['azienda']} <span style="font-size:0.85rem; font-weight:normal; color:#64748b;">(Milano)</span></h3>
                    <p style="margin:4px 0; font-size:0.95rem; font-weight:600; color:#334155;">Mansione: {offerta['mansione']}</p>
                    <p style="margin:4px 0; color:#475569; font-size:0.85rem;">📅 {offerta['data']} &nbsp;|&nbsp; 🕒 {offerta['orario']}</p>
                    <p style="margin:8px 0 0 0; font-size:1.1rem; font-weight:700; color:#16a34a;">💰 Compenso: {offerta['compenso']}</p>
                </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            f"🔥 Candidati Subito per {offerta['azienda']}",
            key=f"cand_{offerta['id']}",
        ):
          nuova_candidatura = {
              "id": len(st.session_state.candidature) + 1,
              "offerta_id": offerta["id"],
              "nome_lavoratore": lavoratore_info["nome"],
              "telefono": lavoratore_info["telefono"],
              "data_candidatura": datetime.now().strftime("%H:%M:%S"),
          }
          st.session_state.candidature.append(nuova_candidatura)
          st.success(
              "🎉 Candidatura inoltrata con successo! L'azienda riceverà il tuo"
              " contatto WhatsApp."
          )


# ==========================================
# 💼 AREA AZIENDA (PUBBLICAZIONE TURNO)
# ==========================================
elif "Azienda" in ruolo and "PRO" not in ruolo:
  st.subheader("💼 Pubblica un Turno d'Emergenza (Milano)")

  st.markdown(
      """
        <div style="background-color: #eff6ff; border: 1px dashed #3b82f6; padding: 14px; border-radius: 10px; margin-bottom: 20px; text-align: center; color: #1e3a8a; font-size: 0.88rem;">
        💡 <b>Soluzione Last-Minute:</b> Il turno viene pubblicato istantaneamente nella bacheca di Milano. Passa ad <b>Azienda PRO</b> per soli <b>5€ al mese</b> per sbloccare annunci illimitati e massima visibilità in cima alla lista!
        </div>
    """,
      unsafe_allow_html=True,
  )

  with st.form("form_azienda_free", clear_on_submit=True):
    nome_azienda = st.text_input(
        "Nome Attività / Locale *", placeholder="Es. Ristorante Navigli"
    )
    mansione = st.text_input(
        "Mansione Richiesta *", placeholder="Es. Cameriere / Barista"
    )

    col1, col2 = st.columns(2)
    with col1:
      data_turno = st.date_input("Data del Turno *")
    with col2:
      orario = st.text_input("Orario *", placeholder="Es. 18:00 - 00:00")

    compenso = st.text_input("Compenso Netto *", placeholder="Es. 80€ netti")

    st.markdown(
        "<div style='margin-top: 8px; font-size:0.8rem;"
        " color:#64748b;'>*Campi obbligatori</div>",
        unsafe_allow_html=True,
    )
    pubblica = st.form_submit_button("🚀 Pubblica Turno in Bacheca (Gratis)")

    if pubblica:
      if nome_azienda and mansione and compenso and orario:
        nuova_offerta = {
            "id": len(st.session_state.offerte) + 1,
            "azienda": nome_azienda,
            "citta": "Milano",
            "mansione": mansione,
            "data": str(data_turno),
            "orario": orario,
            "compenso": compenso,
            "stato": "Aperta",
            "premium": False,
        }
        st.session_state.offerte.append(nuova_offerta)
        st.success(
            "🎉 Turno pubblicato con successo nella bacheca di Milano!"
        )
        st.rerun()
      else:
        st.warning("Compila tutti i campi obbligatori per procedere.")

  st.markdown(
      "<hr style='margin: 25px 0; border: none; border-top: 1px solid"
      " #e2e8f0;'>",
      unsafe_allow_html=True,
  )
  st.subheader("📋 Candidature Ricevute dai Lavoratori Schedulati")

  if not st.session_state.candidature:
    st.info("Nessuna candidatura ricevuta al momento.")
  else:
    for cand in st.session_state.candidature:
      st.markdown(
          f"""
            <div class="flash-card">
                <p style="margin:0; font-weight:bold; color:#0f172a;">👤 {cand['nome_lavoratore']}</p>
                <p style="margin:4px 0 0 0; color:#334155;">📞 Contatto WhatsApp: <b style="color:#0f172a;">{cand['telefono']}</b></p>
                <p style="margin:4px 0 0 0; font-size:0.75rem; color:#64748b;">Candidatura inviata alle ore {cand['data_candidatura']}</p>
            </div>
        """,
          unsafe_allow_html=True,
      )


# ==========================================
# ⭐ AREA AZIENDA PRO (ABBONAMENTO 5€/MESE)
# ==========================================
else:
  st.subheader("⭐ FlashJob PRO - Abbonamento Aziende")
  st.markdown(
      "<p style='color: #475569; font-size: 0.95rem;'>Massimizza la ricerca di personale a Milano con il piano professionale illimitato.</p>",
      unsafe_allow_html=True,
  )

  col_p1, col_p2 = st.columns(2)

  with col_p1:
    st.markdown(
        """
        <div class="flash-card" style="text-align: center; height: 100%;">
            <h4 style="margin-bottom:5px; color:#0f172a;">Piano Base</h4>
            <p style="font-size:0.8rem; color:#64748b; margin-bottom:15px;">Per piccoli locali occasionali</p>
            <p style="font-size:1.2rem; font-weight:800; color:#0f172a; margin-bottom:15px;">Gratis</p>
            <ul style="text-align:left; font-size:0.85rem; color:#475569; padding-left:15px; margin-bottom:0;">
                <li>Visibilità standard</li>
                <li>Annunci limitati</li>
            </ul>
        </div>
    """,
        unsafe_allow_html=True,
    )

  with col_p2:
    st.markdown(
        """
        <div class="flash-card-pro" style="text-align: center; height: 100%;">
            <h4 style="margin-bottom:5px; color:#854d0e;">Piano PRO</h4>
            <p style="font-size:0.8rem; color:#854d0e; margin-bottom:15px;"><b>Il più scelto a Milano</b></p>
            <p style="font-size:1.4rem; font-weight:800; color:#ca8a04; margin-bottom:15px;">5 € <span style="font-size:0.8rem; font-weight:normal;">/ mese</span></p>
            <ul style="text-align:left; font-size:0.85rem; color:#713f12; padding-left:15px; margin-bottom:0;">
                <li><b>Turni illimitati</b></li>
                <li><b>Badge "IN EVIDENZA"</b> in cima alla bacheca</li>
                <li>Notifica prioritaria ai lavoratori</li>
            </ul>
        </div>
    """,
        unsafe_allow_html=True,
    )

  st.markdown(
      "<div style='margin-top: 20px;'></div>", unsafe_allow_html=True
  )

  if st.button("💳 Attiva FlashJob PRO (5€ / mese)"):
    st.success(
        "🎉 Abbonamento PRO attivato con successo! La tua attività ha ora priorità"
        " assoluta a Milano."
    )

# --- FOOTER / NOTE LEGALI ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #94a3b8; font-size: 0.75rem; line-height: 1.4;'>
        <b>FlashJob Milano</b> è esclusivamente una piattaforma tecnologica di comunicazione e bacheca annunci.<br>
        Non gestisce contratti di lavoro, retribuzioni o pagamenti diretti tra le parti.<br>
        Consulta i <a href="https://github.com/TuoNomeUtente/TuoRepo/blob/main/TERMINI.md" target="_blank" style="color: #64748b; text-decoration: underline;">Termini e Condizioni Legali</a>.
    </div>
""",
    unsafe_allow_html=True,
)