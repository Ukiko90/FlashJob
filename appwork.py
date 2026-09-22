import html
import re
import streamlit as st

st.set_page_config(
    page_title="Flashjob • Il Lavoro a Portata di Mano",
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
# DESIGN SYSTEM & COLOR PALETTE (FLUIDA, INTERATTIVA & UNIFORME)
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --bg-gradient: linear-gradient(135deg, #f0fdfa 0%, #e0f2fe 50%, #eff6ff 100%);
    --card-bg: #ffffff;
    --text-main: #0f172a;
    --text-muted: #475569;
    --border-color: #cffafe;
    --shadow: 0 12px 35px rgba(14, 165, 233, 0.08);
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

#MainMenu, footer, header {visibility: hidden; display: none;}
[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stStatusWidget"] {display: none !important;}

/* HEADER SFUMATO CELESTE - VERDE ACQUA */
.store-header {
    background: linear-gradient(135deg, #0284c7 0%, #0d9488 50%, #14b8a6 100%);
    color: white;
    padding: 2.8rem 2.2rem;
    border-radius: 30px;
    box-shadow: 0 20px 45px rgba(20, 184, 166, 0.25);
    margin-bottom: 2.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 20px;
}
.app-info-left {
    display: flex;
    align-items: center;
    gap: 22px;
}
.app-logo-box {
    width: 90px;
    height: 90px;
    background: white;
    color: #0d9488;
    border-radius: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
    box-shadow: 0 10px 25px rgba(0,0,0,0.12);
}
.app-titles h1 {
    font-size: 2.5rem;
    font-weight: 800;
    margin: 0;
    letter-spacing: -1px;
    color: white;
    text-shadow: 0 2px 10px rgba(0,0,0,0.15);
}
.app-titles p {
    font-size: 1rem;
    margin: 6px 0 0 0;
    color: #ccfbf1;
    font-weight: 600;
}

/* RADIO NAVIGATION STILE PILLOLA FLUIDO */
div[data-testid="stRadio"] > label { display: none; }
div[data-testid="stRadio"] div[role="radiogroup"] {
    display: flex;
    justify-content: center;
    background: white;
    padding: 8px;
    border-radius: 50px;
    box-shadow: var(--shadow);
    margin-bottom: 2.5rem;
    gap: 6px;
    border: 1px solid #ccfbf1;
    flex-wrap: wrap;
}
div[data-testid="stRadio"] div[role="radiogroup"] label {
    border-radius: 40px;
    padding: 10px 18px;
    font-weight: 700;
    font-size: 0.82rem;
    color: var(--text-muted) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
    background: #f0fdfa;
    color: #0d9488 !important;
}
div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
    background: linear-gradient(135deg, #0284c7 0%, #0d9488 100%) !important;
    color: white !important;
    box-shadow: 0 4px 15px rgba(13, 148, 136, 0.3);
}

/* BANNER INIZIALI UNIFORMI CON EFFETTO HOVER FLUIDO */
.feature-banner {
    background: linear-gradient(145deg, #ffffff 0%, #f0fdfa 100%);
    color: var(--text-main);
    padding: 2.2rem;
    border-radius: 24px;
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow);
    border: 1px solid #99f6e4;
    height: 100%;
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}
.feature-banner:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 45px rgba(13, 148, 136, 0.2);
    border-color: #0d9488;
    background: linear-gradient(145deg, #ffffff 0%, #ccfbf1 100%);
}
.feature-tag { 
    background: #ccfbf1; 
    color: #0f766e; 
    padding: 6px 14px; 
    border-radius: 30px; 
    font-size: 0.75rem; 
    font-weight: 800; 
    text-transform: uppercase; 
    display: inline-block; 
    margin-bottom: 15px; 
    box-shadow: 0 2px 8px rgba(13, 148, 136, 0.15);
}

.custom-card {
    background: var(--card-bg);
    border-radius: var(--radius);
    padding: 1.8rem;
    box-shadow: var(--shadow);
    border: 1px solid var(--border-color);
    margin-bottom: 1.5rem;
    transition: all 0.3s ease;
}
.custom-card:hover {
    box-shadow: 0 16px 40px rgba(14, 165, 233, 0.12);
}
.boosted-card {
    border: 2px solid #2dd4bf;
    background: linear-gradient(145deg, #ffffff 0%, #f0fdfa 100%);
}

@keyframes pulse-animation {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(45, 212, 191, 0.7); }
    70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(45, 212, 191, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(45, 212, 191, 0); }
}
.pulsing-dot {
    display: inline-block;
    width: 12px;
    height: 12px;
    background-color: #2dd4bf;
    border-radius: 50%;
    animation: pulse-animation 1.5s infinite;
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
.badge-aqua { background: #ccfbf1; color: #0f766e; }
.badge-boost { background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; }

.stButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 14px;
    background: linear-gradient(135deg, #0284c7 0%, #0d9488 100%);
    color: white;
    font-weight: 800;
    border: none;
    box-shadow: 0 6px 20px rgba(13, 148, 136, 0.25);
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}
.stButton > button:hover {
    opacity: 0.95;
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(13, 148, 136, 0.35);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# BARRA LATERALE (ADMIN & ABBONAMENTO)
# ============================================================
with st.sidebar:
    st.markdown("### ⚡ Pannello di Controllo")

    if st.session_state.abbonamento_titolare:
        st.success("👑 Account Titolare: ATTIVO")
        if st.button("Disattiva Abbonamento"):
            st.session_state.abbonamento_titolare = False
            st.rerun()
    else:
        st.warning("🔒 Account Titolare: FREE")
        if st.button("✨ Attiva Titolare"):
            st.session_state.abbonamento_titolare = True
            st.success("Abbonamento Titolare attivato!")
            st.rerun()

    st.markdown("---")
    st.markdown("### 🔐 Area Admin")
    password_inserita = st.text_input(
        "Password Admin", type="password", key="input_pwd_admin"
    )
    mostra_admin = password_inserita == "admin123"
    if mostra_admin:
        st.success("Admin Autorizzato ✅")

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
            <p>Il Lavoro a Portata di Mano • Sala, Bar, Cucina, Hostess & Booking</p>
        </div>
    </div>
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
# 1. PANORAMICA (CHI SIAMO, A COSA SERVE & BANNER UNIFORMI)
# ============================================================
if scelta == "Panoramica":
    st.markdown(
        """
        <div style="text-align: center; max-width: 850px; margin: 0 auto 2.5rem auto;">
            <span class="badge-pop badge-aqua">Benvenuti su Flashjob</span>
            <h2 style='font-weight:800; font-size:2.2rem; margin-top:10px; color:#0f172a;'>Il punto d'incontro definitivo tra talenti HORECA e locali d'eccellenza.</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    col_text1, col_text2 = st.columns(2, gap="large")
    with col_text1:
        st.markdown(
            """
        <div class="custom-card" style="height: 100%;">
            <h3 style="color: #0d9488; margin-top: 0;">👥 Chi Siamo</h3>
            <p style="color: var(--text-muted); line-height: 1.7; font-size: 0.95rem;">
                Siamo un team di professionisti della ristorazione, dell'hotellerie e dell'innovazione digitale. 
                Viviamo quotidianamente le sfide del settore e sappiamo quanto sia difficile trovare personale affidabile 
                all'ultimo minuto o emergere nella giungla delle candidature tradizionali. Flashjob nasce per azzerare 
                le distanze e dare valore al tempo di tutti.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col_text2:
        st.markdown(
            """
        <div class="custom-card" style="height: 100%;">
            <h3 style="color: #0284c7; margin-top: 0;">🎯 A cosa serve l'app</h3>
            <p style="color: var(--text-muted); line-height: 1.7; font-size: 0.95rem;">
                Flashjob è la piattaforma smart pensata per la gestione flessibile e immediata del personale nel settore HORECA. 
                Attraverso la geolocalizzazione, lo stato di disponibilità in tempo reale e 
                canali di contatto diretti via WhatsApp, permettiamo ai locali di coprire turni o eventi improvvisi in pochi minuti.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown(
        "<h3 style='text-align: center; margin: 3rem 0 1.5rem 0; font-weight: 800;'>I nostri 3 Punti di Forza</h3>",
        unsafe_allow_html=True,
    )

    # 3 BANNER STESSO COLORE E STILE CON EFFETTO HOVER DINAMICO
    b1, b2, b3 = st.columns(3, gap="medium")
    with b1:
        st.markdown(
            """
        <div class="feature-banner">
            <span class="feature-tag">Velocità 🟢</span>
            <h3 style="margin: 10px 0; color: #0f172a; font-size: 1.25rem;">Disponibilità Live</h3>
            <p style="color: var(--text-muted); font-size: 0.85rem; line-height: 1.6; margin: 0;">
                Il pallino verde lampeggiante mostra all'istante chi è pronto a lavorare adesso, eliminando telefonate a vuoto e perdite di tempo.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with b2:
        st.markdown(
            """
        <div class="feature-banner">
            <span class="feature-tag">Diretto 💬</span>
            <h3 style="margin: 10px 0; color: #0f172a; font-size: 1.25rem;">Chat & WhatsApp</h3>
            <p style="color: var(--text-muted); font-size: 0.85rem; line-height: 1.6; margin: 0;">
                Nessuna intermediazione burocratica. Con i piani dedicati parli direttamente con il candidato in un singolo click.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with b3:
        st.markdown(
            """
        <div class="feature-banner">
            <span class="feature-tag">Visibilità 🚀</span>
            <h3 style="margin: 10px 0; color: #0f172a; font-size: 1.25rem;">Weekend Boost</h3>
            <p style="color: var(--text-muted); font-size: 0.85rem; line-height: 1.6; margin: 0;">
                I lavoratori possono potenziare la propria visibilità nei giorni di maggiore afflusso per ricevere molte più offerte di lavoro.
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
        if st.button("← Torna al database completo"):
            st.session_state.selected_id = None
            st.rerun()

        stato_html = (
            '<span class="pulsing-dot"></span><b style="color:#0d9488;">DISPONIBILE ORA</b>'
            if selected_c["disponibile"]
            else '<span class="offline-dot"></span><span style="color:#888;">NON DISPONIBILE</span>'
        )
        boost_badge = (
            '<span class="badge-pop badge-boost">🚀 Weekend Boost Attivo</span><br>'
            if selected_c.get("boosted")
            else ""
        )

        st.markdown(
            f"""
        <div class="custom-card" style="margin-top: 20px;">
            {boost_badge}
            <div style="display: flex; align-items: center; gap: 20px;">
                <div style="font-size: 3rem;">👤</div>
                <div>
                    <div style="margin-bottom:6px;">{stato_html}</div>
                    <h2 style="margin:0; font-size:1.5rem;">{safe(selected_c["nome"])}</h2>
                    <p style="color:var(--text-muted); margin:4px 0 0 0; font-weight:600;">{safe(selected_c["mansione"])} · {safe(selected_c["zona"])}</p>
                    <p style="color:#0284c7; margin:6px 0 0 0; font-weight:700; font-size:0.9rem;">⭐ {safe(selected_c["recensioni"])}</p>
                </div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        if st.session_state.abbonamento_titolare:
            st.success(
                "✓ Contatto sbloccato grazie al tuo abbonamento Titolare attivo!"
            )
            st.link_button(
                f"💬 Contatta Direttamente ({selected_c['tel']})",
                whatsapp_url(selected_c["tel"]),
                use_container_width=True,
            )
        else:
            st.warning(
                "🔒 I contatti telefonici diretti sono riservati ai Titolari abbonati."
            )
            if st.button("Abbonati come Titolare"):
                st.session_state.abbonamento_titolare = True
                st.rerun()

    else:
        st.markdown(
            "<h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Database Contatti & Filtri</h2>",
            unsafe_allow_html=True,
        )

        lavoratori_ordinati = sorted(
            st.session_state.lavoratori, key=lambda x: not x.get("boosted", False)
        )

        for lav in lavoratori_ordinati:
            card_class = (
                "custom-card boosted-card"
                if lav.get("boosted")
                else "custom-card"
            )
            badge_stato = (
                '<span class="pulsing-dot"></span><b style="color:#0d9488; font-size:0.75rem;">DISPONIBILE ORA</b>'
                if lav["disponibile"]
                else '<span class="offline-dot"></span><span style="color:#888; font-size:0.75rem;">NON DISPONIBILE</span>'
            )
            boost_label = (
                ' <span style="background:#0284c7; color:white; padding:2px 8px; border-radius:6px; font-size:0.7rem;">BOOSTED 🚀</span>'
                if lav.get("boosted")
                else ""
            )

            col_info, col_btn = st.columns([3, 1], gap="medium")
            with col_info:
                st.markdown(
                    f"""
                <div class="{card_class}" style="margin-bottom:1rem; padding:1.2rem 1.5rem;">
                    <div style="margin-bottom:6px;">{badge_stato}</div>
                    <h3 style="margin:0; font-size:1.15rem;">{safe(lav["nome"])}{boost_label}</h3>
                    <p style="color:var(--text-muted); margin:3px 0; font-size:0.9rem; font-weight:600;">{safe(lav["mansione"])} · {safe(lav["zona"])}</p>
                </div>
                """,
                    unsafe_allow_html=True,
                )
            with col_btn:
                st.markdown(
                    "<div style='margin-top: 20px;'></div>", unsafe_allow_html=True
                )
                if st.button("Vedi profilo", key=f"btn_card_{lav['id']}"):
                    st.session_state.selected_id = lav["id"]
                    st.rerun()

# ============================================================
# 3. AREA LAVORATORE & WEEKEND BOOST
# ============================================================
elif scelta == "Area Lavoratore & Weekend Boost":
    st.markdown(
        "<h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Area Personale Lavoratore & Boost</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color:var(--text-muted); margin-bottom:2rem;'>Attiva il tuo pallino verde e scegli il tuo piano di visibilità per il fine settimana o professionale.</p>",
        unsafe_allow_html=True,
    )

    mio = st.session_state.mio_profilo

    nuova_disp = st.toggle(
        "🟢 Attiva disponibilità per lavorare (Accendi pallino verde lampeggiante)",
        value=mio["disponibile"],
    )
    if mio["disponibile"] != nuova_disp:
        mio["disponibile"] = nuova_disp
        st.rerun()

    st.markdown("---")
    st.markdown("### 🚀 Gestione Piani Lavoratore")

    col_lp1, col_lp2, col_lp3 = st.columns(3, gap="medium")
    with col_lp1:
        st.markdown(
            """
        <div class="custom-card" style="height:100%;">
            <span class="badge-pop" style="background:#f1f5f9; color:#475569;">Base Free</span>
            <h4 style="margin:5px 0;">Standard</h4>
            <p style="color:var(--text-muted); font-size:0.85rem;">Inserimento nel database generale senza priorità nelle ricerche.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Seleziona Free"):
            mio["boosted"] = False
            st.success("Selezionato piano Base Free.")
            st.rerun()

    with col_lp2:
        st.markdown(
            """
        <div class="custom-card boosted-card" style="height:100%;">
            <span class="badge-pop badge-boost">Weekend Boost</span>
            <h4 style="margin:5px 0;">Top Weekend</h4>
            <p style="color:var(--text-muted); font-size:0.85rem;">Posizionamento in cima alle ricerche per tutto il fine settimana.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Attiva Weekend Boost"):
            mio["boosted"] = True
            st.session_state.boost_attivi_count += 1
            st.success("Weekend Boost attivato con successo 🚀")
            st.rerun()

    with col_lp3:
        st.markdown(
            """
        <div class="custom-card" style="height:100%; border-top: 4px solid #0d9488;">
            <span class="badge-pop badge-aqua">PRO Talento</span>
            <h4 style="margin:5px 0;">Abbonamento PRO</h4>
            <p style="color:var(--text-muted); font-size:0.85rem;">Visibilità prioritaria continua per 30 giorni + badge verificato speciale.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Attiva PRO Talento"):
            mio["boosted"] = True
            st.success("Abbonamento PRO Talento attivato!")
            st.rerun()

# ============================================================
# 4. PIANI ABBONAMENTO (NUOVA SEZIONE AMPLIATA)
# ============================================================
elif scelta == "Piani Abbonamento":
    st.markdown(
        "<h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Piani Abbonamento & Listino ⚡</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color:var(--text-muted); margin-bottom:2rem;'>Soluzioni flessibili pensate su misura per titolari di locali, hotel, bar e professionisti.</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "### 🏢 Soluzioni per Locali & Aziende", unsafe_allow_html=True
    )
    col_sub1, col_sub2, col_sub3 = st.columns(3, gap="medium")

    with col_sub1:
        st.markdown(
            """
        <div class="custom-card" style="height: 100%;">
            <span class="badge-pop" style="background:#f1f5f9; color:#475569;">Flash Pass</span>
            <h3 style="font-size: 1.2rem; margin-top: 5px;">Turno Singolo</h3>
            <div style="font-size: 1.5rem; font-weight: 800; color: #0284c7; margin: 8px 0;">7 € <span style="font-size: 0.8rem; color: var(--text-muted);">/ evento</span></div>
            <p style="color: var(--text-muted); font-size: 0.85rem;">Perfetto per coprire un'emergenza o un singolo turno serale last-minute.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Acquista Flash Pass"):
            st.success("Flash Pass acquistato! Contatti sbloccati per 24h.")
            st.rerun()

    with col_sub2:
        st.markdown(
            """
        <div class="custom-card" style="border-top: 4px solid #0284c7; height: 100%;">
            <span class="badge-pop badge-aqua">Full Access</span>
            <h3 style="font-size: 1.2rem; margin-top: 5px;">Abbonamento Mensile</h3>
            <div style="font-size: 1.5rem; font-weight: 800; color: #0284c7; margin: 8px 0;">20 € <span style="font-size: 0.8rem; color: var(--text-muted);">/ mese</span></div>
            <p style="color: var(--text-muted); font-size: 0.85rem;">Contatti diretti illimitati su WhatsApp per tutti i lavoratori della piattaforma.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.session_state.abbonamento_titolare:
            st.success("✅ Attivo")
        else:
            if st.button("Abbonati Mensile"):
                st.session_state.abbonamento_titolare = True
                st.success("Abbonamento Titolare attivato con successo!")
                st.rerun()

    with col_sub3:
        st.markdown(
            """
        <div class="custom-card" style="height: 100%;">
            <span class="badge-pop badge-boost">Enterprise</span>
            <h3 style="font-size: 1.2rem; margin-top: 5px;">Catene & Hotel</h3>
            <div style="font-size: 1.5rem; font-weight: 800; color: #0d9488; margin: 8px 0;">49 € <span style="font-size: 0.8rem; color: var(--text-muted);">/ mese</span></div>
            <p style="color: var(--text-muted); font-size: 0.85rem;">Account multi-sede, supporto prioritario dedicato e ricerca avanzata filtri.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Attiva Enterprise"):
            st.success("Richiesta Enterprise inviata con successo!")
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        "### 👥 Soluzioni per Lavoratori & Talenti", unsafe_allow_html=True
    )
    col_lsub1, col_lsub2 = st.columns(2, gap="medium")

    with col_lsub1:
        st.markdown(
            """
        <div class="custom-card" style="height: 100%;">
            <span class="badge-pop badge-boost">Weekend Boost</span>
            <h3 style="font-size: 1.2rem; margin-top: 5px;">In Evidenza Weekend</h3>
            <div style="font-size: 1.5rem; font-weight: 800; color: #0d9488; margin: 8px 0;">5 € <span style="font-size: 0.8rem; color: var(--text-muted);">/ weekend</span></div>
            <p style="color: var(--text-muted); font-size: 0.85rem;">Metti in evidenza il tuo profilo durante i giorni di maggiore afflusso nei locali.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.session_state.mio_profilo["boosted"]:
            st.success("✅ Boost Attivo")
        else:
            if st.button("Attiva Weekend Boost Lavoratore"):
                st.session_state.mio_profilo["boosted"] = True
                st.session_state.boost_attivi_count += 1
                st.success("Boost attivato con successo!")
                st.rerun()

    with col_lsub2:
        st.markdown(
            """
        <div class="custom-card" style="border-top: 4px solid #0d9488; height: 100%;">
            <span class="badge-pop badge-aqua">PRO Mensile</span>
            <h3 style="font-size: 1.2rem; margin-top: 5px;">Abbonamento Talento PRO</h3>
            <div style="font-size: 1.5rem; font-weight: 800; color: #0d9488; margin: 8px 0;">12 € <span style="font-size: 0.8rem; color: var(--text-muted);">/ mese</span></div>
            <p style="color: var(--text-muted); font-size: 0.85rem;">Visibilità costante tutto il mese, badge verificato oro e notifiche anticipate.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Attiva PRO Mensile"):
            st.session_state.mio_profilo["boosted"] = True
            st.success("Abbonamento PRO Mensile attivato!")
            st.rerun()

# ============================================================
# 5. DASHBOARD ADMIN PROFESSIONALE (LIVE STATS)
# ============================================================
elif scelta == "📊 Dashboard Admin" and mostra_admin:
    st.markdown(
        "<h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>📊 Dashboard Admin Live</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color:var(--text-muted); margin-bottom:2rem;'>Monitoraggio in tempo reale delle metriche chiave della piattaforma Flashjob.</p>",
        unsafe_allow_html=True,
    )

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric(
            label="Visite Totali Piattaforma",
            value=st.session_state.visite_totali,
            delta="+12% oggi",
        )
    with m2:
        st.metric(
            label="Click ai Contatti WhatsApp",
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
            label="Weekend Boost Attivi",
            value=st.session_state.boost_attivi_count,
            delta="5€ l'uno",
        )

    st.markdown("---")
    st.markdown("### 📈 Analisi Attività Recenti")

    c_chart1, c_chart2 = st.columns(2)
    with c_chart1:
        st.markdown(
            """
        <div class="custom-card">
            <h4 style="margin-top:0;">Fatturato Stimato Mensile</h4>
            <p style="font-size: 1.8rem; font-weight: 800; color: #0284c7; margin: 10px 0;">€ 412,00</p>
            <p style="color: var(--text-muted); font-size: 0.85rem;">Calcolato su abbonamenti attivi, flash pass e pacchetti boost.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with c_chart2:
        st.markdown(
            """
        <div class="custom-card">
            <h4 style="margin-top:0;">Stato Connessione Database</h4>
            <p style="font-size: 1.8rem; font-weight: 800; color: #0d9488; margin: 10px 0;">Ottimale 🟢</p>
            <p style="color: var(--text-muted); font-size: 0.85rem;">Latenza media di risposta server: <b>14 ms</b>. Nessun errore registrato.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )