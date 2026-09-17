import streamlit as st

st.set_page_config(page_title="Fla⚡️hJob - H&R Hub", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .block-container { padding: 0rem 3rem 2rem 3rem; max-width: 100% !important; }
    .stApp { background: #000000; color: #f8fafc; }
    .content-wrapper { max-width: 950px; margin: 0 auto; }
    .hero-full-bleed { width: 100vw; position: relative; left: 50%; right: 50%; margin-left: -50vw; margin-right: -50vw; background-image: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.85)), url('https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=1800'); background-size: cover; background-position: center; color: white; padding: 90px 20px; text-align: center; margin-bottom: 40px; }
    .brand-title { color: white; font-size: 3.5rem; font-weight: 900; letter-spacing: -3px; }
    .feature-card { background: #111111; padding: 25px; border-radius: 16px; margin-bottom: 20px; border: 1px solid #333333; color: #f8fafc; }
    .badge-tag { background-color: #fef08a; color: #713f12; padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; display: inline-block; margin-bottom: 10px; }
    .profile-container { background: #111111; border: 1px solid #333333; border-radius: 24px; padding: 30px; max-width: 700px; margin: 0 auto 30px auto; text-align: center; }
    .profile-img { width: 90px; height: 90px; border-radius: 50%; object-fit: cover; border: 3px solid #4ade80; margin: 0 auto 15px auto; }
    .profile-stats-row { display: flex; justify-content: space-around; background: #18181b; border: 1px solid #27272a; border-radius: 16px; padding: 15px; margin: 20px 0; }
    .menu-item-card { background: #18181b; border: 1px solid #27272a; border-radius: 14px; padding: 16px 20px; margin-bottom: 12px; display: flex; align-items: center; justify-content: space-between; color: #f8fafc; text-align: left; }
    .framed-gallery-container { width: 100%; max-width: 950px; margin: 40px auto; background: #161616; border-radius: 20px; border: 1px solid #333333; overflow: hidden; }
    .image-strip { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; }
    .fluid-slide { flex: 0 0 100%; width: 100%; height: 500px; scroll-snap-align: start; position: relative; }
    .fluid-slide img { width: 100%; height: 100%; object-fit: cover; display: block; }
    .slide-caption { position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(0,0,0,0.95), rgba(0,0,0,0.4)); color: #f8fafc; padding: 25px; text-align: center; }
    .legal-footer { background-color: #111111; color: #94a3b8; padding: 25px; border-radius: 14px; font-size: 0.75rem; line-height: 1.6; margin-top: 50px; border: 1px solid #333333; }
    </style>
""", unsafe_allow_html=True)

if "lavoratori" not in st.session_state:
    st.session_state.lavoratori = [
        {"nome": "Marco R.", "mansione": "Cameriere / Sala", "zona": "Navigli", "tel": "+39 333 1234567"},
        {"nome": "Sara B.", "mansione": "Barista / Bartender", "zona": "Porta Romana", "tel": "+39 340 9876543"}
    ]

st.markdown("""
    <div class="hero-full-bleed">
        <div class="hero-content">
            <h1 class="brand-title">Fla<span style="margin: 0 -4px;">⚡️</span>hJob</h1>
            <p style="color: #cbd5e1; font-size: 1.25rem; max-width: 650px; margin: 0 auto;">Il primo hub digitale che unisce i locali della ristorazione milanese con i migliori professionisti dell'accoglienza in tempo reale.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
scelta = st.radio("Navigazione rapida:", ["🏠 Chi Siamo & Atmosfera", "⭐ Area Aziende (Database)", "👤 Area Lavoratori"], horizontal=True)
st.markdown("---")
st.markdown('</div>', unsafe_allow_html=True)

if scelta == "🏠 Chi Siamo & Atmosfera":
    st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>🎯 Chi Siamo e Cosa Facciamo</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #cbd5e1;'><b>Fla⚡️hJob</b> nasce per sradicare il caos dei gruppi di messaggistica e dare una svolta professionale all'H&R milanese.</p>", unsafe_allow_html=True)
    
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.markdown("""<div class="feature-card"><span class="badge-tag">PER LE AZIENDE 🏢</span><h4 style="color: #fff;">Perché sceglierci</h4><ul style="color: #cbd5e1;"><li>Zero commissioni</li><li>Contatto diretto WhatsApp</li><li>Copertura turni in 2 min</li></ul></div>""", unsafe_allow_html=True)
    with col_v2:
        st.markdown("""<div class="feature-card"><span class="badge-tag" style="background:#bbf7d0;color:#166534;">PER I LAVORATORI 👤</span><h4 style="color: #fff;">I tuoi vantaggi</h4><ul style="color: #cbd5e1;"><li>100% Gratuito</li><li>Vetrina d'eccellenza</li><li>Zero intermediari</li></ul></div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="framed-gallery-container">
        <div class="image-strip">
            <div class="fluid-slide"><img src="https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=1600" /><div class="slide-caption">🍸 Fla⚡️hJob &bull; Mixology d'eccellenza</div></div>
            <div class="fluid-slide"><img src="https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1600" /><div class="slide-caption">🍽️ Fla⚡️hJob &bull; Cucina e servizio</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif scelta == "⭐ Area Aziende (Database)":
    st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>⭐ Database Lavoratori Disponibili a Milano</h3>", unsafe_allow_html=True)
    for lav in st.session_state.lavoratori:
        st.markdown(f"""<div class="feature-card"><h4 style="color: white; margin-top:0;">👤 {lav['nome']}</h4><p style="color: #cbd5e1;">Mansione: {lav['mansione']} | Zona: {lav['zona']}</p><p>📞 <a href="https://wa.me/{lav['tel'].replace(' ', '')}" target="_blank" style="color: #4ade80;">{lav['tel']}</a></p></div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
    st.markdown("""
    <div class="profile-container">
        <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400" class="profile-img" />
        <h2 style="color: white; margin-bottom: 2px;">Hello, Giulia Rossi</h2>
        <p style="color: #4ade80; font-weight: 600;">+39 334 5678901</p>
        <p style="color: #94a3b8; font-size: 0.85rem;">H&R Professional &bull; Milano Centro</p>
        <div class="profile-stats-row">
            <div><div style="font-size: 1.25rem; font-weight: bold; color: #fef08a;">03</div><div style="font-size: 0.75rem; color: #94a3b8;">In Attesa</div></div>
            <div><div style="font-size: 1.25rem; font-weight: bold; color: #38bdf8;">02</div><div style="font-size: 0.75rem; color: #94a3b8;">In Corso</div></div>
            <div><div style="font-size: 1.25rem; font-weight: bold; color: #4ade80;">18</div><div style="font-size: 0.75rem; color: #94a3b8;">Completati</div></div>
        </div>
        <div style="text-align: left; margin-top: 20px;">
            <div class="menu-item-card"><span>🌐 Lingua (IT / EN)</span><span style="color: #4ade80;">EN</span></div>
            <div class="menu-item-card"><span>🔒 Modifica Password</span><span style="color: #71717a;">&gt;</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
st.markdown("""<div class="legal-footer"><b style="color: #ffffff;">⚖️ Note Legali - Fla⚡️hJob</b><br>Bacheca digitale B2B/B2C per il settore H&R. Nessun rapporto di agenzia o intermediazione lavorativa.</div>""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)