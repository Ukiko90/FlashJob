import html
import re
import streamlit as st

st.set_page_config(
    page_title="Flashjob • Enterprise Hub",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# DATI E STATO
# ============================================================
if "lavoratori" not in st.session_state:
    st.session_state.lavoratori = [
        {
            "nome": "Marco Rossi",
            "mansione": "Cameriere / Sala",
            "zona": "Navigli, Milano",
            "tel": "+39 333 1234567",
            "completati": 18,
            "referenze": "Puntuale, professionale e con ottime capacità di gestione sala anche nei momenti di massimo afflusso.",
        },
        {
            "nome": "Sara Bianchi",
            "mansione": "Barista / Bartender",
            "zona": "Porta Romana, Milano",
            "tel": "+39 340 9876543",
            "completati": 24,
            "referenze": "Eccezionale nella mixology, rapidissima e dotata di grande empatia con la clientela.",
        },
    ]

if "selected_candidate" not in st.session_state:
    st.session_state.selected_candidate = None


def safe(value):
    return html.escape(str(value))


def whatsapp_url(phone):
    return "https://wa.me/" + re.sub(r"\D", "", phone)


# ============================================================
# DESIGN SYSTEM & STYLING
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

:root {
    --bg: #f0ebe3;
    --surface: rgba(255,255,255,.88);
    --surface-strong: #ffffff;
    --text: #17181b;
    --muted: #6b7280;
    --line: #e7e9ed;
    --blue: #1769ff;
    --blue-soft: #edf4ff;
    --green: #20a463;
    --green-soft: #eaf8f1;
    --shadow: 0 12px 40px rgba(17,24,39,.07);
    --radius: 18px;
}

html, body, [class*="css"] {
    font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.stApp {
    background: #f0ebe3;
    color: var(--text);
}

.block-container {
    max-width: 1180px !important;
    padding: 0 28px 60px !important;
}

[data-testid="stHeader"] { background: transparent; }
[data-testid="stToolbar"] { display: none; }
footer { visibility: hidden; }

/* HERO */
.hero {
    margin: 0 -28px 34px;
    padding: 54px 28px 42px;
    text-align: center;
    background: rgba(255,255,255,.82);
    border-bottom: 1px solid var(--line);
    box-shadow: 0 1px 0 rgba(0,0,0,.02);
    backdrop-filter: blur(10px);
}

.logo-mark {
    width: 48px;
    height: 48px;
    margin: 0 auto 15px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #17181b;
    color: #fff;
    font-size: 23px;
    font-weight: 700;
    box-shadow: 0 8px 20px rgba(0,0,0,.13);
}

.hero h1 {
    margin: 0;
    font-size: clamp(2.2rem, 5vw, 3.7rem);
    letter-spacing: -.055em;
    line-height: 1;
    font-weight: 700;
}

.hero p {
    max-width: 680px;
    margin: 15px auto 0;
    color: var(--muted);
    font-size: 1rem;
    line-height: 1.6;
}

/* NAV */
div[data-testid="stRadio"] > label { display: none; }
div[data-testid="stRadio"] div[role="radiogroup"] {
    width: fit-content;
    margin: 0 auto 34px;
    padding: 5px;
    gap: 3px;
    border: 1px solid var(--line);
    border-radius: 13px;
    background: rgba(255,255,255,.82);
    box-shadow: 0 4px 18px rgba(17,24,39,.04);
    backdrop-filter: blur(10px);
}
div[data-testid="stRadio"] div[role="radiogroup"] label {
    border-radius: 9px;
    padding: 8px 15px;
    color: #616873 !important;
    font-size: .82rem;
    font-weight: 600;
}
div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
    background: #f2f4f7;
}
div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
    background: #17181b;
    color: #fff !important;
}

/* TITOLI */
.section-title {
    margin: 0 0 7px;
    font-size: 1.55rem;
    letter-spacing: -.025em;
    font-weight: 700;
}
.section-subtitle {
    margin: 0 0 25px;
    color: var(--muted);
    line-height: 1.6;
    font-size: .94rem;
}

/* FULL BLEED HORIZONTAL SCROLL GALLERY */
.full-bleed-container {
    width: 100vw;
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    padding: 10px 4vw 25px 4vw;
    overflow-x: auto;
    display: flex;
    gap: 12px;
    scrollbar-width: thin;
    scroll-snap-type: x mandatory;
    scroll-padding-left: 4vw;
}

.full-bleed-container::-webkit-scrollbar { height: 6px; }
.full-bleed-container::-webkit-scrollbar-thumb {
    background: rgba(0,0,0,0.25);
    border-radius: 3px;
}

.full-bleed-item {
    flex: 0 0 420px;
    height: 280px;
    scroll-snap-align: start;
    border-radius: 14px;
    overflow: hidden;
    position: relative;
    box-shadow: 0 8px 24px rgba(0,0,0,0.12);
    background: #2a2a2a;
    border: 1px solid rgba(255,255,255,0.15);
}

@media (max-width: 768px) {
    .full-bleed-item {
        flex: 0 0 280px;
        height: 200px;
    }
}

.full-bleed-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
}

.full-bleed-item:hover img {
    transform: scale(1.03);
}

.full-bleed-caption {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 18px 20px;
    background: linear-gradient(transparent, rgba(0,0,0,0.85));
    color: #fff;
    font-size: 0.88rem;
    font-weight: 500;
    letter-spacing: -0.01em;
}

/* CARD */
.card {
    background: var(--surface);
    border: 1px solid rgba(17,24,39,.07);
    border-radius: var(--radius);
    padding: 25px;
    box-shadow: var(--shadow);
    backdrop-filter: blur(18px);
}
.card h3 { margin: 0 0 9px; font-size: 1.08rem; letter-spacing: -.015em; }
.card p, .card li { color: #626975; font-size: .9rem; line-height: 1.65; }
.card ul { margin: 12px 0 0; padding-left: 19px; }

/* PRICING CARD */
.price-tag {
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--text);
    margin: 12px 0 15px 0;
    letter-spacing: -.03em;
}
.price-tag span {
    font-size: .85rem;
    color: var(--muted);
    font-weight: 400;
}

/* BADGE */
.badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 5px 9px;
    border-radius: 999px;
    background: #f0f2f5;
    color: #515762;
    font-size: .66rem;
    font-weight: 700;
    letter-spacing: .07em;
    text-transform: uppercase;
}
.badge.blue { background: var(--blue-soft); color: var(--blue); }
.badge.green { background: var(--green-soft); color: var(--green); }

/* STATS */
.stats {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    margin: 24px 0;
    overflow: hidden;
    border: 1px solid var(--line);
    border-radius: 15px;
    background: #fafbfc;
}
.stat { padding: 17px 10px; text-align: center; border-right: 1px solid var(--line); }
.stat:last-child { border-right: 0; }
.stat strong { display: block; font-size: 1.35rem; letter-spacing: -.03em; }
.stat span {
    display: block;
    margin-top: 3px;
    color: var(--muted);
    font-size: .64rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .07em;
}

/* PROFILE */
.profile {
    max-width: 760px;
    margin: 0 auto;
    padding: 34px;
    background: var(--surface-strong);
    border: 1px solid var(--line);
    border-radius: 22px;
    box-shadow: var(--shadow);
    backdrop-filter: blur(18px);
}
.profile-head { display: flex; align-items: center; gap: 17px; }
.avatar {
    width: 72px;
    height: 72px;
    flex: 0 0 72px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid #fff;
    box-shadow: 0 5px 18px rgba(0,0,0,.12);
}
.profile h2 { margin: 0; font-size: 1.4rem; letter-spacing: -.03em; }
.role { margin: 4px 0 0; color: var(--blue); font-size: .88rem; font-weight: 600; }
.meta { margin: 4px 0 0; color: var(--muted); font-size: .78rem; }
.divider { height: 1px; margin: 25px 0; background: var(--line); }
.quote {
    padding: 17px 18px;
    border-left: 3px solid var(--blue);
    border-radius: 0 12px 12px 0;
    background: #f7f9fc;
    color: #3f4650;
    font-size: .9rem;
    line-height: 1.65;
}

/* DATABASE */
.worker { min-height: 165px; }
.worker-top { display: flex; align-items: flex-start; justify-content: space-between; gap: 15px; }
.worker h3 { margin: 0; font-size: 1.04rem; }
.worker-role { margin: 5px 0; color: #626975; font-size: .86rem; }
.worker-meta { color: var(--muted); font-size: .78rem; }
.worker-status { color: var(--green); font-size: .72rem; font-weight: 700; }

/* LEGAL */
.legal {
    margin-top: 48px;
    padding: 22px;
    border: 1px solid var(--line);
    border-radius: 16px;
    background: rgba(255,255,255,.62);
    color: #7b818a;
    font-size: .7rem;
    line-height: 1.65;
    backdrop-filter: blur(10px);
}
.legal b { color: #333840; }

/* STREAMLIT BUTTONS */
.stButton > button {
    width: 100%;
    min-height: 42px;
    border: 1px solid #17181b;
    border-radius: 11px;
    background: #17181b;
    color: #fff;
    font-weight: 600;
    font-size: .82rem;
    transition: all .15s ease;
}
.stButton > button:hover {
    border-color: #000;
    background: #000;
    color: #fff;
    transform: translateY(-1px);
}
.back-button .stButton > button {
    width: auto;
    background: transparent;
    color: #333840;
    border-color: var(--line);
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# HERO SECTION
# ============================================================
st.markdown("""
<div class="hero">
    <div class="logo-mark">⚡</div>
    <h1>Flashjob</h1>
    <p>
        Enterprise Workforce Hub per Hotel, Restaurant e Hospitality.
        Trova professionisti disponibili e copri i turni critici in pochi minuti.
    </p>
</div>
""", unsafe_allow_html=True)

scelta = st.radio(
    "Navigazione",
    [
        "Panoramica & Modello",
        "Database Aziendale",
        "Area Personale Lavoratore",
        "Piani & Abbonamenti ⚡",
    ],
    horizontal=True,
)

# ============================================================
# PANORAMICA & MODELLO
# ============================================================
if scelta == "Panoramica & Modello":
    st.markdown("""
<div class="section-title">Infrastruttura Operativa</div>
<div class="section-subtitle">
Flashjob mette in contatto aziende e professionisti hospitality attraverso
un database operativo con profili, disponibilità, storico e referenze.
</div>
""", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
<div class="card">
    <span class="badge blue">Area Aziende</span>
    <h3>Standard di Servizio</h3>
    <ul>
        <li>Profili professionali con referenze e storico verificabile.</li>
        <li>Selezione rapida per coprire assenze e picchi di lavoro.</li>
        <li>Contatto diretto con il professionista.</li>
        <li>Processo semplice, pensato per le esigenze operative.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div class="card">
    <span class="badge green">Area Lavoratori</span>
    <h3>Affidabilità & Compliance</h3>
    <ul>
        <li>Accesso gratuito alla piattaforma.</li>
        <li>Accettazione formale dell'offerta prima del turno.</li>
        <li>Storico delle collaborazioni completate.</li>
        <li>Policy di affidabilità e gestione delle assenze.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

    st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)

    st.markdown("""
<div class="section-title">Standard Visivo & Atmosfera</div>
<div class="section-subtitle">
Esplora la galleria full-bleed a scorrimento orizzontale con i momenti chiave del servizio hospitality.
</div>
""", unsafe_allow_html=True)

    img_url_1 = (
        "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=800&q=80"
    )
    img_url_2 = (
        "https://images.unsplash.com/photo-1514933651103-005eec06c04b?w=800&q=80"
    )
    img_url_3 = (
        "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80"
    )
    img_url_4 = (
        "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800&q=80"
    )

    st.markdown(
        f"""
<div class="full-bleed-container">
    <div class="full-bleed-item">
        <img src="{img_url_1}" alt="Cura del piatto">
        <div class="full-bleed-caption">Presentazione e cura sartoriale del piatto</div>
    </div>
    <div class="full-bleed-item">
        <img src="{img_url_2}" alt="Cocktail & Sound">
        <div class="full-bleed-caption">Atmosfera unica tra mixology e design</div>
    </div>
    <div class="full-bleed-item">
        <img src="{img_url_3}" alt="Servizio di sala">
        <div class="full-bleed-caption">Accoglienza e servizio impeccabile in sala</div>
    </div>
    <div class="full-bleed-item">
        <img src="{img_url_4}" alt="Food & Drink pairing">
        <div class="full-bleed-caption">Food pairing di alto livello per ogni evento</div>
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

# ============================================================
# DATABASE AZIENDALE
# ============================================================
elif scelta == "Database Aziendale":
    selected = st.session_state.selected_candidate

    if selected is not None:
        st.markdown('<div class="back-button">', unsafe_allow_html=True)
        if st.button("← Torna al database"):
            st.session_state.selected_candidate = None
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

        c = selected

        profile_html = f"""<div class="profile">
    <div class="profile-head">
        <img class="avatar" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300" alt="Profilo">
        <div>
            <h2>{safe(c["nome"])}</h2>
            <p class="role">{safe(c["mansione"])} · {safe(c["zona"])}</p>
            <p class="meta">● Disponibile per turni urgenti</p>
        </div>
    </div>
    <div class="divider"></div>
    <span class="badge">Performance</span>
    <div class="stats">
        <div class="stat">
            <strong>{safe(c["completati"])}</strong>
            <span>Turni completati</span>
        </div>
        <div class="stat">
            <strong>100%</strong>
            <span>Affidabilità</span>
        </div>
        <div class="stat">
            <strong>✓</strong>
            <span>Profilo verificato</span>
        </div>
    </div>
    <span class="badge">Referenza</span>
    <div class="quote">“{safe(c["referenze"])}”</div>
</div>"""

        st.markdown(profile_html, unsafe_allow_html=True)

        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

        st.link_button(
            "Contatta e prenota via WhatsApp →",
            whatsapp_url(c["tel"]),
            use_container_width=True,
        )

    else:
        st.markdown("""
<div class="section-title">Database Professionisti</div>
<div class="section-subtitle">
Seleziona un professionista per visualizzare profilo, storico e referenze.
</div>
""", unsafe_allow_html=True)

        for idx, lav in enumerate(st.session_state.lavoratori):
            left, right = st.columns([5, 1.7], gap="large")

            with left:
                worker_html = f"""<div class="card worker">
    <div class="worker-top">
        <div>
            <h3>{safe(lav["nome"])}</h3>
            <div class="worker-role">
                {safe(lav["mansione"])} · {safe(lav["zona"])}
            </div>
        </div>
        <div class="worker-status">● DISPONIBILE</div>
    </div>
    <div class="worker-meta">
        {safe(lav["completati"])} turni completati · Profilo verificato
    </div>
</div>"""
                st.markdown(worker_html, unsafe_allow_html=True)

            with right:
                st.markdown("<div style='height:42px'></div>", unsafe_allow_html=True)
                if st.button(
                    "Visualizza profilo",
                    key=f"profile_{idx}",
                    use_container_width=True,
                ):
                    st.session_state.selected_candidate = lav
                    st.rerun()

# ============================================================
# AREA LAVORATORE
# ============================================================
elif scelta == "Area Personale Lavoratore":
    st.markdown("""
<div class="section-title">Area Personale</div>
<div class="section-subtitle">
Gestisci il tuo profilo, monitora i turni e consulta lo storico delle attività.
</div>
""", unsafe_allow_html=True)

    area_html = """<div class="profile">
<div class="profile-head">
<img class="avatar" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300" alt="Giulia Rossi">
<div>
<h2>Giulia Rossi</h2>
<p class="role">Professionista Hospitality · Milano Centro</p>
<p class="meta">● Profilo verificato · +39 334 5678901</p>
</div>
</div>
<div class="stats">
<div class="stat">
<strong>03</strong>
<span>In attesa</span>
</div>
<div class="stat">
<strong>02</strong>
<span>In corso</span>
</div>
<div class="stat">
<strong>18</strong>
<span>Completati</span>
</div>
</div>
<span class="badge">Configurazione account</span>
<div class="card" style="margin-top:12px; box-shadow:none; background:#fafbfc;">
<div style="display:flex;justify-content:space-between;gap:20px;padding:7px 0;color:#343942;font-size:.88rem;">
<span>Lingua di sistema</span>
<strong>Italiano</strong>
</div>
<div style="height:1px;background:#e7e9ed;margin:9px 0;"></div>
<div style="display:flex;justify-content:space-between;gap:20px;padding:7px 0;color:#343942;font-size:.88rem;">
<span>Credenziali di sicurezza</span>
<span style="color:#8a9099;">›</span>
</div>
</div>
</div>"""

    st.markdown(area_html, unsafe_allow_html=True)

# ============================================================
# PIANI & ABBONAMENTI
# ============================================================
else:
    st.markdown("""
<div class="section-title">Listino Piani & Abbonamenti ⚡</div>
<div class="section-subtitle">
Scegli la soluzione su misura per la tua attività o per accelerare le tue opportunità di lavoro.
</div>
""", unsafe_allow_html=True)

    col_a, col_b = st.columns(2, gap="large")

    with col_a:
        st.markdown("""
<div class="card">
    <span class="badge blue">Aziende & Locali</span>
    <h3>Abbonamento Mensile Standard</h3>
    <div class="price-tag">20€ <span>/ mese</span></div>
    <p>Accesso illimitato al database dei professionisti hospitality e pubblicazione dei turni di copertura immediata.</p>
    <ul>
        <li>Ricerca avanzata per zona e mansione</li>
        <li>Contatto diretto e chat sbloccata</li>
        <li>Gestione completa delle emergenze di sala e cucina</li>
    </ul>
    <div style="margin-top: 22px;"></div>
</div>
""", unsafe_allow_html=True)
        if st.button("Attiva Abbonamento Azienda (20€/mo)"):
            st.success(
                "Richiesta di attivazione abbonamento aziendale registrata con successo!"
            )

        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

        st.markdown("""
<div class="card">
    <span class="badge blue">Add-on Urgenze</span>
    <h3>Job Boosting Urgente</h3>
    <div class="price-tag">5€ <span>/ settimana</span></div>
    <p>Per le emergenze critiche dell'ultimo minuto: metti in cima la tua richiesta e invia notifiche prioritarie.</p>
    <ul>
        <li>Posizionamento in evidenza nel feed dei lavoratori</li>
        <li>Notifica push prioritaria immediata in zona</li>
        <li>Copertura garantita in tempi record</li>
    </ul>
    <div style="margin-top: 22px;"></div>
</div>
""", unsafe_allow_html=True)
        if st.button("Lancia Job Boosting (5€/sett)"):
            st.success(
                "Job Boosting attivato! La tua richiesta è ora in evidenza tra i lavoratori."
            )

    with col_b:
        st.markdown("""
<div class="card">
    <span class="badge green">Professionisti & Lavoratori</span>
    <h3>Piano Lavoratore Premium</h3>
    <div class="price-tag">10€ <span>/ mese</span></div>
    <p>Massimizza le tue opportunità e sali in cima alle preferenze dei migliori ristoranti e hotel di Milano.</p>
    <ul>
        <li><strong>Profilo in Primo Piano</strong> nel database aziendale</li>
        <li><strong>Badge "Top Verified"</strong> per massima affidabilità</li>
        <li><strong>Anticipo Notifiche</strong> sui turni liberi in arrivo</li>
        <li>Zero commissioni sui guadagni dei turni</li>
    </ul>
    <div style="margin-top: 22px;"></div>
</div>
""", unsafe_allow_html=True)
        if st.button("Passa a Lavoratore Premium (10€/mo)"):
            st.success(
                "Ottimo! Il tuo account è stato aggiornato allo status Premium."
            )

# ============================================================
# LEGAL
# ============================================================
st.markdown("""
<div class="legal">
    <b>Note legali e regolamento Enterprise — Flashjob</b><br><br>
    La piattaforma è progettata come directory e bacheca di contatto B2B
    per il settore Hospitality & Restaurant. Le modalità effettive di
    selezione, ingaggio e collaborazione devono essere configurate in
    conformità alla normativa applicabile. La policy interna di affidabilità
    può prevedere la sospensione dell'accesso in caso di assenze ingiustificate
    reiterate.
</div>
""", unsafe_allow_html=True)