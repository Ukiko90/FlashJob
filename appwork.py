from datetime import datetime
import pandas as pd
import streamlit as st

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(
    page_title="FlashJob - Lavoro Last Minute", page_icon="⚡", layout="centered"
)

# --- STILE GRAFICO MOBILE PRO ---
st.markdown(
    """
    <style>
    .main { background-color: #f8fafc; }
    .block-container { padding-top: 1rem !important; padding-bottom: 2rem !important; max-width: 700px; }
    .stButton > button {
        border-radius: 10px; font-weight: 600; width: 100%; padding: 0.6rem 1rem;
        background-color: #0f172a; color: white; border: none; box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton > button:hover { background-color: #1e293b; color: white; }
    .stTextInput > div > div > input, .stSelectbox > div > div > div { border-radius: 8px; border-color: #cbd5e1; }
    h1 { font-size: 1.5rem !important; font-weight: 800 !important; color: #0f172a; }
    h2 { font-size: 1.2rem !important; font-weight: 700 !important; color: #1e293b; }
    .ad-box { background-color: #eff6ff; border: 1px dashed #3b82f6; padding: 10px; border-radius: 8px; text-align: center; color: #1e3a8a; font-size: 0.85rem; margin-bottom: 15px; }
    .pro-badge { background-color: #fef08a; color: #854d0e; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: bold; }
    </style>
""",
    unsafe_allow_html=True,
)

# --- MEMORIA DI STATO ---
if "offerte" not in st.session_state:
    st.session_state.offerte = [
        {
            "id": 1,
            "azienda": "The Sanctuary",
            "mansione": "Addetto Sala / Bar",
            "data": "2026-06-20",
            "orario": "16:00 - 00:00",
            "compenso": "90€ (Pagamento Immediato a fine turno)",
            "stato": "Aperta",
            "premium": True,
        }
    ]

if "candidature" not in st.session_state:
    st.session_state.candidature = []

# --- INTESTAZIONE ---
st.markdown("⚡ **FlashJob**: Il lavoro last-minute a chiamata")
st.write(
    "Trova personale immediato o guadagna subito. Pagamenti trasparenti e tracciati a fine turno."
)
st.divider()

# --- SELETTORE RUOLO ---
ruolo = st.selectbox(
    "Come vuoi accedere?",
    [
        "👤 Sono un Lavoratore (Cerco Turno)",
        "💼 Sono un'Azienda (Pubblica Offerta)",
        "⭐ Area Azienda PRO / Abbonamenti",
    ],
)

# ==========================================
# 👤 AREA LAVORATORE
# ==========================================
if "Lavoratore" in ruolo:
    st.subheader("Bacheca Turni Urgenti ⚡")
    st.write(
        "Candidati con un tap. I turni prevedono compenso immediato a fine prestazione."
    )

    offerte_aperte = [
        o for o in st.session_state.offerte if o["stato"] == "Aperta"
    ]

    # Mostra prima le offerte in evidenza (PRO)
    offerte_aperte.sort(key=lambda x: x.get("premium", False), reverse=True)

    if not offerte_aperte:
        st.info("Nessun turno disponibile al momento. Torna a controllare tra poco!")
    else:
        nome_utente = st.text_input(
            "Il tuo Nome e Cognome:", placeholder="Es. Marco Rossi"
        )
        telefono_utente = st.text_input(
            "Il tuo Recapito / WhatsApp (per farti chiamare subito):",
            placeholder="Es. 3331234567",
        )

        st.divider()

        for offerta in offerte_aperte:
            with st.container():
                if offerta.get("premium"):
                    st.markdown(
                        "<span class='pro-badge'>⚡ IN EVIDENZA (TOP AZIENDA)</span>",
                        unsafe_allow_html=True,
                    )

                st.markdown(f"### 📍 {offerta['azienda']}")
                st.write(f"**Mansione:** {offerta['mansione']}")
                st.markdown(
                    f"📅 **Data:** {offerta['data']} | 🕒 **Orario:** {offerta['orario']}"
                )
                st.markdown(f"💰 **Compenso:** **{offerta['compenso']}**")
                st.caption(
                    "💡 *Regola FlashJob:* Compenso accreditato/consegnato in modo tracciato subito alla fine del turno."
                )

                if st.button(
                    f"🔥 Voglio farlo io! (Candidati)",
                    key=f"cand_{offerta['id']}",
                ):
                    if not nome_utente or not telefono_utente:
                        st.warning(
                            "Inserisci nome e telefono prima di candidarti!"
                        )
                    else:
                        nuova_candidatura = {
                            "id": len(st.session_state.candidature) + 1,
                            "offerta_id": offerta["id"],
                            "nome_lavoratore": nome_utente,
                            "telefono": telefono_utente,
                            "data_candidatura": datetime.now().strftime(
                                "%H:%M:%S"
                            ),
                        }
                        st.session_state.candidature.append(nuova_candidatura)
                        st.success(
                            f"Ottimo {nome_utente}! L'azienda ha ricevuto il tuo contatto e ti chiamerà subito se idoneo."
                        )
                        st.rerun()
                st.divider()

# ==========================================
# 💼 AREA AZIENDA
# ==========================================
elif "Azienda" in ruolo and "PRO" not in ruolo:
    st.subheader("Pubblica un Turno d'Emergenza")

    # Banner pubblicitario per piano FREE
    st.markdown(
        """
        <div class="ad-box">
        📢 <b>Spazio Sponsorizzato Locale</b><br>
        <i>Promuovi qui la tua attività o scopri il piano FlashJob PRO per azzerare la pubblicità!</i>
        </div>
    """,
        unsafe_allow_html=True,
    )

    with st.form("form_azienda", clear_on_submit=True):
        nome_azienda = st.text_input(
            "Nome Attività", placeholder="Es. Bar Centrale Milano"
        )
        mansione = st.text_input(
            "Mansione", placeholder="Es. Bartender / Aiuto Cuoco"
        )
        col1, col2 = st.columns(2)
        with col1:
            data_turno = st.date_input("Data del turno")
        with col2:
            orario = st.text_input("Orario", placeholder="Es. 18:00 - 02:00")

        compenso = st.text_input(
            "Compenso Netto (es. 100€ con pagamento immediato a fine turno)",
            placeholder="Es. 100€",
        )

        pubblica = st.form_submit_button("🚀 Pubblica Subito in Bacheca")
        if pubblica:
            if nome_azienda and mansione and compenso:
                nuova_offerta = {
                    "id": len(st.session_state.offerte) + 1,
                    "azienda": nome_azienda,
                    "mansione": mansione,
                    "data": str(data_turno),
                    "orario": orario,
                    "compenso": compenso,
                    "stato": "Aperta",
                    "premium": False,
                }
                st.session_state.offerte.append(nuova_offerta)
                st.success("Offerta online! I lavoratori la vedranno all'istante.")
                st.rerun()
            else:
                st.warning("Compila tutti i campi.")

    st.divider()
    st.subheader("📋 Candidature Ricevute per i tuoi turni")

    if not st.session_state.candidature:
        st.info("Nessun lavoratore candidato al momento.")
    else:
        for cand in st.session_state.candidature:
            st.markdown(
                f"👤 **{cand['nome_lavoratore']}** | 📞 Tel: `{cand['telefono']}` (Candidato alle {cand['data_candidatura']})"
            )
            st.caption(
                "💡 Ricordati di regolare il compenso in modo tracciato (bonifico istantaneo o Satispay) a fine turno."
            )
            st.divider()

# ==========================================
# ⭐ AREA AZIENDA PRO (Abbonamento & Zero Ads)
# ==========================================
else:
    st.subheader("⭐ FlashJob PRO - Piano Abbonamento Aziende")
    st.write(
        "Fai lavorare la tua attività senza limiti e senza pubblicità."
    )

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown("### 🏷️ Piano Base (Free)")
        st.markdown(
            """
        - Pubblicazione standard
        - Visibilità normale in bacheca
        - Presenza di banner pubblicitari
        - **Costo:** 0€ (Gratis per sempre)
        """
        )
    with col_p2:
        st.markdown("### 🚀 Piano PRO (Abbonamento)")
        st.markdown(
            """
        - **Annunci in Evidenza** (In cima alla lista)
        - **Zero Pubblicità** nell'app
        - Notifiche prioritarie ai lavoratori
        - **Costo:** 39€ / mese
        """
        )

    if st.button("Abbonati subito a FlashJob PRO (39€/mese)"):
        st.success(
            "🎉 Grazie! Il tuo account aziendale è stato aggiornato a PRO. I tuoi prossimi annunci saranno in evidenza e senza pubblicità!"
        )