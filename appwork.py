import html
import re
import streamlit as st

st.set_page_config(
    page_title="Flashjob • Il talento che cercavi alla portata di mano",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# STATO INIZIALE & DATABASE PROFESSIONISTI MILANO
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
        },
        {
            "id": 4,
            "nome": "Sofia Neri",
            "mansione": "Aiuto Cuoco",
            "zona": "Brera / Garibaldi",
            "tel": "+39 333 7778899",
            "completati": 18,
            "disponibile": True,
            "referenze": "Grande precisione nella linea e velocità nei piatti freddi.",
            "recensioni": "4.9 ⭐ (14 recensioni verificate)",
            "competenze": ["HACCP Avanzato", "Preparazione Linea"],
        },
        {
            "id": 5,
            "nome": "Luca Colombo",
            "mansione": "Cameriere / Sala",
            "zona": "Città Studi / Lambrate",
            "tel": "+39 333 4443322",
            "completati": 9,
            "disponibile": True,
            "referenze": "Puntuale, solare e molto gradito dalla clientela universitaria.",
            "recensioni": "4.7 ⭐ (8 recensioni verificate)",
            "competenze": ["Lingua Inglese", "Piattaforma POS"],
        },
        {
            "id": 6,
            "nome": "Martina Rinaldi",
            "mansione": "Barista / Bartender",
            "zona": "Fiera / CityLife",
            "tel": "+39 333 6661122",
            "completati": 27,
            "disponibile": True,
            "referenze": "Top livello nella caffetteria e cocktail di alto standing.",
            "recensioni": "5.0 ⭐ (24 recensioni verificate)",
            "competenze": ["Caffetteria Pro", "Mixology Avanzata"],
        },
        {
            "id": 7,
            "nome": "Alessandro Gallo",
            "mansione": "Chef de Rang / Jolly",
            "zona": "Isola",
            "tel": "+39 333 2221144",
            "completati": 16,
            "disponibile": True,
            "referenze": "Grande professionalità e ottima parlata inglese.",
            "recensioni": "4.9 ⭐ (11 recensioni verificate)",
            "competenze": ["Lingua Inglese", "Vini & Sommelier Base"],
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
        "nome": "Il Tuo Nome",
        "mansione": "Cameriere / Sala",
        "zona": "Milano Centro",
        "tel": "+39 333 0000000",
        "completati": 0,
        "disponibile": False,
        "referenze": "Professionista verificato nel settore HORECA e Accoglienza.",
        "recensioni": "Nuovo utente (0 recensioni)",
        "competenze": ["Lingua Inglese"],
    }


def safe(value):
    return html.escape(str(value))


def whatsapp_url(phone):
    return "https://wa.me/" + re.sub(r"\D", "", phone)


# ============================================================
# DESIGN SYSTEM ELITE & CSS NATIVO
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
    --shadow: 0 10px 30px rgba(138, 114, 239, 0.06);
    --radius: 24px;
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

#MainMenu {visibility: hidden; display: none;}
footer {visibility: hidden; display: none;}
header {visibility: hidden; display: none;}
[data-testid="stHeader"] {display: none !important;}
[data-testid="stToolbar"] {display: none !important; visibility: hidden !important;}
[data-testid="stDecoration"] {display: none !important;}
[data-testid="stStatusWidget"] {display: none !important;}

/* STORE HEADER PRO */
.store-header {
    background: linear-gradient(135deg, #a78bfa 0%, #60a5fa 50%, #34d399 100%);
    padding: 2.8rem 2.2rem;
    border-radius: 28px;
    box-shadow: 0 20px 40px rgba(167, 139, 250, 0.2);
    margin-bottom: 2.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 20px;
    color: white;
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
    border-radius: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}
.app-titles h1 {
    font-size: 2.5rem;
    font-weight: 800;
    margin: 0;
    letter-spacing: -1px;
    color: white;
}
.app-titles p {
    font-size: 1.05rem;
    margin: 6px 0 0 0;
    color: #f8fafc;
    font-weight: 600;
    opacity: 0.95;
}
.app-badges-right {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}
.store-badge {
    background: rgba(0, 0, 0, 0.85);
    color: white;
    padding: 10px 16px;
    border-radius: 14px;
    font-size: 0.75rem;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
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
    padding: 10px 16px;
    font-weight: 700;
    font-size: 0.8rem;
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
    70% { transform: scale(1); box-shadow: 0 0 0 12px rgba(52, 211, 153, 0); }
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
# BARRA LATERALE ADMIN & SIMULAZIONE ABBONAMENTO
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

    st.markdown("---")
    st.markdown("### 🏢 Stato Account Locale")
    if st.session_state.abbonamento_attivo:
        st.success("🌟 Abbonamento Elite Attivo\n(Database interamente sbloccato)")
        if st.button("Torna a Piano Base (Free)"):
            st.session_state.abbonamento_attivo = False
            st.rerun()
    else:
        st.warning("🔒 Account Free (Vedi solo 4 candidati)")
        if st.button("✨ Sblocca Tutto il Database"):
            st.session_state.abbonamento_attivo = True
            st.rerun()

# ============================================================
# STORE HEADER UFFICIALE
# ============================================================
st.markdown(
    """
<div class="store-header">
    <div class="app-info-left">
        <div class="app-logo-box">⚡</div>
        <div class="app-titles">
            <h1>Flashjob</h1>
            <p>Il talento che cercavi alla portata di mano • Milano & Hinterland</p>
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
            <h2 style='font-weight:800; font-size:2.3rem; margin-top:10px; color:#211e33;'>Il talento che cercavi alla portata di mano.</h2>
            <p style='color:var(--text-muted); font-size:1.1rem; line-height:1.6; margin-top:10px;'>Flashjob connette in tempo reale i migliori professionisti dell'HORECA e dell'accoglienza a Milano, azzerando le attese e le agenzie di intermediazione.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
        <div class="custom-card" style="height: 100%;">
            <span class="badge-pop badge-blue">Per i Ristoratori & Locali</span>
            <h3 style="font-size: 1.3rem; margin-top: 5px;">Copri i turni vuoti in 10 secondi</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6;">
                Visualizza un'anteprima gratuita di 4 candidati oppure attiva l'abbonamento per accedere all'intero database di professionisti verificati a Milano.
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
            <h3 style="font-size: 1.3rem; margin-top: 5px;">Lavora quando vuoi, vicino a casa</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6;">
                Accendi la disponibilità, metti in mostra le tue competenze certificate (sommelier, mixology, lingue) e ricevi proposte immediate.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

# ============================================================
# 2. DATABASE & FILTRI AZIENDA (CON PAYWALL FREEMIUM RIGOROSO)
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
        if st.button("← Torna alla lista candidati"):
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
            <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Database Professionisti Milano</h2>
            <p style='color:var(--text-muted); margin-bottom:1.5rem;'>Cerca i migliori profili HORECA pronti per turni immediati.</p>
        """,
            unsafe_allow_html=True,
        )

        # Filtri
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

        # PAYWALL: Se l'abbonamento non è attivo, mostriamo al massimo 4 candidati
        limite_visib = len(lavoratori_filtrati)
        if not st.session_state.abbonamento_attivo and len(lavoratori_filtrati) > 4:
            limite_visib = 4

        for lav in lavoratori_filtrati[:limite_visib]:
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

        # Blocco visivo se ci sono altri candidati nascosti dal paywall free
        if (
            not st.session_state.abbonamento_attivo
            and len(lavoratori_filtrati) > 4
        ):
            st.markdown(
                """
            <div class="custom-card" style="text-align: center; background: linear-gradient(135deg, #f3e8ff 0%, #e0f2fe 100%); border: 2px dashed #a78bfa; padding: 2.5rem; margin-top: 2rem;">
                <span class="badge-pop badge-purple">🔒 Anteprima Free (4 di """
                + str(len(lavoratori_filtrati))
                + """ professionisti)</span>
                <h3 style="margin-top: 10px; font-size: 1.4rem; font-weight: 800;">Vuoi vedere tutti gli altri professionisti a Milano?</h3>
                <p style="color: var(--text-muted); font-size: 0.95rem; max-width: 600px; margin: 10px auto 20px auto;">
                    Il piano gratuito ti mostra solo i primi 4 candidati. Sblocca l'abbonamento Elite per accedere all'intero database illimitato di Milano e contattare chi vuoi.
                </p>
            </div>
            """,
                unsafe_allow_html=True,
            )
            if st.button("🚀 Sblocca Tutto il Database Ora"):
                st.session_state.abbonamento_attivo = True
                st.success(
                    "Abbonamento Elite sbloccato! Ora hai accesso completo."
                )
                st.rerun()

# ============================================================
# 3. AREA LAVORATORE
# ============================================================
elif scelta == "Area Lavoratore":
    st.markdown(
        """
        <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Area Personale Lavoratore</h2>
        <p style='color:var(--text-muted); margin-bottom:2rem;'>Imposta la tua zona di Milano, le tue competenze e gestisci il tuo pallino verde.</p>
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
            "Isola",
        ],
        index=0,
    )
    mio["zona"] = nuova_zona

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
            "HACCP Avanzato",
        ],
        default=mio["competenze"],
    )
    mio["competenze"] = scelta_comp

    st.markdown("### Gestione Stato in Tempo Reale")
    nuova_disp = st.toggle(
        "🟢 Attiva disponibilità sul database di Milano",
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
                trovato["competenze"] = mio["competenze"]
            else:
                st.session_state.lavoratori.append(mio.copy())
        else:
            if trovato:
                st.session_state.lavoratori = [
                    item for item in st.session_state.lavoratori if item["id"] != mio["id"]
                ]

        st.success("Stato aggiornato con successo!")

# ============================================================
# 4. PIANI & ABBONAMENTI
# ============================================================
elif scelta == "Piani & Abbonamenti":
    st.markdown(
        """
        <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Piani & Funzioni Elite ⚡</h2>
        <p style='color:var(--text-muted); margin-bottom:2rem;'>Scegli il piano ideale per il tuo locale e sblocca l'accesso illimitato ai lavoratori di Milano.</p>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.markdown(
            """
        <div class="custom-card" style="border: 2px solid #e2e8f0;">
            <span class="badge-pop badge-blue">Piano Base Free</span>
            <h3 style="margin-top:10px; font-size:1.3rem;">Anteprima Gratuita</h3>
            <div style="font-size: 1.5rem; font-weight: 800; color: #0284c7; margin: 10px 0;">0 € / mese</div>
            <p style="font-size:0.9rem; color:var(--text-muted);">Accesso limitato ai primi 4 candidati di prova per ogni ricerca.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Seleziona Piano Base", key="btn_base_plan"):
            st.session_state.abbonamento_attivo = False
            st.toast("Attivo il piano Base Free (4 candidati visibili).")
            st.rerun()

    with col2:
        st.markdown(
            """
        <div class="custom-card" style="border: 2px solid #a78bfa; background: linear-gradient(135deg, #fcfbfe 0%, #f3e8ff 100%);">
            <span class="badge-pop badge-purple">Piano Elite Ristoratori 🌟</span>
            <h3 style="margin-top:10px; font-size:1.3rem;">Database Illimitato</h3>
            <div style="font-size: 1.5rem; font-weight: 800; color: #9333ea; margin: 10px 0;">79 € / mese</div>
            <p style="font-size:0.9rem; color:var(--text-muted);">Sblocca all'istante l'intero database di professionisti a Milano e contatta chiunque via WhatsApp.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Attiva Abbonamento Elite"):
            st.session_state.abbonamento_attivo = True
            st.success(
                "🎉 Abbonamento Elite attivato! Database completamente sbloccato."
            )
            st.rerun()

# ============================================================
# 5. DASHBOARD ADMIN
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
            <h3 style="color: var(--text-muted); font-size: 1rem; margin-top: 10px;">Lavoratori Online</h3>
            <div style="font-size: 3rem; font-weight: 800; color: #9333ea; margin: 15px 0;">{len(st.session_state.lavoratori)}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )