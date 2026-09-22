import html
import re
import streamlit as st

st.set_page_config(
    page_title="Flashjob • Professional Tech Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
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
            "competenze": ["Lingua Inglese", "Vini & Sommelier Base", "POS"],
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
            "competenze": ["Mixology Avanzata", "Caffetteria Pro", "Cassa"],
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
        "referenze": "Professionista verificato nel settore HORECA.",
        "recensioni": "Nuovo utente",
        "competenze": ["Lingua Inglese"],
    }


def safe(value):
    return html.escape(str(value))


def whatsapp_url(phone):
    st.session_state.click_whatsapp += 1
    return "https://wa.me/" + re.sub(r"\D", "", phone)


# ============================================================
# DESIGN SYSTEM CON SFONDO PREMIUM PROFONDO E DINAMICO
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --text-main: #f8fafc;
    --text-muted: #94a3b8;
    --accent-teal: #14b8a6;
    --border-glass: rgba(255, 255, 255, 0.1);
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

/* SFONDO D'IMPATTO (PROFONDO, ELEGANTE E MODERNO) */
.stApp {
    background: 
        radial-gradient(circle at 15% 15%, rgba(20, 184, 166, 0.15) 0%, transparent 50%),
        radial-gradient(circle at 85% 85%, rgba(99, 102, 241, 0.15) 0%, transparent 50%),
        linear-gradient(135deg, #090d16 0%, #111827 50%, #0f172a 100%);
    background-attachment: fixed;
    color: var(--text-main);
}

/* CONTENITORE RESPONSIVE */
.block-container {
    max-width: 1050px !important;
    padding: 1.5rem 1rem 5rem 1rem !important;
}

@media (min-width: 768px) {
    .block-container {
        padding: 2.5rem 2rem 6rem 2rem !important;
    }
}

#MainMenu, footer, header {visibility: hidden; display: none;}
[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] {display: none !important;}

/* HEADER TECH CON EFFETTO GLASS SCURO */
.tech-header {
    background: rgba(17, 24, 39, 0.75);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 1.5rem 1.5rem;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    margin-bottom: 2rem;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}
@media (min-width: 768px) {
    .tech-header {
        padding: 2rem 2.5rem;
        border-radius: 20px;
    }
}
.tech-title h1 {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 1.8rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    color: #ffffff;
    margin: 0;
}
@media (min-width: 768px) {
    .tech-title h1 {
        font-size: 2.2rem;
    }
}
.tech-title p {
    font-size: 0.85rem;
    color: var(--text-muted);
    margin: 4px 0 0 0;
    font-weight: 500;
}

/* NAVIGAZIONE DINAMICA A TABS */
div[data-testid="stRadio"] > label { display: none; }
div[data-testid="stRadio"] div[role="radiogroup"] {
    display: flex;
    justify-content: center;
    background: rgba(17, 24, 39, 0.75);
    backdrop-filter: blur(16px);
    padding: 5px;
    border-radius: 14px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.4);
    margin-bottom: 2.5rem;
    gap: 4px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    flex-wrap: wrap;
}
div[data-testid="stRadio"] div[role="radiogroup"] label {
    border-radius: 10px;
    padding: 8px 16px;
    font-weight: 600;
    font-size: 0.82rem;
    color: var(--text-muted) !important;
    transition: all 0.2s ease;
}
div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
    background: rgba(20, 184, 166, 0.1);
    color: #14b8a6 !important;
}
div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
    background: #14b8a6 !important;
    color: #0f172a !important;
    box-shadow: 0 4px 12px rgba(20, 184, 166, 0.3);
    font-weight: 700;
}

/* CARD CON EFFETTO GLASSMORPHISM SCURO PULITO */
.tech-card {
    background: rgba(17, 24, 39, 0.65);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 1.5rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    margin-bottom: 1.2rem;
    transition: all 0.2s ease;
    color: #f8fafc;
}
.tech-card:hover {
    background: rgba(17, 24, 39, 0.85);
    border-color: rgba(20, 184, 166, 0.4);
    box-shadow: 0 12px 35px rgba(0,0,0,0.5);
}
.tech-card-highlight {
    background: rgba(17, 24, 39, 0.85);
    border: 2px solid #14b8a6;
}

.tech-tag {
    font-size: 0.68rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #14b8a6;
    background: rgba(20, 184, 166, 0.1);
    padding: 4px 10px;
    border-radius: 6px;
    display: inline-block;
    margin-bottom: 0.8rem;
    border: 1px solid rgba(20, 184, 166, 0.3);
}

@keyframes pulse-animation {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(20, 184, 166, 0.7); }
    70% { transform: scale(1); box-shadow: 0 0 0 8px rgba(20, 184, 166, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(20, 184, 166, 0); }
}
.pulsing-dot {
    display: inline-block;
    width: 8px; height: 8px;
    background-color: #14b8a6;
    border-radius: 50%;
    animation: pulse-animation 1.5s infinite;
    margin-right: 6px;
    vertical-align: middle;
}
.offline-dot {
    display: inline-block;
    width: 8px; height: 8px;
    background-color: #64748b;
    border-radius: 50%;
    margin-right: 6px;
    vertical-align: middle;
}

.stButton > button {
    width: 100%;
    min-height: 44px;
    border-radius: 10px;
    background: #14b8a6;
    color: #0f172a;
    font-weight: 700;
    font-size: 0.88rem;
    border: none;
    box-shadow: 0 4px 12px rgba(20, 184, 166, 0.2);
    transition: all 0.2s ease;
}
.stButton > button:hover {
    background: #0d9488;
    color: #ffffff;
    transform: translateY(-1px);
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
        st.success("👑 Titolare: ATTIVO")
        if st.button("Disattiva Account"):
            st.session_state.abbonamento_titolare = False
            st.rerun()
    else:
        st.warning("🔒 Titolare: FREE")
        if st.button("✨ Simula Titolare"):
            st.session_state.abbonamento_titolare = True
            st.success("Attivato!")
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
# HEADER PRINCIPALE
# ============================================================
st.markdown(
    """
<div class="tech-header">
    <div class="tech-title">
        <h1>Flashjob.</h1>
        <p>Curated Hospitality Network • Milano</p>
    </div>
    <div style="font-size: 1.5rem; background: rgba(20,184,166,0.1); padding: 10px 14px; border-radius: 12px; border: 1px solid rgba(20,184,166,0.3);">⚡</div>
</div>
""",
    unsafe_allow_html=True,
)

menu_opzioni = [
    "Panoramica",
    "Database Talenti",
    "Area Lavoratore",
    "Piani (Coming Soon)",
]
if mostra_admin:
    menu_opzioni.append("📊 Admin")

scelta = st.radio("Navigazione", menu_opzioni, horizontal=True)

# ============================================================
# 1. PANORAMICA
# ============================================================
if scelta == "Panoramica":
    st.markdown(
        """
        <div style="text-align: center; max-width: 700px; margin: 0 auto 2.5rem auto;">
            <span class="tech-tag">Network & Soluzioni</span>
            <h2 style="font-weight: 800; font-size: 1.7rem; color: #ffffff; margin-top: 4px; letter-spacing: -0.02em;">Connettiamo locali d'eccellenza e professionisti HORECA.</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2, gap="medium")
    with c1:
        st.markdown(
            """
        <div class="tech-card">
            <h3 style="color: #14b8a6; margin-top: 0; font-size: 1.05rem; font-weight: 700;">Per le Aziende</h3>
            <p style="color: var(--text-muted); line-height: 1.5; font-size: 0.88rem; margin-bottom: 0;">
                Trova personale qualificato immediatamente disponibile a Milano, riducendo i tempi di ricerca e le chiamate a vuoto.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
        <div class="tech-card">
            <h3 style="color: #ffffff; margin-top: 0; font-size: 1.05rem; font-weight: 700;">Per i Talenti</h3>
            <p style="color: var(--text-muted); line-height: 1.5; font-size: 0.88rem; margin-bottom: 0;">
                Gestisci la tua disponibilità in tempo reale e fatti contattare direttamente dai migliori locali della zona.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

# ============================================================
# 2. DATABASE & FILTRI AZIENDA
# ============================================================
elif scelta == "Database Talenti":
    selected_c = next(
        (
            item
            for item in st.session_state.lavoratori
            if item["id"] == st.session_state.selected_id
        ),
        None,
    )

    if selected_c is not None:
        if st.button("← Torna alla lista"):
            st.session_state.selected_id = None
            st.rerun()

        stato_html = (
            '<span class="pulsing-dot"></span><b style="color:#14b8a6; font-size:0.8rem;">DISPONIBILE ORA</b>'
            if selected_c["disponibile"]
            else '<span class="offline-dot"></span><span style="color:#94a3b8; font-size:0.8rem;">NON DISPONIBILE</span>'
        )

        st.markdown(
            f"""
        <div class="tech-card tech-card-highlight" style="margin-top: 10px;">
            <span class="tech-tag">Profilo Selezionato</span>
            <div style="margin-top: 6px; margin-bottom: 4px;">{stato_html}</div>
            <h2 style="font-weight: 800; margin: 0; font-size: 1.5rem; letter-spacing: -0.02em; color: #ffffff;">{safe(selected_c["nome"])}</h2>
            <p style="color: var(--text-muted); margin: 4px 0 6px 0; font-weight: 600; font-size: 0.88rem;">{safe(selected_c["mansione"])} · {safe(selected_c["zona"])}</p>
            <p style="color: #14b8a6; font-weight: 700; font-size: 0.88rem;">{safe(selected_c["recensioni"])}</p>
            <hr style="border: 0; border-top: 1px solid rgba(255, 255, 255, 0.1); margin: 12px 0;">
            <p style="color: var(--text-muted); font-size: 0.88rem; margin: 0;"><b>Referenze:</b> {safe(selected_c["referenze"])}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        if st.session_state.abbonamento_titolare:
            st.success("✓ Contatto sbloccato con il tuo account Titolare!")
            st.link_button(
                f"💬 Apri Chat WhatsApp ({selected_c['tel']})",
                whatsapp_url(selected_c["tel"]),
                use_container_width=True,
            )
        else:
            st.warning("🔒 I numeri di telefono diretti sono riservati.")
            if st.button("Sblocca Contatti (Simula Titolare)"):
                st.session_state.abbonamento_titolare = True
                st.rerun()

    else:
        st.markdown(
            "<h2 style='font-weight: 800; font-size: 1.5rem; letter-spacing: -0.02em; margin-bottom: 4px; color: #ffffff;'>Database Talenti</h2>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='color: var(--text-muted); margin-bottom: 1.5rem; font-size: 0.88rem;'>Esplora i professionisti disponibili in tempo reale.</p>",
            unsafe_allow_html=True,
        )

        lavoratori_ordinati = sorted(
            st.session_state.lavoratori, key=lambda x: not x.get("boosted", False)
        )

        for lav in lavoratori_ordinati:
            card_class = (
                "tech-card tech-card-highlight"
                if lav.get("boosted")
                else "tech-card"
            )
            badge_stato = (
                '<span class="pulsing-dot"></span><b style="color:#14b8a6; font-size:0.7rem;">DISPONIBILE ORA</b>'
                if lav["disponibile"]
                else '<span class="offline-dot"></span><span style="color:#94a3b8; font-size:0.7rem;">NON DISPONIBILE</span>'
            )
            boost_label = (
                ' <span style="background:#14b8a6; color:#0f172a; padding:2px 6px; border-radius:4px; font-size:0.65rem; font-weight:700;">BOOSTED</span>'
                if lav.get("boosted")
                else ""
            )

            st.markdown(
                f"""
            <div class="{card_class}" style="margin-bottom: 1rem; padding: 1.2rem 1.4rem;">
                <div style="margin-bottom: 4px;">{badge_stato}</div>
                <h3 style="margin: 0; font-size: 1.05rem; font-weight: 700; color: #ffffff;">{safe(lav["nome"])}{boost_label}</h3>
                <p style="color: var(--text-muted); margin: 4px 0 0 0; font-size: 0.82rem; font-weight: 600;">{safe(lav["mansione"])} · {safe(lav["zona"])}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )
            if st.button("Vedi profilo", key=f"btn_card_{lav['id']}"):
                st.session_state.selected_id = lav["id"]
                st.rerun()

# ============================================================
# 3. AREA LAVORATORE & WEEKEND BOOST
# ============================================================
elif scelta == "Area Lavoratore":
    st.markdown(
        "<h2 style='font-weight: 800; font-size: 1.5rem; letter-spacing: -0.02em; margin-bottom: 4px; color: #ffffff;'>Area Personale</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: var(--text-muted); margin-bottom: 1.5rem; font-size: 0.88rem;'>Gestisci la tua disponibilità live e scegli il piano visibilità.</p>",
        unsafe_allow_html=True,
    )

    mio = st.session_state.mio_profilo

    nuova_disp = st.toggle(
        "🟢 Attiva disponibilità per lavorare", value=mio["disponibile"]
    )
    if mio["disponibile"] != nuova_disp:
        mio["disponibile"] = nuova_disp
        st.rerun()

    st.markdown("---")
    st.markdown("### 🚀 Livello Visibilità")

    col_lp1, col_lp2 = st.columns(2, gap="small")
    with col_lp1:
        st.markdown(
            """
        <div class="tech-card" style="height:100%;">
            <span class="tech-tag" style="background:rgba(255,255,255,0.05); color:#94a3b8; border-color:rgba(255,255,255,0.1);">Free</span>
            <h4 style="margin: 4px 0; font-size: 0.95rem; font-weight: 700; color: #ffffff;">Standard</h4>
            <p style="color: var(--text-muted); font-size: 0.8rem; margin:0;">Database generale senza priorità di ricerca.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Seleziona Free"):
            mio["boosted"] = False
            st.success("Impostato piano Base.")
            st.rerun()

    with col_lp2:
        st.markdown(
            """
        <div class="tech-card tech-card-highlight" style="height:100%;">
            <span class="tech-tag">Weekend</span>
            <h4 style="margin: 4px 0; font-size: 0.95rem; font-weight: 700; color: #ffffff;">Top Weekend</h4>
            <p style="color: var(--text-muted); font-size: 0.8rem; margin:0;">In cima alle ricerche dei locali per tutto il fine settimana.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Attiva Boost"):
            mio["boosted"] = True
            st.session_state.boost_attivi_count += 1
            st.success("Weekend Boost attivato 🚀")
            st.rerun()

# ============================================================
# 4. PIANI ABBONAMENTO (COMING SOON)
# ============================================================
elif scelta == "Piani (Coming Soon)":
    st.markdown(
        "<h2 style='font-weight: 800; font-size: 1.5rem; letter-spacing: -0.02em; margin-bottom: 4px; color: #ffffff;'>Piani & Listino ⚡</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: var(--text-muted); margin-bottom: 2rem; font-size: 0.88rem;'>Stiamo ultimando lo sviluppo. I piani saranno attivi a breve.</p>",
        unsafe_allow_html=True,
    )

    st.markdown("### 🏢 Per Locali & Aziende", unsafe_allow_html=True)
    st.markdown(
        """
    <div class="tech-card" style="opacity: 0.9;">
        <span class="tech-tag" style="background:rgba(255,255,255,0.05); color:#94a3b8; border-color:rgba(255,255,255,0.1);">Coming Soon</span>
        <h3 style="font-size: 1.05rem; font-weight: 700; margin: 4px 0; color: #ffffff;">Mensile Titolari & Pass</h3>
        <div style="font-size: 1.3rem; font-weight: 800; color: #14b8a6; margin: 4px 0;">20 € <span style="font-size: 0.75rem; color: var(--text-muted); font-weight: 500;">/ mese</span></div>
        <p style="color: var(--text-muted); font-size: 0.82rem; margin:0;">Contatti diretti illimitati su WhatsApp per tutti i profili.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.info("🕒 In arrivo prossimamente")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 👥 Per Lavoratori", unsafe_allow_html=True)
    st.markdown(
        """
    <div class="tech-card tech-card-highlight" style="opacity: 0.9;">
        <span class="tech-tag" style="background:rgba(255,255,255,0.05); color:#94a3b8; border-color:rgba(255,255,255,0.1);">Coming Soon</span>
        <h3 style="font-size: 1.05rem; font-weight: 700; margin: 4px 0; color: #ffffff;">Abbonamento PRO Talento</h3>
        <div style="font-size: 1.3rem; font-weight: 800; color: #14b8a6; margin: 4px 0;">12 € <span style="font-size: 0.75rem; color: var(--text-muted); font-weight: 500;">/ mese</span></div>
        <p style="color: var(--text-muted); font-size: 0.82rem; margin:0;">Visibilità costante tutto il mese e badge verificato oro.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.info("🕒 In arrivo prossimamente")

# ============================================================
# 5. DASHBOARD ADMIN
# ============================================================
elif scelta == "📊 Admin" and mostra_admin:
    st.markdown(
        "<h2 style='font-weight: 800; font-size: 1.5rem; letter-spacing: -0.02em; margin-bottom: 4px; color: #ffffff;'>📊 Dashboard Admin</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: var(--text-muted); margin-bottom: 1.5rem; font-size: 0.88rem;'>Monitoraggio in tempo reale delle metriche.</p>",
        unsafe_allow_html=True,
    )

    m1, m2 = st.columns(2, gap="small")
    with m1:
        st.metric(
            label="Visite Totali",
            value=st.session_state.visite_totali,
            delta="+12%",
        )
    with m2:
        st.metric(
            label="Click WhatsApp",
            value=st.session_state.click_whatsapp,
            delta="+5",
        )

    st.markdown("---")
    st.markdown(
        """
    <div class="tech-card">
        <h4 style="margin-top:0; font-weight:700; font-size:0.95rem; color: #ffffff;">Stato Sistema</h4>
        <p style="font-size: 1.2rem; font-weight: 800; color: #14b8a6; margin: 4px 0;">Ottimale & Responsive 🟢</p>
        <p style="color: var(--text-muted); font-size: 0.82rem; margin:0;">Layout completamente adattato per smartphone e desktop con sfondo coordinato.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )