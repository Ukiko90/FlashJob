import html
import re
import streamlit as st

st.set_page_config(
    page_title="Flashjob • Editorial Design",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# STATO INIZIALE & TRACCIAMENTO METRICHE LIVE
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
            "boosted": True,
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
            "boosted": False,
            "referenze": "Velocità incredibile nei momenti di massimo afflusso.",
            "recensioni": "5.0 ⭐ (19 recensioni verificate)",
            "competenze": ["Mixology Avanzata", "Caffetteria Pro", "Gestione cassa"],
        },
    ]

if "selected_id" not in st.session_state:
    st.session_state.selected_id = None

if "abbonamento_titolare" not in st.session_state:
    st.session_state.abbonamento_titolare = False

if "visite_totali" not in st.session_state:
    st.session_state.visite_totali = 1240

if "click_whatsapp" not in st.session_state:
    st.session_state.click_whatsapp = 312

if "boost_attivi_count" not in st.session_state:
    st.session_state.boost_attivi_count = 8

if "sessione_contata" not in st.session_state:
    st.session_state.visite_totali += 1
    st.session_state.sessione_contata = True

if "mio_profilo" not in st.session_state:
    st.session_state.mio_profilo = {
        "id": 999,
        "nome": "Il Tuo Nome",
        "mansione": "Cameriere / Sala",
        "zona": "Milano",
        "tel": "+39 333 0000000",
        "completati": 0,
        "disponibile": False,
        "boosted": False,
        "referenze": "Professionista verificato nel settore HORECA e Accoglienza.",
        "recensioni": "Nuovo utente (0 recensioni)",
        "competenze": ["Lingua Inglese"],
    }


def safe(value):
    return html.escape(str(value))


def whatsapp_url(phone):
    st.session_state.click_whatsapp += 1
    return "https://wa.me/" + re.sub(r"\D", "", phone)


# ============================================================
# DESIGN SYSTEM EDITORIALE (ISPIRATO A TEMPLATE MODERNI)
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

:root {
    --bg-main: #f8fafc;
    --card-bg: #ffffff;
    --text-main: #0f172a;
    --text-muted: #64748b;
    --accent-teal: #0d9488;
    --accent-sky: #0284c7;
    --border-subtle: #e2e8f0;
    --shadow-editorial: 0 20px 40px -15px rgba(13, 148, 136, 0.07);
    --radius-editorial: 20px;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background-color: var(--bg-main);
    color: var(--text-main);
}

.block-container {
    max-width: 1150px !important;
    padding: 3rem 2rem 6rem !important;
}

#MainMenu, footer, header {visibility: hidden; display: none;}
[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stStatusWidget"] {display: none !important;}

/* HEADER EDITORIALE PULITO */
.editorial-header {
    background: linear-gradient(135deg, #ffffff 0%, #f0fdfa 100%);
    border: 1px solid #ccfbf1;
    padding: 3rem 2.5rem;
    border-radius: 28px;
    box-shadow: var(--shadow-editorial);
    margin-bottom: 2.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    overflow: hidden;
}
.editorial-header::before {
    content: '';
    position: absolute;
    top: 0; left: 0; width: 6px; height: 100%;
    background: linear-gradient(to bottom, #0284c7, #0d9488);
}
.editorial-title h1 {
    font-size: 2.8rem;
    font-weight: 800;
    letter-spacing: -1.5px;
    color: #0f172a;
    margin: 0;
}
.editorial-title p {
    font-size: 1.05rem;
    color: #475569;
    margin: 8px 0 0 0;
    font-weight: 500;
}

/* RADIO NAVIGATION STILE MAGAZINE */
div[data-testid="stRadio"] > label { display: none; }
div[data-testid="stRadio"] div[role="radiogroup"] {
    display: flex;
    justify-content: center;
    background: #ffffff;
    padding: 6px;
    border-radius: 40px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.04);
    margin-bottom: 3rem;
    gap: 4px;
    border: 1px solid var(--border-subtle);
    flex-wrap: wrap;
}
div[data-testid="stRadio"] div[role="radiogroup"] label {
    border-radius: 30px;
    padding: 10px 20px;
    font-weight: 600;
    font-size: 0.85rem;
    color: var(--text-muted) !important;
    transition: all 0.25s ease;
}
div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
    background: #f0fdfa;
    color: var(--accent-teal) !important;
}
div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
    background: #0f172a !important;
    color: white !important;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
}

/* BANNER EDITORIALI CON HOVER FLUIDO (STILE CANVA) */
.editorial-banner {
    background: #ffffff;
    border: 1px solid var(--border-subtle);
    padding: 2.5rem 2rem;
    border-radius: var(--radius-editorial);
    box-shadow: var(--shadow-editorial);
    height: 100%;
    position: relative;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
.editorial-banner:hover {
    transform: translateY(-6px);
    border-color: #99f6e4;
    box-shadow: 0 25px 50px -12px rgba(13, 148, 136, 0.12);
}
.editorial-tag {
    font-size: 0.7rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #0d9488;
    background: #f0fdfa;
    padding: 6px 12px;
    border-radius: 20px;
    display: inline-block;
    margin-bottom: 1rem;
    border: 1px solid #ccfbf1;
}

/* CARD EDITORIALI */
.editorial-card {
    background: #ffffff;
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-editorial);
    padding: 2rem;
    box-shadow: var(--shadow-editorial);
    margin-bottom: 1.5rem;
    transition: all 0.3s ease;
}
.editorial-card:hover {
    border-color: #cbd5e1;
    box-shadow: 0 20px 35px rgba(0,0,0,0.05);
}
.editorial-card-highlight {
    background: linear-gradient(135deg, #ffffff 0%, #f0fdfa 100%);
    border: 2px solid #5eead4;
}

@keyframes pulse-animation {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(13, 148, 136, 0.7); }
    70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(13, 148, 136, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(13, 148, 136, 0); }
}
.pulsing-dot {
    display: inline-block;
    width: 10px; height: 10px;
    background-color: #0d9488;
    border-radius: 50%;
    animation: pulse-animation 1.5s infinite;
    margin-right: 6px;
    vertical-align: middle;
}
.offline-dot {
    display: inline-block;
    width: 10px; height: 10px;
    background-color: #cbd5e1;
    border-radius: 50%;
    margin-right: 6px;
    vertical-align: middle;
}

.stButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 14px;
    background: #0f172a;
    color: white;
    font-weight: 700;
    border: none;
    box-shadow: 0 4px 15px rgba(15, 23, 42, 0.15);
    transition: all 0.25s ease;
}
.stButton > button:hover {
    background: #0d9488;
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(13, 148, 136, 0.25);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# BARRA LATERALE
# ============================================================
with st.sidebar:
    st.markdown("### ⚡ Controllo Rapido")

    if st.session_state.abbonamento_titolare:
        st.success("👑 Account Titolare: ATTIVO")
        if st.button("Disattiva Abbonamento"):
            st.session_state.abbonamento_titolare = False
            st.rerun()
    else:
        st.warning("🔒 Account Titolare: FREE")
        if st.button("✨ Attiva Titolare"):
            st.session_state.abbonamento_titolare = True
            st.success("Abbonamento attivato!")
            st.rerun()

    st.markdown("---")
    st.markdown("### 🔐 Admin")
    password_inserita = st.text_input(
        "Password", type="password", key="input_pwd_admin"
    )
    mostra_admin = password_inserita == "admin123"
    if mostra_admin:
        st.success("Autorizzato ✅")

# ============================================================
# HEADER EDITORIALE
# ============================================================
st.markdown(
    """
<div class="editorial-header">
    <div class="editorial-title">
        <h1>Flashjob.</h1>
        <p>Curated Staffing & Hospitality Network • Milano HORECA</p>
    </div>
    <div style="font-size: 2.5rem; background: #f0fdfa; padding: 15px 22px; border-radius: 20px; border: 1px solid #ccfbf1;">⚡</div>
</div>
""",
    unsafe_allow_html=True,
)

menu_opzioni = [
    "Panoramica",
    "Database & Filtri Azienda",
    "Area Lavoratore & Weekend Boost",
    "Piani Abbonamento",
]
if mostra_admin:
    menu_opzioni.append("📊 Dashboard Admin")

scelta = st.radio("Navigazione", menu_opzioni, horizontal=True)

# ============================================================
# 1. PANORAMICA EDITORIALE
# ============================================================
if scelta == "Panoramica":
    st.markdown(
        """
        <div style="text-align: center; max-width: 800px; margin: 0 auto 3rem auto;">
            <span class="editorial-tag">Editoriale & Visione</span>
            <h2 style='font-weight:800; font-size:2.4rem; letter-spacing:-1px; color:#0f172a; margin-top:5px;'>Il punto d'incontro tra talenti HORECA e locali d'eccellenza.</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown(
            """
        <div class="editorial-card" style="height:100%;">
            <h3 style="color: #0d9488; margin-top: 0; font-weight:700;">Chi Siamo</h3>
            <p style="color: var(--text-muted); line-height: 1.7; font-size: 0.95rem;">
                Siamo professionisti della ristorazione e dell'innovazione digitale. Viviamo le sfide quotidiane 
                del settore e sappiamo quanto sia cruciale trovare personale affidabile o emergere rapidamente 
                nella giungla delle candidature tradizionali.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
        <div class="editorial-card" style="height:100%;">
            <h3 style="color: #0284c7; margin-top: 0; font-weight:700;">La Nostra Mission</h3>
            <p style="color: var(--text-muted); line-height: 1.7; font-size: 0.95rem;">
                Azzerare le distanze tra locali e lavoratori tramite geolocalizzazione smart, disponibilità in tempo reale 
                e contatti diretti via WhatsApp, eliminando ogni intermediario e burocrazia superflua.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown(
        "<h3 style='text-align: center; margin: 3.5rem 0 2rem 0; font-weight: 800; letter-spacing:-0.5px;'>I Pilastri del Servizio</h3>",
        unsafe_allow_html=True,
    )

    # 3 BANNER STILE EDITORIALE UNIFORME CON EFFETTO HOVER FLUIDO
    b1, b2, b3 = st.columns(3, gap="medium")
    with b1:
        st.markdown(
            """
        <div class="editorial-banner">
            <span class="editorial-tag">01 / Live</span>
            <h3 style="margin: 0 0 10px 0; font-size: 1.2rem; font-weight:700;">Disponibilità Immediata</h3>
            <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin: 0;">
                Il pallino verde lampeggiante indica chi è pronto a lavorare adesso, azzerando le telefonate a vuoto.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with b2:
        st.markdown(
            """
        <div class="editorial-banner">
            <span class="editorial-tag">02 / Direct</span>
            <h3 style="margin: 0 0 10px 0; font-size: 1.2rem; font-weight:700;">Contatto WhatsApp</h3>
            <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin: 0;">
                Parla direttamente con il candidato in un singolo click grazie ai piani di accesso dedicati.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with b3:
        st.markdown(
            """
        <div class="editorial-banner">
            <span class="editorial-tag">03 / Boost</span>
            <h3 style="margin: 0 0 10px 0; font-size: 1.2rem; font-weight:700;">Weekend Visibilità</h3>
            <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin: 0;">
                I lavoratori possono potenziare il profilo nei giorni di maggiore afflusso per ottenere più offerte.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

# ============================================================
# 2. DATABASE & FILTRI AZIENDA
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
        if st.button("← Torna alla lista completa"):
            st.session_state.selected_id = None
            st.rerun()

        stato_html = (
            '<span class="pulsing-dot"></span><b style="color:#0d9488;">DISPONIBILE ORA</b>'
            if selected_c["disponibile"]
            else '<span class="offline-dot"></span><span style="color:#888;">NON DISPONIBILE</span>'
        )

        st.markdown(
            f"""
        <div class="editorial-card editorial-card-highlight" style="margin-top: 20px;">
            <span class="editorial-tag">Profilo Selezionato</span>
            <div style="margin-top: 10px; margin-bottom: 8px;">{stato_html}</div>
            <h2 style="margin:0; font-size:1.8rem; font-weight:800;">{safe(selected_c["nome"])}</h2>
            <p style="color:var(--text-muted); margin:4px 0 10px 0; font-weight:600;">{safe(selected_c["mansione"])} · {safe(selected_c["zona"])}</p>
            <p style="color:#0284c7; font-weight:700; font-size:0.95rem;">⭐ {safe(selected_c["recensioni"])}</p>
            <hr style="border:0; border-top:1px solid #ccfbf1; margin:15px 0;">
            <p style="color:#475569; font-size:0.95rem;"><b>Referenze:</b> {safe(selected_c["referenze"])}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        if st.session_state.abbonamento_titolare:
            st.success("✓ Contatto sbloccato con il tuo abbonamento Titolare!")
            st.link_button(
                f"💬 Apri Chat WhatsApp ({selected_c['tel']})",
                whatsapp_url(selected_c["tel"]),
                use_container_width=True,
            )
        else:
            st.warning(
                "🔒 I numeri di telefono diretti sono riservati ai Titolari abbonati."
            )
            if st.button("Sblocca Contatti (Abbonati)"):
                st.session_state.abbonamento_titolare = True
                st.rerun()

    else:
        st.markdown(
            "<h2 style='font-weight:800; font-size:1.8rem; letter-spacing:-0.5px;'>Database Talenti & Filtri</h2>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='color:var(--text-muted); margin-bottom:2rem;'>Esplora i professionisti disponibili in tempo reale per la tua attività.</p>",
            unsafe_allow_html=True,
        )

        lavoratori_ordinati = sorted(
            st.session_state.lavoratori, key=lambda x: not x.get("boosted", False)
        )

        for lav in lavoratori_ordinati:
            card_class = (
                "editorial-card editorial-card-highlight"
                if lav.get("boosted")
                else "editorial-card"
            )
            badge_stato = (
                '<span class="pulsing-dot"></span><b style="color:#0d9488; font-size:0.75rem;">DISPONIBILE ORA</b>'
                if lav["disponibile"]
                else '<span class="offline-dot"></span><span style="color:#888; font-size:0.75rem;">NON DISPONIBILE</span>'
            )
            boost_label = (
                ' <span style="background:#0f172a; color:white; padding:3px 10px; border-radius:20px; font-size:0.7rem; font-weight:700;">BOOSTED 🚀</span>'
                if lav.get("boosted")
                else ""
            )

            col_info, col_btn = st.columns([3, 1], gap="medium")
            with col_info:
                st.markdown(
                    f"""
                <div class="{card_class}" style="margin-bottom:1rem; padding:1.4rem 1.8rem;">
                    <div style="margin-bottom:6px;">{badge_stato}</div>
                    <h3 style="margin:0; font-size:1.2rem; font-weight:700;">{safe(lav["nome"])}{boost_label}</h3>
                    <p style="color:var(--text-muted); margin:4px 0 0 0; font-size:0.9rem; font-weight:600;">{safe(lav["mansione"])} · {safe(lav["zona"])}</p>
                </div>
                """,
                    unsafe_allow_html=True,
                )
            with col_btn:
                st.markdown(
                    "<div style='margin-top: 18px;'></div>", unsafe_allow_html=True
                )
                if st.button("Vedi profilo", key=f"btn_card_{lav['id']}"):
                    st.session_state.selected_id = lav["id"]
                    st.rerun()

# ============================================================
# 3. AREA LAVORATORE & WEEKEND BOOST
# ============================================================
elif scelta == "Area Lavoratore & Weekend Boost":
    st.markdown(
        "<h2 style='font-weight:800; font-size:1.8rem; letter-spacing:-0.5px;'>Area Personale Lavoratore</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color:var(--text-muted); margin-bottom:2rem;'>Gestisci la tua disponibilità live e scegli il livello di visibilità ideale.</p>",
        unsafe_allow_html=True,
    )

    mio = st.session_state.mio_profilo

    nuova_disp = st.toggle(
        "🟢 Attiva disponibilità per lavorare (Accendi pallino verde)",
        value=mio["disponibile"],
    )
    if mio["disponibile"] != nuova_disp:
        mio["disponibile"] = nuova_disp
        st.rerun()

    st.markdown("---")
    st.markdown("### 🚀 Scegli il tuo piano visibilità")

    col_lp1, col_lp2, col_lp3 = st.columns(3, gap="medium")
    with col_lp1:
        st.markdown(
            """
        <div class="editorial-card" style="height:100%;">
            <span class="editorial-tag">Free</span>
            <h4 style="margin:5px 0; font-weight:700;">Standard</h4>
            <p style="color:var(--text-muted); font-size:0.85rem;">Inserimento nel database generale senza priorità nelle ricerche.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Seleziona Free"):
            mio["boosted"] = False
            st.success("Impostato piano Base Free.")
            st.rerun()

    with col_lp2:
        st.markdown(
            """
        <div class="editorial-card editorial-card-highlight" style="height:100%;">
            <span class="editorial-tag">Weekend</span>
            <h4 style="margin:5px 0; font-weight:700;">Top Weekend</h4>
            <p style="color:var(--text-muted); font-size:0.85rem;">In cima alle ricerche dei locali per tutto il fine settimana.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Attiva Weekend Boost"):
            mio["boosted"] = True
            st.session_state.boost_attivi_count += 1
            st.success("Weekend Boost attivato 🚀")
            st.rerun()

    with col_lp3:
        st.markdown(
            """
        <div class="editorial-card" style="height:100%;">
            <span class="editorial-tag">PRO</span>
            <h4 style="margin:5px 0; font-weight:700;">Abbonamento PRO</h4>
            <p style="color:var(--text-muted); font-size:0.85rem;">Visibilità continua 30 giorni e badge verificato oro.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Attiva PRO Talento"):
            mio["boosted"] = True
            st.success("Abbonamento PRO Talento attivato!")
            st.rerun()

# ============================================================
# 4. PIANI ABBONAMENTO
# ============================================================
elif scelta == "Piani Abbonamento":
    st.markdown(
        "<h2 style='font-weight:800; font-size:1.8rem; letter-spacing:-0.5px;'>Piani & Listino Prezzi ⚡</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color:var(--text-muted); margin-bottom:2.5rem;'>Soluzioni trasparenti e flessibili per locali, hotel e professionisti dell'HORECA.</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "### 🏢 Soluzioni per Locali & Aziende", unsafe_allow_html=True
    )
    col_sub1, col_sub2, col_sub3 = st.columns(3, gap="medium")

    with col_sub1:
        st.markdown(
            """
        <div class="editorial-card" style="height: 100%;">
            <span class="editorial-tag">Pass</span>
            <h3 style="font-size: 1.2rem; font-weight:700; margin-top: 5px;">Turno Singolo</h3>
            <div style="font-size: 1.6rem; font-weight: 800; color: #0284c7; margin: 8px 0;">7 € <span style="font-size: 0.8rem; color: var(--text-muted);">/ evento</span></div>
            <p style="color: var(--text-muted); font-size: 0.85rem;">Ideale per coprire un'emergenza o un turno serale last-minute.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Acquista Flash Pass"):
            st.success("Flash Pass acquistato!")
            st.rerun()

    with col_sub2:
        st.markdown(
            """
        <div class="editorial-card editorial-card-highlight" style="height: 100%;">
            <span class="editorial-tag">Full Access</span>
            <h3 style="font-size: 1.2rem; font-weight:700; margin-top: 5px;">Mensile Titolari</h3>
            <div style="font-size: 1.6rem; font-weight: 800; color: #0d9488; margin: 8px 0;">20 € <span style="font-size: 0.8rem; color: var(--text-muted);">/ mese</span></div>
            <p style="color: var(--text-muted); font-size: 0.85rem;">Contatti diretti illimitati su WhatsApp per tutti i lavoratori.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.session_state.abbonamento_titolare:
            st.success("✅ Attivo")
        else:
            if st.button("Abbonati Mensile"):
                st.session_state.abbonamento_titolare = True
                st.success("Abbonamento Titolare attivato!")
                st.rerun()

    with col_sub3:
        st.markdown(
            """
        <div class="editorial-card" style="height: 100%;">
            <span class="editorial-tag">Enterprise</span>
            <h3 style="font-size: 1.2rem; font-weight:700; margin-top: 5px;">Catene & Hotel</h3>
            <div style="font-size: 1.6rem; font-weight: 800; color: #0f172a; margin: 8px 0;">49 € <span style="font-size: 0.8rem; color: var(--text-muted);">/ mese</span></div>
            <p style="color: var(--text-muted); font-size: 0.85rem;">Account multi-sede e supporto prioritario dedicato.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Attiva Enterprise"):
            st.success("Richiesta Enterprise inviata!")
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        "### 👥 Soluzioni per Lavoratori & Talenti", unsafe_allow_html=True
    )
    col_lsub1, col_lsub2 = st.columns(2, gap="medium")

    with col_lsub1:
        st.markdown(
            """
        <div class="editorial-card" style="height: 100%;">
            <span class="editorial-tag">Weekend</span>
            <h3 style="font-size: 1.2rem; font-weight:700; margin-top: 5px;">In Evidenza Weekend</h3>
            <div style="font-size: 1.6rem; font-weight: 800; color: #0d9488; margin: 8px 0;">5 € <span style="font-size: 0.8rem; color: var(--text-muted);">/ weekend</span></div>
            <p style="color: var(--text-muted); font-size: 0.85rem;">Metti in evidenza il profilo nei giorni di maggiore afflusso.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.session_state.mio_profilo["boosted"]:
            st.success("✅ Boost Attivo")
        else:
            if st.button("Attiva Weekend Boost"):
                st.session_state.mio_profilo["boosted"] = True
                st.session_state.boost_attivi_count += 1
                st.success("Boost attivato!")
                st.rerun()

    with col_lsub2:
        st.markdown(
            """
        <div class="editorial-card editorial-card-highlight" style="height: 100%;">
            <span class="editorial-tag">PRO Talento</span>
            <h3 style="font-size: 1.2rem; font-weight:700; margin-top: 5px;">Abbonamento PRO</h3>
            <div style="font-size: 1.6rem; font-weight: 800; color: #0d9488; margin: 8px 0;">12 € <span style="font-size: 0.8rem; color: var(--text-muted);">/ mese</span></div>
            <p style="color: var(--text-muted); font-size: 0.85rem;">Visibilità costante tutto il mese e badge verificato oro.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Attiva PRO Mensile"):
            st.session_state.mio_profilo["boosted"] = True
            st.success("Abbonamento PRO attivato!")
            st.rerun()

# ============================================================
# 5. DASHBOARD ADMIN
# ============================================================
elif scelta == "📊 Dashboard Admin" and mostra_admin:
    st.markdown(
        "<h2 style='font-weight:800; font-size:1.8rem; letter-spacing:-0.5px;'>📊 Dashboard Admin Live</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color:var(--text-muted); margin-bottom:2rem;'>Monitoraggio in tempo reale delle metriche chiave di Flashjob.</p>",
        unsafe_allow_html=True,
    )

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric(
            label="Visite Totali",
            value=st.session_state.visite_totali,
            delta="+12% oggi",
        )
    with m2:
        st.metric(
            label="Click WhatsApp",
            value=st.session_state.click_whatsapp,
            delta="+5 da ieri",
        )
    with m3:
        st.metric(
            label="Abbonamenti Titolari",
            value="Attivo" if st.session_state.abbonamento_titolare else "Inattivo",
            delta="20€ / mo",
        )
    with m4:
        st.metric(
            label="Boost Attivi",
            value=st.session_state.boost_attivi_count,
            delta="5€ l'uno",
        )

    st.markdown("---")

    c_chart1, c_chart2 = st.columns(2)
    with c_chart1:
        st.markdown(
            """
        <div class="editorial-card">
            <h4 style="margin-top:0; font-weight:700;">Fatturato Stimato Mensile</h4>
            <p style="font-size: 1.8rem; font-weight: 800; color: #0d9488; margin: 10px 0;">€ 412,00</p>
            <p style="color: var(--text-muted); font-size: 0.85rem;">Calcolato su abbonamenti attivi, flash pass e boost.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with c_chart2:
        st.markdown(
            """
        <div class="editorial-card">
            <h4 style="margin-top:0; font-weight:700;">Stato Database</h4>
            <p style="font-size: 1.8rem; font-weight: 800; color: #0d9488; margin: 10px 0;">Ottimale 🟢</p>
            <p style="color: var(--text-muted); font-size: 0.85rem;">Latenza media di risposta server: <b>14 ms</b>.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )