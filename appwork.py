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
# DESIGN SYSTEM: SFONDO CELESTE SFUMATO VERDE CHIARO ABSTRACT
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

:root {
    --bg-app: linear-gradient(135deg, #e0f2fe 0%, #f0fdf4 50%, #e0e7ff 100%);
    --surface: rgba(255, 255, 255, 0.85);
    --surface-hover: rgba(255, 255, 255, 0.95);
    --border-subtle: rgba(148, 163, 184, 0.25);
    --border-hover: rgba(37, 99, 235, 0.4);
    --text-main: #0f172a;
    --text-muted: #475569;
    --brand-accent: #2563eb;
    --success: #059669;
    --success-bg: #d1fae5;
    --radius-sm: 8px;
    --radius-md: 14px;
    --radius-lg: 20px;
    --shadow-card: 0 10px 25px -5px rgba(15, 23, 42, 0.05), 0 8px 10px -6px rgba(15, 23, 42, 0.05);
    --transition: all 0.2s ease-in-out;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

.stApp {
    background: var(--bg-app);
    background-attachment: fixed;
    color: var(--text-main);
}

.block-container {
    max-width: 1300px !important;
    padding: 2rem 2rem 5rem 2rem !important;
}

#MainMenu, footer, header {visibility: hidden; display: none;}
[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] {display: none !important;}

/* HEADER GLASSMORPHISM MODERNO */
.enterprise-header {
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
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
    font-weight: 700;
    font-size: 1.15rem;
    letter-spacing: -0.02em;
    color: var(--text-main);
    display: flex;
    align-items: center;
    gap: 8px;
}

/* CARD PULITE ED ELEGANTI */
.enterprise-card {
    background: var(--surface);
    backdrop-filter: blur(8px);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-md);
    padding: 1.5rem;
    box-shadow: var(--shadow-card);
    transition: var(--transition);
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.enterprise-card:hover {
    border-color: var(--border-hover);
    background: var(--surface-hover);
    transform: translateY(-2px);
}
.enterprise-card-highlight {
    border: 1.5px solid var(--brand-accent);
    background: rgba(239, 246, 255, 0.9);
}

/* BADGE DI STATO */
.badge-available {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 0.7rem;
    font-weight: 700;
    color: var(--success);
    background: var(--success-bg);
    padding: 3px 8px;
    border-radius: 6px;
    text-transform: uppercase;
    border: 1px solid #6ee7b7;
}
.badge-offline {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 0.7rem;
    font-weight: 700;
    color: var(--text-muted);
    background: rgba(226, 232, 240, 0.6);
    padding: 3px 8px;
    border-radius: 6px;
    text-transform: uppercase;
    border: 1px solid var(--border-subtle);
}
.badge-top {
    background: var(--brand-accent);
    color: white;
    font-size: 0.65rem;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 6px;
    text-transform: uppercase;
}

/* STREAMLIT COMPONENTS OVERRIDE */
.stButton > button {
    width: 100%;
    min-height: 40px;
    border-radius: var(--radius-sm);
    background: rgba(255, 255, 255, 0.9);
    color: var(--text-main);
    font-weight: 600;
    font-size: 0.85rem;
    border: 1px solid var(--border-subtle);
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    transition: var(--transition);
}
.stButton > button:hover {
    background: #ffffff;
    border-color: var(--brand-accent);
    color: var(--brand-accent);
}
.stTextInput input, .stSelectbox select {
    background: rgba(255, 255, 255, 0.9) !important;
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
        <span>⚡</span> FLASHJOB <span style="font-size: 0.68rem; font-weight: 600; background: #dbeafe; color: #1e40af; padding: 2px 8px; border-radius: 6px;">B2B PLATFORM</span>
    </div>
    <div style="font-size: 0.82rem; font-weight: 600; color: var(--text-muted); display: flex; align-items: center; gap: 14px;">
        <span>Milano Hub</span>
        <span style="color: var(--success); display: flex; align-items: center; gap: 5px;">● Online</span>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# Configurazione laterale (Admin)
with st.sidebar:
    st.markdown("### Configurazione")
    password_inserita = st.text_input(
        "Password Admin", type="password", key="input_pwd_admin"
    )
    mostra_admin = password_inserita == "admin123"

    st.markdown("---")
    if st.session_state.abbonamento_titolare:
        st.success("Titolare: ATTIVO")
        if st.button("Disattiva Account"):
            st.session_state.abbonamento_titolare = False
            st.rerun()
    else:
        st.warning("Titolare: FREE")
        if st.button("Simula Titolare"):
            st.session_state.abbonamento_titolare = True
            st.rerun()

# Menu di navigazione pulito
menu_voci = [
    "Panoramica",
    "Database Talenti",
    "Area Lavoratori",
    "Area Aziende",
    "Piani",
]
if mostra_admin:
    menu_voci.append("📊 Admin")

cols_nav = st.columns(len(menu_voci), gap="small")
for i, voce in enumerate(menu_voci):
    with cols_nav[i]:
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
        <div style="padding: 2.5rem; background: var(--surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); margin-bottom: 2rem; box-shadow: var(--shadow-card); backdrop-filter: blur(8px);">
            <span style="font-size: 0.7rem; font-weight: 700; text-transform: uppercase; color: var(--brand-accent); background: #dbeafe; padding: 4px 10px; border-radius: 6px;">Network Verificato Servizi & Corporate</span>
            <h1 style="font-size: 2rem; font-weight: 700; color: var(--text-main); margin: 12px 0 10px 0; letter-spacing: -0.02em; line-height: 1.2;">Il talento giusto.<br>Quando serve davvero.</h1>
            <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 0; max-width: 600px; line-height: 1.5;">Piattaforma B2B leader per il matching istantaneo tra aziende d'eccellenza e professionisti qualificati nel territorio di Milano.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    s1, s2, s3, s4 = st.columns(4, gap="medium")
    with s1:
        st.markdown(
            """
            <div class="enterprise-card" style="text-align: center; padding: 1.25rem;">
                <div style="font-size: 1.5rem; font-weight: 700; color: var(--text-main);">+1.420</div>
                <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 600; margin-top: 4px;">Professionisti</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
    with s2:
        st.markdown(
            """
            <div class="enterprise-card" style="text-align: center; padding: 1.25rem;">
                <div style="font-size: 1.5rem; font-weight: 700; color: var(--text-main);">+380</div>
                <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 600; margin-top: 4px;">Aziende Partner</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
    with s3:
        st.markdown(
            """
            <div class="enterprise-card" style="text-align: center; padding: 1.25rem;">
                <div style="font-size: 1.5rem; font-weight: 700; color: var(--success);">94%</div>
                <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 600; margin-top: 4px;">Disponibilità Media</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
    with s4:
        st.markdown(
            """
            <div class="enterprise-card" style="text-align: center; padding: 1.25rem;">
                <div style="font-size: 1.5rem; font-weight: 700; color: var(--brand-accent);">12h</div>
                <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 600; margin-top: 4px;">Tempo di Risposta</div>
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
        <div class="enterprise-card enterprise-card-highlight" style="margin-top: 10px; padding: 2rem;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 10px;">
                <div>
                    <span style="font-size: 0.7rem; font-weight: 700; text-transform: uppercase; color: var(--brand-accent);">Dettaglio Profilo Verificato</span>
                    <h2 style="font-weight: 700; margin: 6px 0 4px 0; font-size: 1.5rem; color: var(--text-main);">{safe(selected_c["nome"])}</h2>
                    <p style="color: var(--text-muted); margin: 0; font-weight: 600; font-size: 0.9rem;">{safe(selected_c["mansione"])} • {safe(selected_c["zona"])}</p>
                </div>
                <div>{stato_badge}</div>
            </div>
            <p style="color: var(--brand-accent); font-weight: 600; font-size: 0.85rem; margin: 8px 0;">{safe(selected_c["recensioni"])}</p>
            <hr style="border: 0; border-top: 1px solid var(--border-subtle); margin: 15px 0;">
            <div style="margin-bottom: 12px;">
                <span style="font-size: 0.72rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase;">Competenze chiave:</span>
                <div style="display: flex; gap: 6px; margin-top: 6px; flex-wrap: wrap;">
        """,
            unsafe_allow_html=True,
        )

        for comp in selected_c.get("competenze", []):
            st.markdown(
                f'<span style="background: rgba(255,255,255,0.8); color: var(--text-main); font-size: 0.75rem; font-weight: 600; padding: 4px 8px; border-radius: 6px; border: 1px solid var(--border-subtle);">{safe(comp)}</span>',
                unsafe_allow_html=True,
            )

        st.markdown(
            f"""
                </div>
            </div>
            <p style="color: var(--text-muted); font-size: 0.88rem; margin: 0;"><b>Referenze:</b> {safe(selected_c["referenze"])}</p>
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
            "<h2 style='font-weight: 700; font-size: 1.3rem; margin-bottom: 4px;'>Database Talenti</h2>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='color: var(--text-muted); margin-bottom: 1.25rem; font-size: 0.88rem;'>Esplora i professionisti disponibili e filtra per ruolo, zona o competenze.</p>",
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
                    <div class="{card_class}" style="margin-bottom: 0.75rem; min-height: 180px;">
                        <div>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                                {badge_stato}
                                {boost_label}
                            </div>
                            <h3 style="margin: 0 0 4px 0; font-size: 1.05rem; font-weight: 700; color: var(--text-main);">{safe(lav["nome"])}</h3>
                            <p style="color: var(--text-muted); margin: 0 0 6px 0; font-size: 0.82rem; font-weight: 600;">{safe(lav["mansione"])} • {safe(lav["zona"])}</p>
                            <p style="color: var(--text-muted); font-size: 0.78rem; margin: 0;">{safe(lav["recensioni"])}</p>
                        </div>
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )
                    if st.button("Visualizza profilo", key=f"btn_card_{lav['id']}"):
                        st.session_state.selected_id = lav["id"]
                        st.rerun()

# ============================================================
# 3. AREA LAVORATORI (MODIFICA PROFILO INTEGRATA)
# ============================================================
elif scelta == "Area Lavoratori":
    st.markdown(
        "<h2 style='font-weight: 700; font-size: 1.3rem; margin-bottom: 4px;'>Area Personale Lavoratore</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: var(--text-muted); margin-bottom: 1.25rem; font-size: 0.88rem;'>Gestisci in tempo reale la tua operatività, il piano di visibilità e modifica i dati del tuo profilo.</p>",
        unsafe_allow_html=True,
    )

    mio = st.session_state.mio_profilo

    # Sezione Modifica Profilo Personale
    st.markdown(
        """
        <div class="enterprise-card" style="margin-bottom: 1.25rem;">
            <h4 style="margin-top:0; font-size: 0.95rem; font-weight: 700;">Modifica Informazioni Profilo</h4>
            <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 1rem;">Aggiorna i tuoi dati visibili nel network B2B.</p>
    """,
        unsafe_allow_html=True,
    )

    with st.form(key="form_modifica_profilo"):
        col_m1, col_m2 = st.columns(2, gap="medium")
        with col_m1:
            nuovo_nome = st.text_input("Nome e Cognome", value=mio["nome"])
            nuova_mansione = st.text_input("Mansione / Ruolo", value=mio["mansione"])
        with col_m2:
            nuova_zona = st.text_input("Zona / Quartiere", value=mio["zona"])
            nuovo_tel = st.text_input("Telefono", value=mio["tel"])
        
        nuove_referenze = st.text_area("Referenze / Descrizione", value=mio["referenze"])
        
        submit_modifica = st.form_submit_button("Salva Modifiche Profilo")
        if submit_modifica:
            mio["nome"] = nuovo_nome
            mio["mansione"] = nuova_mansione
            mio["zona"] = nuova_zona
            mio["tel"] = nuovo_tel
            mio["referenze"] = nuove_referenze
            st.success("Modifiche salvate con successo!")
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="enterprise-card" style="margin-bottom: 1.25rem;">
            <h4 style="margin-top:0; font-size: 0.95rem; font-weight: 700;">Stato Operativo Live</h4>
            <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 0.75rem;">Attiva lo stato per risultare visibile immediatamente alle aziende in cerca di supporto urgente.</p>
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

    st.markdown(
        "<h3 style='font-size: 1.1rem; font-weight: 700;'>Livello Visibilità e Promozione</h3>",
        unsafe_allow_html=True,
    )
    col_lp1, col_lp2 = st.columns(2, gap="medium")
    with col_lp1:
        st.markdown(
            """
        <div class="enterprise-card" style="height:100%;">
            <div>
                <span style="font-size: 0.7rem; font-weight: 600; color: var(--text-muted); background: rgba(226, 232, 240, 0.6); padding: 3px 8px; border-radius: 6px;">Standard</span>
                <h4 style="margin: 8px 0 6px 0; font-size: 0.95rem; font-weight: 700;">Base Database</h4>
                <p style="color: var(--text-muted); font-size: 0.82rem; margin:0; line-height: 1.4;">Inserimento standard nel network senza priorità di posizionamento.</p>
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
                <h4 style="margin: 8px 0 6px 0; font-size: 0.95rem; font-weight: 700;">Top Weekend Boost</h4>
                <p style="color: var(--text-muted); font-size: 0.82rem; margin:0; line-height: 1.4;">Posizionamento in vetta alle ricerche delle aziende per tutto il fine settimana.</p>
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
        "<h2 style='font-weight: 700; font-size: 1.3rem; margin-bottom: 4px;'>Soluzioni per Aziende e Attività</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: var(--text-muted); margin-bottom: 1.25rem; font-size: 0.88rem;'>Ottimizza la ricerca di personale qualificato per strutture e corporate.</p>",
        unsafe_allow_html=True,
    )

    a1, a2 = st.columns(2, gap="medium")
    with a1:
        st.markdown(
            """
        <div class="enterprise-card">
            <h3 style="font-size: 1.05rem; font-weight: 700; margin-top:0;">Ricerca Veloce Turni</h3>
            <p style="color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;">Trova personale qualificato coperto da referenze verificate nel giro di poche ore.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
    with a2:
        st.markdown(
            """
        <div class="enterprise-card">
            <h3 style="font-size: 1.05rem; font-weight: 700; margin-top:0;">Abbonamento Dedicato</h3>
            <p style="color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;">Accedi direttamente ai contatti telefonici e gestisci team multipli con fatturazione centralizzata.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

# ============================================================
# 5. PIANI ABBONAMENTO
# ============================================================
elif scelta == "Piani":
    st.markdown(
        "<h2 style='font-weight: 700; font-size: 1.3rem; margin-bottom: 4px;'>Listino Piani & Abbonamenti</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: var(--text-muted); margin-bottom: 1.25rem; font-size: 0.88rem;'>Soluzioni commerciali strutturate per aziende e professionisti.</p>",
        unsafe_allow_html=True,
    )

    p1, p2 = st.columns(2, gap="medium")
    with p1:
        st.markdown(
            """
        <div class="enterprise-card">
            <div>
                <span style="font-size: 0.7rem; font-weight: 600; color: var(--text-muted); background: rgba(226, 232, 240, 0.6); padding: 3px 8px; border-radius: 6px;">In arrivo</span>
                <h3 style="font-size: 1.1rem; font-weight: 700; margin: 10px 0 4px 0;">Abbonamento Aziende</h3>
                <div style="font-size: 1.35rem; font-weight: 700; color: var(--text-main); margin: 8px 0;">20 € <span style="font-size: 0.75rem; color: var(--text-muted); font-weight: 400;">/ mese</span></div>
                <p style="color: var(--text-muted); font-size: 0.85rem; margin: 0; line-height: 1.4;">Contatti diretti illimitati su WhatsApp e sblocco completo di tutti i profili del database.</p>
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
                <span style="font-size: 0.7rem; font-weight: 600; color: var(--brand-accent); background: #dbeafe; padding: 3px 8px; border-radius: 6px;">In arrivo</span>
                <h3 style="font-size: 1.1rem; font-weight: 700; margin: 10px 0 4px 0;">PRO Talento</h3>
                <div style="font-size: 1.35rem; font-weight: 700; color: var(--text-main); margin: 8px 0;">12 € <span style="font-size: 0.75rem; color: var(--text-muted); font-weight: 400;">/ mese</span></div>
                <p style="color: var(--text-muted); font-size: 0.85rem; margin: 0; line-height: 1.4;">Visibilità prioritaria costante per l'intero mese e badge oro di qualifica verificata.</p>
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
        "<h2 style='font-weight: 700; font-size: 1.3rem; margin-bottom: 4px;'>Dashboard Amministrativa</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: var(--text-muted); margin-bottom: 1.25rem; font-size: 0.88rem;'>Monitoraggio in tempo reale delle metriche di utilizzo e della piattaforma.</p>",
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
        <h4 style="margin-top:0; font-weight:700; font-size:0.95rem;">Stato Infrastruttura Cloud</h4>
        <p style="font-size: 1.1rem; font-weight: 700; color: var(--success); margin: 6px 0;">Operativo & Sincronizzato 🟢</p>
        <p style="color: var(--text-muted); font-size: 0.85rem; margin:0;">Palette celeste sfumata verde chiaro applicata con successo.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )