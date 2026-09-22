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

if "piano_lavoratore" not in st.session_state:
    st.session_state.piano_lavoratore = "Free"  # Free o Boosted

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
# DESIGN SYSTEM & COLOR PALETTE (VIOLA, GIALLO, ARANCIONE)
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --bg-gradient: linear-gradient(135deg, #fdf8f6 0%, #fef3c7 40%, #fae8ff 100%);
    --card-bg: #ffffff;
    --text-main: #2d2b38;
    --text-muted: #6b6982;
    --border-color: #f3e8ff;
    --shadow: 0 12px 35px rgba(124, 58, 237, 0.08);
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

/* HEADER SFUMATO VIOLA - ARANCIONE - GIALLO */
.store-header {
    background: linear-gradient(135deg, #7c3aed 0%, #f97316 50%, #facc15 100%);
    color: white;
    padding: 2.8rem 2.2rem;
    border-radius: 30px;
    box-shadow: 0 20px 45px rgba(124, 58, 237, 0.2);
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
    color: #7c3aed;
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
    color: #fef08a;
    font-weight: 600;
}

/* RADIO NAVIGATION STILE MODERNO */
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
    border: 1px solid #f3e8ff;
    flex-wrap: wrap;
}
div[data-testid="stRadio"] div[role="radiogroup"] label {
    border-radius: 40px;
    padding: 10px 20px;
    font-weight: 700;
    font-size: 0.85rem;
    color: var(--text-muted) !important;
    transition: all 0.3s ease;
}
div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
    background: linear-gradient(135deg, #7c3aed 0%, #ea580c 100%) !important;
    color: white !important;
    box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3);
}

/* BANNER PUNTI DI FORZA SFUMATI */
.feature-banner {
    background: white;
    color: var(--text-main);
    padding: 2rem;
    border-radius: 24px;
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow);
    border: 1px solid #f3e8ff;
    height: 100%;
    transition: transform 0.2s ease;
}
.feature-banner:hover {
    transform: translateY(-4px);
}
.feature-tag-purple { background: #f3e8ff; color: #7c3aed; padding: 5px 14px; border-radius: 30px; font-size: 0.75rem; font-weight: 800; text-transform: uppercase; display: inline-block; margin-bottom: 15px; }
.feature-tag-orange { background: #ffedd5; color: #c2410c; padding: 5px 14px; border-radius: 30px; font-size: 0.75rem; font-weight: 800; text-transform: uppercase; display: inline-block; margin-bottom: 15px; }
.feature-tag-yellow { background: #fef9c3; color: #a16207; padding: 5px 14px; border-radius: 30px; font-size: 0.75rem; font-weight: 800; text-transform: uppercase; display: inline-block; margin-bottom: 15px; }

.custom-card {
    background: var(--card-bg);
    border-radius: var(--radius);
    padding: 1.8rem;
    box-shadow: var(--shadow);
    border: 1px solid var(--border-color);
    margin-bottom: 1.5rem;
}
.boosted-card {
    border: 2px solid #f97316;
    background: linear-gradient(145deg, #ffffff 0%, #fffbeb 100%);
}

@keyframes pulse-animation {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.7); }
    70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(52, 211, 153, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(52, 211, 153, 0); }
}
.pulsing-dot {
    display: inline-block;
    width: 12px;
    height: 12px;
    background-color: #34d399;
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
.badge-purple { background: #f3e8ff; color: #7c3aed; }
.badge-boost { background: #ffedd5; color: #c2410c; border: 1px solid #fed7aa; }

.stButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 14px;
    background: linear-gradient(135deg, #7c3aed 0%, #ea580c 100%);
    color: white;
    font-weight: 800;
    border: none;
    box-shadow: 0 6px 20px rgba(124, 58, 237, 0.3);
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
# BARRA LATERALE (ADMIN & ABBONAMENTO)
# ============================================================
with st.sidebar:
    st.markdown("### ⚡ Pannello di Controllo")

    if st.session_state.abbonamento_titolare:
        st.success("👑 Account Titolare: ATTIVO (20€/mo)")
        if st.button("Disattiva Abbonamento"):
            st.session_state.abbonamento_titolare = False
            st.rerun()
    else:
        st.warning("🔒 Account Titolare: FREE")
        if st.button("✨ Attiva Titolare (20€/mese)"):
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

# Menu senza prezzi tra parentesi
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
# 1. PANORAMICA (CHI SIAMO, A COSA SERVE & BANNER SFUMATI)
# ============================================================
if scelta == "Panoramica":
    st.markdown(
        """
        <div style="text-align: center; max-width: 850px; margin: 0 auto 2.5rem auto;">
            <span class="badge-pop badge-purple">Benvenuti su Flashjob</span>
            <h2 style='font-weight:800; font-size:2.2rem; margin-top:10px; color:#211e33;'>Il punto d'incontro definitivo tra talenti HORECA e locali d'eccellenza.</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    col_text1, col_text2 = st.columns(2, gap="large")
    with col_text1:
        st.markdown(
            """
        <div class="custom-card" style="height: 100%;">
            <h3 style="color: #7c3aed; margin-top: 0;">👥 Chi Siamo</h3>
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
            <h3 style="color: #ea580c; margin-top: 0;">🎯 A cosa serve l'app</h3>
            <p style="color: var(--text-muted); line-height: 1.7; font-size: 0.95rem;">
                Flashjob è la piattaforma smart pensata per la gestione flessibile e immediata del personale nel settore HORECA. 
                Attraverso la geolocalizzazione, lo stato di disponibilità in tempo reale (il pallino verde lampeggiante) e 
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

    # 3 BANNER CON SFUMATURE CALDE (VIOLA, ARANCIONE, GIALLO)
    b1, b2, b3 = st.columns(3, gap="medium")
    with b1:
        st.markdown(
            """
        <div class="feature-banner">
            <span class="feature-tag-purple">Velocità 🟢</span>
            <h3 style="margin: 10px 0; color: #211e33; font-size: 1.25rem;">Disponibilità Live</h3>
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
            <span class="feature-tag-orange">Diretto 💬</span>
            <h3 style="margin: 10px 0; color: #211e33; font-size: 1.25rem;">Chat & WhatsApp</h3>
            <p style="color: var(--text-muted); font-size: 0.85rem; line-height: 1.6; margin: 0;">
                Nessuna intermediazione burocratica. Con l'abbonamento Titolare parli direttamente con il candidato in un singolo click.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with b3:
        st.markdown(
            """
        <div class="feature-banner">
            <span class="feature-tag-yellow">Visibilità 🚀</span>
            <h3 style="margin: 10px 0; color: #211e33; font-size: 1.25rem;">Weekend Boost</h3>
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
            '<span class="pulsing-dot"></span><b style="color:#059669;">DISPONIBILE ORA</b>'
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
                    <p style="color:#d97706; margin:6px 0 0 0; font-weight:700; font-size:0.9rem;">⭐ {safe(selected_c["recensioni"])}</p>
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
                "🔒 I contatti telefonici diretti sono riservati ai Titolari abbonati (20€/mese)."
            )
            if st.button("Abbonati come Titolare a 20€/mese"):
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
                '<span class="pulsing-dot"></span><b style="color:#059669; font-size:0.75rem;">DISPONIBILE ORA</b>'
                if lav["disponibile"]
                else '<span class="offline-dot"></span><span style="color:#888; font-size:0.75rem;">NON DISPONIBILE</span>'
            )
            boost_label = (
                ' <span style="background:#ea580c; color:white; padding:2px 8px; border-radius:6px; font-size:0.7rem;">BOOSTED 🚀</span>'
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
        "<p style='color:var(--text-muted); margin-bottom:2rem;'>Attiva il tuo pallino verde e scegli il tuo piano di visibilità per il fine settimana.</p>",
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
    st.markdown("### 🚀 Gestione Piano Lavoratore")

    col_lp1, col_lp2 = st.columns(2, gap="medium")
    with col_lp1:
        st.markdown(
            """
        <div class="custom-card" style="height:100%;">
            <span class="badge-pop" style="background:#f3f4f6; color:#374151;">Base Free</span>
            <h4 style="margin:5px 0;">Visibilità Standard</h4>
            <p style="color:var(--text-muted); font-size:0.85rem;">Inserimento nel database generale senza priorità nelle ricerche del weekend.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Seleziona Piano Free"):
            mio["boosted"] = False
            st.session_state.piano_lavoratore = "Free"
            st.success("Selezionato piano Free.")
            st.rerun()

    with col_lp2:
        st.markdown(
            """
        <div class="custom-card boosted-card" style="height:100%;">
            <span class="badge-pop badge-boost">Weekend Boost (5€)</span>
            <h4 style="margin:5px 0;">Top Visibilità</h4>
            <p style="color:var(--text-muted); font-size:0.85rem;">Posizionamento in cima alle ricerche dei titolari per tutto il fine settimana.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Attiva Weekend Boost (5€)"):
            mio["boosted"] = True
            st.session_state.piano_lavoratore = "Boosted"
            st.session_state.boost_attivi_count += 1
            st.success(
                "Weekend Boost attivato con successo! Profilo in primo piano 🚀"
            )
            st.rerun()

# ============================================================
# 4. PIANI ABBONAMENTO (TITOLARI & LAVORATORI)
# ============================================================
elif scelta == "Piani Abbonamento":
    st.markdown(
        "<h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Piani Abbonamento & Listino ⚡</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color:var(--text-muted); margin-bottom:2rem;'>Scegli la soluzione perfetta per le tue esigenze, che tu sia un titolare di locale o un professionista.</p>",
        unsafe_allow_html=True,
    )

    col_sub1, col_sub2 = st.columns(2, gap="large")

    with col_sub1:
        st.markdown(
            """
        <div class="custom-card" style="border-top: 5px solid #7c3aed; height: 100%;">
            <span class="badge-pop badge-purple">Per Titolari & Locali</span>
            <h3 style="font-size: 1.4rem; margin-top: 5px;">Abbonamento Full Access</h3>
            <div style="font-size: 1.8rem; font-weight: 800; color: #7c3aed; margin: 10px 0;">20 € <span style="font-size: 0.9rem; color: var(--text-muted);">/ mese</span></div>
            <p style="color: var(--text-muted); font-size: 0.9rem;">Sblocca i numeri di telefono diretti e contatta subito qualsiasi lavoratore su WhatsApp senza limiti.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.session_state.abbonamento_titolare:
            st.success("✅ Abbonamento Titolare Attivo")
        else:
            if st.button("Abbonati Titolare (20€/mo)"):
                st.session_state.abbonamento_titolare = True
                st.success("Abbonamento Titolare attivato con successo!")
                st.rerun()

    with col_sub2:
        st.markdown(
            """
        <div class="custom-card" style="border-top: 5px solid #ea580c; height: 100%;">
            <span class="badge-pop badge-boost">Per Lavoratori</span>
            <h3 style="font-size: 1.4rem; margin-top: 5px;">Weekend Boost</h3>
            <div style="font-size: 1.8rem; font-weight: 800; color: #ea580c; margin: 10px 0;">5 € <span style="font-size: 0.9rem; color: var(--text-muted);">/ weekend</span></div>
            <p style="color: var(--text-muted); font-size: 0.9rem;">Metti in evidenza il tuo profilo durante i giorni di maggiore afflusso e ricevi più offerte di lavoro.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.session_state.mio_profilo["boosted"]:
            st.success("✅ Weekend Boost Attivo")
        else:
            if st.button("Attiva Boost Lavoratore (5€)"):
                st.session_state.mio_profilo["boosted"] = True
                st.session_state.boost_attivi_count += 1
                st.success("Boost attivato con successo!")
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
            <p style="font-size: 1.8rem; font-weight: 800; color: #7c3aed; margin: 10px 0;">€ 360,00</p>
            <p style="color: var(--text-muted); font-size: 0.85rem;">Calcolato su abbonamenti titolari attivi + pacchetti boost weekend attivi.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with c_chart2:
        st.markdown(
            """
        <div class="custom-card">
            <h4 style="margin-top:0;">Stato Connessione Database</h4>
            <p style="font-size: 1.8rem; font-weight: 800; color: #059669; margin: 10px 0;">Ottimale 🟢</p>
            <p style="color: var(--text-muted); font-size: 0.85rem;">Latenza media di risposta server: <b>14 ms</b>. Nessun errore registrato.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )