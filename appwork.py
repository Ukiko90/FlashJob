import streamlit as st
import pandas as pd
from datetime import datetime

# Configurazione della pagina
st.set_page_config(page_title="FlashJob - Trova Lavoro Last-Minute", layout="wide")

# Inizializzazione dello Stato della sessione
if "offerte_lavoro" not in st.session_state:
    st.session_state.offerte_lavoro = [
        {
            "id": 1,
            "azienda": "The Sanctuary Eco Retreat",
            "mansione": "Addetto Sala / Bar",
            "data": "2026-06-20",
            "orario": "18:00 - 02:00",
            "compenso": "90€",
            "stato": "Aperta",
            "candidato_assegnato": None
        },
        {
            "id": 2,
            "azienda": "Terrazza Duomo Milano",
            "mansione": "Supporto Accoglienza",
            "data": "2026-06-22",
            "orario": "10:00 - 16:00",
            "compenso": "60€",
            "stato": "Aperta",
            "candidato_assegnato": None
        }
    ]

if "candidature" not in st.session_state:
    st.session_state.candidature = []

# Titolo principale
st.title("⚡ FlashJob: Il lavoro last-minute a misura di persona")
st.markdown("La piattaforma dove l'azienda pubblica l'esigenza e **il lavoratore si propone all'ultimo secondo!**")

# Sidebar per scegliere la visualizzazione
modalita = st.sidebar.radio("Scegli la tua modalità:", ["🏢 Sono un'Azienda (Pubblica Offerta)", "🙋‍♂️ Sono un Lavoratore (Trova & Proponiti)"])

st.divider()

# --- AREA 1: AZIENDA ---
if modalita == "🏢 Sono un'Azienda (Pubblica Offerta)":
    st.header("Gestione Annunci & Turni Urgenti")
    
    with st.form("form_offerta"):
        st.subheader("Crea una nuova richiesta di lavoro")
        col1, col2 = st.columns(2)
        
        with col1:
            nome_azienda = st.text_input("Nome Attività / Azienda", value="The Sanctuary")
            mansione = st.text_input("Mansione richiesta", value="Addetto Vendite / Eventi")
            data_turno = st.date_input("Data del turno", value=datetime.today())
            
        with col2:
            orario_turno = st.text_input("Orario (es. 15:00 - 23:00)", value="16:00 - 00:00")
            compenso_offerto = st.text_input("Compenso totale stimato", value="80€")
            
        submitted = st.form_submit_button("🚀 Pubblica Offerta Last-Minute")
        if submitted:
            nuova_offerta = {
                "id": len(st.session_state.offerte_lavoro) + 1,
                "azienda": nome_azienda,
                "mansione": mansione,
                "data": str(data_turno),
                "orario": orario_turno,
                "compenso": compenso_offerto,
                "stato": "Aperta",
                "candidato_assegnato": None
            }
            st.session_state.offerte_lavoro.append(nuova_offerta)
            st.success("Offerta pubblicata con successo! I lavoratori ora possono vederla e proporsi.")

    st.subheader("📊 Le tue offerte attive e stato candidature")
    if not st.session_state.offerte_lavoro:
        st.info("Nessuna offerta pubblicata.")
    else:
        for offerta in st.session_state.offerte_lavoro:
            with st.expander(f"{offerta['azienda']} - {offerta['mansione']} ({offerta['data']}) | Stato: {offerta['stato']}"):
                st.write(f"**Orario:** {offerta['orario']}")
                st.write(f"**Compenso:** {offerta['compenso']}")
                
                # Mostra chi si è candidato per questa offerta
                candidati_per_questo = [c for c in st.session_state.candidature if c["offerta_id"] == offerta["id"]]
                
                if candidati_per_questo:
                    st.markdown("---")
                    st.markdown("### 👥 Lavoratori che si sono proposti:")
                    for cand in candidati_per_questo:
                        col_c1, col_c2 = st.columns([3, 1])
                        with col_c1:
                            st.write(f"• **{cand['nome_lavoratore']}** (Affidabilità: ⭐ 4.9)")
                        with col_c2:
                            if offerta["stato"] == "Aperta":
                                if st.button(f"Conferma {cand['nome_lavoratore']}", key=f"conf_{cand['id']} "):
                                    offerta["stato"] = "Assegnato"
                                    offerta["candidato_assegnato"] = cand["nome_lavoratore"]
                                    st.success(f"Hai assegnato il turno a {cand['nome_lavoratore']}!")
                                    st.rerun()
                else:
                    st.info("Nessun lavoratore si è ancora proposto per questo turno.")

# --- AREA 2: LAVORATORE ---
else:
    st.header("Bacheca Lavori Disponibili (Candidati al volo)")
    st.markdown("Scegli tra le offerte aperte e **proponiti subito** con un click prima che lo faccia qualcun altro!")
    
    nome_utente = st.text_input("Inserisci il tuo nome e cognome per candidarti:", value="Mario Rossi")
    
    offerte_aperte = [o for o in st.session_state.offerte_lavoro if o["stato"] == "Aperta"]
    
    if not offerte_aperte:
        st.info("Al momento non ci sono offerte di lavoro attive. Torna a controllare più tardi!")
    else:
        for offerta in offerte_aperte:
            with st.container():
                st.markdown(f"""
                ### 🏷️ {offerta['mansione']} presso **{offerta['azienda']}**
                * **Data:** {offerta['data']} ({offerta['orario']})
                * **Compenso:** 💰 {offerta['compenso']}
                """)
                
                # Verifica se l'utente si è già candidato
                gia_candidato = any(c["offerta_id"] == offerta["id"] and c["nome_lavoratore"] == nome_utente for c in st.session_state.candidature)
                
                if gia_candidato:
                    st.info("✅ Ti sei già candidato per questa posizione. In attesa di risposta dall'azienda.")
                else:
                    if st.button(f"🙋‍♂️ Voglio farlo io! (Candidati)", key=f"proponiti_{offerta['id']}"):
                        nuova_candidatura = {
                            "id": len(st.session_state.candidature) + 1,
                            "offerta_id": offerta["id"],
                            "nome_lavoratore": nome_utente,
                            "data_candidatura": datetime.now().strftime("%H:%M:%S")
                        }
                        st.session_state.candidature.append(nuova_candidatura)
                        st.success(f"Ottimo {nome_utente}! Ti sei proposto con successo. L'azienda valuterà la tua candidatura.")
                        st.rerun()
                st.divider()