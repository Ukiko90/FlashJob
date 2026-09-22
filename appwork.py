import html
import re
import streamlit as st

st.set_page_config(
    page_title="Flashjob • Professional B2B Platform",
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
# DESIGN SYSTEM: STILE COMMERCIALE B2B PULITO E ORDINATO
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

:root {
    --bg-app: #f4f5f7;
    --surface-white: #ffffff;
    --border-color: #d1d5db;
    --border-light: #e5e7eb;
    --text-main: #111827;
    --text-muted: #4b5563;
    --brand-blue: #0f172a;
    --brand-accent: #007185;
    --brand-cta: #ffd814;
    --brand-cta-hover: #f7ca00;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

/* SFONDO PULITO E NEUTRO */
.stApp {
    background-color: var(--bg-app);
    color: var(--text-main);
}

/* CONTENITORE PRINCIPALE GRID */
.block-container {
    max-width: 1100px !important;
    padding: 2rem 1.5rem 5rem 1.5rem !important;
}

#MainMenu, footer, header {visibility: hidden; display: none;}
[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] {display: none !important;}

/* HEADER ISTITUZIONALE RIGOROSO */
.b2b-header {
    background: var(--surface-white);
    border: 1px solid var(--border-color);
    padding: 1.25rem 1.75rem;
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    margin-bottom: 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.b2b-title h1 {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-main);
    margin: 0;
    letter-spacing: -0.02em;
}
.b2b-title p {
    font-size: 0.8rem;
    color: var(--text-muted);
    margin: 2px 0 0 0;
    font-weight: 500;
}

/* NAVIGAZIONE A TABS ORIZZONTALI (STILE PIATTAFORMA) */
div[data-testid="stRadio"] > label { display: none; }
div[data-testid="stRadio"] div[role="radiogroup"] {
    display: flex;
    background: var(--surface-white);
    padding: 4px;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    margin-bottom: 2rem;
    gap: 4px;
}
div[data-testid="stRadio"] div[role="radiogroup"] label {
    border-radius: 6px;
    padding: 8px 16px;
    font-weight: 600;
    font-size: 0.85rem;
    color: var(--text-muted) !important;
    transition: background 0.15s ease;
}
div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
    background: var(--bg-app);
    color: var(--text-main) !important;
}
div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
    background: var(--brand-blue) !important;
    color: white !important;
}

/* CARD STRUTTURATE COMMERCIALI */
.b2b-card {
    background: var(--surface-white);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 1.25rem 1.5rem;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03);
    margin-bottom: 1rem;
}
.b2b-card-highlight {
    border: 2px solid var(--brand-accent);
    background: var(--surface-white);
}

/* BADGE & TAG RIGOROSI */
.b2b-tag {
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--brand-accent);
    background: #f0fdf4;
    padding: 3px 8px;
    border-radius: 4px;
    border: 1px solid #bbf7d0;
    display: inline-block;
    margin-bottom: 0.5rem;
}

/* PULSANTI STANDARD AZIENDALI */
.stButton > button {
    width: 100%;
    min-height: 40px;
    border-radius: 6px;
    background: #ffffff;
    color: var(--text-main);
    font-weight: 600;
    font-size: 0.85rem;
    border: 1px solid var(--border-color);
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    transition: background 0.15s ease;
}
.stButton > button:hover {
    background: #f3f4f6;
    border-color: #9ca3af;
    color: var(--text-main);
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# BARRA LATERALE
# ============================================================
with st.sidebar:
    st.markdown("### Controllo Rapido")

    if st.session_state.abbonamento_titolare:
        st.success("Titolare: ATTIVO")
        if st.button("Disattiva Account"):
            st.session_state.abbonamento_titolare = False
            st.rerun()
    else:
        st.warning("Titolare: FREE")
        if st.button("Simula Titolare"):
            st.session_state.abbonamento_titolare = True
            st.success("Attivato!")
            st.rerun()

    st.markdown("---")
    st.markdown("### Accesso Admin")
    password_inserita = st.text_input(
        "Password", type="password", key="input_pwd_admin"
    )
    mostra_admin = password_inserita == "admin123"
    if mostra_admin:
        st.success("Autorizzato")

# ============================================================
# HEADER PRINCIPALE
# ============================================================
st.markdown(
    """
<div class="b2b-header">
    <div class="b2b-title">
        <h1>Flashjob B2B</h1>
        <p>Curated Hospitality Network • Milano</p>
    </div>
    <div style="font-size: 0.85rem; font-weight: 600; color: var(--text-muted); background: #f3f4f6; padding: 6px 12px; border-radius: 6px; border: 1px solid var(--border-light);">Area Commerciale</div>
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
        <div style="margin-bottom: 2rem;">
            <span class="b2b-tag">Piattaforma Verificata</span>
            <h2 style="font-size: 1.35rem; font-weight: 700; color: var(--text-main); margin-top: 4px;">Gestione e matching professionale per il settore HORECA.</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2, gap="medium")
    with c1:
        st.markdown(
            """
        <div class="b2b-card">
            <h3 style="color: var(--text-main); margin-top: 0; font-size: 1rem; font-weight: 700;">Per le Aziende</h3>
            <p style="color: var(--text-muted); line-height: 1.4; font-size: 0.85rem; margin-bottom: 0;">
                Individua personale qualificato a Milano con disponibilità certificata, riducendo i tempi operativi di ricerca.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
        <div class="b2b-card">
            <h3 style="color: var(--text-main); margin-top: 0; font-size: 1rem; font-weight: 700;">Per i Talenti</h3>
            <p style="color: var(--text-muted); line-height: 1.4; font-size: 0.85rem; margin-bottom: 0;">
                Aggiorna il tuo stato operativo in tempo reale ed entra in contatto diretto con i locali partner della rete.
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
        if st.button("← Torna all'elenco"):
            st.session_state.selected_id = None
            st.rerun()

        stato_html = (
            '<b style="color:#059669; font-size:0.75rem;">● DISPONIBILE ORA</b>'
            if selected_c["disponibile"]
            else '<span style="color:#6b7280; font-size:0.75rem;">○ NON DISPONIBILE</span>'
        )

        st.markdown(
            f"""
        <div class="b2b-card b2b-card-highlight" style="margin-top: 10px;">
            <span class="b2b-tag">Scheda Professionista</span>
            <div style="margin-top: 4px; margin-bottom: 4px;">{stato_html}</div>
            <h2 style="font-weight: 700; margin: 0; font-size: 1.25rem; color: var(--text-main);">{safe(selected_c["nome"])}</h2>
            <p style="color: var(--text-muted); margin: 2px 0 4px 0; font-weight: 600; font-size: 0.85rem;">{safe(selected_c["mansione"])} • {safe(selected_c["zona"])}</p>
            <p style="color: var(--brand-accent); font-weight: 600; font-size: 0.85rem;">{safe(selected_c["recensioni"])}</p>
            <hr style="border: 0; border-top: 1px solid var(--border-light); margin: 10px 0;">
            <p style="color: var(--text-muted); font-size: 0.85rem; margin: 0;"><b>Referenze:</b> {safe(selected_c["referenze"])}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        if st.session_state.abbonamento_titolare:
            st.success("Contatto sbloccato con abbonamento Titolare attivo.")
            st.link_button(
                f"Apri Chat WhatsApp ({selected_c['tel']})",
                whatsapp_url(selected_c["tel"]),
                use_container_width=True,
            )
        else:
            st.warning("I contatti telefonici diretti richiedono un account Titolare.")
            if st.button("Sblocca Contatti (Simula Titolare)"):
                st.session_state.abbonamento_titolare = True
                st.rerun()

    else:
        st.markdown(
            "<h2 style='font-weight: 700; font-size: 1.25rem; margin-bottom: 2px;'>Database Talenti</h2>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='color: var(--text-muted); margin-bottom: 1.25rem; font-size: 0.85rem;'>Elenco verificato dei professionisti attivi.</p>",
            unsafe_allow_html=True,
        )

        lavoratori_ordinati = sorted(
            st.session_state.lavoratori, key=lambda x: not x.get("boosted", False)
        )

        for lav in lavoratori_ordinati:
            card_class = (
                "b2b-card b2b-card-highlight"
                if lav.get("boosted")
                else "b2b-card"
            )
            badge_stato = (
                '<b style="color:#059669; font-size:0.7rem;">● DISPONIBILE ORA</b>'
                if lav["disponibile"]
                else '<span style="color:#6b7280; font-size:0.7rem;">○ NON DISPONIBILE</span>'
            )
            boost_label = (
                ' <span style="background:#111827; color:white; padding:1px 6px; border-radius:3px; font-size:0.65rem; font-weight:600;">TOP</span>'
                if lav.get("boosted")
                else ""
            )

            st.markdown(
                f"""
            <div class="{card_class}" style="margin-bottom: 0.75rem; padding: 1rem 1.25rem;">
                <div style="margin-bottom: 2px;">{badge_stato}</div>
                <h3 style="margin: 0; font-size: 1rem; font-weight: 700; color: var(--text-main);">{safe(lav["nome"])}{boost_label}</h3>
                <p style="color: var(--text-muted); margin: 2px 0 0 0; font-size: 0.8rem; font-weight: 500;">{safe(lav["mansione"])} • {safe(lav["zona"])}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )
            if st.button("Visualizza profilo", key=f"btn_card_{lav['id']}"):
                st.session_state.selected_id = lav["id"]
                st.rerun()

# ============================================================
# 3. AREA LAVORATORE & WEEKEND BOOST
# ============================================================
elif scelta == "Area Lavoratore":
    st.markdown(
        "<h2 style='font-weight: 700; font-size: 1.25rem; margin-bottom: 2px;'>Area Personale</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: var(--text-muted); margin-bottom: 1.25rem; font-size: 0.85rem;'>Gestisci le preferenze di visibilità e disponibilità.</p>",
        unsafe_allow_html=True,
    )

    mio = st.session_state.mio_profilo

    nuova_disp = st.toggle(
        "Attiva disponibilità operativa", value=mio["disponibile"]
    )
    if mio["disponibile"] != nuova_disp:
        mio["disponibile"] = nuova_disp
        st.rerun()

    st.markdown("---")
    st.markdown("### Livello Visibilità")

    col_lp1, col_lp2 = st.columns(2, gap="small")
    with col_lp1:
        st.markdown(
            """
        <div class="b2b-card" style="height:100%;">
            <span class="b2b-tag" style="background:#f3f4f6; color:#4b5563; border-color:#d1d5db;">Base</span>
            <h4 style="margin: 4px 0; font-size: 0.9rem; font-weight: 700;">Standard</h4>
            <p style="color: var(--text-muted); font-size: 0.78rem; margin:0;">Inserimento nel database generale senza priorità.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Seleziona Standard"):
            mio["boosted"] = False
            st.success("Profilo impostato su piano Standard.")
            st.rerun()

    with col_lp2:
        st.markdown(
            """
        <div class="b2b-card b2b-card-highlight" style="height:100%;">
            <span class="b2b-tag">E优先</span>
            <h4 style="margin: 4px 0; font-size: 0.9rem; font-weight: 700;">Top Weekend</h4>
            <p style="color: var(--text-muted); font-size: 0.78rem; margin:0;">Priorità nelle ricerche dei locali per il fine settimana.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Attiva Top Weekend"):
            mio["boosted"] = True
            st.session_state.boost_attivi_count += 1
            st.success("Opzione Top Weekend attivata.")
            st.rerun()

# ============================================================
# 4. PIANI ABBONAMENTO (COMING SOON)
# ============================================================
elif scelta == "Piani (Coming Soon)":
    st.markdown(
        "<h2 style='font-weight: 700; font-size: 1.25rem; margin-bottom: 2px;'>Listino Piani</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: var(--text-muted); margin-bottom: 1.5rem; font-size: 0.85rem;'>Soluzioni commerciali in fase di attivazione.</p>",
        unsafe_allow_html=True,
    )

    st.markdown("### Per Locali & Aziende", unsafe_allow_html=True)
    st.markdown(
        """
    <div class="b2b-card">
        <span class="b2b-tag" style="background:#f3f4f6; color:#4b5563; border-color:#d1d5db;">In arrivo</span>
        <h3 style="font-size: 0.95rem; font-weight: 700; margin: 4px 0;">Abbonamento Mensile Titolari</h3>
        <div style="font-size: 1.15rem; font-weight: 700; color: var(--text-main); margin: 4px 0;">20 € <span style="font-size: 0.75rem; color: var(--text-muted); font-weight: 400;">/ mese</span></div>
        <p style="color: var(--text-muted); font-size: 0.8rem; margin:0;">Accesso illimitato ai contatti diretti dei professionisti.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.info("Disponibile prossimamente.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Per Lavoratori", unsafe_allow_html=True)
    st.markdown(
        """
    <div class="b2b-card b2b-card-highlight">
        <span class="b2b-tag" style="background:#f3f4f6; color:#4b5563; border-color:#d1d5db;">In arrivo</span>
        <h3 style="font-size: 0.95rem; font-weight: 700; margin: 4px 0;">PRO Talento</h3>
        <div style="font-size: 1.15rem; font-weight: 700; color: var(--text-main); margin: 4px 0;">12 € <span style="font-size: 0.75rem; color: var(--text-muted); font-weight: 400;">/ mese</span></div>
        <p style="color: var(--text-muted); font-size: 0.8rem; margin:0;">Visibilità estesa e badge di qualifica verificata.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.info("Disponibile prossimamente.")

# ============================================================
# 5. DASHBOARD ADMIN
# ============================================================
elif scelta == "📊 Admin" and mostra_admin:
    st.markdown(
        "<h2 style='font-weight: 700; font-size: 1.25rem; margin-bottom: 2px;'>Dashboard Admin</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: var(--text-muted); margin-bottom: 1.25rem; font-size: 0.85rem;'>Controllo metriche di utilizzo della piattaforma.</p>",
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
    <div class="b2b-card">
        <h4 style="margin-top:0; font-weight:700; font-size:0.9rem;">Stato Infrastruttura</h4>
        <p style="font-size: 1rem; font-weight: 700; color: #059669; margin: 4px 0;">Operativo & Sincronizzato</p>
        <p style="color: var(--text-muted); font-size: 0.8rem; margin:0;">Interfaccia aggiornata secondo le specifiche B2B commerciali.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )