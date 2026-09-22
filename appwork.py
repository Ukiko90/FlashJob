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
# STATO INIZIALE & TRACCIAMENTO DATI
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
    st.session_state.visite_totali = 1420

if "click_whatsapp" not in st.session_state:
    st.session_state.click_whatsapp = 348

if "sessione_contata" not in st.session_state:
    st.session_state.visite_totali += 1
    st.session_state.sessione_contata = True

if "mio_profilo" not in st.session_state:
    st.session_state.mio_profilo = {
        "id": 999,
        "nome": "Il Tuo Profilo",
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

if "nav_active" not in st.session_state:
    st.session_state.nav_active = "Panoramica"


def safe(value):
    return html.escape(str(value))


def whatsapp_url(phone):
    st.session_state.click_whatsapp += 1
    return "https://wa.me/" + re.sub(r"\D", "", phone)


# ============================================================
# DESIGN SYSTEM UNIFICATO (SFONDO SFUMATO ELEVATO & UI PULITA)
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --bg-app: #090d16;
    --bg-gradient: radial-gradient(circle at 50% 0%, #1e293b 0%, #090d16 100%);
    --surface: rgba(30, 41, 59, 0.7);
    --surface-solid: #131c2e;
    --surface-hover: rgba(51, 65, 85, 0.8);
    --border-subtle: rgba(255, 255, 255, 0.08);
    --border-hover: rgba(255, 255, 255, 0.2);
    --text-main: #f8fafc;
    --text-muted: #94a3b8;
    --brand-accent: #3b82f6;
    --brand-gradient: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
    --success: #10b981;
    --success-bg: rgba(16, 185, 129, 0.1);
    --radius-sm: 8px;
    --radius-md: 14px;
    --radius-lg: 20px;
    --shadow-card: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
    --transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

/* SFONDO GENERALE PROFONDO E NON PIATTO */
.stApp {
    background: var(--bg-app);
    background-image: var(--bg-gradient);
    color: var(--text-main);
    background-attachment: fixed;
}

.block-container {
    max-width: 1320px !important;
    padding: 2rem 2.5rem 6rem 2.5rem !important;
}

#MainMenu, footer, header {visibility: hidden; display: none;}
[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] {display: none !important;}

/* HEADER SUPERIORE GLASSMORPHISM */
.enterprise-header {
    background: rgba(19, 28, 46, 0.75);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-lg);
    padding: 1rem 1.75rem;
    margin-bottom: 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: var(--shadow-card);
    position: sticky;
    top: 1rem;
    z-index: 999;
}

.enterprise-logo {
    font-weight: 800;
    font-size: 1.25rem;
    letter-spacing: -0.03em;
    color: var(--text-main);
    display: flex;
    align-items: center;
    gap: 10px;
}

/* CARD PROFESSIONALI ELEVATE */
.enterprise-card {
    background: var(--surface);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-md);
    padding: 1.75rem;
    box-shadow: var(--shadow-card);
    transition: var(--transition);
    height: 100%;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.enterprise-card:hover {
    transform: translateY(-4px);
    border-color: var(--border-hover);
    background: var(--surface-hover);
}
.enterprise-card-highlight {
    border: 1.5px solid rgba(59, 130, 246, 0.5);
    background: rgba(30, 41, 59, 0.85);
}

/* BADGE DI STATO PULITI */
.badge-available {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 0.72rem;
    font-weight: 700;
    color: var(--success);
    background: var(--success-bg);
    padding: 4px 10px;
    border-radius: 6px;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    border: 1px solid rgba(16, 185, 129, 0.2);
}
.badge-offline {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 0.72rem;
    font-weight: 700;
    color: var(--text-muted);
    background: rgba(255, 255, 255, 0.04);
    padding: 4px 10px;
    border-radius: 6px;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    border: 1px solid var(--border-subtle);
}
.badge-top {
    background: var(--brand-gradient);
    color: white;
    font-size: 0.68rem;
    font-weight: 800;
    padding: 4px 10px;
    border-radius: 6px;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
}

/* OVERRIDE PULSANTI & INPUT STREAMLIT PER COERENZA TOTALE */
.stButton > button {
    width: 100%;
    min-height: 42px;
    border-radius: var(--radius-sm);
    background: rgba(255, 255, 255, 0.06);
    color: var(--text-main);
    font-weight: 600;
    font-size: 0.88rem;
    border: 1px solid var(--border-subtle);
    box-shadow: 0 2px 6px rgba(0,0,0,0.2);
    transition: var(--transition);
}
.stButton > button:hover {
    background: rgba(59, 130, 246, 0.2);
    border-color: var(--brand-accent);
    color: white;
    transform: translateY(-1px);
}
.stTextInput input, .stSelectbox select {
    background: rgba(19, 28, 46, 0.8) !important;
    border: 1px solid var(--border-subtle) !important;
    color: var(--text-main) !important;
    border-radius: var(--radius-sm) !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# HEADER PRINCIPALE
# ============================================================
st.markdown(
    """
<div class="enterprise-header">
    <div class="enterprise-logo">
        <span>⚡</span> FLASHJOB <span style="font-size: 0.72rem; font-weight: 700; background: rgba(59, 130, 246, 0.15); color: #60a5fa; padding: 4px 10px; border-radius: 6px; border: 1px solid rgba(59, 130, 246, 0.3);">ENTERPRISE B2B</span>
    </div>
    <div style="font-size: 0.85rem; font-weight: 600; color: var(--text-muted); display: flex; align-items: center; gap: 16px;">
        <span>Milano Hub Centrale</span>
        <span style="color: var(--success); display: flex; align-items: center; gap: 6px;">● Sistema Attivo</span>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# Sidebar per accesso Admin e simulazioni
with st.sidebar:
    st.markdown("### Configurazione")
    password_inserita = st.text_input(
        "Password Admin", type="password", key="input_pwd_admin"
    )
    mostra_admin = password_inserita == "admin123"

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

# Menu di navigazione pulito tramite bottoni orizzontali
menu_voci = [
    "Panoramica",
    "Database Talenti",
    "Area Lavoratori",
    "Area Aziende",
    "Piani",
]
if mostra_admin:
    menu_voci.append("📊 Admin")

cols_nav = st.len_cols = st.columns(len(menu_voci), gap="small")
for i, voce in enumerate(menu_voci):
    with cols_nav[i]:
        is_selected = st.session_state.nav_active == voce
        btn_style = (
            "background: var(--brand-accent); color: white; border-color: var(--brand-accent);"
            if is_selected
            else ""
        )
        if st.button(voce, key=f"nav_btn_{voce}"):
            st.session_state.nav_active = voce
            st.rerun()

scelta = st.session_state.nav_active
st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# 1. PANORAMICA
# ============================================================
if scelta == "Panoramica":
    st.markdown(
        """
        <div style="padding: 3rem 2.5rem; background: var(--surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); margin-bottom: 2rem; box-shadow: var(--shadow-card); position: relative; overflow: hidden; backdrop-filter: blur(12px);">
            <div style="position: absolute; right: -20px; bottom: -20px; font-size: 12rem; opacity: 0.02; font-weight: 800;">⚡</div>
            <span style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; color: #60a5fa; background: rgba(59, 130, 246, 0.15); padding: 5px 12px; border-radius: 6px; border: 1px solid rgba(59, 130, 246, 0.3);">Network Verificato Servizi & Corporate</span>
            <h1 style="font-size: 2.25rem; font-weight: 800; color: var(--text-main); margin: 14px 0 12px 0; letter-spacing: -0.03em; line-height: 1.15;">Il talento giusto.<br>Quando serve davvero.</h1>
            <p style="color: var(--text-muted); font-size: 1rem; margin-bottom: 0; max-width: 620px; line-height: 1.5;">Piattaforma B2B leader per il matching istantaneo tra aziende d'eccellenza e professionisti qualificati nel territorio di Milano.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    s1, s2, s3, s4 = st.columns(4, gap="medium")
    with s1:
        st.markdown(
            """
            <div class="enterprise-card" style="text-align: center; padding: 1.5rem;">
                <div style="font-size: 1.75rem; font-weight: 800; color: var(--text-main);">+1.420</div>
                <div style="font-size: 0.78rem; color: var(--text-muted); font-weight: 600; margin-top: 6px;">Professionisti</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
    with s2:
        st.markdown(
            """
            <div class="enterprise-card" style="text-align: center; padding: 1.5rem;">
                <div style="font-size: 1.75rem; font-weight: 800; color: var(--text-main);">+380</div>
                <div style="font-size: 0.78rem; color: var(--text-muted); font-weight: 600; margin-top: 6px;">Aziende Partner</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
    with s3:
        st.markdown(
            """
            <div class="enterprise-card" style="text-align: center; padding: 1.5rem;">
                <div style="font-size: 1.75rem; font-weight: 800; color: var(--success);">94%</div>
                <div style="font-size: 0.78rem; color: var(--text-muted); font-weight: 600; margin-top: 6px;">Disponibilità Media</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
    with s4:
        st.markdown(
            """
            <div class="enterprise-card" style="text-align: center; padding: 1.5rem;">
                <div style="font-size: 1.75rem; font-weight: 800; color: #60a5fa;">12h</div>
                <div style="font-size: 0.78rem; color: var(--text-muted); font-weight: 600; margin-top: 6px;">Tempo di Risposta</div>
            </div>
        """,
            unsafe_allow_html=True,
        )

# ============================================================
# 2. DATABASE TALENTI
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
        <div class="enterprise-card enterprise-card-highlight" style="margin-top: 15px; padding: 2.25rem;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
                <div>
                    <span style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; color: #60a5fa;">Dettaglio Profilo Verificato</span>
                    <h2 style="font-weight: 800; margin: 8px 0 4px 0; font-size: 1.75rem; color: var(--text-main);">{safe(selected_c["nome"])}</h2>
                    <p style="color: var(--text-muted); margin: 0; font-weight: 600; font-size: 0.95rem;">{safe(selected_c["mansione"])} • {safe(selected_c["zona"])}</p>
                </div>
                <div>{stato_badge}</div>
            </div>
            <p style="color: #60a5fa; font-weight: 600; font-size: 0.9rem; margin: 10px 0;">{safe(selected_c["recensioni"])}</p>
            <hr style="border: 0; border-top: 1px solid var(--border-subtle); margin: 20px 0;">
            <div style="margin-bottom: 15px;">
                <span style="font-size: 0.75rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase;">Competenze chiave:</span>
                <div style="display: flex; gap: 8px; margin-top: 8px; flex-wrap: wrap;">
        """,
            unsafe_allow_html=True,
        )

        for comp in selected_c.get("competenze", []):
            st.markdown(
                f'<span style="background: rgba(255,255,255,0.06); color: var(--text-main); font-size: 0.78rem; font-weight: 600; padding: 5px 10px; border-radius: 6px; border: 1px solid var(--border-subtle);">{safe(comp)}</span>',
                unsafe_allow_html=True,
            )

        st.markdown(
            f"""
                </div>
            </div>
            <p style="color: var(--text-muted); font-size: 0.9rem; margin: 0;"><b>Referenze:</b> {safe(selected_c["referenze"])}</p>
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
            "<h2 style='font-weight: 800; font-size: 1.4rem; margin-bottom: 4px;'>Database Talenti</h2>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='color: var(--text-muted); margin-bottom: 1.5rem; font-size: 0.9rem;'>Esplora i professionisti disponibili e filtra per ruolo, zona o competenze.</p>",
            unsafe_allow_html=True,
        )

        f_col1, f_col2, f_col3 = st.columns([2, 1, 1], gap="small")
        with f_col1:
            ricerca_testo = st.text_input(
                "Cerca",
                placeholder="Cerca ruolo o competenza...",
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
                boost_label = (
                    ' <span class="badge-top">Top</span>'
                    if lav.get("boosted")
                    else ""
                )

                with c_target:
                    st.markdown(
                        f"""
                    <div class="{card_class}" style="margin-bottom: 1rem; min-height: 190px;">
                        <div>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                                {badge_stato}
                                {boost_label}
                            </div>
                            <h3 style="margin: 0 0 6px 0; font-size: 1.1rem; font-weight: 700; color: var(--text-main);">{safe(lav["nome"])}</h3>
                            <p style="color: var(--text-muted); margin: 0 0 8px 0; font-size: 0.85rem; font-weight: 600;">{safe(lav["mansione"])} • {safe(lav["zona"])}</p>
                            <p style="color: var(--text-muted); font-size: 0.8rem; margin: 0;">{safe(lav["recensioni"])}</p>
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
        "<h2 style='font-weight: 800; font-size: 1.4rem; margin-bottom: 4px;'>Area Personale Lavoratore</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: var(--text-muted); margin-bottom: 1.5rem; font-size: 0.9rem;'>Gestisci in tempo reale la tua operatività e il piano di visibilità.</p>",
        unsafe_allow_html=True,
    )

    mio = st.session_state.mio_profilo

    st.markdown(
        """
        <div class="enterprise-card" style="margin-bottom: 1.5rem;">
            <h4 style="margin-top:0; font-size: 1rem; font-weight: 700;">Stato Operativo Live</h4>
            <p style="color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1rem;">Attiva lo stato per risultare visibile immediatamente alle aziende in cerca di supporto urgente.</p>
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
            <div>
                <span style="font-size: 0.72rem; font-weight: 700; color: var(--text-muted); background: rgba(255,255,255,0.06); padding: 4px 10px; border-radius: 6px;">Standard</span>
                <h4 style="margin: 10px 0 6px 0; font-size: 1rem; font-weight: 700;">Base Database</h4>
                <p style="color: var(--text-muted); font-size: 0.85rem; margin:0; line-height: 1.4;">Inserimento standard nel network senza priorità di posizionamento.</p>
            </div>
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
            <div>
                <span class="badge-top">Consigliato</span>
                <h4 style="margin: 10px 0 6px 0; font-size: 1rem; font-weight: 700;">Top Weekend Boost</h4>
                <p style="color: var(--text-muted); font-size: 0.85rem; margin:0; line-height: 1.4;">Posizionamento in vetta alle ricerche delle aziende per tutto il fine settimana.</p>
            </div>
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
        "<h2 style='font-weight: 800; font-size: 1.4rem; margin-bottom: 4px;'>Soluzioni per Aziende e Attività</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: var(--text-muted); margin-bottom: 1.5rem; font-size: 0.9rem;'>Ottimizza la ricerca di personale qualificato per strutture e corporate.</p>",
        unsafe_allow_html=True,
    )

    a1, a2 = st.columns(2, gap="medium")
    with a1:
        st.markdown(
            """
        <div class="enterprise-card">
            <h3 style="font-size: 1.1rem; font-weight: 700; margin-top:0;">Ricerca Veloce Turni</h3>
            <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.5;">Trova personale qualificato coperto da referenze verificate nel giro di poche ore.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
    with a2:
        st.markdown(
            """
        <div class="enterprise-card">
            <h3 style="font-size: 1.1rem; font-weight: 700; margin-top:0;">Abbonamento Dedicato</h3>
            <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.5;">Accedi direttamente ai contatti telefonici e gestisci team multipli con fatturazione centralizzata.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

# ============================================================
# 5. PIANI ABBONAMENTO
# ============================================================
elif scelta == "Piani":
    st.markdown(
        "<h2 style='font-weight: 800; font-size: 1.4rem; margin-bottom: 4px;'>Listino Piani & Abbonamenti</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: var(--text-muted); margin-bottom: 1.5rem; font-size: 0.9rem;'>Soluzioni commerciali strutturate per aziende e professionisti.</p>",
        unsafe_allow_html=True,
    )

    p1, p2 = st.columns(2, gap="medium")
    with p1:
        st.markdown(
            """
        <div class="enterprise-card">
            <div>
                <span style="font-size: 0.72rem; font-weight: 700; color: var(--text-muted); background: rgba(255,255,255,0.06); padding: 4px 10px; border-radius: 6px;">In arrivo</span>
                <h3 style="font-size: 1.15rem; font-weight: 700; margin: 12px 0 6px 0;">Abbonamento Aziende</h3>
                <div style="font-size: 1.5rem; font-weight: 800; color: var(--text-main); margin: 8px 0;">20 € <span style="font-size: 0.78rem; color: var(--text-muted); font-weight: 400;">/ mese</span></div>
                <p style="color: var(--text-muted); font-size: 0.88rem; margin: 0; line-height: 1.4;">Contatti diretti illimitati su WhatsApp e sblocco completo di tutti i profili del database.</p>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )
        st.info("Disponibile prossimamente.")

    with p2:
        st.markdown(
            """
        <div class="enterprise-card enterprise-card-highlight">
            <div>
                <span style="font-size: 0.72rem; font-weight: 700; color: #60a5fa; background: rgba(59, 130, 246, 0.15); padding: 4px 10px; border-radius: 6px; border: 1px solid rgba(59, 130, 246, 0.3);">In arrivo</span>
                <h3 style="font-size: 1.15rem; font-weight: 700; margin: 12px 0 6px 0;">PRO Talento</h3>
                <div style="font-size: 1.5rem; font-weight: 800; color: var(--text-main); margin: 8px 0;">12 € <span style="font-size: 0.78rem; color: var(--text-muted); font-weight: 400;">/ mese</span></div>
                <p style="color: var(--text-muted); font-size: 0.88rem; margin: 0; line-height: 1.4;">Visibilità prioritaria costante per l'intero mese e badge oro di qualifica verificata.</p>
            </div>
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
        "<h2 style='font-weight: 800; font-size: 1.4rem; margin-bottom: 4px;'>Dashboard Amministrativa</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: var(--text-muted); margin-bottom: 1.5rem; font-size: 0.9rem;'>Monitoraggio in tempo reale delle metriche di utilizzo e della piattaforma.</p>",
        unsafe_allow_html=True,
    )

    m1, m2 = st.columns(2, gap="medium")
    with m1:
        st.metric(
            label="Visite Totali Piattaforma",
            value=st.session_state.visite_totali,
            delta="+14% vs week prec.",
        )
    with m2:
        st.metric(
            label="Click diretti WhatsApp",
            value=st.session_state.click_whatsapp,
            delta="+8 oggi",
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """
    <div class="enterprise-card">
        <h4 style="margin-top:0; font-weight:700; font-size:1rem;">Stato Infrastruttura Cloud</h4>
        <p style="font-size: 1.25rem; font-weight: 800; color: var(--success); margin: 8px 0;">Operativo & Sincronizzato 🟢</p>
        <p style="color: var(--text-muted); font-size: 0.88rem; margin:0;">Design system corporativo avanzato e dark glassmorphism applicato con successo.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )