import streamlit as st

st.set_page_config(
    page_title="Flashjob - H&R Enterprise Hub", page_icon="⚡", layout="wide"
)

st.markdown(
    """
    <style>
    .block-container { padding: 0rem 3rem 2rem 3rem; max-width: 100% !important; }
    
    /* SFONDO GLOBALE LUMINOSO ED ELEGANTE */
    .stApp {
        background-color: #6b5545;
        background-image: 
            radial-gradient(circle at 25% 15%, rgba(230, 205, 180, 0.4) 0%, transparent 65%),
            linear-gradient(140deg, #4e3d30 0%, #7d6552 50%, #3e3025 100%);
        background-attachment: fixed;
        color: #ffffff;
    }

    /* MENU DI NAVIGAZIONE RAPIDA UNIFORME E PULITO */
    .stRadio > label {
        color: #e2e8f0 !important;
        font-weight: 500;
        font-size: 0.9rem;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    .stRadio div[role="radiogroup"] {
        background: rgba(45, 35, 28, 0.6);
        padding: 10px 20px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .stRadio label span {
        color: #ffffff !important;
        font-weight: 600;
    }

    .content-wrapper { max-width: 950px; margin: 0 auto; }
    
    /* HERO SECTION PROFESSIONALE */
    .hero-full-bleed { 
        width: 100vw; 
        position: relative; 
        left: 50%; 
        right: 50%; 
        margin-left: -50vw; 
        margin-right: -50vw; 
        background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.6)), url('https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?w=1800'); 
        background-size: cover; 
        background-position: center; 
        color: white; 
        padding: 80px 20px; 
        text-align: center; 
        margin-bottom: 40px; 
        border: none;
    }
    
    .brand-title { 
        color: white; 
        font-size: 3rem; 
        font-weight: 800; 
        letter-spacing: -1px; 
    }
    
    /* CARD STRUTTURATE IN STILE ENTERPRISE */
    .feature-card { 
        background: rgba(55, 42, 33, 0.85); 
        padding: 30px; 
        border-radius: 16px; 
        margin-bottom: 20px; 
        border: 1px solid rgba(255, 255, 255, 0.08); 
        color: #ffffff; 
    }
    
    .badge-tag { 
        background-color: #e2e8f0; 
        color: #3e3025; 
        padding: 4px 12px; 
        border-radius: 6px; 
        font-size: 0.7rem; 
        font-weight: 700; 
        text-transform: uppercase;
        letter-spacing: 1px;
        display: inline-block; 
        margin-bottom: 15px; 
    }
    
    .profile-container { 
        background: rgba(55, 42, 33, 0.9); 
        border: 1px solid rgba(255, 255, 255, 0.08); 
        border-radius: 20px; 
        padding: 30px; 
        max-width: 700px; 
        margin: 0 auto 30px auto; 
        text-align: center; 
    }
    
    .profile-img { 
        width: 85px; 
        height: 85px; 
        border-radius: 50%; 
        object-fit: cover; 
        border: 2px solid #ffffff; 
        margin: 0 auto 15px auto; 
    }
    
    .profile-stats-row { 
        display: flex; 
        justify-content: space-around; 
        background: rgba(42, 32, 25, 0.95); 
        border-radius: 12px; 
        padding: 15px; 
        margin: 20px 0; 
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    .menu-item-card { 
        background: rgba(42, 32, 25, 0.95); 
        border-radius: 10px; 
        padding: 14px 20px; 
        margin-bottom: 10px; 
        display: flex; 
        align-items: center; 
        justify-content: space-between; 
        color: #ffffff; 
        text-align: left; 
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    .framed-gallery-container { 
        width: 100%; 
        max-width: 950px; 
        margin: 40px auto; 
        background: rgba(55, 42, 33, 0.85); 
        border-radius: 20px; 
        border: 1px solid rgba(255, 255, 255, 0.08); 
        overflow: hidden; 
    }
    .image-strip { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; }
    .fluid-slide { flex: 0 0 100%; width: 100%; height: 450px; scroll-snap-align: start; position: relative; }
    .fluid-slide img { width: 100%; height: 100%; object-fit: cover; display: block; }
    .slide-caption { position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(0,0,0,0.9), rgba(0,0,0,0.2)); color: #ffffff; padding: 20px; text-align: center; font-size: 0.95rem; }
    
    .legal-footer { 
        background-color: rgba(55, 42, 33, 0.85); 
        color: #cbd5e1; 
        padding: 25px; 
        border-radius: 16px; 
        font-size: 0.75rem; 
        line-height: 1.6; 
        margin-top: 50px; 
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    </style>
""",
    unsafe_allow_html=True,
)

if "lavoratori" not in st.session_state:
  st.session_state.lavoratori = [
      {
          "nome": "Marco R.",
          "mansione": "Cameriere / Sala",
          "zona": "Navigli",
          "tel": "+39 333 1234567",
      },
      {
          "nome": "Sara B.",
          "mansione": "Barista / Bartender",
          "zona": "Porta Romana",
          "tel": "+39 340 9876543",
      },
  ]

# HEADER PRINCIPALE
st.markdown(
    """
    <div class="hero-full-bleed">
        <div class="hero-content">
            <h1 class="brand-title">Flashjob</h1>
            <p style="color: #cbd5e1; font-size: 1.1rem; max-width: 650px; margin: 0 auto; font-weight: 300;">Enterprise Workforce Hub &bull; Soluzioni di ingaggio rapido per l'Hotellerie & Ristorazione a Milano</p>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
scelta = st.radio(
    "Navigazione Rapida:",
    ["Panoramica & Modello", "Database Aziendale", "Area Personale Lavoratore"],
    horizontal=True,
)
st.markdown("---")
st.markdown("</div>", unsafe_allow_html=True)

if scelta == "Panoramica & Modello":
  st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
  st.markdown(
      "<h3 style='color: #ffffff; font-weight: 700; font-size: 1.4rem;"
      " margin-bottom: 15px;'>Infrastruttura Operativa</h3>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='color: #cbd5e1; line-height: 1.6;'>Flashjob"
      " ottimizza la gestione del personale riducendo i tempi di copertura"
      " delle turnazioni critiche. I titolari possono individuare e contattare"
      " direttamente i professionisti qualificati per interventi last-minute"
      " sul territorio di Milano.</p>",
      unsafe_allow_html=True,
  )

  st.markdown("<br>", unsafe_allow_html=True)
  col_v1, col_v2 = st.columns(2)

  with col_v1:
    st.markdown(
        """
        <div class="feature-card">
            <span class="badge-tag">Area Aziende</span>
            <h4 style="color: #ffffff; margin-top:5px; font-weight: 600;">Standard di Servizio</h4>
            <ul style="padding-left: 18px; color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;">
                <li>Zero commissioni sulle selezioni attive.</li>
                <li>Canale di comunicazione diretto via WhatsApp.</li>
                <li>Copertura tempestiva dei turni operativi.</li>
                <li>Profili verificati e referenziati.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

  with col_v2:
    st.markdown(
        """
        <div class="feature-card">
            <span class="badge-tag">Area Lavoratori</span>
            <h4 style="color: #ffffff; margin-top:5px; font-weight: 600;">Protocollo e Compliance</h4>
            <ul style="padding-left: 18px; color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;">
                <li>Piattaforma interamente gratuita per lo staff.</li>
                <li>Patto di serietà vincolante all'accettazione dell'offerta.</li>
                <li><b>Policy di affidabilità (3 Strike):</b> Tre assenze ingiustificate comportano la revoca dell'accesso al database.</li>
                <li>Visibilità prioritaria sui locali partner.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

  st.markdown("<br>", unsafe_allow_html=True)
  st.markdown(
      "<h3 style='color: #ffffff; font-weight: 700; font-size: 1.4rem;"
      " margin-bottom: 15px;'>Standard Visivo e Location</h3>",
      unsafe_allow_html=True,
  )
  st.markdown("</div>", unsafe_allow_html=True)

  st.markdown(
      """
    <div class="framed-gallery-container">
        <div class="image-strip">
            <div class="fluid-slide">
                <img src="https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=1600" />
                <div class="slide-caption">Mixology di alto livello e standard di servizio premium a Milano</div>
            </div>
            <div class="fluid-slide">
                <img src="https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1600" />
                <div class="slide-caption">Organizzazione e gestione impeccabile della cucina e della sala</div>
            </div>
        </div>
    </div>
    """,
      unsafe_allow_html=True,
  )

elif scelta == "Database Aziendale":
  st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
  st.markdown(
      "<h3 style='color: #ffffff; font-weight: 700; font-size: 1.4rem;"
      " margin-bottom: 10px;'>Database Professionisti</h3>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='color: #cbd5e1; margin-bottom: 25px;'>Directory attiva"
      " del personale disponibile per ingaggi rapidi in area"
      " metropolitana.</p>",
      unsafe_allow_html=True,
  )

  for lav in st.session_state.lavoratori:
    st.markdown(
        f"""
        <div class="feature-card">
            <h4 style="color: white; margin-top:0; font-weight: 600;">{lav['nome']}</h4>
            <p style="margin: 6px 0; color: #cbd5e1; font-size: 0.95rem;"><b>Qualifica:</b> {lav['mansione']} &bull; <b>Area:</b> {lav['zona']}</p>
            <p style="margin: 6px 0; font-size: 0.9rem;"><b>Contatto Diretto:</b> <a href="https://wa.me/{lav['tel'].replace(' ', '')}" target="_blank" style="color: #ffffff; font-weight: 600; text-decoration: underline;">{lav['tel']}</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
  st.markdown("</div>", unsafe_allow_html=True)

else:
  st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
  st.markdown(
      """
    <div class="profile-container">
        <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400" class="profile-img" />
        <h2 style="color: white; margin-bottom: 2px; font-weight: 700; font-size: 1.3rem;">Giulia Rossi</h2>
        <p style="color: #ffffff; font-weight: 600; font-size: 0.95rem;">+39 334 5678901</p>
        <p style="color: #cbd5e1; font-size: 0.85rem; margin-top: 2px;">Profilo Verificato &bull; Milano Centro</p>
        
        <div class="profile-stats-row">
            <div>
                <div style="font-size: 1.2rem; font-weight: 700; color: #fef08a;">03</div>
                <div style="font-size: 0.75rem; color: #cbd5e1; text-transform: uppercase;">In Attesa</div>
            </div>
            <div>
                <div style="font-size: 1.2rem; font-weight: 700; color: #38bdf8;">02</div>
                <div style="font-size: 0.75rem; color: #cbd5e1; text-transform: uppercase;">In Corso</div>
            </div>
            <div>
                <div style="font-size: 1.2rem; font-weight: 700; color: #ffffff;">18</div>
                <div style="font-size: 0.75rem; color: #cbd5e1; text-transform: uppercase;">Completati</div>
            </div>
        </div>

        <div style="text-align: left; margin-top: 25px;">
            <p style="color: #cbd5e1; font-size: 0.75rem; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">Configurazione Account</p>
            <div class="menu-item-card">
                <span style="font-size: 0.9rem;">Lingua di Sistema</span>
                <span style="color: #ffffff; font-weight: 600; font-size: 0.9rem;">Italiano</span>
            </div>
            <div class="menu-item-card">
                <span style="font-size: 0.9rem;">Credenziali di Sicurezza</span>
                <span style="color: #cbd5e1; font-size: 0.9rem;">&gt;</span>
            </div>
        </div>
    </div>
    """,
      unsafe_allow_html=True,
  )
  st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="legal-footer">
        <b style="color: #ffffff; font-size: 0.8rem;">Note Legali e Regolamento Enterprise - Flashjob</b><br><br>
        La piattaforma opera esclusivamente come directory e bacheca di contatto B2B per il settore Hotellerie & Restaurant (H&R). <b>Protocollo di Affidabilità:</b> L'accettazione formale di un turno vincola il lavoratore alla presenza; la violazione reiterata (3 strike) comporta la disattivazione immediata dell'account. Il servizio non configura agenzia di somministrazione o intermediazione di manodopera ai sensi della normativa vigente.
    </div>
""",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)