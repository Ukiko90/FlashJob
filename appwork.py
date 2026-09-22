import html
import re
import streamlit as st

st.set_page_config(
    page_title="Flashjob • Il talento che cercavi alla portata di mano",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# STATO INIZIALE & DATABASE PROFESSIONISTI
# ============================================================
if "lavoratori" not in st.session_state:
    st.session_state.lavoratori = [
        {
            "id": 1,
            "nome": "Marco Rossi",
            "mansione": "Project Manager / Senior",
            "zona": "Milano Centro",
            "tel": "+39 333 1234567",
            "completati": 14,
            "disponibile": True,
            "referenze": "Eccellente gestione dei team e coordinamento progetti complessi.",
            "recensioni": "4.9 ⭐ (12 recensioni verificate)",
            "competenze": ["Agile & Scrum", "Leadership", "Risk Management"],
        },
        {
            "id": 2,
            "nome": "Giulia Bianchi",
            "mansione": "UI/UX Designer",
            "zona": "Navigli / Ticinese",
            "tel": "+39 333 9876543",
            "completati": 22,
            "disponibile": True,
            "referenze": "Velocità incredibile nella prototipazione e design system.",
            "recensioni": "5.0 ⭐ (19 recensioni verificate)",
            "competenze": ["Figma", "Design Systems", "User Research"],
        },
        {
            "id": 3,
            "nome": "Davide Verdi",
            "mansione": "Full Stack Developer",
            "zona": "Porta Nuova / Como",
            "tel": "+39 333 5554433",
            "completati": 30,
            "disponibile": True,
            "referenze": "Ottima attitudine al problem solving e architetture scalabili.",
            "recensioni": "4.8 ⭐ (15 recensioni verificate)",
            "competenze": ["Python", "React", "Cloud Architecture"],
        },
        {
            "id": 4,
            "nome": "Sofia Neri",
            "mansione": "Data Analyst",
            "zona": "Brera / Garibaldi",
            "tel": "+39 333 7778899",
            "completati": 18,
            "disponibile": True,
            "referenze": "Grande precisione nell'analisi dei dati e modellazione predittiva.",
            "recensioni": "4.9 ⭐ (14 recensioni verificate)",
            "competenze": ["SQL", "Tableau", "Python"],
        },
    ]

if "selected_id" not in st.session_state:
    st.session_state.selected_id = None

if "visite_totali" not in st.session_state:
    st.session_state.visite_totali = 0

if "sessione_contata" not in st.session_state:
    st.session_state.visite_totali += 1
    st.session_state.sessione_contata = True

if "abbonamento_attivo" not in st.session_state:
    st.session_state.abbonamento_attivo = False


def safe(value):
    return html.escape(str(value))


def whatsapp_url(phone):
    return "https://wa.me/" + re.sub(r"\D", "", phone)


# ============================================================
# DESIGN SYSTEM PROFESSIONALE (LIGHT MODE PULITO)
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --bg-gradient: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
    --card-bg: #ffffff;
    --text-main: #0f172a;
    --text-muted: #64748b;
    --border-color: #e2e8f0;
    --shadow: 0 10px 25px rgba(15, 23, 42, 0.05);
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
    max-width: 1050px !important;
    padding: 2rem 1.5rem 5rem !important;
}

#MainMenu {visibility: hidden; display: none;}
footer {visibility: hidden; display: none;}
header {visibility: hidden; display: none;}
[data-testid="stHeader"] {display: none !important;}
[data-testid="stToolbar"] {display: none !important;}
[data-testid="stDecoration"] {display: none !important;}

/* HEADER AZIENDALE */
.store-header {
    background: linear-gradient(135deg, #0f172a 100%);
    padding: 2.5rem;
    border-radius: 24px;
    box-shadow: 0 20px 40px rgba(15, 23, 42, 0.15);
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 20px;
    color: white;
}
.app-titles h1 {
    font-size: 2.2rem;
    font-weight: 800;
    margin: 0;
    color: white;
}
.app-titles p {
    font-size: 1rem;
    margin: 6px 0 0 0;
    color: #94a3b8;
    font-weight: 500;
}

/* CARD */
.custom-card {
    background: var(--card-bg);
    border-radius: var(--radius);
    padding: 1.8rem;
    box-shadow: var(--shadow);
    border: 1px solid var(--border-color);
    margin-bottom: 1.5rem;
}

/* PALLINO VERDE */
@keyframes pulse-animation {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.6); }
    70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(16, 185, 129, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}
.pulsing-dot {
    display: inline-block;
    width: 10px;
    height: 10px;
    background-color: #10b981;
    border-radius: 50%;
    animation: pulse-animation 1.8s infinite;
    margin-right: 6px;
    vertical-align: middle;
}

.skill-pill {
    display: inline-block;
    background: #f1f5f9;
    color: #334155;
    padding: 5px 12px;
    border-radius: 8px;
    font-size: 0.75rem;
    font-weight: 700;
    margin-right: 6px;
    margin-bottom: 6px;
}

.stButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 12px;
    background: #0f172a;
    color: white;
    font-weight: 700;
    border: none;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
    transition: all 0.2s ease;
}
.stButton > button:hover {
    background: #1e293b;
    color: white;
    transform: translateY(-1px);
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# BARRA LATERALE ADMIN
# ============================================================
with st.sidebar:
    st.markdown("### 🔐 Area Riservata Admin")
    pwd = st.text_input("Password Admin", type="password")
    mostra_admin = False
    if pwd == "admin123":
        st.success("Accesso Autorizzato ✅")
        mostra_admin = True
    elif pwd != "":
        st.error("Password errata ❌")

    st.markdown("---")
    st.markdown("### 🏢 Stato Account")
    if st.session_state.abbonamento_attivo:
        st.success("🌟 Abbonamento Elite Attivo")
        if st.button("Torna a Piano Base"):
            st.session_state.abbonamento_attivo = False
            st.rerun()
    else:
        st.warning("🔒 Account Free (Limitato)")
        if st.button("✨ Sblocca Tutto"):
            st.session_state.abbonamento_attivo = True
            st.rerun()

# ============================================================
# HEADER PRINCIPALE
# ============================================================
st.markdown(
    """
<div class="store-header">
    <div class="app-titles">
        <h1>Flashjob Pro</h1>
        <p>Marketplace Professionale per la Selezione di Talenti & Risorse</p>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

menu = ["Panoramica", "Ricerca Talenti", "Area Professionista", "Piani"]
if mostra_admin:
    menu.append("Dashboard Admin")

scelta = st.radio("Navigazione", menu, horizontal=True)

# ============================================================
# 1. PANORAMICA
# ============================================================
if scelta == "Panoramica":
    st.markdown(
        """
        <div style="text-align: center; max-width: 750px; margin: 0 auto 2.5rem auto;">
            <h2 style='font-weight:800; font-size:2.2rem; color:#0f172a;'>Il professionista giusto, esattamente quando serve.</h2>
            <p style='color:var(--text-muted); font-size:1.05rem; line-height:1.6; margin-top:10px;'>Flashjob mette in contatto aziende e specialisti qualificati a Milano, azzerando le tempistiche di intermediazione e semplificando la gestione del personale.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown(
            """
        <div class="custom-card" style="height: 100%;">
            <h3 style="font-size: 1.25rem; margin-top: 0; color:#0f172a;">Per le Aziende</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6;">
                Trova profili verificati in pochi secondi. Filtra per competenze specifiche e avvia subito il contatto diretto.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
        <div class="custom-card" style="height: 100%;">
            <h3 style="font-size: 1.25rem; margin-top: 0; color:#0f172a;">Per i Professionisti</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6;">
                Metti in mostra le tue competenze certificate, gestisci la tua disponibilità in tempo reale e ricevi offerte immediate.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

# ============================================================
# 2. RICERCA TALENTI
# ============================================================
elif scelta == "Ricerca Talenti":
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

        comp_html = "".join(
            [f'<span class="skill-pill">✓ {c}</span>' for c in selected_c["competenze"]]
        )
        st.markdown(
            f"""
        <div class="custom-card" style="margin-top: 20px;">
            <h2 style="margin:0; font-size:1.5rem; color:#0f172a;">{safe(selected_c["nome"])}</h2>
            <p style="color:var(--text-muted); margin:4px 0 15px 0; font-weight:600;">{safe(selected_c["mansione"])} · 📍 {safe(selected_c["zona"])}</p>
            <div style="margin-bottom: 15px;">{comp_html}</div>
            <div style="background:#f8fafc; border-left:4px solid #0f172a; padding:15px; border-radius:0 12px 12px 0; font-style:italic; color:#334155;">
                “{safe(selected_c["referenze"])}”
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )
        st.link_button(
            "💬 Contatta su WhatsApp", whatsapp_url(selected_c["tel"])
        )
    else:
        st.markdown(
            "<h2 style='font-size:1.6rem; font-weight:800; color:#0f172a;'>Database Professionisti</h2>",
            unsafe_allow_html=True,
        )

        for lav in st.session_state.lavoratori:
            col_info, col_btn = st.columns([3, 1], gap="medium")
            with col_info:
                st.markdown(
                    f"""
                    <div class="custom-card" style="padding: 1.2rem 1.5rem; margin-bottom: 1rem;">
                        <h3 style="margin:0; font-size:1.1rem; color:#0f172a;">{safe(lav["nome"])}</h3>
                        <p style="color:var(--text-muted); margin:3px 0; font-size:0.9rem; font-weight:600;">{safe(lav["mansione"])} · 📍 {safe(lav["zona"])}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with col_btn:
                st.markdown(
                    "<div style='margin-top: 20px;'></div>", unsafe_allow_html=True
                )
                if st.button("Vedi profilo", key=f"btn_{lav['id']}"):
                    st.session_state.selected_id = lav["id"]
                    st.rerun()

# ============================================================
# 3. AREA PROFESSIONISTA
# ============================================================
elif scelta == "Area Professionista":
    st.markdown(
        "<h2 style='font-size:1.6rem; font-weight:800; color:#0f172a;'>Gestione Profilo</h2>",
        unsafe_allow_html=True,
    )
    st.text_input("Il tuo Nome e Cognome", value="Il Tuo Nome")
    st.selectbox("Mansione Principale", ["Project Manager", "UI/UX Designer", "Full Stack Developer", "Data Analyst"])
    st.toggle("🟢 Disponibile per nuove opportunità", value=True)

# ============================================================
# 4. PIANI
# ============================================================
elif scelta == "Piani":
    st.markdown(
        "<h2 style='font-size:1.6rem; font-weight:800; color:#0f172a;'>Piani di Abbonamento</h2>",
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            '<div class="custom-card"><h3>Base</h3><p>Gratuito per esplorazione limitata.</p></div>',
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            '<div class="custom-card"><h3>Elite</h3><p>Accesso illimitato a tutti i talenti.</p></div>',
            unsafe_allow_html=True,
        )

# ============================================================
# 5. DASHBOARD ADMIN
# ============================================================
elif scelta == "Dashboard Admin" and mostra_admin:
    st.markdown(
        f"<h2 style='font-size:1.6rem; font-weight:800; color:#0f172a;'>Dashboard Admin</h2><p>Visite totali: {st.session_state.visite_totali}</p>",
        unsafe_allow_html=True,
    )