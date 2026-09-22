import html
import re
import streamlit as st

st.set_page_config(
    page_title="Flashjob • Professional B2B Enterprise Platform",
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
            "mansione": "Project Manager / Sala",
            "zona": "Milano Centro",
            "tel": "+39 333 1234567",
            "completati": 14,
            "disponibile": True,
            "boosted": True,
            "referenze": "Eccellente gestione dei team e coordinamento.",
            "recensioni": "4.9 ⭐ (12 recensioni verificate)",
            "competenze": ["Hospitality", "Events", "Management"],
        },
        {
            "id": 2,
            "nome": "Giulia Bianchi",
            "mansione": "Bartender / Mixologist",
            "zona": "Navigli / Ticinese",
            "tel": "+39 333 9876543",
            "completati": 22,
            "disponibile": True,
            "boosted": False,
            "referenze": "Velocità incredibile nei momenti di massimo afflusso.",
            "recensioni": "5.0 ⭐ (19 recensioni verificate)",
            "competenze": ["Mixology", "Beverage", "Cassa"],
        },
        {
            "id": 3,
            "nome": "Davide Moretti",
            "mansione": "Chef de Rang",
            "zona": "Porta Romana",
            "tel": "+39 333 4567890",
            "completati": 31,
            "disponibile": True,
            "boosted": True,
            "referenze": "Puntuale, preciso e con grande leadership in squadra.",
            "recensioni": "4.8 ⭐ (24 recensioni verificate)",
            "competenze": ["Coordinamento", "Lingua Inglese", "POS"],
        },
        {
            "id": 4,
            "nome": "Sara Neri",
            "mansione": "Event Manager",
            "zona": "Brera / Duomo",
            "tel": "+39 333 7654321",
            "completati": 19,
            "disponibile": False,
            "boosted": False,
            "referenze": "Ottima coordinazione di eventi corporate e catering.",
            "recensioni": "4.9 ⭐ (15 recensioni verificate)",
            "competenze": ["Events", "Problem Solving", "Management"],
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

if "sessione_contata" not in st.session_state:
    st.session_state.visite_totali += 1
    st.session_state.sessione_contata = True

if "mio_profilo" not in st.session_state:
    st.session_state.mio_profilo = {
        "id": 999,
        "nome": "Il Tuo Nome",
        "mansione": "Professionista / Sala",
        "zona": "Milano",
        "tel": "+39 333 0000000",
        "completati": 0,
        "disponibile": False,
        "boosted": False,
        "referenze": "Professionista verificato nel settore servizi.",
        "recensioni": "Nuovo utente",
        "competenze": ["Hospitality", "Management"],
    }


def safe(value):
    return html.escape(str(value))


def whatsapp_url(phone):
    st.session_state.click_whatsapp += 1
    return "https://wa.me/" + re.sub(r"\D", "", phone)


# ============================================================
# DESIGN SYSTEM ENTERPRISE (CSS AVANZATO & MICRO-INTERAZIONI)
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --bg-main: #f7f8fa;
    --surface: #ffffff;
    --border-subtle: #e5e7eb;
    --border-hover: #d1d5db;
    --text-main: #111827;
    --text-muted: #4b5563;
    --text-light: #9ca3af;
    --brand: #0f172a;
    --brand-accent: #2563eb;
    --success: #059669;
    --success-bg: #ecfdf5;
    --radius-sm: 6px;
    --radius-md: 10px;
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
    --transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

.stApp {
    background-color: var(--bg-main);
    color: var(--text-main);
}

.block-container {
    max-width: 1280px !important;
    padding: 1rem 2rem 5rem 2rem !important;
}

#MainMenu, footer, header {visibility: hidden; display: none;}
[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] {display: none !important;}

/* HEADER STICKY MODERNO */
.enterprise-header {
    background: rgba(255, 255, 255, 0.92);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border-subtle);
    padding: 0.75rem 1.5rem;
    border-radius: var(--radius-md);
    margin-bottom: 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: var(--shadow-sm);
    position: sticky;
    top: 0;
    z-index: 999;
}

.enterprise-logo {
    font-weight: 800;
    font-size: 1.2rem;
    letter-spacing: -0.03em;
    color: var(--brand);
    display: flex;
    align-items: center;
    gap: 6px;
}

/* NAVIGAZIONE A TABS STILE SAAS */
div[data-testid="stRadio"] > label { display: none; }
div[data-testid="stRadio"] div[role="radiogroup"] {
    display: flex;
    background: var(--surface);
    padding: 4px;
    border-radius: var(--radius-md);
    border: 1px solid var(--border-subtle);
    margin-bottom: 1.5rem;
    gap: 4px;
    box-shadow: var(--shadow-sm);
}
div[data-testid="stRadio"] div[role="radiogroup"] label {
    border-radius: var(--radius-sm);
    padding: 6px 16px;
    font-weight: 600;
    font-size: 0.82rem;
    color: var(--text-muted) !important;
    transition: var(--transition);
}
div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
    background: var(--bg-main);
    color: var(--text-main) !important;
}
div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
    background: var(--brand) !important;
    color: white !important;
    box-shadow: var(--shadow-sm);
}

/* CARD PROFESSIONALI CON MICRO-INTERAZIONI */
.enterprise-card {
    background: var(--surface);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-md);
    padding: 1.1rem 1.25rem;
    box-shadow: var(--shadow-sm);
    transition: var(--transition);
    height: 100%;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.enterprise-card:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
    border-color: var(--border-hover);
}
.enterprise-card-highlight {
    border: 1.5px solid var(--brand-accent);
}

/* BADGE DI STATO */
.badge-available {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 0.68rem;
    font-weight: 700;
    color: var(--success);
    background: var(--success-bg);
    padding: 2px 6px;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}
.badge-offline {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 0.68rem;
    font-weight: 700;
    color: var(--text-light);
    background: #f3f4f6;
    padding: 2px 6px;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}
.badge-top {
    background: var(--brand);
    color: white;
    font-size: 0.62rem;
    font-weight: 700;
    padding: 2px 5px;
    border-radius: 3px;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

/* BOTTONI STANDARD AZIENDALI */
.stButton > button {
    width: 100%;
    min-height: 36px;
    border-radius: var(--radius-sm);
    background: var(--surface);
    color: var(--text-main);
    font-weight: 600;
    font-size: 0.81rem;
    border: 1px solid var(--border-subtle);
    box-shadow: var(--shadow-sm);
    transition: var(--transition);
}
.stButton > button:hover {
    background: var(--bg-main);
    border-color: var(--border-hover);
    color: var(--text-main);
    transform: translateY(-1px);
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# HEADER PRINCIPALE MODERNO
# ============================================================
st.markdown(
    """
<div class="enterprise-header">
    <div class="enterprise-logo">
        <span>⚡</span> FLASHJOB <span style="font-size: 0.65rem; font-weight: 600; background: #e0f2fe; color: #0369a1; padding: 2px 5px; border-radius: 4px;">ENTERPRISE B2B</span>
    </div>
    <div style="font-size: 0.78rem; font-weight: 600; color: var(--text-muted); display: flex; align-items: center; gap: 12px;">
        <span>Milano Hub</span>
        <span style="color: var(--success);">● Live System</span>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

menu_opzioni = [
    "Panoramica",
    "Database Talenti",
    "Area Lavoratori",
    "Area Aziende",
    "Piani",
]

# Gestione password admin via sidebar
with st.sidebar:
    st.markdown("### Configurazione")
    password_inserita = st.text_input(
        "Password Admin", type="password", key="input_pwd_admin"
    )
    mostra_admin = password_inserita == "admin123"
    if mostra_admin:
        menu_opzioni.append("📊 Admin")
        st.success("Accesso Admin Sbloccato")

    st.markdown("---")
    if st.session_state.abbonamento_titolare:
        st.success("Stato Titolare: ATTIVO")
        if st.button("Disattiva Account"):
            st.session_state.abbonamento_titolare = False
            st.rerun()
    else:
        st.warning("Stato Titolare: FREE")
        if st.button("Simula Titolare"):
            st.session_state.abbonamento_titolare = True
            st.rerun()

scelta = st.radio("Navigazione", menu_opzioni, horizontal=True)

# ============================================================
# 1. PANORAMICA (HERO + STATISTICHE + BLOCCHI)
# ============================================================
if scelta == "Panoramica":
    st.markdown(
        """
        <div style="padding: 2.2rem 2rem; background: var(--surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); margin-bottom: 1.5rem; box-shadow: var(--shadow-sm);">
            <span style="font-size: 0.68rem; font-weight: 700; text-transform: uppercase; color: var(--brand-accent); background: #eff6ff; padding: 3px 8px; border-radius: 4px; border: 1px solid #dbeafe;">Network Verificato Servizi & Corporate</span>
            <h1 style="font-size: 1.85rem; font-weight: 800; color: var(--text-main); margin: 8px 0 6px 0; letter-spacing: -0.03em; line-height: 1.2;">Il talento giusto.<br>Quando serve.</h1>
            <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.25rem; max-width: 580px;">Piattaforma B2B leader per il matching istantaneo tra aziende d'eccellenza e professionisti qualificati a Milano.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    s1, s2, s3, s4 = st.columns(4, gap="small")
    with s1:
        st.markdown(
            """
            <div class="enterprise-card" style="text-align: center; padding: 0.85rem;">
                <div style="font-size: 1.3rem; font-weight: 800; color: var(--text-main);">+1.240</div>
                <div style="font-size: 0.72rem; color: var(--text-muted); font-weight: 600; margin-top: 2px;">Professionisti</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
    with s2:
        st.markdown(
            """
            <div class="enterprise-card" style="text-align: center; padding: 0.85rem;">
                <div style="font-size: 1.3rem; font-weight: 800; color: var(--text-main);">+380</div>
                <div style="font-size: 0.72rem; color: var(--text-muted); font-weight: 600; margin-top: 2px;">Aziende Partner</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
    with s3:
        st.markdown(
            """
            <div class="enterprise-card" style="text-align: center; padding: 0.85rem;">
                <div style="font-size: 1.3rem; font-weight: 800; color: var(--success);">92%</div>
                <div style="font-size: 0.72rem; color: var(--text-muted); font-weight: 600; margin-top: 2px;">Profili Disponibili</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
    with s4:
        st.markdown(
            """
            <div class="enterprise-card" style="text-align: center; padding: 0.85rem;">
                <div style="font-size: 1.3rem; font-weight: 800; color: var(--brand-accent);">24h</div>
                <div style="font-size: 0.72rem; color: var(--text-muted); font-weight: 600; margin-top: 2px;">Tempo Risposta</div>
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        "<h3 style='font-size: 1.1rem; font-weight: 700; margin-bottom: 0.85rem;'>Come funziona per le aziende</h3>",
        unsafe_allow_html=True,
    )
    b1, b2, b3 = st.columns(3, gap="medium")
    with b1:
        st.markdown(
            """
            <div class="enterprise-card">
                <div style="font-size: 0.72rem; font-weight: 800; color: var(--brand-accent); margin-bottom: 4px;">01</div>
                <h4 style="margin: 0 0 4px 0; font-size: 0.9rem; font-weight: 700;">Cerca</h4>
                <p style="color: var(--text-muted); font-size: 0.8rem; margin:0; line-height: 1.4;">Filtra per ruolo, zona di Milano e competenze verificate in tempo reale.</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
    with b2:
        st.markdown(
            """
            <div class="enterprise-card">
                <div style="font-size: 0.72rem; font-weight: 800; color: var(--brand-accent); margin-bottom: 4px;">02</div>
                <h4 style="margin: 0 0 4px 0; font-size: 0.9rem; font-weight: 700;">Seleziona</h4>
                <p style="color: var(--text-muted); font-size: 0.8rem; margin:0; line-height: 1.4;">Consulta recensioni certificate, referenze e storico dei servizi completati.</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
    with b3:
        st.markdown(
            """
            <div class="enterprise-card">
                <div style="font-size: 0.72rem; font-weight: 800; color: var(--brand-accent); margin-bottom: 4px;">03</div>
                <h4 style="margin: 0 0 4px 0; font-size: 0.9rem; font-weight: 700;">Contatta</h4>
                <p style="color: var(--text-muted); font-size: 0.8rem; margin:0; line-height: 1.4;">Avvia la chat diretta su WhatsApp con un singolo click per confermare il servizio.</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

# ============================================================
# 2. DATABASE TALENTI (GRIGLIA COMPATTA & FILTRI PROFESSIONALI)
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
        if st.button("← Torna all'elenco talenti"):
            st.session_state.selected_id = None
            st.rerun()

        stato_badge = (
            '<span class="badge-available">● Disponibile ora</span>'
            if selected_c["disponibile"]
            else '<span class="badge-offline">○ Non disponibile</span>'
        )

        st.markdown(
            f"""
        <div class="enterprise-card enterprise-card-highlight" style="margin-top: 10px; padding: 1.5rem;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 6px;">
                <div>
                    <span style="font-size: 0.68rem; font-weight: 700; text-transform: uppercase; color: var(--brand-accent);">Dettaglio Profilo Verificato</span>
                    <h2 style="font-weight: 800; margin: 4px 0 2px 0; font-size: 1.3rem; color: var(--text-main);">{safe(selected_c["nome"])}</h2>
                    <p style="color: var(--text-muted); margin: 0; font-weight: 600; font-size: 0.85rem;">{safe(selected_c["mansione"])} • {safe(selected_c["zona"])}</p>
                </div>
                <div>{stato_badge}</div>
            </div>
            <p style="color: var(--brand-accent); font-weight: 600; font-size: 0.82rem; margin: 6px 0;">{safe(selected_c["recensioni"])}</p>
            <hr style="border: 0; border-top: 1px solid var(--border-subtle); margin: 10px 0;">
            <div style="margin-bottom: 10px;">
                <span style="font-size: 0.72rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase;">Competenze chiave:</span>
                <div style="display: flex; gap: 6px; margin-top: 4px; flex-wrap: wrap;">
        """,
            unsafe_allow_html=True,
        )

        for comp in selected_c.get("competenze", []):
            st.markdown(
                f'<span style="background: #f3f4f6; color: var(--text-main); font-size: 0.72rem; font-weight: 600; padding: 2px 6px; border-radius: 4px;">{safe(comp)}</span>',
                unsafe_allow_html=True,
            )

        st.markdown(
            f"""
                </div>
            </div>
            <p style="color: var(--text-muted); font-size: 0.82rem; margin: 0;"><b>Referenze:</b> {safe(selected_c["referenze"])}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.session_state.abbonamento_titolare:
            st.success("Contatto sbloccato con abbonamento Titolare attivo.")
            st.link_button(
                f"💬 Apri Chat WhatsApp ({selected_c['tel']})",
                whatsapp_url(selected_c["tel"]),
                use_container_width=True,
            )
        else:
            st.warning(
                "🔒 I numeri di telefono diretti sono riservati agli account Titolari verificati."
            )
            if st.button("Sblocca Contatti (Simula Titolare)"):
                st.session_state.abbonamento_titolare = True
                st.rerun()

    else:
        st.markdown(
            "<h2 style='font-weight: 800; font-size: 1.2rem; margin-bottom: 2px;'>Database Talenti</h2>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='color: var(--text-muted); margin-bottom: 1rem; font-size: 0.82rem;'>Esplora i professionisti disponibili e filtra per ruolo, zona o competenze.</p>",
            unsafe_allow_html=True,
        )

        f_col1, f_col2, f_col3 = st.columns([2, 1, 1], gap="small")
        with f_col1:
            ricerca_testo = st.text_input(
                "Cerca",
                placeholder="Cerca ruolo o competenza (es. Manager, Bartender)...",
                label_visibility="collapsed",
            )
        with f_col2:
            filtro_zona = st.selectbox(
                "Zona",
                ["Tutte le zone", "Milano Centro", "Navigli", "Porta Romana"],
                label_visibility="collapsed",
            )
        with f_col3:
            filtro_stato = st.selectbox(
                "Disponibilità",
                ["Tutti", "Disponibili ora"],
                label_visibility="collapsed",
            )

        st.markdown(
            """
            <div style="display: flex; gap: 6px; margin: 10px 0 15px 0; flex-wrap: wrap; align-items: center;">
                <span style="font-size: 0.72rem; color: var(--text-muted); font-weight: 600;">Filtri rapidi:</span>
                <span style="background: #ffffff; border: 1px solid var(--border-subtle); padding: 2px 8px; border-radius: 4px; font-size: 0.72rem; font-weight: 600; cursor: pointer;">Chef</span>
                <span style="background: #ffffff; border: 1px solid var(--border-subtle); padding: 2px 8px; border-radius: 4px; font-size: 0.72rem; font-weight: 600; cursor: pointer;">Bartender</span>
                <span style="background: #ffffff; border: 1px solid var(--border-subtle); padding: 2px 8px; border-radius: 4px; font-size: 0.72rem; font-weight: 600; cursor: pointer;">Manager</span>
                <span style="background: #ffffff; border: 1px solid var(--border-subtle); padding: 2px 8px; border-radius: 4px; font-size: 0.72rem; font-weight: 600; cursor: pointer;">Hospitality</span>
            </div>
        """,
            unsafe_allow_html=True,
        )

        lavoratori_filtrati = []
        for lav in st.session_state.lavoratori:
            match_testo = (
                not ricerca_testo
                or ricerca_testo.lower() in lav["nome"].lower()
                or ricerca_testo.lower() in lav["mansione"].lower()
                or any(
                    ricerca_testo.lower() in c.lower()
                    for c in lav.get("competenze", [])
                )
            )
            match_zona = (
                filtro_zona == "Tutte le zone"
                or filtro_zona.lower() in lav["zona"].lower()
            )
            match_disp = (
                filtro_stato == "Tutti" or (filtro_stato == "Disponibili ora" and lav["disponibile"])
            )
            if match_testo and match_zona and match_disp:
                lavoratori_filtrati.append(lav)

        lavoratori_ordinati = sorted(
            lavoratori_filtrati, key=lambda x: not x.get("boosted", False)
        )

        if not lavoratori_ordinati:
            st.info(
                "Nessun professionista corrisponde ai filtri di ricerca selezionati."
            )
        else:
            cols = st.columns(3, gap="medium")
            for idx, lav in enumerate(lavoratori_ordinati):
                c_target = cols[idx % 3]
                card_class = (
                    "enterprise-card enterprise-card-highlight"
                    if lav.get("boosted")
                    else "enterprise-card"
                )
                badge_stato = (
                    '<span class="badge-available">● Disponibile ora</span>'
                    if lav["disponibile"]
                    else '<span class="badge-offline">○ Non disponibile</span>'
                )
                boost_label = ' <span class="badge-top">Top</span>' if lav.get("boosted") else ""

                with c_target:
                    # Contenitore unificato pulito per evitare scompaginamenti nella griglia
                    st.markdown(
                        f"""
                    <div class="{card_class}" style="margin-bottom: 1rem; min-height: 160px;">
                        <div>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                                {badge_stato}
                                {boost_label}
                            </div>
                            <h3 style="margin: 0 0 2px 0; font-size: 1rem; font-weight: 700; color: var(--text-main);">{safe(lav["nome"])}</h3>
                            <p style="color: var(--text-muted); margin: 0 0 6px 0; font-size: 0.78rem; font-weight: 600;">{safe(lav["mansione"])} • {safe(lav["zona"])}</p>
                            <p style="color: var(--text-muted); font-size: 0.75rem; margin: 0 0 8px 0;">{safe(lav["recensioni"])}</p>
                        </div>
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )
                    if st.button("Visualizza profilo", key=f"btn_card_{lav['id']}"):
                        st.session_state.selected_id = lav["id"]
                        st.rerun()

# ============================================================
# 3. AREA LAVORATORI
# ============================================================
elif scelta == "Area Lavoratori":
    st.markdown(
        "<h2 style='font-weight: 800; font-size: 1.2rem; margin-bottom: 2px;'>Area Personale Lavoratore</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: var(--text-muted); margin-bottom: 1.25rem; font-size: 0.82rem;'>Gestisci in tempo reale la tua operatività e il piano di visibilità.</p>",
        unsafe_allow_html=True,
    )

    mio = st.session_state.mio_profilo

    st.markdown(
        """
        <div class="enterprise-card" style="margin-bottom: 1.25rem;">
            <h4 style="margin-top:0; font-size: 0.9rem; font-weight: 700;">Stato Operativo Live</h4>
            <p style="color: var(--text-muted); font-size: 0.8rem; margin-bottom: 0.85rem;">Attiva lo stato per risultare visibile immediatamente alle aziende in cerca di supporto urgente.</p>
    """,
        unsafe_allow_html=True,
    )
    nuova_disp = st.toggle(
        "Attiva disponibilità immediata per i turni", value=mio["disponibile"]
    )
    if mio["disponibile"] != nuova_disp:
        mio["disponibile"] = nuova_disp
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### Livello Visibilità e Promozione")

    col_lp1, col_lp2 = st.columns(2, gap="medium")
    with col_lp1:
        st.markdown(
            """
        <div class="enterprise-card" style="height:100%;">
            <span style="font-size: 0.68rem; font-weight: 700; color: var(--text-muted); background: #f3f4f6; padding: 2px 6px; border-radius: 4px;">Standard</span>
            <h4 style="margin: 6px 0 4px 0; font-size: 0.9rem; font-weight: 700;">Base Database</h4>
            <p style="color: var(--text-muted); font-size: 0.78rem; margin:0; line-height: 1.4;">Inserimento standard nel network senza priorità di posizionamento.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Seleziona Standard"):
            mio["boosted"] = False
            st.success("Profilo impostato su piano Base.")
            st.rerun()

    with col_lp2:
        st.markdown(
            """
        <div class="enterprise-card enterprise-card-highlight" style="height:100%;">
            <span class="badge-top">Consigliato</span>
            <h4 style="margin: 6px 0 4px 0; font-size: 0.9rem; font-weight: 700;">Top Weekend Boost</h4>
            <p style="color: var(--text-muted); font-size: 0.78rem; margin:0; line-height: 1.4;">Posizionamento in vetta alle ricerche delle aziende per tutto il fine settimana.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Attiva Top Weekend"):
            mio["boosted"] = True
            st.success("Opzione Top Weekend attivata con successo 🚀")
            st.rerun()

# ============================================================
# 4. AREA AZIENDE
# ============================================================
elif scelta == "Area Aziende":
    st.markdown(
        "<h2 style='font-weight: 800; font-size: 1.2rem; margin-bottom: 2px;'>Soluzioni per Aziende e Attività</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: var(--text-muted); margin-bottom: 1.25rem; font-size: 0.82rem;'>Ottimizza la ricerca di personale qualificato per strutture e corporate.</p>",
        unsafe_allow_html=True,
    )

    a1, a2 = st.columns(2, gap="medium")
    with a1:
        st.markdown(
            """
        <div class="enterprise-card">
            <h3 style="font-size: 1rem; font-weight: 700; margin-top:0;">Ricerca Veloce Turni</h3>
            <p style="color: var(--text-muted); font-size: 0.8rem; line-height: 1.4;">Trova personale qualificato coperto da referenze verificate nel giro di poche ore.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
    with a2:
        st.markdown(
            """
        <div class="enterprise-card">
            <h3 style="font-size: 1rem; font-weight: 700; margin-top:0;">Abbonamento Dedicato</h3>
            <p style="color: var(--text-muted); font-size: 0.8rem; line-height: 1.4;">Accedi direttamente ai contatti telefonici e gestisci team multipli con fatturazione centralizzata.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

# ============================================================
# 5. PIANI ABBONAMENTO
# ============================================================
elif scelta == "Piani":
    st.markdown(
        "<h2 style='font-weight: 800; font-size: 1.2rem; margin-bottom: 2px;'>Listino Piani & Abbonamenti</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: var(--text-muted); margin-bottom: 1.25rem; font-size: 0.82rem;'>Soluzioni commerciali strutturate per aziende e professionisti.</p>",
        unsafe_allow_html=True,
    )

    p1, p2 = st.columns(2, gap="medium")
    with p1:
        st.markdown(
            """
        <div class="enterprise-card">
            <span style="font-size: 0.68rem; font-weight: 700; color: var(--text-muted); background: #f3f4f6; padding: 2px 6px; border-radius: 4px;">In arrivo</span>
            <h3 style="font-size: 1rem; font-weight: 700; margin: 8px 0 2px 0;">Abbonamento Aziende</h3>
            <div style="font-size: 1.25rem; font-weight: 800; color: var(--text-main); margin: 6px 0;">20 € <span style="font-size: 0.72rem; color: var(--text-muted); font-weight: 400;">/ mese</span></div>
            <p style="color: var(--text-muted); font-size: 0.8rem; margin: 0; line-height: 1.4;">Contatti diretti illimitati su WhatsApp e sblocco completo di tutti i profili del database.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        st.info("Disponibile prossimamente.")

    with p2:
        st.markdown(
            """
        <div class="enterprise-card enterprise-card-highlight">
            <span style="font-size: 0.68rem; font-weight: 700; color: var(--brand-accent); background: #eff6ff; padding: 2px 6px; border-radius: 4px;">In arrivo</span>
            <h3 style="font-size: 1rem; font-weight: 700; margin: 8px 0 2px 0;">PRO Talento</h3>
            <div style="font-size: 1.25rem; font-weight: 800; color: var(--text-main); margin: 6px 0;">12 € <span style="font-size: 0.72rem; color: var(--text-muted); font-weight: 400;">/ mese</span></div>
            <p style="color: var(--text-muted); font-size: 0.8rem; margin: 0; line-height: 1.4;">Visibilità prioritaria costante per l'intero mese e badge oro di qualifica verificata.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        st.info("Disponibile prossimamente.")

# ============================================================
# 6. DASHBOARD ADMIN
# ============================================================
elif scelta == "📊 Admin" and mostra_admin:
    st.markdown(
        "<h2 style='font-weight: 800; font-size: 1.2rem; margin-bottom: 2px;'>Dashboard Amministrativa</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: var(--text-muted); margin-bottom: 1.25rem; font-size: 0.82rem;'>Monitoraggio in tempo reale delle metriche di utilizzo e della piattaforma.</p>",
        unsafe_allow_html=True,
    )

    m1, m2 = st.columns(2, gap="medium")
    with m1:
        st.metric(
            label="Visite Totali Piattaforma",
            value=st.session_state.visite_totali,
            delta="+12% vs week prec.",
        )
    with m2:
        st.metric(
            label="Click diretti WhatsApp",
            value=st.session_state.click_whatsapp,
            delta="+5 oggi",
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """
    <div class="enterprise-card">
        <h4 style="margin-top:0; font-weight:700; font-size:0.9rem;">Stato Infrastruttura Cloud</h4>
        <p style="font-size: 1.05rem; font-weight: 800; color: var(--success); margin: 4px 0;">Operativo & Sincronizzato 🟢</p>
        <p style="color: var(--text-muted); font-size: 0.8rem; margin:0;">Design system enterprise B2B applicato uniformemente a tutte le sezioni.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )