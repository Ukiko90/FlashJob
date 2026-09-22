import html
import re
import streamlit as st

st.set_page_config(
    page_title="Flashjob • Mobile & Editorial Design",
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
# DESIGN SYSTEM OTTIMIZZATO PER MOBILE & SFONDO ASTRATTO
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Cinzel:wght@600;700&display=swap');

:root {
    --text-main: #1e293b;
    --text-muted: #64748b;
    --accent-teal: #0d9488;
    --border-glass: rgba(255, 255, 255, 0.7);
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* SFONDO ASTRATTO COLORATO E DELICATO */
.stApp {
    background: 
        radial-gradient(circle at 15% 15%, rgba(186, 230, 253, 0.6) 0%, transparent 45%),
        radial-gradient(circle at 85% 85%, rgba(153, 246, 228, 0.5) 0%, transparent 45%),
        radial-gradient(circle at 50% 50%, rgba(254, 240, 138, 0.3) 0%, transparent 55%),
        linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
    background-attachment: fixed;
    color: var(--text-main);
}

/* CONTENITORE PRINCIPALE ADATTIVO PER MOBILE */
.block-container {
    max-width: 1100px !important;
    padding: 1.5rem 1rem 5rem 1rem !important;
}

@media (min-width: 768px) {
    .block-container {
        padding: 2.5rem 2rem 6rem 2rem !important;
    }
}

#MainMenu, footer, header {visibility: hidden; display: none;}
[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] {display: none !important;}

/* HEADER EDITORIALE MOBILE-FRIENDLY */
.editorial-header {
    background: rgba(255, 255, 255, 0.88);
    backdrop-filter: blur(16px);
    border: 1px solid var(--border-glass);
    padding: 1.8rem 1.5rem;
    border-radius: 24px;
    box-shadow: 0 15px 35px rgba(13, 148, 136, 0.06);
    margin-bottom: 2rem;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    position: relative;
    overflow: hidden;
}
@media (min-width: 768px) {
    .editorial-header {
        padding: 2.5rem 2.5rem;
        border-radius: 30px;
    }
}
.editorial-header::before {
    content: '';
    position: absolute;
    top: 0; left: 0; width: 5px; height: 100%;
    background: linear-gradient(to bottom, #0284c7, #0d9488);
}
.editorial-title h1 {
    font-family: 'Cinzel', serif;
    font-size: 2.2rem;
    font-weight: 700;
    letter-spacing: -0.5px;
    color: #0f172a;
    margin: 0;
}
@media (min-width: 768px) {
    .editorial-title h1 {
        font-size: 2.8rem;
    }
}
.editorial-title p {
    font-size: 0.9rem;
    color: var(--text-muted);
    margin: 6px 0 0 0;
    font-weight: 500;
}
@media (min-width: 768px) {
    .editorial-title p {
        font-size: 1rem;
    }
}

/* NAVIGAZIONE RADIO STILE MAGAZINE FLUIDA */
div[data-testid="stRadio"] > label { display: none; }
div[data-testid="stRadio"] div[role="radiogroup"] {
    display: flex;
    justify-content: center;
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(12px);
    padding: 6px;
    border-radius: 25px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.03);
    margin-bottom: 2.5rem;
    gap: 4px;
    border: 1px solid var(--border-glass);
    flex-wrap: wrap;
}
div[data-testid="stRadio"] div[role="radiogroup"] label {
    border-radius: 20px;
    padding: 8px 14px;
    font-weight: 600;
    font-size: 0.8rem;
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
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.2);
}

/* BANNER & CARD EDITORIALI RESPONSIVE */
.editorial-banner {
    background: rgba(255, 255, 255, 0.88);
    backdrop-filter: blur(12px);
    border: 1px solid var(--border-glass);
    padding: 1.8rem 1.4rem;
    border-radius: 20px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.03);
    height: 100%;
    margin-bottom: 1rem;
    transition: all 0.3s ease;
}
.editorial-banner:hover {
    transform: translateY(-4px);
    background: rgba(255, 255, 255, 0.96);
    border-color: #99f6e4;
}

.editorial-tag {
    font-size: 0.65rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: #0d9488;
    background: #f0fdfa;
    padding: 5px 10px;
    border-radius: 15px;
    display: inline-block;
    margin-bottom: 0.8rem;
    border: 1px solid #ccfbf1;
}

.editorial-card {
    background: rgba(255, 255, 255, 0.88);
    backdrop-filter: blur(12px);
    border: 1px solid var(--border-glass);
    border-radius: 20px;
    padding: 1.5rem;
    box-shadow: 0 12px 30px rgba(0,0,0,0.03);
    margin-bottom: 1.2rem;
    transition: all 0.3s ease;
}
.editorial-card:hover {
    background: rgba(255, 255, 255, 0.96);
    border-color: #cbd5e1;
}
.editorial-card-highlight {
    background: linear-gradient(135deg, rgba(255,255,255,0.96) 0%, rgba(240,253,250,0.92) 100%);
    border: 2px solid #5eead4;
}

@keyframes pulse-animation {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(13, 148, 136, 0.7); }
    70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(13, 148, 136, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(13, 148, 136, 0); }
}
.pulsing-dot {
    display: inline-block;
    width: 9px; height: 9px;
    background-color: #0d9488;
    border-radius: 50%;
    animation: pulse-animation 1.5s infinite;
    margin-right: 6px;
    vertical-align: middle;
}
.offline-dot {
    display: inline-block;
    width: 9px; height: 9px;
    background-color: #cbd5e1;
    border-radius: 50%;
    margin-right: 6px;
    vertical-align: middle;
}

.stButton > button {
    width: 100%;
    min-height: 45px;
    border-radius: 12px;
    background: #0f172a;
    color: white;
    font-weight: 700;
    font-size: 0.9rem;
    border: none;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
    transition: all 0.25s ease;
}
.stButton > button:hover {
    background: #0d9488;
    transform: translateY(-2px);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# BARRA LATERALE COMPATTA
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
<div class="editorial-header">
    <div class="editorial-title">
        <h1>Flashjob.</h1>
        <p>Curated Hospitality Network • Milano</p>
    </div>
    <div style="font-size: 2rem; background: rgba(240,253,250,0.85); padding: 12px 18px; border-radius: 16px; border: 1px solid #ccfbf1;">⚡</div>
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
        <div style="text-align: center; max-width: 750px; margin: 0 auto 2.5rem auto;">
            <span class="editorial-tag">Editoriale & Visione</span>
            <h2 style='font-family: "Cinzel", serif; font-weight:700; font-size:1.9rem; color:#0f172a; margin-top:5px;'>Il punto d'incontro tra talenti HORECA e locali d'eccellenza.</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2, gap="medium")
    with c1:
        st.markdown(
            """
        <div class="editorial-card">
            <h3 style="color: #0d9488; margin-top: 0; font-size: 1.1rem; font-weight:700;">Chi Siamo</h3>
            <p style="color: var(--text-muted); line-height: 1.6; font-size: 0.9rem;">
                Professionisti della ristorazione e del digitale uniti per semplificare la ricerca di personale qualificato e dare valore ai lavoratori del settore.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
        <div class="editorial-card">
            <h3 style="color: #0284c7; margin-top: 0; font-size: 1.1rem; font-weight:700;">La Nostra Mission</h3>
            <p style="color: var(--text-muted); line-height: 1.6; font-size: 0.9rem;">
                Azzerare le distanze tramite geolocalizzazione smart e contatti diretti via WhatsApp, eliminando intermediazioni lente e farraginose.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown(
        "<h3 style='text-align: center; margin: 2.5rem 0 1.5rem 0; font-family: Cinzel, serif; font-weight: 700; font-size: 1.5rem;'>I Pilastri del Servizio</h3>",
        unsafe_allow_html=True,
    )

    b1, b2, b3 = st.columns(3, gap="small")
    with b1:
        st.markdown(
            """
        <div class="editorial-banner">
            <span class="editorial-tag">01 / Live</span>
            <h4 style="margin: 0 0 8px 0; font-size: 1rem; font-weight:700;">Disponibilità</h4>
            <p style="color: var(--text-muted); font-size: 0.82rem; line-height: 1.5; margin: 0;">
                Il pallino verde indica chi è pronto a lavorare adesso senza chiamate a vuoto.
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
            <h4 style="margin: 0 0 8px 0; font-size: 1rem; font-weight:700;">WhatsApp</h4>
            <p style="color: var(--text-muted); font-size: 0.82rem; line-height: 1.5; margin: 0;">
                Parla direttamente con il candidato in un singolo click dai piani dedicati.
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
            <h4 style="margin: 0 0 8px 0; font-size: 1rem; font-weight:700;">Visibilità</h4>
            <p style="color: var(--text-muted); font-size: 0.82rem; line-height: 1.5; margin: 0;">
                Potenzia il profilo nei giorni di maggiore afflusso per ottenere più offerte.
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
            '<span class="pulsing-dot"></span><b style="color:#0d9488; font-size:0.85rem;">DISPONIBILE ORA</b>'
            if selected_c["disponibile"]
            else '<span class="offline-dot"></span><span style="color:#888; font-size:0.85rem;">NON DISPONIBILE</span>'
        )

        st.markdown(
            f"""
        <div class="editorial-card editorial-card-highlight" style="margin-top: 10px;">
            <span class="editorial-tag">Profilo Selezionato</span>
            <div style="margin-top: 8px; margin-bottom: 6px;">{stato_html}</div>
            <h2 style="font-family: 'Cinzel', serif; margin:0; font-size:1.6rem; font-weight:700;">{safe(selected_c["nome"])}</h2>
            <p style="color:var(--text-muted); margin:4px 0 8px 0; font-weight:600; font-size:0.9rem;">{safe(selected_c["mansione"])} · {safe(selected_c["zona"])}</p>
            <p style="color:#0284c7; font-weight:700; font-size:0.9rem;">⭐ {safe(selected_c["recensioni"])}</p>
            <hr style="border:0; border-top:1px solid #ccfbf1; margin:12px 0;">
            <p style="color:#475569; font-size:0.9rem;"><b>Referenze:</b> {safe(selected_c["referenze"])}</p>
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
            "<h2 style='font-family: Cinzel, serif; font-weight:700; font-size:1.7rem;'>Database Talenti</h2>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='color:var(--text-muted); margin-bottom:1.5rem; font-size:0.9rem;'>Esplora i professionisti disponibili in tempo reale.</p>",
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
                '<span class="pulsing-dot"></span><b style="color:#0d9488; font-size:0.7rem;">DISPONIBILE ORA</b>'
                if lav["disponibile"]
                else '<span class="offline-dot"></span><span style="color:#888; font-size:0.7rem;">NON DISPONIBILE</span>'
            )
            boost_label = (
                ' <span style="background:#0f172a; color:white; padding:2px 8px; border-radius:15px; font-size:0.65rem; font-weight:700;">BOOSTED 🚀</span>'
                if lav.get("boosted")
                else ""
            )

            st.markdown(
                f"""
            <div class="{card_class}" style="margin-bottom:1rem; padding:1.2rem 1.4rem;">
                <div style="margin-bottom:4px;">{badge_stato}</div>
                <h3 style="margin:0; font-size:1.1rem; font-weight:700;">{safe(lav["nome"])}{boost_label}</h3>
                <p style="color:var(--text-muted); margin:4px 0 10px 0; font-size:0.85rem; font-weight:600;">{safe(lav["mansione"])} · {safe(lav["zona"])}</p>
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
        "<h2 style='font-family: Cinzel, serif; font-weight:700; font-size:1.7rem;'>Area Personale</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color:var(--text-muted); margin-bottom:1.5rem; font-size:0.9rem;'>Gestisci la tua disponibilità live e scegli il piano visibilità.</p>",
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
        <div class="editorial-card" style="height:100%;">
            <span class="editorial-tag">Free</span>
            <h4 style="margin:5px 0; font-size:1rem; font-weight:700;">Standard</h4>
            <p style="color:var(--text-muted); font-size:0.8rem;">Database generale senza priorità di ricerca.</p>
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
        <div class="editorial-card editorial-card-highlight" style="height:100%;">
            <span class="editorial-tag">Weekend</span>
            <h4 style="margin:5px 0; font-size:1rem; font-weight:700;">Top Weekend</h4>
            <p style="color:var(--text-muted); font-size:0.8rem;">In cima alle ricerche dei locali per tutto il fine settimana.</p>
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
        "<h2 style='font-family: Cinzel, serif; font-weight:700; font-size:1.7rem;'>Piani & Listino ⚡</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color:var(--text-muted); margin-bottom:2rem; font-size:0.9rem;'>Stiamo ultimando lo sviluppo. I piani saranno attivi a breve.</p>",
        unsafe_allow_html=True,
    )

    st.markdown("### 🏢 Per Locali & Aziende", unsafe_allow_html=True)
    st.markdown(
        """
    <div class="editorial-card" style="opacity: 0.85;">
        <span class="editorial-tag" style="background:#f1f5f9; color:#475569; border-color:#cbd5e1;">Coming Soon</span>
        <h3 style="font-size: 1.1rem; font-weight:700; margin: 5px 0;">Mensile Titolari & Pass</h3>
        <div style="font-size: 1.4rem; font-weight: 800; color: #0d9488; margin: 6px 0;">20 € <span style="font-size: 0.75rem; color: var(--text-muted);">/ mese</span></div>
        <p style="color: var(--text-muted); font-size: 0.82rem; margin:0;">Contatti diretti illimitati su WhatsApp per tutti i profili.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.info("🕒 Arriva tra poco")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 👥 Per Lavoratori", unsafe_allow_html=True)
    st.markdown(
        """
    <div class="editorial-card editorial-card-highlight" style="opacity: 0.85;">
        <span class="editorial-tag" style="background:#f1f5f9; color:#475569; border-color:#cbd5e1;">Coming Soon</span>
        <h3 style="font-size: 1.1rem; font-weight:700; margin: 5px 0;">Abbonamento PRO Talento</h3>
        <div style="font-size: 1.4rem; font-weight: 800; color: #0d9488; margin: 6px 0;">12 € <span style="font-size: 0.75rem; color: var(--text-muted);">/ mese</span></div>
        <p style="color: var(--text-muted); font-size: 0.82rem; margin:0;">Visibilità costante tutto il mese e badge verificato oro.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.info("🕒 Arriva tra poco")

# ============================================================
# 5. DASHBOARD ADMIN
# ============================================================
elif scelta == "📊 Admin" and mostra_admin:
    st.markdown(
        "<h2 style='font-family: Cinzel, serif; font-weight:700; font-size:1.7rem;'>📊 Dashboard Admin</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color:var(--text-muted); margin-bottom:1.5rem; font-size:0.9rem;'>Monitoraggio in tempo reale delle metriche.</p>",
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
    <div class="editorial-card">
        <h4 style="margin-top:0; font-weight:700; font-size:1rem;">Stato Sistema</h4>
        <p style="font-size: 1.3rem; font-weight: 800; color: #0d9488; margin: 6px 0;">Ottimale & Responsive 🟢</p>
        <p style="color: var(--text-muted); font-size: 0.82rem; margin:0;">Interfaccia mobile corretta e fluidità delle slide garantita.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )