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
# STATO INIZIALE (DATABASE PUBBLICO VUOTO & PROFILO PERSONALE)
# ============================================================
if "lavoratori" not in st.session_state:
    st.session_state.lavoratori = []

if "selected_id" not in st.session_state:
    st.session_state.selected_id = None

if "mio_profilo" not in st.session_state:
    st.session_state.mio_profilo = {
        "id": 999,
        "nome": "Il Tuo Nome",
        "mansione": "Cameriere / Sala",
        "zona": "Milano",
        "tel": "+39 333 0000000",
        "completati": 0,
        "disponibile": False,
        "referenze": "Professionista verificato nel settore HORECA.",
    }


def safe(value):
    return html.escape(str(value))


def whatsapp_url(phone):
    return "https://wa.me/" + re.sub(r"\D", "", phone)


# ============================================================
# DESIGN SYSTEM: UI FLUIDA E PULITA
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

/* STORE HEADER */
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

/* PALLINO VERDE LAMPEGGIANTE */
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
# STORE HEADER
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
# 1. PANORAMICA (COSA FACCIAMO & COME FUNZIONA)
# ============================================================
if scelta == "Panoramica":
    st.markdown(
        """
        <div style="text-align: center; max-width: 800px; margin: 0 auto 2.5rem auto;">
            <span class="badge-pop badge-purple">Il tuo partner strategico HORECA</span>
            <h2 style='font-weight:800; font-size:2.2rem; margin-top:10px; color:#211e33;'>Rivoluzioniamo il modo in cui il lavoro incontra il talento.</h2>
            <p style='color:var(--text-muted); font-size:1.1rem; line-height:1.6; margin-top:10px;'>Flashjob è la piattaforma intelligente progettata per azzerare i tempi morti del recruiting nella ristorazione e nell'ospitalità. Che tu sia un locale in cerca di supporto immediato o un professionista pronto a scendere in campo, noi facciamo una sola cosa: ti connettiamo in tempo zero.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
        <div class="custom-card" style="height: 100%;">
            <span class="badge-pop badge-blue">Per i Ristoratori & Locali</span>
            <h3 style="font-size: 1.3rem; margin-top: 5px;">Cerca il professionista perfetto, senza attese</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6;">
                Un'emergenza in sala o un picco di lavoro inaspettato? Con Flashjob non devi sfogliare centinaia di CV cartacei o fare decine di chiamate a vuoto. 
            </p>
            <ul style="padding-left: 18px; color: #444; font-size: 0.9rem; line-height: 1.6; margin-top: 15px;">
                <li><b>Filtri di precisione:</b> Seleziona mansione, zona di Milano o competenze specifiche con un click.</li>
                <li><b>Indicatori di stato live:</b> Visualizza all'istante chi ha il pallino verde acceso, segnalando di essere libero e pronto a lavorare adesso.</li>
                <li><b>Contatto diretto:</b> Accedi subito al numero verificato e avvia la trattativa o la prenotazione tramite chat istantanea.</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="custom-card" style="height: 100%;">
            <span class="badge-pop badge-purple">Per i Lavoratori HORECA</span>
            <h3 style="font-size: 1.3rem; margin-top: 5px;">Il lavoro cerca te, esattamente quando vuoi</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6;">
                Sei un cameriere, un barista, uno chef de rang o un aiuto cuoco? Gestisci i tuoi turni e la tua libertà professionale senza intermediari.
            </p>
            <ul style="padding-left: 18px; color: #444; font-size: 0.9rem; line-height: 1.6; margin-top: 15px;">
                <li><b>Disponibilità a comando:</b> Accendi il tuo profilo dall'Area Lavoratore e renditi visibile a decine di ristoranti in cerca di rinforzi.</li>
                <li><b>Massima flessibilità:</b> Lavora quando ti è più comodo, gestendo i tuoi impegni in totale autonomia.</li>
                <li><b>Visibilità garantita:</b> Mettiti in mostra con recensioni verificate, storico turni e referenze certificate.</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

# ============================================================
# 2. DATABASE & FILTRI AZIENDA
# ============================================================
elif scelta == "Database & Filtri Azienda":
    selected_c = next(
        (
            item
            for item in st.session_state.lavoratori
            if item["id"] == st.session_state.selected_id
        ),
        None,
    )

    if selected_c is not None:
        if st.button("← Torna al database completo"):
            st.session_state.selected_id = None
            st.rerun()

        stato_html = (
            '<span class="pulsing-dot"></span><b style="color:#059669;">DISPONIBILE ORA</b>'
            if selected_c["disponibile"]
            else '<span class="offline-dot"></span><span style="color:#888;">NON DISPONIBILE</span>'
        )

        st.markdown(
            f"""
        <div class="custom-card" style="margin-top: 20px;">
            <div style="display: flex; align-items: center; gap: 20px;">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300" style="width:80px; height:80px; border-radius:50%; object-fit:cover; border:3px solid #a78bfa;" />
                <div>
                    <div style="margin-bottom:6px;">{stato_html}</div>
                    <h2 style="margin:0; font-size:1.5rem;">{safe(selected_c["nome"])}</h2>
                    <p style="color:var(--text-muted); margin:4px 0 0 0; font-weight:600;">{safe(selected_c["mansione"])} · {safe(selected_c["zona"])}</p>
                </div>
            </div>
            
            <div class="stats-container">
                <div class="stat-box">
                    <strong>{safe(selected_c["completati"])}</strong>
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
                “{safe(selected_c["referenze"])}”
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.link_button(
            "💬 Contatta e Prenota su WhatsApp",
            whatsapp_url(selected_c["tel"]),
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
                key="filtro_mansione_box",
            )

        with col_f2:
            solo_disponibili = st.checkbox(
                "Mostra solo disponibili con pallino verde",
                value=False,
                key="filtro_disp_box",
            )

        with col_f3:
            ricerca_testo = st.text_input(
                "Cerca per nome o zona",
                placeholder="Es. Navigli o Marco...",
                key="filtro_testo_box",
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

        if not lavoratori_filtrati:
            st.info(
                "Nessun lavoratore trovato nel database al momento. I"
                " lavoratori possono registrarsi o attivarsi dall'Area"
                " Lavoratore."
            )

        for lav in lavoratori_filtrati:
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
                if st.button("Vedi profilo", key=f"btn_card_{lav['id']}"):
                    st.session_state.selected_id = lav["id"]
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

    mio = st.session_state.mio_profilo

    st.markdown(
        f"""
    <div class="custom-card">
        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 1.5rem;">
            <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300" style="width:70px; height:70px; border-radius:50%; object-fit:cover;" />
            <div>
                <h3 style="margin:0;">{safe(mio["nome"])}</h3>
                <p style="color:var(--text-muted); margin:2px 0; font-size:0.85rem;">{safe(mio["mansione"])} · {safe(mio["zona"])}</p>
                <span class="badge-pop badge-purple" style="margin:0;">Profilo Verificato</span>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("### Gestione Stato in Tempo Reale")
    nuova_disp = st.toggle(
        "🟢 Attiva disponibilità per lavorare (Accendi pallino verde lampeggiante)",
        value=mio["disponibile"],
        key="toggle_disponibilita_lavoratore",
    )

    if nuova_disp != mio["disponibile"]:
        mio["disponibile"] = nuova_disp
        trovato = next(
            (item for item in st.session_state.lavoratori if item["id"] == mio["id"]),
            None,
        )
        if nuova_disp:
            if trovato:
                trovato["disponibile"] = True
            else:
                st.session_state.lavoratori.append(mio.copy())
        else:
            if trovato:
                st.session_state.lavoratori = [
                    item
                    for item in st.session_state.lavoratori
                    if item["id"] != mio["id"]
                ]

        st.success(
            "Stato aggiornato con successo nel database! I ristoranti vedranno"
            " immediatamente la modifica."
        )

    if mio["disponibile"]:
        st.markdown(
            """
        <div style="background:#ecfdf5; color:#059669; padding:12px; border-radius:12px; font-weight:700; margin-top:15px;">
            <span class="pulsing-dot"></span> Il tuo profilo è attualmente ONLINE con il pallino verde lampeggiante nel database pubblico!
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
# 4. PIANI & ABBONAMENTI (COMING SOON 🚀)
# ============================================================
else:
    st.markdown(
        """
        <h2 style='font-weight:800; font-size:1.8rem; margin-bottom:5px;'>Piani & Funzioni Elite ⚡</h2>
        <p style='color:var(--text-muted); margin-bottom:2rem;'>Stiamo preparando strumenti rivoluzionari per connettere locali e professionisti HORECA alla massima velocità. Scopri cosa sta arrivando!</p>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown(
            """
        <div class="custom-card">
            <span class="badge-pop badge-blue">Coming Soon 🚀</span>
            <h3 style="margin-top:10px; font-size:1.2rem;">Aziende Elite</h3>
            <div style="font-size: 1.4rem; font-weight: 800; color: #0284c7; margin: 10px 0;">Accesso Anticipato</div>
            <p style="font-size:0.85rem; color:var(--text-muted);">Hai un locale e vuoi sbloccare ricerche illimitate senza attese?</p>
            <ul style="padding-left:16px; color:#555; font-size:0.85rem; line-height:1.5;">
                <li>Matchmaking IA con i candidati</li>
                <li>Gestione emergenze last-minute in 1 click</li>
                <li>Zero commissioni sulle chiamate</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Mettiti in Lista d'Attesa", key="btn_std"):
            st.toast(
                "Ottimo! Ti sei iscritto alla lista d'attesa prioritaria"
                " Aziende. Ti avviseremo al lancio!"
            )

    with col2:
        st.markdown(
            """
        <div class="custom-card">
            <span class="badge-pop badge-orange">Coming Soon 🌟</span>
            <h3 style="margin-top:10px; font-size:1.2rem;">Lavoratore Pro Pass</h3>
            <div style="font-size: 1.4rem; font-weight: 800; color: #ea580c; margin: 10px 0;">Presto Disponibile</div>
            <p style="font-size:0.85rem; color:var(--text-muted);">Vuoi saltare la fila e finire dritto in cima alle preferenze dei migliori locali?</p>
            <ul style="padding-left:16px; color:#555; font-size:0.85rem; line-height:1.5;">
                <li>Badge esclusivo "Top Verified Pro"</li>
                <li>Notifiche anticipate per i turni più remunerativi</li>
                <li>Visibilità prioritaria garantita</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Avvisami al Lancio", key="btn_prem"):
            st.toast(
                "Registrato con successo! Sarai tra i primi a testare il Pro"
                " Pass."
            )

    with col3:
        st.markdown(
            """
        <div class="custom-card">
            <span class="badge-pop badge-yellow">Coming Soon ⚡</span>
            <h3 style="margin-top:10px; font-size:1.2rem;">Radar Urgenze VIP</h3>
            <div style="font-size: 1.4rem; font-weight: 800; color: #ca8a04; margin: 10px 0;">In Fase di Test</div>
            <p style="font-size:0.85rem; color:var(--text-muted);">La funzione segreta per chi cerca o offre aiuto nel weekend in tempo zero.</p>
            <ul style="padding-left:16px; color:#555; font-size:0.85rem; line-height:1.5;">
                <li>Allarmi radar geolocalizzati live</li>
                <li>Filtro ultra-rapido per urgenze notturne</li>
                <li>Posti limitati per i primi aderenti</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Richiedi Accesso Anteprima", key="btn_boost"):
            st.toast(
                "Richiesta inviata! Ti contatteremo per l'accesso in anteprima"
                " esclusiva."
            )