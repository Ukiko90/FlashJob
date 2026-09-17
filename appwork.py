import streamlit as st

st.set_page_config(
    page_title="Flashjob &bull; Enterprise Hub", page_icon="⚡", layout="wide"
)

st.markdown(
    """
    <style>
    .block-container { padding: 0rem 3rem 3rem 3rem; max-width: 100% !important; }
    
    /* SFONDO MINIMAL STILE APPLE (CLEAN & WARM) */
    .stApp {
        background-color: #f5f2eb;
        background-image: linear-gradient(135deg, #f7f4ed 0%, #eae3d5 100%);
        background-attachment: fixed;
        color: #1d1d1f;
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Helvetica Neue", Helvetica, Arial, sans-serif;
    }

    /* MENU DI NAVIGAZIONE RAPIDA STILE SEGMENTED CONTROL APPLE */
    .stRadio > label {
        color: #86868b !important;
        font-weight: 500;
        font-size: 0.75rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 8px;
    }
    .stRadio div[role="radiogroup"] {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        padding: 6px;
        border-radius: 12px;
        border: 1px solid rgba(0, 0, 0, 0.06);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
        display: flex;
        gap: 6px;
    }
    .stRadio label span {
        color: #1d1d1f !important;
        font-weight: 500;
        font-size: 0.9rem;
    }

    .content-wrapper { max-width: 980px; margin: 0 auto; }
    
    /* HERO BANNER CRISTALLINO (ALTA LEGGIBILITÀ) */
    .apple-hero { 
        width: 100vw; 
        position: relative; 
        left: 50%; 
        right: 50%; 
        margin-left: -50vw; 
        margin-right: -50vw; 
        background: linear-gradient(180deg, rgba(255,255,255,0.95) 0%, rgba(245,242,235,0.9) 100%);
        border-bottom: 1px solid rgba(0, 0, 0, 0.08);
        padding: 70px 20px 60px 20px; 
        text-align: center; 
        margin-bottom: 50px; 
    }
    
    .brand-title { 
        color: #1d1d1f; 
        font-size: 3rem; 
        font-weight: 700; 
        letter-spacing: -0.015em; 
        margin-bottom: 12px;
    }
    
    /* CARD STILE GLASSMORPHISM ELEGANTE */
    .feature-card { 
        background: rgba(255, 255, 255, 0.8); 
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        padding: 35px; 
        border-radius: 20px; 
        margin-bottom: 24px; 
        border: 1px solid rgba(0, 0, 0, 0.04); 
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
        color: #1d1d1f; 
    }
    
    .badge-tag { 
        background-color: #1d1d1f; 
        color: #ffffff; 
        padding: 5px 12px; 
        border-radius: 20px; 
        font-size: 0.65rem; 
        font-weight: 600; 
        text-transform: uppercase;
        letter-spacing: 0.1em;
        display: inline-block; 
        margin-bottom: 18px; 
    }
    
    .profile-container { 
        background: rgba(255, 255, 255, 0.85); 
        backdrop-filter: blur(25px);
        border: 1px solid rgba(0, 0, 0, 0.04); 
        border-radius: 24px; 
        padding: 40px; 
        max-width: 700px; 
        margin: 0 auto 30px auto; 
        text-align: center; 
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
    }
    
    .profile-img { 
        width: 90px; 
        height: 90px; 
        border-radius: 50%; 
        object-fit: cover; 
        border: 2px solid #ffffff; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin: 0 auto 16px auto; 
    }
    
    .profile-stats-row { 
        display: flex; 
        justify-content: space-around; 
        background: rgba(245, 242, 235, 0.7); 
        border-radius: 16px; 
        padding: 20px; 
        margin: 24px 0; 
        border: 1px solid rgba(0, 0, 0, 0.03);
    }
    
    .menu-item-card { 
        background: rgba(245, 242, 235, 0.7); 
        border-radius: 12px; 
        padding: 16px 20px; 
        margin-bottom: 12px; 
        display: flex; 
        align-items: center; 
        justify-content: space-between; 
        color: #1d1d1f; 
        text-align: left; 
        border: 1px solid rgba(0, 0, 0, 0.03);
    }
    
    .framed-gallery-container { 
        width: 100%; 
        max-width: 980px; 
        margin: 40px auto; 
        background: rgba(255, 255, 255, 0.8); 
        backdrop-filter: blur(25px);
        border-radius: 24px; 
        border: 1px solid rgba(0, 0, 0, 0.04); 
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
        overflow: hidden; 
    }
    .image-strip { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; }
    .fluid-slide { flex: 0 0 100%; width: 100%; height: 460px; scroll-snap-align: start; position: relative; }
    .fluid-slide img { width: 100%; height: 100%; object-fit: cover; display: block; }
    .slide-caption { position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(0,0,0,0.8), rgba(0,0,0,0)); color: #ffffff; padding: 25px; text-align: center; font-size: 0.95rem; font-weight: 500; }
    
    .legal-footer { 
        background-color: rgba(255, 255, 255, 0.6); 
        color: #86868b; 
        padding: 30px; 
        border-radius: 20px; 
        font-size: 0.75rem; 
        line-height: 1.6; 
        margin-top: 60px; 
        border: 1px solid rgba(0, 0, 0, 0.04);
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

# HEADER PRINCIPALE STILE APPLE
st.markdown(
    """
    <div class="apple-hero">
        <div class="hero-content">
            <h1 class="brand-title">Flashjob</h1>
            <p style="color: #515154; font-size: 1.15rem; max-width: 680px; margin: 0 auto; font-weight: 400; line-height: 1.5;">Enterprise Workforce Hub &bull; Soluzioni di ingaggio rapido per l'Hotellerie & Ristorazione a Milano.</p>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
scelta = st.radio(
    "Navigazione Rapida",
    ["Panoramica & Modello", "Database Aziendale", "Area Personale Lavoratore"],
    horizontal=True,
)
st.markdown("<div style='margin: 30px 0;'></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

if scelta == "Panoramica & Modello":
  st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
  st.markdown(
      "<h3 style='color: #1d1d1f; font-weight: 600; font-size: 1.5rem;"
      " margin-bottom: 12px; letter-spacing: -0.01em;'>Infrastruttura"
      " Operativa</h3>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='color: #515154; line-height: 1.65; font-size: 1.05rem;"
      " margin-bottom: 30px;'>Flashjob ottimizza la gestione del personale"
      " riducendo i tempi di copertura delle turnazioni critiche. I titolari"
      " possono individuare e contattare direttamente i professionisti"
      " qualificati per interventi last-minute sul territorio di Milano.</p>",
      unsafe_allow_html=True,
  )

  col_v1, col_v2 = st.columns(2)

  with col_v1:
    st.markdown(
        """
        <div class="feature-card">
            <span class="badge-tag">Area Aziende</span>
            <h4 style="color: #1d1d1f; margin-top:5px; font-weight: 600; font-size: 1.2rem;">Standard di Servizio</h4>
            <ul style="padding-left: 18px; color: #515154; font-size: 0.95rem; line-height: 1.7; margin-top: 12px;">
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
            <h4 style="color: #1d1d1f; margin-top:5px; font-weight: 600; font-size: 1.2rem;">Protocollo e Compliance</h4>
            <ul style="padding-left: 18px; color: #515154; font-size: 0.95rem; line-height: 1.7; margin-top: 12px;">
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
      "<h3 style='color: #1d1d1f; font-weight: 600; font-size: 1.5rem;"
      " margin-bottom: 15px; letter-spacing: -0.01em;'>Standard Visivo e"
      " Location</h3>",
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
      "<h3 style='color: #1d1d1f; font-weight: 600; font-size: 1.5rem;"
      " margin-bottom: 8px;'>Database Professionisti</h3>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='color: #515154; margin-bottom: 25px; font-size: 1.05rem;'>Directory"
      " attiva del personale disponibile per ingaggi rapidi in area"
      " metropolitana.</p>",
      unsafe_allow_html=True,
  )

  for lav in st.session_state.lavoratori:
    st.markdown(
        f"""
        <div class="feature-card">
            <h4 style="color: #1d1d1f; margin-top:0; font-weight: 600; font-size: 1.2rem;">{lav['nome']}</h4>
            <p style="margin: 6px 0; color: #515154; font-size: 0.95rem;"><b>Qualifica:</b> {lav['mansione']} &bull; <b>Area:</b> {lav['zona']}</p>
            <p style="margin: 6px 0; font-size: 0.95rem;"><b>Contatto Diretto:</b> <a href="https://wa.me/{lav['tel'].replace(' ', '')}" target="_blank" style="color: #0066cc; font-weight: 600; text-decoration: none;">{lav['tel']} &rarr;</a></p>
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
        <h2 style="color: #1d1d1f; margin-bottom: 2px; font-weight: 600; font-size: 1.35rem;">Giulia Rossi</h2>
        <p style="color: #1d1d1f; font-weight: 600; font-size: 0.95rem;">+39 334 5678901</p>
        <p style="color: #86868b; font-size: 0.85rem; margin-top: 2px;">Profilo Verificato &bull; Milano Centro</p>
        
        <div class="profile-stats-row">
            <div>
                <div style="font-size: 1.3rem; font-weight: 700; color: #1d1d1f;">03</div>
                <div style="font-size: 0.7rem; color: #86868b; text-transform: uppercase; letter-spacing: 0.05em;">In Attesa</div>
            </div>
            <div>
                <div style="font-size: 1.3rem; font-weight: 700; color: #0066cc;">02</div>
                <div style="font-size: 0.7rem; color: #86868b; text-transform: uppercase; letter-spacing: 0.05em;">In Corso</div>
            </div>
            <div>
                <div style="font-size: 1.3rem; font-weight: 700; color: #34c759;">18</div>
                <div style="font-size: 0.7rem; color: #86868b; text-transform: uppercase; letter-spacing: 0.05em;">Completati</div>
            </div>
        </div>

        <div style="text-align: left; margin-top: 25px;">
            <p style="color: #86868b; font-size: 0.7rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 10px;">Configurazione Account</p>
            <div class="menu-item-card">
                <span style="font-size: 0.95rem; font-weight: 500;">Lingua di Sistema</span>
                <span style="color: #1d1d1f; font-weight: 600; font-size: 0.95rem;">Italiano</span>
            </div>
            <div class="menu-item-card">
                <span style="font-size: 0.95rem; font-weight: 500;">Credenziali di Sicurezza</span>
                <span style="color: #86868b; font-size: 0.95rem;">&gt;</span>
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
        <b style="color: #1d1d1f; font-size: 0.8rem;">Note Legali e Regolamento Enterprise - Flashjob</b><br><br>
        La piattaforma opera esclusivamente come directory e bacheca di contatto B2B per il settore Hotellerie & Restaurant (H&R). <b>Protocollo di Affidabilità:</b> L'accettazione formale di un turno vincola il lavoratore alla presenza; la violazione reiterata (3 strike) comporta la disattivazione immediata dell'account. Il servizio non configura agenzia di somministrazione o intermediazione di manodopera ai sensi della normativa vigente.
    </div>
""",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)