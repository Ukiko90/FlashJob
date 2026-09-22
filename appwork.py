import html
import re
import streamlit as st

st.set_page_config(
    page_title="Flashjob • Freelance Marketplace",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ============================================================
# DESIGN SYSTEM & STYLING (ISPIRATO ALL'APP DI RIFERIMENTO)
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --bg-color: #0f1110;
    --surface-card: #222724;
    --accent-yellow: #d5ff00;
    --text-main: #ffffff;
    --text-muted: #8c9690;
    --border-color: rgba(255, 255, 255, 0.08);
    --radius-pill: 9999px;
    --radius-card: 28px;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--text-main);
}

.stApp {
    background-color: var(--bg-color);
}

/* Nascondi elementi di default di Streamlit */
#MainMenu {visibility: hidden; display: none;}
footer {visibility: hidden; display: none;}
header {visibility: hidden; display: none;}
[data-testid="stHeader"] {display: none !important;}
[data-testid="stToolbar"] {display: none !important;}
[data-testid="stDecoration"] {display: none !important;}

.block-container {
    max-width: 440px !important;
    padding: 2rem 1.2rem 5rem !important;
}

/* Card stile marketplace */
.custom-card {
    background-color: var(--surface-card);
    border-radius: var(--radius-card);
    padding: 24px;
    border: 1px solid var(--border-color);
    margin-bottom: 20px;
}

/* Card in evidenza (Giallo Neon) */
.highlight-card {
    background-color: var(--accent-yellow);
    color: #000000;
    border-radius: var(--radius-card);
    padding: 24px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

.badge-meta {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid var(--border-color);
    padding: 6px 14px;
    border-radius: var(--radius-pill);
    font-size: 12px;
    color: var(--text-muted);
    display: inline-flex;
    align-items: center;
    gap: 6px;
    margin-right: 6px;
    margin-bottom: 6px;
}

/* Bottoni personalizzati */
.stButton > button {
    width: 100%;
    min-height: 52px;
    border-radius: var(--radius-pill);
    background-color: var(--accent-yellow);
    color: #000000;
    font-weight: 700;
    font-size: 15px;
    border: none;
    box-shadow: 0 8px 25px rgba(213, 255, 0, 0.25);
    transition: transform 0.2s ease;
}
.stButton > button:hover {
    opacity: 0.92;
    transform: scale(0.99);
    color: #000000;
    background-color: var(--accent-yellow);
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# STATO DELLA SESSIONE (NAVIGAZIONE TRA LE 3 SCHERMATE)
# ============================================================
if "screen" not in st.session_state:
    st.session_state.screen = "search"  # 'roles', 'search', 'detail'

if "selected_freelancer" not in st.session_state:
    st.session_state.selected_freelancer = {
        "nome": "Jasmin Lowery",
        "ruolo": "Senior Hardware Engineer",
        "tariffa": "$2400 / month",
        "città": "New York",
        "esperienza": "3+ year",
        "tipo": "Full-time",
        "bio": "Hey there! I'm your perfect freelancer for all your hardware engineering projects. 🛠️ Working with me is easy and enjoyable; I'm always ready to dive into the details.",
        "responsabilita": [
            "Developing and designing hardware components for various devices.",
            "Testing and debugging electronic circuits and printed circuit boards.",
        ],
    }

if "roles" not in st.session_state:
    st.session_state.roles = {
        "Product Designer": False,
        "Business Analyst": True,
        "Web Design": False,
        "Database Analyst": False,
        "Data Analyst": False,
        "Software Engineer": False,
        "DevOps Engineer": True,
        "Hardware Engineer": False,
        "Ruby Developer": True,
        "Frontend Developer": False,
        "Swift Developer": False,
        "IT Consultant": False,
        "Cloud Architect": False,
        "Maker-up": True,
        "Backend Developer": False,
        "Systems Administrator": False,
        "Web Developer": False,
        "Programmer": True,
    }


def safe(value):
    return html.escape(str(value))


# ============================================================
# SCHERMATA 1: SELEZIONE RUOLI (Filtri con tag pillola)
# ============================================================
if st.session_state.screen == "roles":
    col_h1, col_h2 = st.columns([6, 1])
    with col_h1:
        if st.button("← Indietro", key="back_r"):
            st.session_state.screen = "search"
            st.rerun()
    with col_h2:
        if st.button("Skip", key="skip_r"):
            st.session_state.screen = "search"
            st.rerun()

    st.markdown(
        "<h1 style='font-size: 26px; font-weight: 700; margin-top: 15px; margin-bottom: 20px;'>Select the role that suits your needs best</h1>",
        unsafe_allow_html=True,
    )

    if st.button("Seleziona / Deseleziona Tutti", key="toggle_all_btn"):
        current_state = all(st.session_state.roles.values())
        for r in st.session_state.roles:
            st.session_state.roles[r] = not current_state
        st.rerun()

    st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)

    # Griglia di chip interattivi
    for role_name in list(st.session_state.roles.keys()):
        is_sel = st.session_state.roles[role_name]
        label = f"✓ {role_name}" if is_sel else role_name
        if st.button(label, key=f"role_chip_{role_name}"):
            st.session_state.roles[role_name] = not is_sel
            st.rerun()

    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
    if st.button("Continue", key="continue_roles"):
        st.session_state.screen = "search"
        st.rerun()

# ============================================================
# SCHERMATA 2: RICERCA E SCHEDE SOVRAPPOSTE (Card Stack)
# ============================================================
elif st.session_state.screen == "search":
    col_top1, col_top2 = st.columns([3, 1])
    with col_top1:
        st.markdown(
            """
            <h1 style='font-size: 30px; font-weight: 800; line-height: 1.1; margin:0;'>Search<br>freelancers</h1>
            <p style='color: var(--text-muted); font-size: 13px; margin-top: 6px;'>DevOps Engineer</p>
        """,
            unsafe_allow_html=True,
        )
    with col_top2:
        if st.button("⚙️ Filters", key="open_filters"):
            st.session_state.screen = "roles"
            st.rerun()

    st.markdown(
        "<p style='color: var(--text-muted); font-size: 12px; margin-top: 15px; margin-bottom: 10px;'>238 results</p>",
        unsafe_allow_html=True,
    )

    # Simulazione della card in primo piano (stile identico all'immagine)
    f = st.session_state.selected_freelancer
    st.markdown(
        f"""
    <div class="highlight-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px;">
            <div style="width: 48px; height: 48px; border-radius: 50%; background: #000; overflow: hidden; display: flex; align-items: center; justify-content: center; font-size: 20px;">👤</div>
            <div style="width: 40px; height: 40px; background: rgba(0,0,0,0.08); border-radius: 50%; display: flex; align-items: center; justify-content: center;">💬</div>
        </div>
        <h2 style="font-size: 26px; font-weight: 800; margin: 0; color: #000;">{safe(f["nome"])}</h2>
        <p style="font-size: 14px; font-weight: 600; opacity: 0.7; margin: 4px 0 35px 0; color: #000;">{safe(f["ruolo"])}</p>
        
        <div style="display: flex; justify-content: space-between; align-items: flex-end;">
            <div>
                <span style="font-size: 22px; font-weight: 800; color: #000;">{safe(f["tariffa"].split('/')[0])}</span>
                <span style="font-size: 12px; font-weight: 600; opacity: 0.7; color: #000;">/ month</span>
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    if st.button("See details", key="btn_see_details"):
        st.session_state.screen = "detail"
        st.rerun()

    # Barra di navigazione finta in basso
    st.markdown(
        """
    <div style="display: flex; justify-content: space-around; background: var(--surface-card); padding: 12px; border-radius: var(--radius-pill); border: 1px solid var(--border-color); margin-top: 25px;">
        <span style="background: var(--accent-yellow); color: #000; width: 38px; height: 38px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">💼</span>
        <span style="color: var(--text-muted); display: flex; align-items: center; justify-content: center;">🔍</span>
        <span style="color: var(--text-muted); display: flex; align-items: center; justify-content: center;">👤</span>
    </div>
    """,
        unsafe_allow_html=True,
    )

# ============================================================
# SCHERMATA 3: DETTAGLIO PROFILO & RESPONSABILITÀ
# ============================================================
elif st.session_state.screen == "detail":
    if st.button("← Indietro alla ricerca", key="back_to_search"):
        st.session_state.screen = "search"
        st.rerun()

    f = st.session_state.selected_freelancer

    st.markdown(
        f"""
    <div class="custom-card">
        <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 14px;">
            <div style="width: 56px; height: 56px; border-radius: 50%; background: #333; display: flex; align-items: center; justify-content: center; font-size: 22px;">👩‍💻</div>
            <div>
                <h2 style="font-size: 18px; font-weight: 700; margin: 0;">{safe(f["nome"])}</h2>
                <p style="font-size: 13px; color: var(--text-muted); margin: 2px 0 0 0;">{safe(f["ruolo"])}</p>
            </div>
        </div>
        
        <div style="margin-bottom: 14px;">
            <span class="badge-meta">📍 {safe(f["città"])}</span>
            <span class="badge-meta">🕒 {safe(f["esperienza"])}</span>
            <span class="badge-meta">💼 {safe(f["tipo"])}</span>
        </div>
        
        <p style="font-size: 13px; color: var(--text-muted); line-height: 1.5; margin: 0;">
            {safe(f["bio"])}
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Tab di navigazione finti
    st.markdown(
        """
    <div style="display: flex; gap: 20px; border-bottom: 1px solid var(--border-color); margin-bottom: 20px; padding-bottom: 8px;">
        <span style="color: var(--accent-yellow); font-weight: 700; font-size: 14px; border-bottom: 2px solid var(--accent-yellow); padding-bottom: 8px; margin-bottom: -9px;">Responsibilities</span>
        <span style="color: var(--text-muted); font-weight: 600; font-size: 14px;">Experience</span>
        <span style="color: var(--text-muted); font-weight: 600; font-size: 14px;">Education</span>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Lista responsabilità
    for idx, resp in enumerate(f["responsabilita"], start=1):
        st.markdown(
            f"""
        <div class="custom-card" style="padding: 14px 18px; display: flex; align-items: center; gap: 14px; margin-bottom: 10px;">
            <div style="width: 24px; height: 24px; background: rgba(213,255,0,0.15); color: var(--accent-yellow); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700; flex-shrink: 0;">{idx}</div>
            <span style="font-size: 13px; color: var(--text-main);">{safe(resp)}</span>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
    if st.button("Send Message", key="send_msg_btn"):
        st.success(f"Messaggio inviato con successo a {f['nome']}! 🎉")