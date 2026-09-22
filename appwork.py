import html
import re
import streamlit as st

st.set_page_config(
    page_title="Flashjob • Il Lavoro a Portata di Mano",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# DATABASE INIZIALE & STATO
# ============================================================
if "lavoratori" not in st.session_state:
    st.session_state.lavoratori = [
        {
            "id": 1,
            "nome": "Marco Rossi",
            "mansione": "Cameriere / Sala",
            "zona": "Navigli, Milano",
            "tel": "+39 333 1234567",
            "completati": 18,
            "disponibile": True,
            "referenze": (
                "Puntuale, professionale e con ottime capacità di gestione"
                " sala anche nei momenti di massimo afflusso."
            ),
        },
        {
            "id": 2,
            "nome": "Sara Bianchi",
            "mansione": "Barista / Bartender",
            "zona": "Porta Romana, Milano",
            "tel": "+39 340 9876543",
            "completati": 24,
            "disponibile": True,
            "referenze": (
                "Eccezionale nella mixology, rapidissima e dotata di grande"
                " empatia con la clientela."
            ),
        },
        {
            "id": 3,
            "nome": "Luca Verdi",
            "mansione": "Chef de Rang / Jolly",
            "zona": "Brera, Milano",
            "tel": "+39 328 1122334",
            "completati": 31,
            "disponibile": False,
            "referenze": (
                "Una sicurezza assoluta per eventi e grandi coperti. Leader"
                " naturale in squadra."
            ),
        },
        {
            "id": 4,
            "nome": "Giulia Neri",
            "mansione": "Aiuto Cuoco",
            "zona": "Duomo, Milano",
            "tel": "+39 349 5544332",
            "completati": 12,
            "disponibile": True,
            "referenze": (
                "Rapida nella linea, pulita e molto attenta alle norme HACCP."
            ),
        },
    ]

if "selected_candidate" not in st.session_state:
    st.session_state.selected_candidate = None


def safe(value):
    return html.escape(str(value))


def whatsapp_url(phone):
    return "https://wa.me/" + re.sub(r"\D", "", phone)


# ============================================================
# DESIGN SYSTEM CELESTINO SFUMATO & PULSAR CSS
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --bg-gradient: linear-gradient(135deg, #f0f7ff 0%, #dbeafe 50%, #eff6ff 100%);
    --card-bg: #ffffff;
    --text-main: #0f172a;
    --text-muted: #475569;
    --border-color: #bfdbfe;
    --shadow: 0 10px 30px rgba(14, 116, 144, 0.08);
    --radius: 20px;
    --primary: #0284c7;
    --primary-dark: #0369a1;
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

/* Nasconde elementi Streamlit */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stHeader"] { display: none !important; }
[data-testid="stToolbar"] { display: none !important; }

/* HERO CELESTINA SFUMATA */
.hero-box {
    background: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%);
    color: white;
    padding: 3.5rem 2rem;
    border-radius: 24px;
    text-align: center;
    box-shadow: 0 15px 35px rgba(2, 132, 199, 0.25);
    margin-bottom: 2rem;
}
.hero-box h1 {
    font-size: 2.8rem;
    font-weight: 800;
    margin: 0 0 10px 0;
    letter-spacing: -1px;
}
.hero-box p {
    font-size: 1.15rem;
    opacity: 0.95;
    max-width: 700px;
    margin: 0 auto;
}

/* NAVIGAZIONE RADIO */
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
}
div[data-testid="stRadio"] div[role="radiogroup"] label {
    border-radius: 40px;
    padding: 10px 18px;
    font-weight: 700;
    font-size: 0.85rem;
    color: var(--text-muted) !important;
    transition: all 0.3s ease;
}
div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
    background: #0284c7 !important;
    color: white !important;
    box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4);
}

/* CARD */
.custom-card {
    background: var(--card-bg);
    border-radius: var(--radius);
    padding: 1.8rem;
    box-shadow: var(--shadow);
    border: 1px solid #e0f2fe;
    margin-bottom: 1.5rem;
}

/* PALLINO VERDE LAMPEGGIANTE (PULSAR) */
@keyframes pulse-animation {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 200, 83, 0.7); }
    70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(0, 200, 83, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 200, 83, 0); }
}

.pulsing-dot {
    display: inline-block;
    width: 12px;
    height: 12px;
    background-color: #00c853;
    border-radius: 50%;
    animation: pulse-animation 1.8s infinite;
    margin-right: 6px;
    vertical-align: middle;
}

.offline-dot {
    display: inline-block;
    width: 12px;
    height: 12px;
    background-color: #ccc;
    border-radius: 50%;
    margin-right: 6px;
    vertical-align: middle;
}

/* BADGE */
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
.badge-green { background: #e8f8f0; color: #00c853; }
.badge-orange { background: #fff3e0; color: #ff9100; }
.badge-blue { background: #e0f2fe; color: #0284c7; }

/* STATS */
.stats-container {
    display: flex;
    background: #f0fdf4;
    border-radius: 16px;
    padding: 1rem;
    margin: 1.2rem 0;
    text-align: center;
    border: 1px solid #bbf7d0;
}
.stat-box { flex: 1; border-right: 1px solid #dcfce7; }
.stat-box:last-child { border-right: none; }
.stat-box strong { display: block; font-size: 1.3rem; color: #0369a1; }
.stat-box span { font-size: 0.7rem; color: #475569; font-weight: 700; text-transform: uppercase; }

/* BOTTONI */
.stButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 14px;
    background: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%);
    color: white;
    font-weight: 700;
    border: none;
    box-shadow: 0 4px 15px rgba(2, 132, 199, 0.35);
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
# HERO
# ============================================================
st.markdown(
    """
<div class="hero-box">
    <h1>⚡ Flashjob</h1>
    <p>La piattaforma intelligente che rivoluziona il recruiting nel settore della ristorazione e degli eventi in tempo reale.</p>
</div>
""",
    unsafe_allow_html=True,
)

scelta = st.radio(
    "Navigazione",
    [
        "Panoramica",
        "Database & Filtri Azienda",
        "Area Lavoratore (Imposta Disponibilità)",
        "Piani & Abbonamenti",
    ],
    horizontal=True,
)

# ============================================================
# 1. PANORAMICA (CHI SIAMO, COSA FACCIAMO, PERCHÉ SCEGLIERCI)
# ============================================================
if scelta == "Panoramica":
    st.markdown(
        """
        <div class="custom-card" style="text-align: center; padding: 2.5rem; background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);">
            <span class="badge-pop badge-blue">Benvenuti in Flashjob</span>
            <h2 style='font-weight:800; font-size:2.2rem; margin-bottom:15px; color:#0f172a;'>Chi Siamo & Cosa Facciamo</h2>
            <p style='color:var(--text-muted); font-size:1.05rem; line-height:1.7; max-width:850px; margin: 0 auto;'>
                <b>Flashjob</b> nasce per risolvere il problema cronico delle urgenze e del reperimento rapido di personale qualificato nella ristorazione e nel mondo degli eventi. 
                Siamo il ponte digitale diretto tra i locali in cerca di supporto immediato (ristoranti, bar, hotel, catering) e professionisti della sala, del bar e della cucina pronti a lavorare. 
                Attraverso il nostro sistema live a <b>pallino verde lampeggiante</b>, azzeriamo i tempi di attesa delle agenzie tradizionali.
            </p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <h3 style='font-weight:800; font-size:1.5rem; margin: 2rem 0 1rem 0; text-align:center; color:#0f172a;'>I Nostri Punti di Forza</h3>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown(
            """
        <div class="custom-card" style="height: 100%;">
            <span style="font-size: 2rem;">⚡</span>
            <h4 style="margin: 10px 0 8px 0; font-weight:700; color:#0369a1;">Velocità Istantanea</h4>
            <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.6;">
                Niente colloqui infiniti o lunghe attese. Visualizza chi è disponibile <b>in tempo reale</b> e contatta subito il lavoratore tramite WhatsApp.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="custom-card" style="height: 100%;">
            <span style="font-size: 2rem;">🎯</span>
            <h4 style="margin: 10px 0 8px 0; font-weight:700; color:#0369a1;">Profili Verificati</h4>
            <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.6;">
                Ogni risorsa ha uno storico di turni completati e referenze verificate sul campo, per garantirti affidabilità e competenza massima sin dal primo giorno.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
        <div class="custom-card" style="height: 100%;">
            <span style="font-size: 2rem;">🤝</span>
            <h4 style="margin: 10px 0 8px 0; font-weight:700; color:#0369a1;">Zero Intermediari</h4>
            <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.6;">
                Un contatto diretto e trasparente tra locale e lavoratore. Gestisci le tue urgenze di turni in piena autonomia e flessibilità.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="custom-card" style="margin-top: 2rem; background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color: white; text-align: center; padding: 2.5rem;">
            <h3 style="font-weight:800; font-size:1.8rem; margin-bottom:10px; color: white;">Perché Scegliere Flashjob?</h3>
            <p style="font-size:1.05rem; opacity:0.95; max-width:750px; margin: 0 auto; line-height:1.6;">
                Perché un imprevisto di personale non deve mai compromettere la qualità del tuo servizio o il fatturato del tuo locale. Con Flashjob hai la certezza di trovare il professionista giusto al momento giusto, ottimizzando costi e tempo.
            </p>
        </div>
    """,
        unsafe_allow_html=True,
    )

# ============================================================
# 2. DATABASE & FILTRI AZIENDA
# ============================================================
elif scelta == "Database & Filtri Azienda":
    selected = st.session_state.selected_candidate

    if selected is not None:
        if st.button("← Torna al database completo", key="back_to_db"):
            st.session_state.selected_candidate = None
            st.rerun()

        c = selected
        stato_html = (
            '<span class="pulsing-dot"></span><b style="color:#00c853;">DISPONIBILE ORA</b>'
            if c["disponibile"]
            else '<span class="offline-dot"></span><span style="color:#888;">NON DISPONIBILE</span>'
        )

        st.markdown(
            f"""
        <div class="custom-card" style="margin-top: 20px;">
            <div style="display: flex; align-items: center; gap: 20px;">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300" style="width:80px; height:80px; border-radius:50%; object-fit:cover; border:3px solid #38bdf8;" />
                <div>
                    <div style="margin-bottom:6px;">{stato_html}</div>
                    <h2 style="margin:0; font-size:1.5rem;">{safe(c["nome"])}</h2>
                    <p style="color:var(--text-muted); margin:4px 0 0 0; font-weight:600;">{safe(c["mansione"])} · {safe(c["zona"])}</p>
                </div>
            </div>
            
            <div class="stats-container">
                <div class="stat-box">
                    <strong>{safe(c["completati"])}</strong>
                    <span>Turni fatti</span>
                </div>
                <div class="stat-box">
                    <strong>100%</strong>
                    <span>Affidabilità</span>
                </div>
                <div class="stat-box">
                    <strong>Verificato</strong>
                    <span>Status</span>
                </div>
            </div>
            
            <div style="background:#f0fdf4; border-left:4px solid #00c853; padding:15px; border-radius:0 12px 12px 0; margin-top:15px; font-style:italic; color:#166534;">
                “{safe(c["referenze"])}”
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.link_button(
            "💬 Contatta e Prenota su WhatsApp",
            whatsapp_url(c["tel"]),
            use_container_width=True,
        )

    else:
        st.markdown(
            """
            <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Database Contatti & Filtri</h2>
            <p style='color:var(--text-muted); margin-bottom:1.5rem;'>Filtra i professionisti per trovare subito la risorsa ideale per il tuo locale.</p>
        """,
            unsafe_allow_html=True,
        )

        # SEZIONE FILTRI
        st.markdown(
            '<div class="custom-card" style="padding: 1.2rem; background: #f8fafc;">',
            unsafe_allow_html=True,
        )
        col_f1, col_f2, col_f3 = st.columns(3)

        with col_f1:
            filtro_mansione = st.selectbox(
                "Filtra per Mansione",
                [
                    "Tutte",
                    "Cameriere / Sala",
                    "Barista / Bartender",
                    "Chef de Rang / Jolly",
                    "Aiuto Cuoco",
                ],
            )

        with col_f2:
            solo_disponibili = st.checkbox(
                "Mostra solo disponibili con pallino verde", value=False
            )

        with col_f3:
            ricerca_testo = st.text_input(
                "Cerca per nome o zona", placeholder="Es. Navigli o Marco..."
            )

        st.markdown("</div>", unsafe_allow_html=True)

        # APPLICAZIONE FILTRI SUL DATABASE
        lavoratori_filtrati = st.session_state.lavoratori
        if filtro_mansione != "Tutte":
            lavoratori_filtrati = [
                l for l in lavoratori_filtrati if l["mansione"] == filtro_mansione
            ]
        if solo_disponibili:
            lavoratori_filtrati = [
                l for l in lavoratori_filtrati if l["disponibile"]
            ]
        if ricerca_testo:
            testo_q = ricerca_testo.lower()
            lavoratori_filtrati = [
                l
                for l in lavoratori_filtrati
                if testo_q in l["nome"].lower() or testo_q in l["zona"].lower()
            ]

        st.markdown(
            f"<p style='color:#475569; font-size:0.9rem; margin: 1rem 0;'>Trovati <b>{len(lavoratori_filtrati)}</b> professionisti in archivio.</p>",
            unsafe_allow_html=True,
        )

        for idx, lav in enumerate(lavoratori_filtrati):
            col_info, col_btn = st.columns([3, 1], gap="medium")

            with col_info:
                if lav["disponibile"]:
                    badge_stato = '<span class="pulsing-dot"></span><b style="color:#00c853; font-size:0.75rem;">DISPONIBILE ORA</b>'
                else:
                    badge_stato = '<span class="offline-dot"></span><span style="color:#888; font-size:0.75rem;">NON DISPONIBILE</span>'

                st.markdown(
                    f"""
                <div class="custom-card" style="margin-bottom:1rem; padding:1.2rem 1.5rem;">
                    <div style="margin-bottom:6px;">{badge_stato}</div>
                    <h3 style="margin:0; font-size:1.15rem;">{safe(lav["nome"])}</h3>
                    <p style="color:var(--text-muted); margin:3px 0; font-size:0.9rem; font-weight:600;">{safe(lav["mansione"])} · {safe(lav["zona"])}</p>
                    <span style="font-size:0.8rem; color:#64748b;">{safe(lav["completati"])} turni completati</span>
                </div>
                """,
                    unsafe_allow_html=True,
                )

            with col_btn:
                st.markdown(
                    "<div style='margin-top: 30px;'></div>", unsafe_allow_html=True
                )
                if st.button("Vedi profilo", key=f"btn_db_{lav['id']}"):
                    st.session_state.selected_candidate = lav
                    st.rerun()

# ============================================================
# 3. AREA LAVORATORE
# ============================================================
elif scelta == "Area Lavoratore (Imposta Disponibilità)":
    st.markdown(
        """
        <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Area Personale Lavoratore</h2>
        <p style='color:var(--text-muted); margin-bottom:2rem;'>Modifica il tuo stato: accendi la disponibilità per farti contattare subito dai ristoranti.</p>
    """,
        unsafe_allow_html=True,
    )

    lavoratore_corrente = st.session_state.lavoratori[0]

    st.markdown(
        """
    <div class="custom-card">
        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 1.5rem;">
            <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300" style="width:70px; height:70px; border-radius:50%; object-fit:cover;" />
            <div>
                <h3 style="margin:0;">Marco Rossi</h3>
                <p style="color:var(--text-muted); margin:2px 0; font-size:0.85rem;">Cameriere / Sala · Navigli, Milano</p>
                <span class="badge-pop badge-blue" style="margin:0;">Profilo Verificato</span>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("### Gestione Stato in Tempo Reale")
    nuova_disp = st.toggle(
        "🟢 Attiva disponibilità per lavorare (Accendi pallino verde lampeggiante)",
        value=lavoratore_corrente["disponibile"],
    )

    if nuova_disp != lavoratore_corrente["disponibile"]:
        lavoratore_corrente["disponibile"] = nuova_disp
        st.success(
            "Stato aggiornato con successo nel database! I ristoranti vedranno"
            " immediatamente la modifica."
        )
        st.rerun()

    if lavoratore_corrente["disponibile"]:
        st.markdown(
            """
        <div style="background:#e8f8f0; color:#00c853; padding:12px; border-radius:12px; font-weight:700; margin-top:15px;">
            <span class="pulsing-dot"></span> Il tuo profilo è attualmente ONLINE con il pallino verde lampeggiante nel database aziendale!
        </div>
        """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
        <div style="background:#f1f5f9; color:#64748b; padding:12px; border-radius:12px; font-weight:700; margin-top:15px;">
            <span class="offline-dot"></span> Il tuo profilo è attualmente offline.
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# 4. PIANI & ABBONAMENTI
# ============================================================
else:
    st.markdown(
        """
        <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Listino & Upgrade ⚡</h2>
        <p style='color:var(--text-muted); margin-bottom:2rem;'>Scegli il piano ideale per sbloccare tutte le potenzialità di Flashjob.</p>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
        <div class="custom-card">
            <span class="badge-pop badge-blue">Per Aziende & Locali</span>
            <h3 style="margin-top:10px;">Abbonamento Standard</h3>
            <div style="font-size: 2.2rem; font-weight: 800; color: #0284c7; margin: 10px 0;">20€ <span style="font-size:0.9rem; color:#777; font-weight:400;">/ mese</span></div>
            <p style="font-size:0.9rem; color:var(--text-muted);">Accesso completo ai filtri avanzati e al database dei professionisti.</p>
            <ul style="padding-left:18px; color:#555; font-size:0.9rem; line-height:1.6;">
                <li>Filtri per mansione e zona in tempo reale</li>
                <li>Contatto diretto WhatsApp sbloccato</li>
                <li>Gestione turni e urgenze senza limiti</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Attiva Abbonamento Azienda", key="btn_sub_az"):
            st.success("Richiesta registrata! Abbonamento attivato.")

    with col2:
        st.markdown(
            """
        <div class="custom-card">
            <span class="badge-pop badge-orange">Per i Lavoratori</span>
            <h3 style="margin-top:10px;">Piano Premium Pro</h3>
            <div style="font-size: 2.2rem; font-weight: 800; color: #ff9100; margin: 10px 0;">10€ <span style="font-size:0.9rem; color:#777; font-weight:400;">/ mese</span></div>
            <p style="font-size:0.9rem; color:var(--text-muted);">Mettiti in cima alle preferenze dei ristoranti e ottieni più turni.</p>
            <ul style="padding-left:18px; color:#555; font-size:0.9rem; line-height:1.6;">
                <li>Priorità sul pallino verde lampeggiante</li>
                <li>Badge esclusivo "Top Verified"</li>
                <li>Anteprima notifiche sui nuovi turni liberi</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Passa a Premium Lavoratore", key="btn_sub_lav"):
            st.success("Account aggiornato con successo allo status Premium!")