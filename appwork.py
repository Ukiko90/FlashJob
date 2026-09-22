import html
import re
import streamlit as st

st.set_page_config(
    page_title="Flashjob Pro • Enterprise Staffing Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# STATE INITIALIZATION & ENTERPRISE DATABASE
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
            "referenze": "Eccellente gestione della sala e dei tavoli numerosi. Standing impeccabile.",
            "recensioni": "4.9 ⭐ (12 recensioni verificate)",
            "competenze": ["Lingua Inglese", "Vini & Sommelier Base", "Piattaforma POS"],
            "tariffa": "22€/h",
            "affidabilita": "99.4%",
        },
        {
            "id": 2,
            "nome": "Giulia Bianchi",
            "mansione": "Barista / Bartender",
            "zona": "Navigli / Ticinese",
            "tel": "+39 333 9876543",
            "completati": 22,
            "disponibile": True,
            "referenze": "Velocità incredibile nei momenti di massimo afflusso e cocktail artigianali.",
            "recensioni": "5.0 ⭐ (19 recensioni verificate)",
            "competenze": ["Mixology Avanzata", "Caffetteria Pro", "Gestione cassa"],
            "tariffa": "25€/h",
            "affidabilita": "99.9%",
        },
        {
            "id": 3,
            "nome": "Davide Verdi",
            "mansione": "Chef de Rang / Jolly",
            "zona": "Porta Nuova / Corso Como",
            "tel": "+39 333 5554433",
            "completati": 30,
            "disponibile": True,
            "referenze": "Ottima attitudine al problem solving e standing elevato per ristoranti stellati.",
            "recensioni": "4.8 ⭐ (15 recensioni verificate)",
            "competenze": ["Lingua Inglese", "Gestione cassa", "Mixology Base"],
            "tariffa": "24€/h",
            "affidabilita": "98.8%",
        },
        {
            "id": 4,
            "nome": "Sofia Neri",
            "mansione": "Aiuto Cuoco",
            "zona": "Brera / Garibaldi",
            "tel": "+39 333 7778899",
            "completati": 18,
            "disponibile": True,
            "referenze": "Grande precisione nella linea e velocità nei piatti freddi e caldi.",
            "recensioni": "4.9 ⭐ (14 recensioni verificate)",
            "competenze": ["HACCP Avanzato", "Preparazione Linea"],
            "tariffa": "20€/h",
            "affidabilita": "99.1%",
        },
        {
            "id": 5,
            "nome": "Luca Colombo",
            "mansione": "Cameriere / Sala",
            "zona": "Città Studi / Lambrate",
            "tel": "+39 333 4443322",
            "completati": 9,
            "disponibile": True,
            "referenze": "Puntuale, solare e molto gradito dalla clientela internazionale.",
            "recensioni": "4.7 ⭐ (8 recensioni verificate)",
            "competenze": ["Lingua Inglese", "Piattaforma POS"],
            "tariffa": "19€/h",
            "affidabilita": "97.5%",
        },
        {
            "id": 6,
            "nome": "Martina Rinaldi",
            "mansione": "Barista / Bartender",
            "zona": "Fiera / CityLife",
            "tel": "+39 333 6661122",
            "completati": 27,
            "disponibile": True,
            "referenze": "Top livello nella caffetteria e cocktail bar di alto standing.",
            "recensioni": "5.0 ⭐ (24 recensioni verificate)",
            "competenze": ["Caffetteria Pro", "Mixology Avanzata"],
            "tariffa": "26€/h",
            "affidabilita": "99.8%",
        },
        {
            "id": 7,
            "nome": "Alessandro Gallo",
            "mansione": "Chef de Rang / Jolly",
            "zona": "Isola",
            "tel": "+39 333 2221144",
            "completati": 16,
            "disponibile": True,
            "referenze": "Grande professionalità e ottima parlata inglese per eventi corporate.",
            "recensioni": "4.9 ⭐ (11 recensioni verificate)",
            "competenze": ["Lingua Inglese", "Vini & Sommelier Base"],
            "tariffa": "23€/h",
            "affidabilita": "98.9%",
        },
    ]

if "selected_id" not in st.session_state:
    st.session_state.selected_id = None

if "visite_totali" not in st.session_state:
    st.session_state.visite_totali = 0

if "sessione_contata" not in st.session_state:
    st.session_state.visite_totali += 1
    st.session_state.sessione_contata = True

if "abbonamento_attivo" not in st.session_state:
    st.session_state.abbonamento_attivo = False

if "mio_profilo" not in st.session_state:
    st.session_state.mio_profilo = {
        "id": 999,
        "nome": "Il Tuo Nome Professionale",
        "mansione": "Cameriere / Sala",
        "zona": "Milano Centro",
        "tel": "+39 333 0000000",
        "completati": 0,
        "disponibile": False,
        "referenze": "Professionista verificato nel settore accoglienza e ristorazione di lusso.",
        "recensioni": "Nuovo utente (In attesa di prima recensione)",
        "competenze": ["Lingua Inglese", "Piattaforma POS"],
        "tariffa": "21€/h",
        "affidabilita": "100%",
    }

if "richieste_turno" not in st.session_state:
    st.session_state.richieste_turno = [
        {"id": 101, "locale": "Ristorante Nobu Milano", "mansione": "Cameriere / Sala", "data": "Domani, 19:30 - 23:30", "compenso": "90€ netti", "stato": "Aperto"},
        {"id": 102, "locale": "Armani Bamboo Bar", "mansione": "Barista / Bartender", "data": "Sabato, 21:00 - 02:00", "compenso": "140€ netti", "stato": "Aperto"},
    ]


def safe(value):
    return html.escape(str(value))


def whatsapp_url(phone):
    return "https://wa.me/" + re.sub(r"\D", "", phone)


# ============================================================
# APPLE & MICROSOFT LIGHT MODE DESIGN SYSTEM (CLEAN & PROFESSIONAL)
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

:root {
    --bg-app: #f8fafc;
    --card-bg: #ffffff;
    --card-border: #e2e8f0;
    --card-border-focus: #cbd5e1;
    --text-primary: #0f172a;
    --text-secondary: #64748b;
    --accent-blue: #0066cc;
    --accent-blue-hover: #0055b3;
    --accent-success: #10b981;
    --radius-xl: 20px;
    --radius-lg: 14px;
    --radius-md: 8px;
    --shadow-elevation: 0 4px 20px rgba(0, 0, 0, 0.04);
    --shadow-hover: 0 10px 30px rgba(0, 0, 0, 0.08);
}

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

.stApp {
    background-color: var(--bg-app);
    color: var(--text-primary);
}

.block-container {
    max-width: 1200px !important;
    padding: 2.5rem 2rem 5rem !important;
}

#MainMenu, footer, header, [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stStatusWidget"] {
    display: none !important;
    visibility: hidden !important;
}

/* APPLE / MICROSOFT CLEAN COMMAND HUB */
.command-hub {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    padding: 2rem 2.5rem;
    border-radius: var(--radius-xl);
    box-shadow: var(--shadow-elevation);
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2.2rem;
    gap: 20px;
    flex-wrap: wrap;
}

.hub-title h1 {
    font-size: 2.2rem;
    font-weight: 800;
    margin: 0;
    letter-spacing: -0.03em;
    color: var(--text-primary);
}

.hub-title p {
    font-size: 0.95rem;
    color: var(--text-secondary);
    margin: 4px 0 0 0;
    font-weight: 400;
}

.hub-status-badge {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    color: #15803d;
    padding: 8px 16px;
    border-radius: 30px;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    display: inline-flex;
    align-items: center;
    gap: 8px;
}

/* CUSTOM CLEAN NAVIGATION PILLS */
div[data-testid="stRadio"] > label { display: none; }
div[data-testid="stRadio"] div[role="radiogroup"] {
    display: flex;
    background: #edf2f7;
    padding: 4px;
    border-radius: 40px;
    border: 1px solid var(--card-border);
    margin-bottom: 2.5rem;
    gap: 4px;
    justify-content: center;
    flex-wrap: wrap;
}
div[data-testid="stRadio"] div[role="radiogroup"] label {
    border-radius: 30px;
    padding: 10px 22px;
    font-weight: 600;
    font-size: 0.85rem;
    color: var(--text-secondary) !important;
    transition: all 0.2s ease;
}
div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
    background: #ffffff !important;
    color: var(--text-primary) !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

/* CLEAN CARDS */
.enterprise-card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: var(--radius-lg);
    padding: 1.8rem;
    box-shadow: var(--shadow-elevation);
    margin-bottom: 1.2rem;
    transition: all 0.2s ease;
}
.enterprise-card:hover {
    border-color: var(--card-border-focus);
    box-shadow: var(--shadow-hover);
}

/* STATUS DOTS */
.radar-dot {
    display: inline-block;
    width: 8px;
    height: 8px;
    background-color: var(--accent-success);
    border-radius: 50%;
    margin-right: 6px;
    vertical-align: middle;
}
.offline-dot {
    display: inline-block;
    width: 8px;
    height: 8px;
    background-color: #cbd5e1;
    border-radius: 50%;
    margin-right: 6px;
    vertical-align: middle;
}

.chip {
    display: inline-block;
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    color: #334155;
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-right: 6px;
    margin-bottom: 6px;
}

.metrics-row {
    display: flex;
    background: #f8fafc;
    border-radius: var(--radius-md);
    padding: 1rem;
    margin: 1.2rem 0;
    text-align: center;
    border: 1px solid var(--card-border);
}
.metric-box { flex: 1; border-right: 1px solid var(--card-border); }
.metric-box:last-child { border-right: none; }
.metric-box strong { display: block; font-size: 1.4rem; color: #0284c7; font-weight: 700; }
.metric-box span { font-size: 0.7rem; color: var(--text-secondary); font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }

.stButton > button {
    width: 100%;
    min-height: 44px;
    border-radius: var(--radius-md);
    background: #0f172a;
    color: white;
    font-weight: 600;
    font-size: 0.9rem;
    border: none;
    box-shadow: 0 2px 6px rgba(15, 23, 42, 0.1);
    transition: all 0.2s ease;
}
.stButton > button:hover {
    background: #1e293b;
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# SIDEBAR ADMIN & SUBSCRIPTION ENGINE
# ============================================================
with st.sidebar:
    st.markdown("### 🔐 Enterprise Console")
    password_inserita = st.text_input(
        "Admin Access Key", type="password", key="input_pwd_admin"
    )

    mostra_admin = False
    if password_inserita == "admin123":
        st.success("Authorized System Access ✅")
        mostra_admin = True
    elif password_inserita != "":
        st.error("Authentication Failed ❌")

    st.markdown("---")
    st.markdown("### 🏢 Subscription Status")
    if st.session_state.abbonamento_attivo:
        st.success("✨ Elite License Active\n(Full Database Unlocked)")
        if st.button("Revert to Free Tier"):
            st.session_state.abbonamento_attivo = False
            st.rerun()
    else:
        st.warning("🔒 Standard Tier (Preview 4 Profiles)")
        if st.button("🚀 Upgrade to Elite Enterprise"):
            st.session_state.abbonamento_attivo = True
            st.rerun()

# ============================================================
# COMMAND HUB HEADER
# ============================================================
st.markdown(
    """
<div class="command-hub">
    <div class="hub-title">
        <h1>Flashjob Pro</h1>
        <p>Professional Staffing Intelligence & Workforce Management • Milan Core Node</p>
    </div>
    <div class="hub-status-badge">
        <span style="width:6px; height:6px; background:#10b981; border-radius:50%; display:inline-block;"></span>
        System Online
    </div>
</div>
""",
    unsafe_allow_html=True,
)

menu_opzioni = [
    "Panoramica",
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
            <span class="chip" style="background: #e0f2fe; color: #0369a1; border-color: #bae6fd;">MILAN REGIONAL ENGINE v4.2</span>
            <h2 style='font-weight:800; font-size:2.4rem; margin-top:12px; letter-spacing:-0.02em;'>Piattaforma Digitale per la Gestione del Personale</h2>
            <p style='color:var(--text-secondary); font-size:1.05rem; line-height:1.6; margin-top:12px;'>Flashjob Pro ottimizza la selezione e il coordinamento di professionisti qualificati per hotel, ristoranti ed eventi corporate a Milano tramite un sistema rapido e trasparente.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown(
            """
        <div class="enterprise-card" style="height: 100%;">
            <span class="chip" style="background: #e0f2fe; color: #0369a1;">Smart Matching</span>
            <h3 style="font-size: 1.15rem; margin-top: 10px; font-weight: 700;">Copertura Turni 24/7</h3>
            <p style="color: var(--text-secondary); font-size: 0.9rem; line-height: 1.5; margin-top: 8px;">
                Assegnazione rapida basata su competenze certificate, geolocalizzazione e storico di affidabilità verificato.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="enterprise-card" style="height: 100%;">
            <span class="chip" style="background: #dcfce7; color: #166534;">Zero Intermediari</span>
            <h3 style="font-size: 1.15rem; margin-top: 10px; font-weight: 700;">Contatto Diretto</h3>
            <p style="color: var(--text-secondary); font-size: 0.9rem; line-height: 1.5; margin-top: 8px;">
                Collega manager e candidati istantaneamente tramite canali dedicati per una comunicazione fluida e senza attese.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
        <div class="enterprise-card" style="height: 100%;">
            <span class="chip" style="background: #f3e8ff; color: #6b21a8;">Elite Verified</span>
            <h3 style="font-size: 1.15rem; margin-top: 10px; font-weight: 700;">Standard Apple & Microsoft</h3>
            <p style="color: var(--text-secondary); font-size: 0.9rem; line-height: 1.5; margin-top: 8px;">
                Interfaccia pulita, minimale e ad alte prestazioni progettata per offrire un'esperienza utente impeccabile.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown(
        """
        <div style="margin-top: 1.5rem;">
            <h3 style="font-size: 1.3rem; font-weight: 700; margin-bottom: 1rem;">⚡ Turni Urgenti in Evidenza (Milano)</h3>
        </div>
    """,
        unsafe_allow_html=True,
    )

    for req in st.session_state.richieste_turno:
        st.markdown(
            f"""
        <div class="enterprise-card" style="display: flex; justify-content: space-between; align-items: center; padding: 1.4rem 1.8rem; margin-bottom: 1rem;">
            <div>
                <span class="chip" style="background: #fee2e2; color: #991b1b; border-color: #fecaca;">URGENTE • {safe(req["locale"])}</span>
                <h4 style="margin: 6px 0 2px 0; font-size: 1.1rem; font-weight: 700;">{safe(req["mansione"])}</h4>
                <p style="color: var(--text-secondary); margin: 0; font-size: 0.85rem;">📅 {safe(req["data"])}</p>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 1.2rem; font-weight: 700; color: #166534;">{safe(req["compenso"])}</div>
                <span style="font-size: 0.75rem; color: var(--text-secondary); font-weight: 600;">Compenso Verificato</span>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

# ============================================================
# 2. DATABASE & FILTRI AZIENDA (FREEMIUM PAYWALL)
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
        if st.button("← Torna alla Directory Candidati"):
            st.session_state.selected_id = None
            st.rerun()

        stato_html = (
            '<span class="radar-dot"></span><b style="color:#15803d; font-size:0.75rem;">DISPONIBILE ORA</b>'
            if selected_c["disponibile"]
            else '<span class="offline-dot"></span><span style="color:#64748b; font-size:0.75rem;">NON DISPONIBILE</span>'
        )

        comp_html = "".join(
            [f'<span class="chip">✓ {c}</span>' for c in selected_c["competenze"]]
        )

        st.markdown(
            f"""
        <div class="enterprise-card" style="margin-top: 10px;">
            <div style="display: flex; align-items: center; gap: 20px; flex-wrap: wrap;">
                <div style="width:80px; height:80px; background:#f1f5f9; border-radius:20px; display:flex; align-items:center; justify-content:center; font-size:2rem; border:1px solid #e2e8f0;">👤</div>
                <div style="flex: 1;">
                    <div style="margin-bottom:4px;">{stato_html}</div>
                    <h2 style="margin:0; font-size:1.6rem; font-weight:800;">{safe(selected_c["nome"])}</h2>
                    <p style="color:var(--text-secondary); margin:4px 0 0 0; font-weight:500; font-size:0.95rem;">{safe(selected_c["mansione"])} · 📍 {safe(selected_c["zona"])}</p>
                    <p style="color:#b45309; margin:4px 0 0 0; font-weight:600; font-size:0.9rem;">⭐ {safe(selected_c["recensioni"])}</p>
                </div>
                <div style="text-align: right; background: #f8fafc; padding: 14px 22px; border-radius: 12px; border: 1px solid var(--card-border);">
                    <div style="font-size: 1.5rem; font-weight: 800; color: #0284c7;">{safe(selected_c["tariffa"])}</div>
                    <span style="font-size: 0.7rem; color: var(--text-secondary); text-transform: uppercase; font-weight: 700;">Tariffa Indicativa</span>
                </div>
            </div>
            
            <div style="margin-top: 22px;">
                <p style="font-size:0.75rem; font-weight:700; color:var(--text-secondary); text-transform:uppercase; letter-spacing:0.05em; margin-bottom:8px;">Competenze certificate:</p>
                {comp_html}
            </div>

            <div class="metrics-row">
                <div class="metric-box">
                    <strong>{safe(selected_c["completati"])}</strong>
                    <span>Turni completati</span>
                </div>
                <div class="metric-box">
                    <strong>{safe(selected_c["affidabilita"])}</strong>
                    <span>Indice Affidabilità</span>
                </div>
                <div class="metric-box">
                    <strong>Milano Node</strong>
                    <span>Copertura</span>
                </div>
            </div>
            
            <div style="background: #f0f9ff; border-left: 4px solid #0284c7; padding: 16px; border-radius: 0 10px 10px 0; margin-top: 18px; font-style: italic; color: #0369a1; font-size: 0.95rem; line-height: 1.5;">
                “{safe(selected_c["referenze"])}”
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.link_button(
            "💬 Contatta su WhatsApp",
            whatsapp_url(selected_c["tel"]),
            use_container_width=True,
        )

    else:
        st.markdown(
            """
            <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:4px;'>Directory Professionisti Milano</h2>
            <p style='color:var(--text-secondary); margin-bottom:1.5rem;'>Filtra e seleziona talenti verificati in tempo reale.</p>
        """,
            unsafe_allow_html=True,
        )

        # Filtri avanzati
        st.markdown(
            '<div class="enterprise-card" style="padding: 1.4rem; background: #ffffff;">',
            unsafe_allow_html=True,
        )
        col_f1, col_f2 = st.columns(2)

        with col_f1:
            filtro_mansione = st.selectbox(
                "Filtro per Mansione",
                [
                    "Tutte",
                    "Cameriere / Sala",
                    "Barista / Bartender",
                    "Chef de Rang / Jolly",
                    "Aiuto Cuoco",
                ],
                key="filtro_mansione_box",
            )

        with col_f2:
            solo_disponibili = st.checkbox(
                "Mostra solo candidati disponibili ora",
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

        # PAYWALL LOGIC: Free limit to 4
        limite_visib = len(lavoratori_filtrati)
        if not st.session_state.abbonamento_attivo and len(lavoratori_filtrati) > 4:
            limite_visib = 4

        for lav in lavoratori_filtrati[:limite_visib]:
            col_info, col_btn = st.columns([3, 1], gap="medium")

            with col_info:
                badge_stato = (
                    '<span class="radar-dot"></span><b style="color:#15803d; font-size:0.75rem;">DISPONIBILE ORA</b>'
                    if lav["disponibile"]
                    else '<span class="offline-dot"></span><span style="color:#64748b; font-size:0.75rem;">NON DISPONIBILE</span>'
                )

                st.markdown(
                    f"""
                    <div class="enterprise-card" style="margin-bottom:1rem; padding:1.2rem 1.6rem;">
                        <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                            <div>
                                <div style="margin-bottom:4px;">{badge_stato}</div>
                                <h3 style="margin:0; font-size:1.15rem; font-weight:700;">{safe(lav["nome"])}</h3>
                                <p style="color:var(--text-secondary); margin:3px 0; font-size:0.9rem; font-weight:500;">{safe(lav["mansione"])} · 📍 {safe(lav["zona"])}</p>
                                <p style="color:#b45309; margin:3px 0; font-weight:600; font-size:0.85rem;">⭐ {safe(lav["recensioni"])}</p>
                            </div>
                            <div style="text-align:right;">
                                <span style="font-size:1.05rem; font-weight:700; color:#0284c7;">{safe(lav["tariffa"])}</span>
                            </div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with col_btn:
                st.markdown(
                    "<div style='margin-top: 32px;'></div>", unsafe_allow_html=True
                )
                if st.button("Profilo", key=f"btn_card_{lav['id']}"):
                    st.session_state.selected_id = lav["id"]
                    st.rerun()

        # PAYWALL BANNER
        if (
            not st.session_state.abbonamento_attivo
            and len(lavoratori_filtrati) > 4
        ):
            st.markdown(
                """
            <div class="enterprise-card" style="text-align: center; background: #ffffff; border: 1px solid #bae6fd; padding: 2.5rem; margin-top: 1.5rem;">
                <span class="chip" style="background: #e0f2fe; color: #0369a1;">🔒 Anteprima Standard (4 di """
                + str(len(lavoratori_filtrati))
                + """ professionisti)</span>
                <h3 style="margin-top: 10px; font-size: 1.4rem; font-weight: 800;">Sblocca l'intero database di Milano</h3>
                <p style="color: var(--text-secondary); font-size: 0.9rem; max-width: 600px; margin: 10px auto 20px auto; line-height: 1.5;">
                    Il piano gratuito consente la visualizzazione dei primi 4 candidati. Attiva il piano Elite Enterprise per accedere a tutti i profili verificati sul territorio.
                </p>
            </div>
            """,
                unsafe_allow_html=True,
            )
            if st.button("🚀 Attiva Accesso Illimitato Ora"):
                st.session_state.abbonamento_attivo = True
                st.success(
                    "Abbonamento Elite attivo! Directory interamente sbloccata."
                )
                st.rerun()

# ============================================================
# 3. AREA LAVORATORE
# ============================================================
elif scelta == "Area Lavoratore":
    st.markdown(
        """
        <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:4px;'>Pannello Operativo Lavoratore</h2>
        <p style='color:var(--text-secondary); margin-bottom:1.8rem;'>Gestisci le tue preferenze, le competenze certificate e la reperibilità sul territorio.</p>
    """,
        unsafe_allow_html=True,
    )

    mio = st.session_state.mio_profilo

    col_l1, col_l2 = st.columns(2, gap="large")

    with col_l1:
        nuova_mansione = st.selectbox(
            "Mansione Principale",
            [
                "Cameriere / Sala",
                "Barista / Bartender",
                "Chef de Rang / Jolly",
                "Aiuto Cuoco",
            ],
            index=0,
        )
        mio["mansione"] = nuova_mansione

        nuova_zona = st.selectbox(
            "Zona di Riferimento a Milano",
            [
                "Milano Centro",
                "Navigli / Ticinese",
                "Porta Nuova / Corso Como",
                "Brera / Garibaldi",
                "Città Studi / Lambrate",
                "Fiera / CityLife",
                "Isola",
            ],
            index=0,
        )
        mio["zona"] = nuova_zona

    with col_l2:
        tariffa_richiesta = st.text_input("Tariffa Oraria Richiesta", value=mio["tariffa"])
        mio["tariffa"] = tariffa_richiesta

        scelta_comp = st.multiselect(
            "Competenze certificate da mostrare ai locali",
            [
                "Lingua Inglese",
                "Vini & Sommelier Base",
                "Mixology Avanzata",
                "Caffetteria Pro",
                "Gestione cassa",
                "Piattaforma POS",
                "HACCP Avanzato",
            ],
            default=mio["competenze"],
        )
        mio["competenze"] = scelta_comp

    st.markdown("---")
    st.markdown("### Stato di Disponibilità Real-Time")
    nuova_disp = st.toggle(
        "🟢 Attiva Disponibilità Lavorativa su Milano",
        value=mio["disponibile"],
        key="toggle_disponibilita_lavoratore",
    )

    if (
        nuova_disp != mio["disponibile"]
        or mio["mansione"] != nuova_mansione
        or mio["zona"] != nuova_zona
        or mio["tariffa"] != tariffa_richiesta
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
                trovato["competenze"] = mio["competenze"]
                trovato["tariffa"] = mio["tariffa"]
            else:
                st.session_state.lavoratori.append(mio.copy())
        else:
            if trovato:
                st.session_state.lavoratori = [
                    item for item in st.session_state.lavoratori if item["id"] != mio["id"]
                ]

        st.success("Configurazione salvata con successo nel sistema.")

# ============================================================
# 4. PIANI & ABBONAMENTI
# ============================================================
elif scelta == "Piani & Abbonamenti":
    st.markdown(
        """
        <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:4px;'>Piani di Licenza Enterprise</h2>
        <p style='color:var(--text-secondary); margin-bottom:1.8rem;'>Scegli la soluzione ideale per la tua azienda e sblocca l'accesso illimitato ai professionisti.</p>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
        <div class="enterprise-card" style="border: 1px solid var(--card-border); height: 100%;">
            <span class="chip">Standard Free</span>
            <h3 style="margin-top:10px; font-size:1.3rem; font-weight:700;">Anteprima Base</h3>
            <div style="font-size: 1.6rem; font-weight: 800; color: #0284c7; margin: 10px 0;">0 € / mese</div>
            <p style="font-size:0.9rem; color:var(--text-secondary); line-height:1.5;">Accesso limitato ai primi 4 candidati verificati per ogni ricerca territoriale su Milano.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Seleziona Standard", key="btn_base_plan"):
            st.session_state.abbonamento_attivo = False
            st.toast("Piano Standard Free impostato.")
            st.rerun()

    with col2:
        st.markdown(
            """
        <div class="enterprise-card" style="border: 1px solid #bae6fd; background: #f0f9ff; height: 100%;">
            <span class="chip" style="background: #e0f2fe; color: #0369a1;">Elite Enterprise 🌟</span>
            <h3 style="margin-top:10px; font-size:1.3rem; font-weight:700;">Database Illimitato</h3>
            <div style="font-size: 1.6rem; font-weight: 800; color: #0284c7; margin: 10px 0;">79 € / mese</div>
            <p style="font-size:0.9rem; color:var(--text-secondary); line-height:1.5;">Sblocca all'istante l'intero database di professionisti verificati, contatti diretti WhatsApp e supporto prioritario.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Attiva Licenza Elite"):
            st.session_state.abbonamento_attivo = True
            st.success(
                "🎉 Licenza Elite attivata con successo! Database interamente sbloccato."
            )
            st.rerun()

# ============================================================
# 5. DASHBOARD ADMIN
# ============================================================
elif scelta == "📊 Dashboard Admin":
    st.markdown(
        """
        <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:4px;'>📊 Dashboard Admin & Telemetria</h2>
        <p style='color:var(--text-secondary); margin-bottom:1.8rem;'>Monitoraggio in tempo reale del traffico cloud e dei nodi operativi attivi.</p>
    """,
        unsafe_allow_html=True,
    )

    col_m1, col_m2, col_m3 = st.columns(3, gap="medium")

    with col_m1:
        st.markdown(
            f"""
        <div class="enterprise-card" style="text-align: center; padding: 2rem;">
            <span class="chip">Traffic Monitor</span>
            <h3 style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px;">Sessioni Totali App</h3>
            <div style="font-size: 2.5rem; font-weight: 800; color: #0284c7; margin: 10px 0;">{st.session_state.visite_totali}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col_m2:
        st.markdown(
            f"""
        <div class="enterprise-card" style="text-align: center; padding: 2rem;">
            <span class="chip" style="background: #f3e8ff; color: #6b21a8;">Node Monitor</span>
            <h3 style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px;">Professionisti Online</h3>
            <div style="font-size: 2.5rem; font-weight: 800; color: #7c3aed; margin: 10px 0;">{len(st.session_state.lavoratori)}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col_m3:
        st.markdown(
            f"""
        <div class="enterprise-card" style="text-align: center; padding: 2rem;">
            <span class="chip" style="background: #dcfce7; color: #166534;">License Status</span>
            <h3 style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 8px;">Stato Abbonamento</h3>
            <div style="font-size: 1.3rem; font-weight: 800; color: #166534; margin: 18px 0;">{"Elite Active" if st.session_state.abbonamento_attivo else "Standard Free"}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )