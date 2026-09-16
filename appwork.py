from datetime import datetime
import pandas as pd
import streamlit as st

# --- CONFIGURAZIONE PAGINA E STILE MOBILE PRO ---
st.set_page_config(
    page_title="FlashJob - Lavoro Last Minute", page_icon="⚡", layout="centered"
)

st.markdown(
    """
    <style>
    /* Stile generale e pulizia sfondi */
    .main {
        background-color: #f8fafc;
    }
    .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 2rem !important;
        max-width: 700px;
    }
    /* Pulsanti moderni e grandi per il tocco mobile */
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        width: 100%;
        padding: 0.6rem 1rem;
        background-color: #0f172a;
        color: white;
        border: none;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton > button:hover {
        background-color: #1e293b;
        color: white;
    }
    /* Input di testo puliti */
    .stTextInput > div > div > input, .stSelectbox > div > div > div {
        border-radius: 8px;
        border-color: #cbd5e1;
    }
    h1 {
        font-size: 1.6rem !important;
        font-weight: 800 !important;
        color: #0f172a;
    }
    h2 {
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        color: #1e293b;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- MEMORIA DI STATO DELL'APP ---
if "offerte" not in st.session_state:
    st.session_state.offerte = [
        {
            "id": 1,
            "azienda": "The Sanctuary",
            "mansione": "Addetto Sala / Bar",
            "data": "2026-06-20",
            "orario": "16:00 - 00:00",
            "compenso": "80€",
            "stato": "Aperta",
        }
    ]

if "candidature" not in st.session_state:
    st.session_state.candidature = []

# --- INTESTAZIONE ---
st.markdown("⚡ **FlashJob**: Il lavoro last minute a misura di persona")
st.write(
    "La piattaforma rapida dove l'azienda pubblica l'esigenza e il lavoratore si propone all'ultimo secondo."
)

st.divider()

# --- MENU A TENDINA PRINCIPALE (Azienda vs Lavoratore) ---
modalita = st.selectbox(
    "Seleziona la tua modalità:",
    [
        "💼 Area Azienda (Pubblica Offerta)",
        "👤 Area Lavoratore (Trova & Candidati)",
    ],
)

# ==========================================
# 💼 AREA AZIENDA
# ==========================================
if "Azienda" in modalita:
    st.subheader("Gestione Annunci & Turni Urgenti")

    with st.form("form_offerta", clear_on_submit=True):
        st.write("Crea una nuova richiesta di lavoro")
        nome_azienda = st.text_input(
            "Nome Attività / Azienda", placeholder="Es. Ristorante Da Mario"
        )
        mansione = st.text_input(
            "Mansione richiesta", placeholder="Es. Addetto Vendite / Eventi"
        )
        col1, col2 = st.columns(2)
        with col1:
            data_turno = st.date_input("Data del turno")
        with col2:
            orario = st.text_input(
                "Orario", placeholder="Es. 15:00 - 23:00"
            )

        compenso = st.text_input(
            "Compenso totale stimato", placeholder="Es. 90€"
        )

        submitted = st.form_submit_button("🚀 Pubblica Offerta Last-Minute")
        if submitted:
            if nome_azienda and mansione and compenso:
                nuova_offerta = {
                    "id": len(st.session_state.offerte) + 1,
                    "azienda": nome_azienda,
                    "mansione": mansione,
                    "data": str(data_turno),
                    "orario": orario,
                    "compenso": compenso,
                    "stato": "Aperta",
                }
                st.session_state.offerte.append(nuova_offerta)
                st.success("Offerta pubblicata con successo in bacheca!")
                st.rerun()
            else:
                st.warning("Per favore, compila tutti i campi obbligatori.")

    st.divider()
    st.subheader("Le tue offerte attive e stato candidature")

    if not st.session_state.offerte:
        st.info("Nessuna offerta pubblicata al momento.")
    else:
        for offerta in st.session_state.offerte:
            with st.container():
                st.markdown(
                    f"**{offerta['azienda']}** - {offerta['mansione']} ({offerta['data']}) | *Stato: {offerta['stato']}*"
                )
                st.caption(
                    f"🕒 {offerta['orario']} | 💰 {offerta['compenso']}"
                )

                # Mostra candidati per questa offerta
                candidati_per_offerta = [
                    c
                    for c in st.session_state.candidature
                    if c["offerta_id"] == offerta["id"]
                ]
                if candidati_per_offerta:
                    st.write("👥 **Candidati proposti:**")
                    for cand in candidati_per_offerta:
                        col_c1, col_c2 = st.columns([3, 1])
                        with col_c1:
                            st.text(
                                f"• {cand['nome_lavoratore']} (alle {cand['data_candidatura']})"
                            )
                        with col_c2:
                            if st.button("Conferma", key=f"conf_{cand['id']}"):
                                offerta["stato"] = "Assegnato"
                                st.success(
                                    f"Turno assegnato a {cand['nome_lavoratore']}!"
                                )
                                st.rerun()
                else:
                    st.caption("Nessuna candidatura ricevuta finora.")
                st.divider()

# ==========================================
# 👤 AREA LAVORATORE
# ==========================================
else:
    st.subheader("Bacheca Turni Last-Minute ⚡")
    st.write("Sfoglia i turni disponibili e candidati con un solo tap.")

    offerte_aperte = [
        o for o in st.session_state.offerte if o["stato"] == "Aperta"
    ]

    if not offerte_aperte:
        st.info(
            "Al momento non ci sono turni last-minute disponibili. Controlla più tardi!"
        )
    else:
        nome_utente = st.text_input(
            "Inserisci il tuo Nome e Cognome per candidarti:",
            placeholder="Es. Mario Rossi",
        )

        for offerta in offerte_aperte:
            with st.container():
                st.markdown(f"### 📍 {offerta['azienda']}")
                st.write(f"**Mansione:** {offerta['mansione']}")
                st.markdown(
                    f"📅 **Data:** {offerta['data']} | 🕒 **Orario:** {offerta['orario']}"
                )
                st.markdown(f"💰 **Compenso:** **{offerta['compenso']}**")

                # Pulsante di candidatura istantanea stile Tinder
                if st.button(
                    f"🔥 Voglio farlo io! (Candidati)",
                    key=f"cand_{offerta['id']}",
                ):
                    if not nome_utente:
                        st.warning(
                            "Inserisci prima il tuo nome sopra per procedere con la candidatura!"
                        )
                    else:
                        nuova_candidatura = {
                            "id": len(st.session_state.candidature) + 1,
                            "offerta_id": offerta["id"],
                            "nome_lavoratore": nome_utente,
                            "data_candidatura": datetime.now().strftime(
                                "%H:%M:%S"
                            ),
                        }
                        st.session_state.candidature.append(nuova_candidatura)
                        st.success(
                            f"Ottimo {nome_utente}! Ti sei proposto con successo. L'azienda valuterà la tua candidatura."
                        )
                        st.rerun()

                st.divider()