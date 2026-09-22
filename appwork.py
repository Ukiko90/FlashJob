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
# DESIGN SYSTEM: APP STORE STYLE & SFUMATURE PASTELLO LUMINOSE
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

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stHeader"] { display: none !important; }
[data-testid="stToolbar"] { display: none !important; }

/* HEADER STILE APP STORE / STORE UFFICIALE */
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
.app-badges-right {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}
.store-badge {
    background: #111;
    color: white;
    padding: 10px 16px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 700;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
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
    font-size: 0.82rem;
    color: var(--text-muted) !important;
    transition: all 0.3s ease;
}
div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
    background: linear-gradient(135deg, #a78bfa 0%, #60a5fa 100%) !important;
    color: white !important;
    box-shadow: 0 4px 15px rgba(167, 139, 250, 0.3);
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

/* PALLINO VERDE LAMPEGGIANTE (PULSAR) */
@keyframes pulse-animation {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.6); }
    70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(52, 211, 153, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(52, 211, 153, 0); }
}

.pulsing-dot {
    display: inline-block;
    width: 12px;
    height: 12px;
    background-color: #34d399;
    border-radius: 50%;
    animation: pulse-animation 1.8s infinite;
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

/* BADGE PASTELLO CHIARI */
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
.badge-orange { background: #ffedd5; color: #ea580c; }
.badge-yellow { background: #fef9c3; color: #ca8a04; }

/* STATS */
.stats-container {
    display: flex;
    background: #f8fafc;
    border-radius: 16px;
    padding: 1rem;
    margin: 1.2rem 0;
    text-align: center;
    border: 1px solid #f1f5f9;
}
.stat-box { flex: 1; border-right: 1px solid #e2e8f0; }
.stat-box:last-child { border-right: none; }
.stat-box strong { display: block; font-size: 1.3rem; color: #8b5cf6; }
.stat-box span { font-size: 0.7rem; color: #7d7a92; font-weight: 700; text-transform: uppercase; }

/* BOTTONI */
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
# STORE HEADER (LOGO E NOME IN EVIDENZA)
# ============================================================
st.markdown(
    """
<div class="store-header">
    <div class="app-info-left">
        <div class="app-logo-box">⚡</div>
        <div class="app-titles">
            <h1>Flashjob</h1>
            <p>Il Lavoro a Portata di Mano • Disponibile per ogni mansione HORECA</p>
        </div>
    </div>
    <div class="app-badges-right">
        <div class="store-badge">🍏 App Store Ufficiale</div>
        <div class="store-badge">🤖 Google Play Ufficiale</div>
    </div>
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
# 1. PANORAMICA
# ============================================================
if scelta == "Panoramica":
    st.markdown(
        """
        <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Come funziona il Database Live</h2>
        <p style='color:var(--text-muted); margin-bottom:2rem;'>I dipendenti di qualsiasi mansione impostano la propria disponibilità e i ristoratori filtrano i profili per trovare subito chi serve.</p>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown(
            """
        <div class="custom-card">
            <span class="badge-pop badge-blue">Per i Ristoratori</span>
            <h3>Filtri e Ricerca Rapida</h3>
            <p>Seleziona la mansione o la zona per visualizzare all'istante qualsiasi profilo con il pallino verde acceso e pronto a lavorare.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
        <div class="custom-card">
            <span class="badge-pop badge-purple">Per i Lavoratori</span>
            <h3>Disponibilità Istantanea</h3>
            <p>Qualunque sia il tuo ruolo, attiva l'interfaccia: il tuo profilo si illumina con un indicatore verde lampeggiante visibile a tutti i locali.</p>
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
        if st.button("← Torna al database completo"):
            st.session_state.selected_candidate = None
            st.rerun()

        c = selected
        stato_html = (
            '<span class="pulsing-dot"></span><b style="color:#059669;">DISPONIBILE ORA</b>'
            if c["disponibile"]
            else '<span class="offline-dot"></span><span style="color:#888;">NON DISPONIBILE</span>'
        )

        st.markdown(
            f"""
        <div class="custom-card" style="margin-top: 20px;">
            <div style="display: flex; align-items: center; gap: 20px;">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300" style="width:80px; height:80px; border-radius:50%; object-fit:cover; border:3px solid #a78bfa;" />
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
            
            <div style="background:#f3e8ff; border-left:4px solid #a78bfa; padding:15px; border-radius:0 12px 12px 0; margin-top:15px; font-style:italic; color:#6b21a8;">
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
            <p style='color:var(--text-muted); margin-bottom:1.5rem;'>Cerca tra tutte le mansioni disponibili per trovare subito la risorsa ideale.</p>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="custom-card" style="padding: 1.2rem; background: #fafafa;">',
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
            f"<p style='color:#7d7a92; font-size:0.9rem; margin: 1rem 0;'>Trovati <b>{len(lavoratori_filtrati)}</b> professionisti in archivio.</p>",
            unsafe_allow_html=True,
        )

        for idx, lav in enumerate(lavoratori_filtrati):
            col_info, col_btn = st.columns([3, 1], gap="medium")

            with col_info:
                if lav["disponibile"]:
                    badge_stato = '<span class="pulsing-dot"></span><b style="color:#059669; font-size:0.75rem;">DISPONIBILE ORA</b>'
                else:
                    badge_stato = '<span class="offline-dot"></span><span style="color:#888; font-size:0.75rem;">NON DISPONIBILE</span>'

                st.markdown(
                    f"""
                <div class="custom-card" style="margin-bottom:1rem; padding:1.2rem 1.5rem;">
                    <div style="margin-bottom:6px;">{badge_stato}</div>
                    <h3 style="margin:0; font-size:1.15rem;">{safe(lav["nome"])}</h3>
                    <p style="color:var(--text-muted); margin:3px 0; font-size:0.9rem; font-weight:600;">{safe(lav["mansione"])} · {safe(lav["zona"])}</p>
                    <span style="font-size:0.8rem; color:#888;">{safe(lav["completati"])} turni completati</span>
                </div>
                """,
                    unsafe_allow_html=True,
                )

            with col_btn:
                st.markdown(
                    "<div style='margin-top: 30px;'></div>", unsafe_allow_html=True
                )
                if st.button("Vedi profilo", key=f"btn_db_{lav['id']}DATA"):
                    st.session_state.selected_candidate = lav
                    st.rerun()

# ============================================================
# 3. AREA LAVORATORE
# ============================================================
elif scelta == "Area Lavoratore (Imposta Disponibilità)":
    st.markdown(
        """
        <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Area Personale Lavoratore</h2>
        <p style='color:var(--text-muted); margin-bottom:2rem;'>Modifica il tuo stato per qualsiasi mansione: accendi la disponibilità per farti contattare subito.</p>
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
                <span class="badge-pop badge-purple" style="margin:0;">Profilo Verificato</span>
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
        <div style="background:#ecfdf5; color:#059669; padding:12px; border-radius:12px; font-weight:700; margin-top:15px;">
            <span class="pulsing-dot"></span> Il tuo profilo è attualmente ONLINE con il pallino verde lampeggiante!
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
# 4. PIANI & ABBONAMENTI (INCLUSO BOOST WEEKEND)
# ============================================================
else:
    st.markdown(
        """
        <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Listino & Upgrade ⚡</h2>
        <p style='color:var(--text-muted); margin-bottom:2rem;'>Soluzioni flessibili per ogni mansione e tipo di locale.</p>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown(
            """
        <div class="custom-card">
            <span class="badge-pop badge-blue">Aziende & Locali</span>
            <h3 style="margin-top:10px; font-size:1.2rem;">Standard</h3>
            <div style="font-size: 1.8rem; font-weight: 800; color: #0284c7; margin: 10px 0;">20€ <span style="font-size:0.8rem; color:#777; font-weight:400;">/ mese</span></div>
            <p style="font-size:0.85rem; color:var(--text-muted);">Accesso completo ai filtri e database per tutte le mansioni.</p>
            <ul style="padding-left:16px; color:#555; font-size:0.85rem; line-height:1.5;">
                <li>Filtri per ogni ruolo e zona</li>
                <li>Contatto diretto WhatsApp</li>
                <li>Gestione urgenze illimitata</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Attiva Azienda", key="btn_std"):
            st.success("Abbonamento Azienda attivato con successo!")

    with col2:
        st.markdown(
            """
        <div class="custom-card">
            <span class="badge-pop badge-orange">Lavoratori</span>
            <h3 style="margin-top:10px; font-size:1.2rem;">Premium Pro</h3>
            <div style="font-size: 1.8rem; font-weight: 800; color: #ea580c; margin: 10px 0;">10€ <span style="font-size:0.8rem; color:#777; font-weight:400;">/ mese</span></div>
            <p style="font-size:0.85rem; color:var(--text-muted);">Mettiti in cima alle preferenze dei ristoranti.</p>
            <ul style="padding-left:16px; color:#555; font-size:0.85rem; line-height:1.5;">
                <li>Priorità sul pallino verde</li>
                <li>Badge "Top Verified"</li>
                <li>Notifiche anticipate turni</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Passa a Premium", key="btn_prem"):
            st.success("Account aggiornato a Premium Pro!")

    with col3:
        st.markdown(
            """
        <div class="custom-card">
            <span class="badge-pop badge-yellow">⚡ Novità</span>
            <h3 style="margin-top:10px; font-size:1.2rem;">Boost Weekend</h3>
            <div style="font-size: 1.8rem; font-weight: 800; color: #ca8a04; margin: 10px 0;">5€ <span style="font-size:0.8rem; color:#777; font-weight:400;">/ settimana</span></div>
            <p style="font-size:0.85rem; color:var(--text-muted);">Disponibile a lavorare nel weekend in evidenza.</p>
            <ul style="padding-left:16px; color:#555; font-size:0.85rem; line-height:1.5;">
                <li>In evidenza Sabato e Domenica</li>
                <li>Visibilità prioritaria urgenze</li>
                <li>Disdetta facile quando vuoi</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Attiva Boost Weekend", key="btn_boost"):
            st.success(
                "Boost Weekend attivato! Sarai in evidenza per tutto il fine"
                " settimana."
            )