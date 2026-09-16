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
    .ad-box { background-color: #eff6ff; border: 1px dashed #3b82f6; padding: 12px; border-radius: 8px; text-align: center; color: #1e3a8a; font-size: 0.85rem; margin-bottom: 15px; }
    .free-badge { background-color: #dcfce7; color: #166534; padding: 3px 8px; border-radius: 6px; font-size: 0.75rem; font-weight: bold; display: inline-block; margin-bottom: 8px; }
    .pro-badge { background-color: #fef08a; color: #854d0e; padding: 3px 8px; border-radius: 6px; font-size: 0.75rem; font-weight: bold; display: inline-block; margin-bottom: 8px; }
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
            "citta": "Milano",
            "mansione": "Addetto Sala / Bar",
            "data": "2026-06-20",
            "orario": "16:00 - 00:00",
            "compenso": "90€ netti (Pagamento Immediato)",
            "stato": "Aperta",
            "premium": True,
        }
    ]

if "candidature" not in st.session_state:
    st.session_state.candidature = []

# --- INTESTAZIONE ---
st.markdown("⚡ **FlashJob**: Il lavoro last-minute a chiamata")
st.markdown(
    "<span class='free-badge'>🛡️ 100% GRATUITO PER I LAVORATORI (Zero Commissioni)</span>",
    unsafe_allow_html=True,
)
st.divider()

# --- SELETTORE RUOLO ---
ruolo = st.selectbox(
    "Seleziona il tuo profilo:",
    [
        "👤 Lavoratore (Cerco Turno / Lavoro)",
        "💼 Azienda (Pubblica Turno Urgente)",
        "⭐ Azienda PRO (Abbonamenti & Vetrina)",
    ],
)

# ==========================================
# 👤 AREA LAVORATORE
# ==========================================
if "Lavoratore" in ruolo:
    st.subheader("Bacheca Turni Disponibili ⚡")
    st.write(
        "Qui trovi i turni last-minute pubblicati dai locali. Candidati subito e fatti chiamare."
    )

    # Filtro rapido per città
    citta_filtro = st.selectbox(
        "Filtra per Zona / Città:", ["Tutte le città", "Milano", "Roma", "Altro"]
    )

    offerte_aperte = [
        o for o in st.session_state.offerte if o["stato"] == "Aperta"
    ]
    if citta_filtro != "Tutte le città":
        offerte_aperte = [
            o for o in offerte_aperte if o["citta"] == citta_filtro
        ]

    # Ordinamento: prima i PRO in evidenza
    offerte_aperte.sort(key=lambda x: x.get("premium", False), reverse=True)

    if not offerte_aperte:
        st.info("Nessun turno disponibile in questa zona al momento.")
    else:
        st.divider()
        nome_utente = st.text_input(
            "Il tuo Nome e Cognome:", placeholder="Es. Mario Rossi"
        )
        telefono_utente = st.text_input(
            "Il tuo WhatsApp / Telefono (per essere ricontattato subito):",
            placeholder="Es. 3331234567",
        )
        st.divider()

        for offerta in offerte_aperte:
            with st.container():
                if offerta.get("premium"):
                    st.markdown(
                        "<span class='pro-badge'>⭐ TURNO IN EVIDENZA (TOP LOCALE)</span>",
                        unsafe_allow_html=True,
                    )

                st.markdown(f"### 📍 {offerta['azienda']} ({offerta['citta']})")
                st.write(f"**Mansione:** {offerta['mansione']}")
                st.markdown(
                    f"📅 **Data:** {offerta['data']} | 🕒 **Orario:** {offerta['orario']}"
                )
                st.markdown(f"💰 **Compenso:** **{offerta['compenso']}**")
                st.caption(
                    "💡 *Nota:* FlashJob è gratuito per te. L'accordo economico e il pagamento avvengono direttamente con l'azienda a fine turno."
                )

                if st.button(
                    f"🔥 Voglio farlo io! (Candidati Subito)",
                    key=f"cand_{offerta['id']}",
                ):
                    if not nome_utente or not telefono_utente:
                        st.warning(
                            "Inserisci prima il tuo nome e il tuo numero di telefono!"
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
                            f"Ottimo {nome_utente}! Candidatura inviata. Se l'azienda ti sceglie, ti chiamerà al numero `{telefono_utente}`."
                        )
                        st.rerun()
                st.divider()

# ==========================================
# 💼 AREA AZIENDA (FREE)
# ==========================================
elif "Azienda" in ruolo and "PRO" not in ruolo:
    st.subheader("Pubblica un Turno d'Emergenza")
    st.write(
        "Hai un'improvvisa assenza di personale? Pubblica l'offerta in 10 secondi."
    )

    # Banner pubblicitario promozionale per la versione Free
    st.markdown(
        """
        <div class="ad-box">
        📢 <b>Spazio Sponsorizzato Locale / Servizi per Aziende</b><br>
        <i>Vuoi rimuovere questi banner e posizionare i tuoi turni sempre in cima? Scopri il piano Azienda PRO!</i>
        </div>
    """,
        unsafe_allow_html=True,
    )

    with st.form("form_azienda_free", clear_on_submit=True):
        nome_azienda = st.text_input(
            "Nome Attività", placeholder="Es. Ristorante La Pergola"
        )
        citta = st.selectbox("Città / Zona", ["Milano", "Roma", "Altro"])
        mansione = st.text_input(
            "Mansione richiesta", placeholder="Es. Cameriere di sala / Cuoco"
        )

        col1, col2 = st.columns(2)
        with col1:
            data_turno = st.date_input("Data del turno")
        with col2:
            orario = st.text_input("Orario", placeholder="Es. 19:00 - 01:00")

        compenso = st.text_input(
            "Compenso Netto stimato (es. 90€)", placeholder="Es. 90€"
        )

        pubblica = st.form_submit_button("🚀 Pubblica Offerta Last-Minute")
        if pubblica:
            if nome_azienda and mansione and compenso:
                nuova_offerta = {
                    "id": len(st.session_state.offerte) + 1,
                    "azienda": nome_azienda,
                    "citta": citta,
                    "mansione": mansione,
                    "data": str(data_turno),
                    "orario": orario,
                    "compenso": compenso,
                    "stato": "Aperta",
                    "premium": False,
                }
                st.session_state.offerte.append(nuova_offerta)
                st.success(
                    "Offerta pubblicata con successo! I lavoratori la vedranno subito."
                )
                st.rerun()
            else:
                st.warning("Per favore, compila tutti i campi.")

    st.divider()
    st.subheader("📋 Gestione Candidature Ricevute")

    if not st.session_state.candidature:
        st.info("Nessuna candidatura ricevuta al momento.")
    else:
        for cand in st.session_state.candidature:
            st.markdown(
                f"👤 **{cand['nome_lavoratore']}** | 📞 WhatsApp/Tel: `{cand['telefono']}`"
            )
            st.caption(
                "💡 Contatta direttamente il lavoratore per confermare l'orario e organizzare il pagamento immediato a fine turno."
            )
            st.divider()

# ==========================================
# ⭐ AREA AZIENDA PRO (Abbonamento & Vetrina)
# ==========================================
else:
    st.subheader("⭐ FlashJob PRO - Soluzione per Attività")
    st.write(
        "Ottimizza la ricerca di personale e dai massima visibilità alle tue urgenze."
    )

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown("### Piano Base (Free)")
        st.markdown(
            """
        - Pubblicità visibile
        - Posizione standard in bacheca
        - Gestione base candidature
        - **Costo:** 0€ (Sempre gratuito)
        """
        )
    with col_p2:
        st.markdown("### Piano PRO (Abbonamento)")
        st.markdown(
            """
        - **Annunci in Evidenza** (Blocco Top)
        - **Zero Pubblicità** nell'app
        - Notifiche push prioritarie ai lavoratori in zona
        - **Costo:** 39€ / mese (disdici quando vuoi)
        """
        )

    if st.button("Attiva Abbonamento Azienda PRO (39€/mese)"):
        st.success(
            "🎉 Account aggiornato a PRO! I tuoi prossimi turni saranno marchiati come 'In Evidenza'."
        )