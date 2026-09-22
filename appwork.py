import html
import re
import streamlit as st

st.set_page_config(
    page_title="Flashjob • Premium Talent Marketplace",
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
            "mansione": "Senior Project Manager",
            "zona": "Milano Centro",
            "tel": "+39 333 1234567",
            "disponibile": True,
            "boosted": True,
            "tariffa": "45 €/h",
            "recensioni": "4.9 ⭐ (28 recensioni)",
            "competenze": ["Agile", "Scrum", "Team Leadership", "Budgeting"],
            "bio": "Specializzato nel coordinamento di progetti digitali complessi con oltre 8 anni di esperienza.",
        },
        {
            "id": 2,
            "nome": "Giulia Bianchi",
            "mansione": "Lead UI/UX Designer",
            "zona": "Navigli / Ticinese",
            "tel": "+39 333 9876543",
            "disponibile": True,
            "boosted": False,
            "tariffa": "40 €/h",
            "recensioni": "5.0 ⭐ (42 recensioni)",
            "competenze": [
                "Figma",
                "Design Systems",
                "Prototyping",
                "User Research",
            ],
            "bio": "Creo esperienze digitali intuitive e design system scalabili per startup e grandi brand.",
        },
        {
            "id": 3,
            "nome": "Davide Verdi",
            "mansione": "Full Stack Engineer",
            "zona": "Porta Nuova",
            "tel": "+39 333 5554433",
            "disponibile": False,
            "boosted": True,
            "tariffa": "50 €/h",
            "recensioni": "4.8 ⭐ (19 recensioni)",
            "competenze": ["Python", "React", "AWS", "Docker"],
            "bio": "Sviluppo architetture web robuste, scalabili e ad alte prestazioni.",
        },
        {
            "id": 4,
            "nome": "Sofia Neri",
            "mansione": "Data Analyst & BI Specialist",
            "zona": "Brera",
            "tel": "+39 333 7778899",
            "disponibile": True,
            "boosted": False,
            "tariffa": "42 €/h",
            "recensioni": "4.9 ⭐ (31 recensioni)",
            "competenze": ["SQL", "Tableau", "PowerBI", "Python"],
            "bio": "Trasformo dati grezzi in insight strategici per accelerare la crescita aziendale.",
        },
    ]

if "selected_id" not in st.session_state:
    st.session_state.selected_id = None

if "abbonamento_titolare" not in st.session_state:
    st.session_state.abbonamento_titolare = False

if "visite" not in st.session_state:
    st.session_state.visite = 1240


def safe(value):
    return html.escape(str(value))


def whatsapp_url(phone):
    return "https://wa.me/" + re.sub(r"\D", "", phone)


# ============================================================
# DESIGN SYSTEM PROFESSIONALE & DARK/MODERN ACCENTS
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --bg-dark: #090d16;
    --card-bg: #111827;
    --card-border: rgba(255, 255, 255, 0.08);
    --accent-glow: #38bdf8;
    --accent-emerald: #10b981;
    --accent-purple: #8b5cf6;
    --text-main: #f8fafc;
    --text-muted: #94a3b8;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: var(--text-main);
}

.stApp {
    background-color: var(--bg-dark);
    background-image: 
        radial-gradient(at 0% 0%, rgba(56, 189, 248, 0.08) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(139, 92, 246, 0.08) 0px, transparent 50%);
}

.block-container {
    max-width: 1100px !important;
    padding: 2.5rem 1.5rem 5rem !important;
}

#MainMenu, footer, header {visibility: hidden; display: none;}
[data-testid="stHeader"] {display: none !important;}

/* HERO BANNER */
.hero-box {
    background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%);
    border: 1px solid rgba(56, 189, 248, 0.2);
    border-radius: 24px;
    padding: 3rem 2.5rem;
    margin-bottom: 2.5rem;
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    position: relative;
    overflow: hidden;
}
.hero-box h1 {
    font-size: 2.5rem;
    font-weight: 800;
    color: #ffffff;
    margin: 0 0 10px 0;
    letter-spacing: -0.5px;
}
.hero-box p {
    color: #94a3b8;
    font-size: 1.1rem;
    margin: 0;
}

/* CARDS */
.pro-card {
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 20px;
    padding: 1.8rem;
    transition: all 0.3s ease;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    position: relative;
}
.pro-card:hover {
    border-color: rgba(56, 189, 248, 0.4);
    transform: translateY(-3px);
}

.boosted-card {
    border: 1px solid rgba(139, 92, 246, 0.6);
    background: linear-gradient(145deg, #111827 0%, #1e1b4b 100%);
}

/* PALLINO LAMPEGGIANTE DISPONIBILITÀ */
@keyframes pulse-green {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
    70% { transform: scale(1); box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}
.live-dot {
    display: inline-block;
    width: 10px;
    height: 10px;
    background-color: #10b981;
    border-radius: 50%;
    animation: pulse-green 1.8s infinite;
    margin-right: 6px;
    vertical-align: middle;
}
.offline-dot {
    display: inline-block;
    width: 10px;
    height: 10px;
    background-color: #64748b;
    border-radius: 50%;
    margin-right: 6px;
    vertical-align: middle;
}

/* BADGES & PILLS */
.badge-skill {
    background: rgba(56, 189, 248, 0.1);
    color: #38bdf8;
    border: 1px solid rgba(56, 189, 248, 0.2);
    padding: 4px 10px;
    border-radius: 8px;
    font-size: 0.75rem;
    font-weight: 700;
    margin-right: 6px;
    margin-bottom: 6px;
    display: inline-block;
}
.badge-boost {
    background: rgba(139, 92, 246, 0.15);
    color: #c084fc;
    border: 1px solid rgba(139, 92, 246, 0.3);
    padding: 4px 10px;
    border-radius: 8px;
    font-size: 0.75rem;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    gap: 4px;
}

/* BOTTONI CUSTOM */
.stButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 12px;
    background: linear-gradient(135deg, #38bdf8 0%, #0284c7 100%);
    color: #0f172a;
    font-weight: 700;
    border: none;
    box-shadow: 0 4px 15px rgba(56, 189, 248, 0.3);
    transition: all 0.2s ease;
}
.stButton > button:hover {
    opacity: 0.9;
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(56, 189, 248, 0.4);
    color: #0f172a;
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# SIDEBAR DI CONTROLLO & STATO ABBONAMENTO
# ============================================================
with st.sidebar:
    st.markdown("### ⚡ Flashjob Command Center")
    st.markdown(
        "<p style='font-size:0.85rem; color:#94a3b8;'>Gestione avanzata sessione e privilegi.</p>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    if st.session_state.abbonamento_titolare:
        st.success("👑 Account Titolare: ELITE ATTIVO")
        st.markdown(
            "<span style='font-size:0.8rem; color:#10b981;'>✓ Accesso illimitato a tutti i contatti diretti sbloccato.</span>",
            unsafe_allow_html=True,
        )
        if st.button("Disattiva Abbonamento (Test)"):
            st.session_state.abbonamento_titolare = False
            st.rerun()
    else:
        st.warning("🔒 Account Titolare: FREE")
        st.markdown(
            "<span style='font-size:0.8rem; color:#94a3b8;'>I contatti telefonici sono oscurati.</span>",
            unsafe_allow_html=True,
        )
        if st.button("✨ Attiva Titolare (20€/mese)"):
            st.session_state.abbonamento_titolare = True
            st.success("Abbonamento attivato con successo!")
            st.rerun()

    st.markdown("---")
    st.markdown(
        f"<p style='font-size:0.75rem; color:#64748b;'>Visite totali piattaforma: <b>{st.session_state.visite}</b></p>",
        unsafe_allow_html=True,
    )

# ============================================================
# HEADER PRINCIPALE
# ============================================================
st.markdown(
    """
<div class="hero-box">
    <h1>Flashjob Marketplace</h1>
    <p>Il network esclusivo che collega aziende innovative ai migliori talenti freelance in tempo reale.</p>
</div>
""",
    unsafe_allow_html=True,
)

# NAVIGAZIONE PRINCIPALE
menu = [
    "Esplora Talenti",
    "Piani & Listino (Titolari & Dipendenti)",
    "Area Dipendente (Attiva Boost)",
]
scelta = st.radio("Menu", menu, horizontal=True, label_visibility="collapsed")

st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)

# ============================================================
# SCHERMATA 1: ESPLORA TALENTI
# ============================================================
if scelta == "Esplora Talenti":
    selected_c = next(
        (
            item
            for item in st.session_state.lavoratori
            if item["id"] == st.session_state.selected_id
        ),
        None,
    )

    if selected_c is not None:
        if st.button("← Torna alla lista completa"):
            st.session_state.selected_id = None
            st.rerun()

        skills_html = "".join(
            [f'<span class="badge-skill">{s}</span>' for s in selected_c["competenze"]]
        )
        boost_badge = (
            '<span class="badge-boost">🚀 Weekend Boost Attivo</span>'
            if selected_c["boosted"]
            else ""
        )
        dot_html = (
            '<span><span class="live-dot"></span>Disponibile ora</span>'
            if selected_c["disponibile"]
            else '<span><span class="offline-dot"></span>Al momento impegnato</span>'
        )

        st.markdown(
            f"""
        <div class="pro-card" style="margin-top: 15px;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 15px;">
                <div>
                    <div style="margin-bottom: 8px;">{boost_badge}</div>
                    <h2 style="margin: 0; font-size: 2rem; color: #fff;">{safe(selected_c["nome"])}</h2>
                    <p style="color: #38bdf8; font-size: 1.1rem; font-weight: 600; margin: 4px 0 12px 0;">{safe(selected_c["mansione"])}</p>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 1.4rem; font-weight: 800; color: #10b981;">{safe(selected_c["tariffa"])}</div>
                    <div style="font-size: 0.85rem; color: #94a3b8;">{safe(selected_c["recensioni"])}</div>
                </div>
            </div>
            
            <div style="margin: 15px 0; font-size: 0.95rem;">{dot_html} &nbsp; | &nbsp; 📍 {safe(selected_c["zona"])}</div>
            
            <p style="color: #cbd5e1; line-height: 1.6; background: rgba(255,255,255,0.03); padding: 15px; border-radius: 12px; margin: 20px 0;">
                {safe(selected_c["bio"])}
            </p>
            
            <div style="margin-bottom: 20px;">{skills_html}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # GESTIONE CONTATTO WHATSAPP / TELEFONO IN BASE ALL'ABBONAMENTO TITOLARE (20€/MESE)
        if st.session_state.abbonamento_titolare:
            st.markdown(
                "<div style='margin-top: 20px;'></div>", unsafe_allow_html=True
            )
            st.link_button(
                f"💬 Contatta Direttamente su WhatsApp ({selected_c['tel']})",
                whatsapp_url(selected_c["tel"]),
            )
        else:
            st.markdown(
                """
            <div style="background: rgba(245, 158, 11, 0.1); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 16px; padding: 20px; text-align: center; margin-top: 20px;">
                <h4 style="color: #f59e0b; margin: 0 0 8px 0;">Contatto Riservato ai Titolari Abbonati</h4>
                <p style="color: #94a3b8; font-size: 0.9rem; margin: 0 0 15px 0;">Abbonati al piano Titolare (20€/mese) per sbloccare i numeri di telefono diretti di tutti i talenti senza commissioni di intermediazione.</p>
            </div>
            """,
                unsafe_allow_html=True,
            )
            if st.button("🔓 Sblocca Contatti con il Piano Titolare (20€/mese)"):
                st.session_state.abbonamento_titolare = True
                st.rerun()

    else:
        st.markdown(
            "<h3 style='margin-bottom: 20px;'>Seleziona un Professionista</h3>",
            unsafe_allow_html=True,
        )

        # Ordina prima i profili con Boost attivo
        lavoratori_ordinati = sorted(
            st.session_state.lavoratori,
            key=lambda x: (not x["boosted"], not x["disponibile"]),
        )

        for lav in lavoratori_ordinati:
            card_class = (
                "pro-card boosted-card" if lav["boosted"] else "pro-card"
            )
            boost_badge = (
                '<span class="badge-boost">🚀 Weekend Boost</span>'
                if lav["boosted"]
                else ""
            )

            # Pallino disponibilità in tempo reale
            dot_html = (
                '<span class="live-dot" title="Disponibile"></span>'
                if lav["disponibile"]
                else '<span class="offline-dot" title="Non disponibile"></span>'
            )
            status_text = (
                "Disponibile" if lav["disponibile"] else "Impegnato"
            )

            col_card, col_action = st.columns([4, 1], gap="medium")
            with col_card:
                st.markdown(
                    f"""
                <div class="{card_class}" style="margin-bottom: 1rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <h3 style="margin: 0; font-size: 1.2rem; color: #fff;">{safe(lav["nome"])}</h3>
                            {boost_badge}
                        </div>
                        <span style="font-weight: 700; color: #10b981; font-size: 0.95rem;">{safe(lav["tariffa"])}</span>
                    </div>
                    <p style="color: #38bdf8; font-size: 0.9rem; font-weight: 600; margin: 4px 0 8px 0;">{safe(lav["mansione"])}</p>
                    <div style="font-size: 0.85rem; color: #94a3b8; display: flex; align-items: center; gap: 12px;">
                        <span>{dot_html} {status_text}</span>
                        <span>📍 {safe(lav["zona"])}</span>
                        <span>⭐ {safe(lav["recensioni"].split()[0])}</span>
                    </div>
                </div>
                """,
                    unsafe_allow_html=True,
                )
            with col_action:
                st.markdown(
                    "<div style='margin-top: 25px;'></div>", unsafe_allow_html=True
                )
                if st.button("Visualizza", key=f"view_{lav['id']}"):
                    st.session_state.selected_id = lav["id"]
                    st.rerun()

# ============================================================
# SCHERMATA 2: PIANI & LISTINO (TITOLARI & DIPENDENTI)
# ============================================================
elif scelta == "Piani & Listino (Titolari & Dipendenti)":
    st.markdown(
        "<h2 style='font-size: 1.8rem; font-weight: 800; margin-bottom: 10px;'>Piani di Monetizzazione Trasparente</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: #94a3b8; margin-bottom: 30px;'>Soluzioni studiate appositamente per massimizzare il valore sia per chi assume che per chi offre servizi.</p>",
        unsafe_allow_html=True,
    )

    col_p1, col_p2 = st.columns(2, gap="large")

    with col_p1:
        st.markdown(
            """
        <div class="pro-card" style="height: 100%; border-top: 4px solid #38bdf8;">
            <div style="font-size: 0.8rem; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">Per Aziende e Titolari</div>
            <h3 style="font-size: 1.8rem; font-weight: 800; margin: 0 0 10px 0;">Abbonamento Titolare</h3>
            <div style="font-size: 2.2rem; font-weight: 800; color: #ffffff; margin-bottom: 20px;">20 € <span style="font-size: 1rem; color: #94a3b8; font-weight: 400;">/ mese</span></div>
            
            <ul style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.8; padding-left: 20px; margin-bottom: 25px;">
                <li><b>Accesso illimitato</b> a tutti i contatti telefonici dei professionisti.</li>
                <li>Contatto diretto via WhatsApp senza commissioni di agenzia.</li>
                <li>Filtri avanzati per competenze, zone e disponibilità in tempo reale.</li>
                <li>Disdetta possibile in qualsiasi momento con un clic.</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )
        st.markdown(
            "<div style='margin-top: 15px;'></div>", unsafe_allow_html=True
        )
        if st.session_state.abbonamento_titolare:
            st.success("✅ Il tuo Abbonamento Titolare è attualmente attivo!")
        else:
            if st.button("Attiva Abbonamento Titolare (20€/mese)"):
                st.session_state.abbonamento_titolare = True
                st.success(
                    "Pagamento simulato con successo! Piano Titolare attivato."
                )
                st.rerun()

    with col_p2:
        st.markdown(
            """
        <div class="pro-card" style="height: 100%; border-top: 4px solid #8b5cf6;">
            <div style="font-size: 0.8rem; font-weight: 700; color: #c084fc; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">Per Dipendenti e Freelance</div>
            <h3 style="font-size: 1.8rem; font-weight: 800; margin: 0 0 10px 0;">Weekend Boost</h3>
            <div style="font-size: 2.2rem; font-weight: 800; color: #ffffff; margin-bottom: 20px;">5 € <span style="font-size: 1rem; color: #94a3b8; font-weight: 400;">/ fine settimana</span></div>
            
            <ul style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.8; padding-left: 20px; margin-bottom: 25px;">
                <li><b>Massima visibilità</b> in cima alla lista dei talenti per tutto il weekend.</li>
                <li>Badge speciale in evidenza sul tuo profilo con stella dorata.</li>
                <li>Fino a 4x contatti e visualizzazioni in più da parte dei titolari.</li>
                <li>Attivazione immediata prima del fine settimana.</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )
        st.markdown(
            "<div style='margin-top: 15px;'></div>", unsafe_allow_html=True
        )
        if st.button("🚀 Vai all'Area Dipendente per attivare il Boost"):
            st.switch_page = True  # handled via radio selection concept below if needed

# ============================================================
# SCHERMATA 3: AREA DIPENDENTE (ATTIVA BOOST)
# ============================================================
elif scelta == "Area Dipendente (Attiva Boost)":
    st.markdown(
        "<h2 style='font-size: 1.8rem; font-weight: 800; margin-bottom: 10px;'>Gestione Profilo & Weekend Boost</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color: #94a3b8; margin-bottom: 25px;'>Aggiorna la tua disponibilità in tempo reale e potenzia la tua visibilità per ricevere offerte di lavoro durante il fine settimana.</p>",
        unsafe_allow_html=True,
    )

    # Seleziona quale profilo simulare
    nomi_lavoratori = [l["nome"] for l in st.session_state.lavoratori]
    scelta_profilo = st.selectbox(
        "Seleziona il tuo profilo da gestire:", nomi_lavoratori
    )

    current_prof = next(
        l for l in st.session_state.lavoratori if l["nome"] == scelta_profilo
    )

    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

    col_d1, col_d2 = st.columns(2, gap="large")

    with col_d1:
        st.markdown("### Stato Attuale")
        nuova_disp = st.toggle(
            "🟢 Disponibile per lavorare", value=current_prof["disponibile"]
        )
        nuova_tariffa = st.text_input(
            "Tariffa oraria", value=current_prof["tariffa"]
        )

        if st.button("Salva Modifiche Profilo"):
            current_prof["disponibile"] = nuova_disp
            current_prof["tariffa"] = nuova_tariffa
            st.success("Profilo aggiornato con successo!")
            st.rerun()

    with col_d2:
        st.markdown("### Promozione Weekend Boost (5€)")
        if current_prof["boosted"]:
            st.info(
                "🚀 Il tuo profilo ha già il **Weekend Boost** attivo ed è in evidenza!"
            )
            if st.button("Disattiva Boost"):
                current_prof["boosted"] = False
                st.rerun()
        else:
            st.markdown(
                "<p style='color: #94a3b8; font-size: 0.9rem;'>Mettiti in cima alla lista per tutto il fine settimana con soli 5€.</p>",
                unsafe_allow_html=True,
            )
            if st.button("💳 Attiva Weekend Boost per 5€"):
                current_prof["boosted"] = True
                st.success(
                    "Pagamento effettuato! Il tuo profilo è ora in evidenza con il Weekend Boost 🚀"
                )
                st.rerun()