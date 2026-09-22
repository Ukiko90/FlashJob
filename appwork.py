import html
import re
import streamlit as st
import pandas as pd  # Necessario per la mappa interattiva nativa di Streamlit

st.set_page_config(
    page_title="Flashjob • Il Lavoro a Portata di Mano",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# STATO INIZIALE & COORDINATE GEOLOCALIZZATE (MILANO)
# ============================================================
if "lavoratori" not in st.session_state:
    st.session_state.lavoratori = [
        {
            "id": 1,
            "nome": "Marco Rossi",
            "mansione": "Cameriere / Sala",
            "zona": "Milano Centro",
            "tel": "+39 333 1234567",
            "completati": 14,
            "disponibile": True,
            "referenze": "Eccellente gestione della sala e dei tavoli numerosi.",
            "recensioni": "4.9 ⭐ (12 recensioni verificate)",
            "competenze": ["Lingua Inglese", "Vini & Sommelier Base", "Piattaforma POS"],
            "lat": 45.4642,
            "lon": 9.1900,  # Duomo / Centro
        },
        {
            "id": 2,
            "nome": "Giulia Bianchi",
            "mansione": "Barista / Bartender",
            "zona": "Navigli / Ticinese",
            "tel": "+39 333 9876543",
            "completati": 22,
            "disponibile": True,
            "referenze": "Velocità incredibile nei momenti di massimo afflusso.",
            "recensioni": "5.0 ⭐ (19 recensioni verificate)",
            "competenze": ["Mixology Avanzata", "Caffetteria Pro", "Gestione cassa"],
            "lat": 45.4451,
            "lon": 9.1702,  # Navigli
        },
        {
            "id": 3,
            "nome": "Davide Verdi",
            "mansione": "Chef de Rang / Jolly",
            "zona": "Porta Nuova / Corso Como",
            "tel": "+39 333 5554433",
            "completati": 30,
            "disponibile": True,
            "referenze": "Ottima attitudine al problem solving e standing elevato.",
            "recensioni": "4.8 ⭐ (15 recensioni verificate)",
            "competenze": ["Lingua Inglese", "Gestione cassa", "Mixology Base"],
            "lat": 45.4815,
            "lon": 9.1905,  # Porta Nuova
        },
    ]

if "selected_id" not in st.session_state:
    st.session_state.selected_id = None

if "visite_totali" not in st.session_state:
    st.session_state.visite_totali = 0

if "sessione_contata" not in st.session_state:
    st.session_state.visite_totali += 1
    st.session_state.sessione_contata = True

if "mio_profilo" not in st.session_state:
    st.session_state.mio_profilo = {
        "id": 999,
        "nome": "Il Tuo Nome",
        "mansione": "Cameriere / Sala",
        "zona": "Milano Centro",
        "tel": "+39 333 0000000",
        "completati": 0,
        "disponibile": False,
        "referenze": "Professionista verificato nel settore HORECA e Accoglienza.",
        "recensioni": "Nuovo utente (0 recensioni)",
        "competenze": ["Lingua Inglese"],
        "lat": 45.4650,
        "lon": 9.1890,
    }


def safe(value):
    return html.escape(str(value))


def whatsapp_url(phone):
    return "https://wa.me/" + re.sub(r"\D", "", phone)


# ============================================================
# DESIGN SYSTEM & STYLING
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --bg-gradient: linear-gradient(135deg, #fcfbfe 0%, #f4f7fc 50%, #fefcf7 100%);
    --card-bg: #ffffff;
    --text-main: #2d2b38;
    --text-muted: #7d7a92;
    --border-color: #f0f2f7;
    --shadow: 0 10px 30px rgba(138, 114, 239, 0.05);
    --radius: 20px;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background: var(--bg-gradient);
    color: var(--text-main);
}

.block-container {
    max-width: 1100px !important;
    padding: 2rem 1.5rem 5rem !important;
}

/* RIMOZIONE TOTALE BARRE STREAMLIT */
#MainMenu {visibility: hidden; display: none;}
footer {visibility: hidden; display: none;}
header {visibility: hidden; display: none;}
[data-testid="stHeader"] {display: none !important;}
[data-testid="stToolbar"] {display: none !important; visibility: hidden !important;}
[data-testid="stDecoration"] {display: none !important;}
[data-testid="stStatusWidget"] {display: none !important;}

/* STORE HEADER */
.store-header {
    background: linear-gradient(135deg, #b19ffb 0%, #8be8e5 50%, #ffd4a3 100%);
    padding: 2.5rem 2rem;
    border-radius: 28px;
    box-shadow: 0 15px 35px rgba(177, 159, 251, 0.15);
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 20px;
}
.app-info-left {
    display: flex;
    align-items: center;
    gap: 20px;
}
.app-logo-box {
    width: 90px;
    height: 90px;
    background: white;
    border-radius: 22px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
}
.app-titles h1 {
    font-size: 2.4rem;
    font-weight: 800;
    margin: 0;
    letter-spacing: -1px;
    color: #211e33;
}
.app-titles p {
    font-size: 1rem;
    margin: 4px 0 0 0;
    color: #3b3750;
    font-weight: 600;
}
.app-badges-right {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}
.store-badge {
    background: #111;
    color: white;
    padding: 10px 16px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

/* NAVIGAZIONE RADIO */
div[data-testid="stRadio"] > label { display: none; }
div[data-testid="stRadio"] div[role="radiogroup"] {
    display: flex;
    justify-content: center;
    background: white;
    padding: 6px;
    border-radius: 50px;
    box-shadow: var(--shadow);
    margin-bottom: 2.5rem;
    gap: 5px;
    border: 1px solid var(--border-color);
    flex-wrap: wrap;
}
div[data-testid="stRadio"] div[role="radiogroup"] label {
    border-radius: 40px;
    padding: 10px 18px;
    font-weight: 700;
    font-size: 0.82rem;
    color: var(--text-muted) !important;
}
div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
    background: linear-gradient(135deg, #a78bfa 0%, #60a5fa 100%) !important;
    color: white !important;
    box-shadow: 0 4px 15px rgba(167, 139, 250, 0.3);
}

/* CARD */
.custom-card {
    background: var(--card-bg);
    border-radius: var(--radius);
    padding: 1.8rem;
    box-shadow: var(--shadow);
    border: 1px solid var(--border-color);
    margin-bottom: 1.5rem;
}

/* PALLINO VERDE */
@keyframes pulse-animation {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.6); }
    70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(52, 211, 153, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(52, 211, 153, 0); }
}
.pulsing-dot {
    display: inline-block;
    width: 12px;
    height: 12px;
    background-color: #34d399;
    border-radius: 50%;
    animation: pulse-animation 1.8s infinite;
    margin-right: 6px;
    vertical-align: middle;
}
.offline-dot {
    display: inline-block;
    width: 12px;
    height: 12px;
    background-color: #cbd5e1;
    border-radius: 50%;
    margin-right: 6px;
    vertical-align: middle;
}

.badge-pop {
    display: inline-block;
    padding: 5px 12px;
    border-radius: 50px;
    font-size: 0.75rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 10px;
}
.badge-purple { background: #f3e8ff; color: #9333ea; }
.badge-blue { background: #e0f2fe; color: #0284c7; }
.badge-orange { background: #ffedd5; color: #ea580c; }
.badge-yellow { background: #fef9c3; color: #ca8a04; }

.skill-pill {
    display: inline-block;
    background: #f1f5f9;
    color: #475569;
    padding: 4px 10px;
    border-radius: 8px;
    font-size: 0.75rem;
    font-weight: 700;
    margin-right: 6px;
    margin-bottom: 6px;
}

.stats-container {
    display: flex;
    background: #f8fafc;
    border-radius: 16px;
    padding: 1rem;
    margin: 1.2rem 0;
    text-align: center;
    border: 1px solid #f1f5f9;
}
.stat-box { flex: 1; border-right: 1px solid #e2e8f0; }
.stat-box:last-child { border-right: none; }
.stat-box strong { display: block; font-size: 1.3rem; color: #8b5cf6; }
.stat-box span { font-size: 0.7rem; color: #7d7a92; font-weight: 700; text-transform: uppercase; }

.stButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 14px;
    background: linear-gradient(135deg, #a78bfa 0%, #60a5fa 100%);
    color: white;
    font-weight: 700;
    border: none;
    box-shadow: 0 4px 15px rgba(167, 139, 250, 0.25);
    transition: all 0.2s ease;
}
.stButton > button:hover {
    opacity: 0.92;
    transform: translateY(-2px);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# BARRA LATERALE (ADMIN)
# ============================================================
with st.sidebar:
    st.markdown("### 🔐 Area Riservata Admin")
    password_inserita = st.text_input(
        "Password Admin", type="password", key="input_pwd_admin"
    )

    mostra_admin = False
    if password_inserita == "admin123":
        st.success("Accesso Admin Autorizzato ✅")
        mostra_admin = True
    elif password_inserita != "":
        st.error("Password errata ❌")

# ============================================================
# STORE HEADER
# ============================================================
st.markdown(
    """
<div class="store-header">
    <div class="app-info-left">
        <div class="app-logo-box">⚡</div>
        <div class="app-titles">
            <h1>Flashjob</h1>
            <p>Il Lavoro a Portata di Mano • Milano & Hinterland</p>
        </div>
    </div>
    <div class="app-badges-right">
        <div class="store-badge">🍏 App Store Ufficiale</div>
        <div class="store-badge">🤖 Google Play Ufficiale</div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

menu_opzioni = [
    "Panoramica",
    "🗺️ Mappa & Radar Milano",
    "Database & Filtri Azienda",
    "Area Lavoratore",
    "Piani & Abbonamenti",
]
if mostra_admin:
    menu_opzioni.append("📊 Dashboard Admin")

scelta = st.radio("Navigazione", menu_opzioni, horizontal=True)

# ============================================================
# 1. PANORAMICA
# ============================================================
if scelta == "Panoramica":
    st.markdown(
        """
        <div style="text-align: center; max-width: 800px; margin: 0 auto 2.5rem auto;">
            <span class="badge-pop badge-purple">Copertura Iper-Locale: Milano</span>
            <h2 style='font-weight:800; font-size:2.2rem; margin-top:10px; color:#211e33;'>Trova personale o lavoro nel raggio di pochi chilometri.</h2>
            <p style='color:var(--text-muted); font-size:1.1rem; line-height:1.6; margin-top:10px;'>Flashjob geolocalizza in tempo reale i professionisti dell'accoglienza a Milano, dai Navigli a Corso Como, dal Centro Storico a Porta Romana.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
        <div class="custom-card" style="height: 100%;">
            <span class="badge-pop badge-blue">Per i Locali di Milano</span>
            <h3 style="font-size: 1.3rem; margin-top: 5px;">Radar Posizione inTempo Reale</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6;">
                Visualizza sulla mappa integrata chi è libero proprio adesso vicino al tuo ristorante o bar per coprire le emergenze dell'ultimo minuto.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="custom-card" style="height: 100%;">
            <span class="badge-pop badge-purple">Per i Lavoratori</span>
            <h3 style="font-size: 1.3rem; margin-top: 5px;">Fatti trovare dai locali vicini</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6;">
                Attiva il pallino verde e segnala la tua presenza nei quartieri più caldi della movida e della ristorazione milanese.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

# ============================================================
# 2. MAPPA & RADAR MILANO (NUOVA SEZIONE)
# ============================================================
elif scelta == "🗺️ Mappa & Radar Milano":
    st.markdown(
        """
        <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>🗺️ Radar Mappa Interattiva - Milano</h2>
        <p style='color:var(--text-muted); margin-bottom:1.5rem;'>Visualizzazione in tempo reale dei professionisti attivi geolocalizzati sul territorio milanese.</p>
    """,
        unsafe_allow_html=True,
    )

    # Filtriamo solo i lavoratori disponibili per la mappa
    lavoratori_attivi = [l for l in st.session_state.lavoratori if l["disponibile"]]

    if lavoratori_attivi:
        df_mappa = pd.DataFrame(lavoratori_attivi)
        # Streamlit st.map richiede colonne denominate 'lat' e 'lon'
        st.map(
            df_mappa,
            latitude="lat",
            longitude="lon",
            size=50,
            color="#a78bfa",
            zoom=13,
        )
        st.caption(
            "📍 I pin sulla mappa indicano i professionisti con pallino verde attivo pronti per interventi last-minute a Milano."
        )
    else:
        st.warning(
            "Nessun professionista con pallino verde attivo al momento. Vai nell'Area Lavoratore per attivarne uno!"
        )

    st.markdown("### 📌 Elenco Rapido nella Zona di Milano")
    for lav in st.session_state.lavoratori:
        if lav["disponibile"]:
            st.markdown(
                f"""
            <div class="custom-card" style="padding: 1rem; margin-bottom: 0.8rem; display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <span class="pulsing-dot"></span><b>{safe(lav["nome"])}</b> — <span style="color:var(--text-muted);">{safe(lav["mansione"])}</span> 
                    <div style="font-size:0.85rem; color:#0284c7; margin-top:4px;">📍 Zona: {safe(lav["zona"])}</div>
                </div>
                <div>
                    <a href="{whatsapp_url(lav["tel"])}" target="_blank" style="background:#34d399; color:white; padding:8px 14px; border-radius:10px; text-decoration:none; font-weight:700; font-size:0.8rem;">Contatta</a>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

# ============================================================
# 3. DATABASE & FILTRI AZIENDA
# ============================================================
elif scelta == "Database & Filtri Azienda":
    selected_c = next(
        (
            item
            for item in st.session_state.lavoratori
            if item["id"] == st.session_state.selected_id
        ),
        None,
    )

    if selected_c is not None:
        if st.button("← Torna al database completo"):
            st.session_state.selected_id = None
            st.rerun()

        stato_html = (
            '<span class="pulsing-dot"></span><b style="color:#059669;">DISPONIBILE ORA</b>'
            if selected_c["disponibile"]
            else '<span class="offline-dot"></span><span style="color:#888;">NON DISPONIBILE</span>'
        )

        comp_html = "".join(
            [f'<span class="skill-pill">✓ {c}</span>' for c in selected_c["competenze"]]
        )

        st.markdown(
            f"""
        <div class="custom-card" style="margin-top: 20px;">
            <div style="display: flex; align-items: center; gap: 20px;">
                <div style="width:80px; height:80px; background:#f3e8ff; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:2rem; border:3px solid #a78bfa;">👤</div>
                <div>
                    <div style="margin-bottom:6px;">{stato_html}</div>
                    <h2 style="margin:0; font-size:1.5rem;">{safe(selected_c["nome"])}</h2>
                    <p style="color:var(--text-muted); margin:4px 0 0 0; font-weight:600;">{safe(selected_c["mansione"])} · 📍 {safe(selected_c["zona"])}</p>
                    <p style="color:#d97706; margin:6px 0 0 0; font-weight:700; font-size:0.9rem;">⭐ {safe(selected_c["recensioni"])}</p>
                </div>
            </div>
            
            <div style="margin-top: 15px;">
                <p style="font-size:0.8rem; font-weight:700; color:#7d7a92; text-transform:uppercase; margin-bottom:8px;">Competenze certificate:</p>
                {comp_html}
            </div>

            <div class="stats-container">
                <div class="stat-box">
                    <strong>{safe(selected_c["completati"])}</strong>
                    <span>Turni fatti</span>
                </div>
                <div class="stat-box">
                    <strong>Milano</strong>
                    <span>Copertura</span>
                </div>
            </div>
            
            <div style="background:#f3e8ff; border-left:4px solid #a78bfa; padding:15px; border-radius:0 12px 12px 0; margin-top:15px; font-style:italic; color:#6b21a8;">
                “{safe(selected_c["referenze"])}”
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.link_button(
            "💬 Contatta e Prenota su WhatsApp",
            whatsapp_url(selected_c["tel"]),
            use_container_width=True,
        )

    else:
        st.markdown(
            """
            <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Database Contatti & Filtri</h2>
            <p style='color:var(--text-muted); margin-bottom:1.5rem;'>Cerca tra i professionisti disponibili a Milano e filtra per competenze.</p>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="custom-card" style="padding: 1.2rem; background: #fafafa;">',
            unsafe_allow_html=True,
        )
        col_f1, col_f2 = st.columns(2)

        with col_f1:
            filtro_mansione = st.selectbox(
                "Filtra per Mansione",
                [
                    "Tutte",
                    "Cameriere / Sala",
                    "Barista / Bartender",
                    "Chef de Rang / Jolly",
                    "Aiuto Cuoco",
                    "Hostess / Accoglienza",
                    "Booking / Reception",
                ],
                key="filtro_mansione_box",
            )

        with col_f2:
            solo_disponibili = st.checkbox(
                "Mostra solo disponibili con pallino verde",
                value=False,
                key="filtro_disp_box",
            )

        st.markdown("</div>", unsafe_allow_html=True)

        lavoratori_filtrati = st.session_state.lavoratori
        if filtro_mansione != "Tutte":
            lavoratori_filtrati = [
                l for l in lavoratori_filtrati if l["mansione"] == filtro_mansione
            ]
        if solo_disponibili:
            lavoratori_filtrati = [l for l in lavoratori_filtrati if l["disponibile"]]

        for lav in lavoratori_filtrati:
            col_info, col_btn = st.columns([3, 1], gap="medium")

            with col_info:
                badge_stato = (
                    '<span class="pulsing-dot"></span><b style="color:#059669; font-size:0.75rem;">DISPONIBILE ORA</b>'
                    if lav["disponibile"]
                    else '<span class="offline-dot"></span><span style="color:#888; font-size:0.75rem;">NON DISPONIBILE</span>'
                )

                st.markdown(
                    f"""
                    <div class="custom-card" style="margin-bottom:1rem; padding:1.2rem 1.5rem;">
                        <div style="margin-bottom:6px;">{badge_stato}</div>
                        <h3 style="margin:0; font-size:1.15rem;">{safe(lav["nome"])}</h3>
                        <p style="color:var(--text-muted); margin:3px 0; font-size:0.9rem; font-weight:600;">{safe(lav["mansione"])} · 📍 {safe(lav["zona"])}</p>
                        <p style="color:#d97706; margin:4px 0; font-weight:700; font-size:0.8rem;">⭐ {safe(lav["recensioni"])}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with col_btn:
                st.markdown(
                    "<div style='margin-top: 30px;'></div>", unsafe_allow_html=True
                )
                if st.button("Vedi profilo", key=f"btn_card_{lav['id']}"):
                    st.session_state.selected_id = lav["id"]
                    st.rerun()

# ============================================================
# 4. AREA LAVORATORE
# ============================================================
elif scelta == "Area Lavoratore":
    st.markdown(
        """
        <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Area Personale Lavoratore</h2>
        <p style='color:var(--text-muted); margin-bottom:2rem;'>Imposta la tua zona di Milano, le tue competenze e la tua disponibilità.</p>
    """,
        unsafe_allow_html=True,
    )

    mio = st.session_state.mio_profilo

    nuova_mansione = st.selectbox(
        "Seleziona la tua mansione principale",
        [
            "Cameriere / Sala",
            "Barista / Bartender",
            "Chef de Rang / Jolly",
            "Aiuto Cuoco",
            "Hostess / Accoglienza",
            "Booking / Reception",
        ],
        index=0,
    )
    mio["mansione"] = nuova_mansione

    nuova_zona = st.selectbox(
        "Seleziona la tua zona a Milano",
        [
            "Milano Centro",
            "Navigli / Ticinese",
            "Porta Nuova / Corso Como",
            "Brera / Garibaldi",
            "Città Studi / Lambrate",
            "Fiera / CityLife",
            "Navigli / Bocconi",
        ],
        index=0,
    )
    mio["zona"] = nuova_zona

    # Aggiorna coordinate approssimative in base alla zona selezionata a Milano
    zone_coords = {
        "Milano Centro": (45.4642, 9.1900),
        "Navigli / Ticinese": (45.4451, 9.1702),
        "Porta Nuova / Corso Como": (45.4815, 9.1905),
        "Brera / Garibaldi": (45.4721, 9.1850),
        "Città Studi / Lambrate": (45.4780, 9.2270),
        "Fiera / CityLife": (45.4770, 9.1550),
        "Navigli / Bocconi": (45.4470, 9.1900),
    }
    mio["lat"], mio["lon"] = zone_coords.get(nuova_zona, (45.4642, 9.1900))

    st.markdown("### Le tue competenze certificate")
    scelta_comp = st.multiselect(
        "Seleziona le abilità da mostrare ai locali",
        [
            "Lingua Inglese",
            "Vini & Sommelier Base",
            "Mixology Avanzata",
            "Caffetteria Pro",
            "Gestione cassa",
            "Piattaforma POS",
        ],
        default=mio["competenze"],
    )
    mio["competenze"] = scelta_comp

    st.markdown("### Gestione Stato in Tempo Reale")
    nuova_disp = st.toggle(
        "🟢 Attiva disponibilità sulla mappa di Milano",
        value=mio["disponibile"],
        key="toggle_disponibilita_lavoratore",
    )

    if (
        nuova_disp != mio["disponibile"]
        or mio["mansione"] != nuova_mansione
        or mio["zona"] != nuova_zona
    ):
        mio["disponibile"] = nuova_disp
        trovato = next(
            (item for item in st.session_state.lavoratori if item["id"] == mio["id"]),
            None,
        )
        if nuova_disp:
            if trovato:
                trovato["disponibile"] = True
                trovato["mansione"] = mio["mansione"]
                trovato["zona"] = mio["zona"]
                trovato["lat"] = mio["lat"]
                trovato["lon"] = mio["lon"]
                trovato["competenze"] = mio["competenze"]
            else:
                st.session_state.lavoratori.append(mio.copy())
        else:
            if trovato:
                st.session_state.lavoratori = [
                    item for item in st.session_state.lavoratori if item["id"] != mio["id"]
                ]

        st.success(
            "Stato e posizione aggiornati con successo sulla mappa di Milano!"
        )

# ============================================================
# 5. PIANI & ABBONAMENTI
# ============================================================
elif scelta == "Piani & Abbonamenti":
    st.markdown(
        """
        <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Piani & Funzioni Elite ⚡</h2>
        <p style='color:var(--text-muted); margin-bottom:2rem;'>Scopri i nuovi strumenti avanzati basati sulla geolocalizzazione milanese.</p>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown(
            """
        <div class="custom-card">
            <span class="badge-pop badge-blue">Novità 🚀</span>
            <h3 style="margin-top:10px; font-size:1.2rem;">Radar Urgenze Milano</h3>
            <div style="font-size: 1.2rem; font-weight: 800; color: #0284c7; margin: 10px 0;">Notifiche Flash Raggio 5km</div>
            <p style="font-size:0.85rem; color:var(--text-muted);">Sistema di allerta istantanea per i locali che cercano personale d'emergenza geolocalizzato.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Attiva Radar", key="btn_radar"):
            st.toast("Radar Urgenze Milano attivato con successo!")

    with col2:
        st.markdown(
            """
        <div class="custom-card">
            <span class="badge-pop badge-orange">Novità 🌟</span>
            <h3 style="margin-top:10px; font-size:1.2rem;">Badge Competenze Pro</h3>
            <div style="font-size: 1.2rem; font-weight: 800; color: #ea580c; margin: 10px 0;">Certificazioni</div>
            <p style="font-size:0.85rem; color:var(--text-muted);">Aggiungi qualifiche speciali al tuo profilo per saltare in cima alle ricerche nella zona.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Richiedi Badge", key="btn_badge"):
            st.toast("Richiesta certificazione inviata!")

    with col3:
        st.markdown(
            """
        <div class="custom-card">
            <span class="badge-pop badge-yellow">Novità ⚡</span>
            <h3 style="margin-top:10px; font-size:1.2rem;">Reputazione Verificata</h3>
            <div style="font-size: 1.2rem; font-weight: 800; color: #ca8a04; margin: 10px 0;">Feedback Bidirezionale</div>
            <p style="font-size:0.85rem; color:var(--text-muted);">Il sistema di recensioni incrociate per garantire affidabilità massima nel settore HORECA.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Scopri di più", key="btn_rep"):
            st.toast("Funzione inclusa nel tuo account!")

# ============================================================
# 6. DASHBOARD ADMIN
# ============================================================
elif scelta == "📊 Dashboard Admin":
    st.markdown(
        """
        <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>📊 Dashboard Admin & Statistiche</h2>
        <p style='color:var(--text-muted); margin-bottom:2rem;'>Area protetta per il controllo del traffico e dei profili attivi sul territorio.</p>
    """,
        unsafe_allow_html=True,
    )

    col_m1, col_m2 = st.columns(2, gap="medium")

    with col_m1:
        st.markdown(
            f"""
        <div class="custom-card" style="text-align: center; padding: 2.5rem;">
            <span class="badge-pop badge-blue">Traffic Monitor</span>
            <h3 style="color: var(--text-muted); font-size: 1rem; margin-top: 10px;">Visite Totali (Aperture App)</h3>
            <div style="font-size: 3rem; font-weight: 800; color: #0284c7; margin: 15px 0;">{st.session_state.visite_totali}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col_m2:
        st.markdown(
            f"""
        <div class="custom-card" style="text-align: center; padding: 2.5rem;">
            <span class="badge-pop badge-purple">Conversion Monitor</span>
            <h3 style="color: var(--text-muted); font-size: 1rem; margin-top: 10px;">Lavoratori Geolocalizzati / Online</h3>
            <div style="font-size: 3rem; font-weight: 800; color: #9333ea; margin: 15px 0;">{len(st.session_state.lavoratori)}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )