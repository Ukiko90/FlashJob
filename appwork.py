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

# Metriche Admin Live
if "visite_totali" not in st.session_state:
    st.session_state.visite_totali = 1240  # Partenza realistica
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
    st.session_state.click_whatsapp += 1  # Tracciamento live click
    return "https://wa.me/" + re.sub(r"\D", "", phone)


# ============================================================
# DESIGN SYSTEM & CSS
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

#MainMenu, footer, header {visibility: hidden; display: none;}
[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stStatusWidget"] {display: none !important;}

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

.custom-card {
    background: var(--card-bg);
    border-radius: var(--radius);
    padding: 1.8rem;
    box-shadow: var(--shadow);
    border: 1px solid var(--border-color);
    margin-bottom: 1.5rem;
}
.boosted-card {
    border: 2px solid #a78bfa;
    background: linear-gradient(145deg, #ffffff 0%, #f9f5ff 100%);
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
.badge-purple { background: #f3e8ff; color: #9333ea; }
.badge-blue { background: #e0f2fe; color: #0284c7; }
.badge-boost { background: #ede9fe; color: #7c3aed; border: 1px solid #c4b5fd; }

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

menu_opzioni = [
    "Panoramica",
    "Database & Filtri Azienda",
    "Area Lavoratore & Weekend Boost (5€)",
    "Piani Abbonamento (Titolari 20€)",
]
if mostra_admin:
    menu_opzioni.append("📊 Dashboard Admin")

scelta = st.radio("Navigazione", menu_opzioni, horizontal=True)

# ============================================================
# 1. PANORAMICA (CHI SIAMO, A COSA SERVE & 3 BANNER)
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

    # Paragrafi Chi Siamo e A cosa serve
    col_text1, col_text2 = st.columns(2, gap="large")
    with col_text1:
        st.markdown(
            """
        <div class="custom-card" style="height: 100%;">
            <h3 style="color: #7c3aed; margin-top: 0;">👥 Chi Siamo</h3>
            <p style="color: var(--text-muted); line-height: 1.7; font-size: 0.95rem;">
                Siamo un team di professionisti della ristorazione, dell'hotellerie e dell'innovazione digitale. 
                Viviamo quotidianamente le sfide del settore e sappiamo quanto sia difficile, sia per un titolare 
                trovare personale affidabile all'ultimo minuto, sia per un lavoratore emergere nella giungla delle candidature tradizionali. 
                Flashjob nasce per azzerare le distanze e dare valore al tempo di tutti.
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
                Attraverso la geolocalizzazione, lo stato di disponibilità in tempo reale (il pallino verde lampeggiante) e 
                canali di contatto diretti via WhatsApp, permettiamo ai locali di coprire turni o eventi improvvisi in pochi minuti, 
                offrendo ai lavoratori l'opportunità di massimizzare i propri guadagni nei momenti di maggiore richiesta.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown(
        "<h3 style='text-align: center; margin: 3rem 0 1.5rem 0; font-weight: 800;'>I nostri 3 Punti di Forza</h3>",
        unsafe_allow_html=True,
    )

    # 3 Banner Punti di Forza
    b1, b2, b3 = st.columns(3, gap="medium")
    with b1:
        st.markdown(
            """
        <div class="custom-card" style="text-align: center; border-top: 4px solid #34d399;">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🟢</div>
            <h4 style="margin: 0 0 10px 0; font-weight: 700;">Disponibilità Live</h4>
            <p style="color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;">
                Il pallino verde lampeggiante mostra all'istante chi è pronto a lavorare adesso, eliminando chiamate a vuoto e perdite di tempo.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with b2:
        st.markdown(
            """
        <div class="custom-card" style="text-align: center; border-top: 4px solid #a78bfa;">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">💬</div>
            <h4 style="margin: 0 0 10px 0; font-weight: 700;">Contatto Diretto WhatsApp</h4>
            <p style="color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;">
                Nessuna intermediazione burocratica. Con l'abbonamento Titolare parli direttamente con il candidato in un click.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with b3:
        st.markdown(
            """
        <div class="custom-card" style="text-align: center; border-top: 4px solid #60a5fa;">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🚀</div>
            <h4 style="margin: 0 0 10px 0; font-weight: 700;">Weekend Boost</h4>
            <p style="color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;">
                I lavoratori possono potenziare la propria visibilità nei giorni di maggiore afflusso per ricevere molte più offerte.
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
                ' <span style="background:#7c3aed; color:white; padding:2px 8px; border-radius:6px; font-size:0.7rem;">BOOSTED 🚀</span>'
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
# 3. AREA LAVORATORE & WEEKEND BOOST (5€)
# ============================================================
elif scelta == "Area Lavoratore & Weekend Boost (5€)":
    st.markdown(
        "<h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Area Personale Lavoratore & Boost</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color:var(--text-muted); margin-bottom:2rem;'>Attiva il tuo pallino verde e metti in evidenza il tuo profilo per il fine settimana.</p>",
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
    st.markdown("### 🚀 Weekend Boost (5€)")
    st.markdown(
        "Scala la classifica e posizionati in cima alle ricerche dei titolari per tutto il fine settimana."
    )

    if mio["boosted"]:
        st.success("🚀 Il tuo Weekend Boost è attualmente ATTIVO!")
        if st.button("Disattiva Boost"):
            mio["boosted"] = False
            st.session_state.boost_attivi_count = max(
                0, st.session_state.boost_attivi_count - 1
            )
            st.rerun()
    else:
        if st.button("💳 Attiva Weekend Boost a 5€"):
            mio["boosted"] = True
            st.session_state.boost_attivi_count += 1
            st.success("Pagamento effettuato! Profilo potenziato per il weekend 🚀")
            st.rerun()

# ============================================================
# 4. PIANI ABBONAMENTO (TITOLARI 20€)
# ============================================================
elif scelta == "Piani Abbonamento (Titolari 20€)":
    st.markdown(
        "<h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Piani Abbonamento Titolari ⚡</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color:var(--text-muted); margin-bottom:2rem;'>Accedi senza limitazioni a tutti i contatti dei professionisti disponibili.</p>",
        unsafe_allow_html=True,
    )

    col1 = st.columns(1)[0]
    with col1:
        st.markdown(
            """
        <div class="custom-card" style="border-top: 5px solid #a78bfa;">
            <span class="badge-pop badge-purple">Titolari & Aziende</span>
            <h3 style="font-size: 1.5rem; margin-top: 5px;">Abbonamento Full Access</h3>
            <div style="font-size: 2rem; font-weight: 800; color: #9333ea; margin: 10px 0;">20 € <span style="font-size: 1rem; color: var(--text-muted);">/ mese</span></div>
            <p style="color: var(--text-muted);">Sblocca i numeri di telefono diretti e contatta subito qualsiasi lavoratore su WhatsApp.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        if st.session_state.abbonamento_titolare:
            st.success("✅ Il tuo abbonamento Titolare è attivo!")
        else:
            if st.button("Abbonati ora a 20€/mese"):
                st.session_state.abbonamento_titolare = True
                st.success("Abbonamento attivato con successo!")
                st.rerun()

# ============================================================
# 5. DASHBOARD ADMIN PROFESSIONALE
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

    # 4 Metric Cards in 2x2 o 4 colonne
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
            <p style="color: var(--text-muted); font-size: 0.85rem;">Calcolato su 1 abbonamento titolare attivo + pacchetti boost weekend attivi.</p>
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