import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Configurazione della pagina (stile e titolo nel browser)
st.set_page_config(page_title="Gestionale Fatture & Clienti", page_icon="💼", layout="wide")

# File locale per salvare i dati (il nostro "database" in formato Excel/CSV)
DB_FILE = "archivio_fatture.csv"

# Funzione per caricare i dati esistenti
def carica_dati():
    if os.path.exists(DB_FILE):
        return pd.read_csv(DB_FILE)
    else:
        # Struttura iniziale del database
        return pd.DataFrame(columns=[
            "Data", "Anno", "Cliente", "Piva_CF", "Regione", "Descrizione", "Imponibile", "IVA", "Totale"
        ])

st.title("💼 Mini Gestionale & Ricerca Fatture")
st.markdown("---")

# Creiamo due sezioni (Tab): una per inserire le fatture, una per cercarle e consultarle
tab1, tab2 = st.tabs(["➕ Nuova Fattura / Ricevuta", "🔍 Archivio e Ricerca Avanzata"])

# ================= TAB 1: INSERIMENTO =================
with tab1:
    st.subheader("Inserisci i dati del documento")
    
    col1, col2 = st.columns(2)
    with col1:
        cliente_nome = st.text_input("Nome / Azienda Cliente")
        piva_cf = st.text_input("Partita IVA / Codice Fiscale")
        regione = st.selectbox("Regione", [
            "Abruzzo", "Basilicata", "Calabria", "Campania", "Emilia-Romagna", 
            "Friuli-Venezia Giulia", "Lazio", "Liguria", "Lombardia", "Marche", 
            "Molise", "Piemonte", "Puglia", "Sardegna", "Sicilia", "Toscana", 
            "Trentino-Alto Adige", "Umbria", "Valle d'Aosta", "Veneto", "Estero / Altro"
        ])
    with col2:
        data_emissione = st.date_input("Data Emissione", datetime.today())
        importo = st.number_input("Imponibile (€)", min_value=0.0, value=500.0, step=50.0)
        applica_iva = st.checkbox("Applica IVA (22%)", value=True)

    descrizione = st.text_area("Descrizione del servizio o prodotto", "Es. Consulenza strategica / Sviluppo software")

    # Calcoli
    iva = importo * 0.22 if applica_iva else 0.0
    totale = importo + iva

    st.info(f"📊 **Totale calcolato:** Imponibile: €{importo:.2f} + IVA: €{iva:.2f} = **Totale: €{totale:.2f}**")

    if st.button("💾 Salva e Registra Documento", type="primary"):
        if not cliente_nome or not piva_cf:
            st.warning("⚠️ Inserisci almeno il Nome Cliente e la Partita IVA/CF per procedere!")
        else:
            df_esistente = carica_dati()
            
            # Prepara la nuova riga
            nuova_riga = {
                "Data": str(data_emissione),
                "Anno": str(data_emissione.year),
                "Cliente": cliente_nome,
                "Piva_CF": piva_cf,
                "Regione": regione,
                "Descrizione": descrizione,
                "Imponibile": round(importo, 2),
                "IVA": round(iva, 2),
                "Totale": round(totale, 2)
            }
            
            # Aggiunge la riga e salva
            df_aggiornato = pd.concat([df_esistente, pd.DataFrame([nuova_riga])], ignore_index=True)
            df_aggiornato.to_csv(DB_FILE, index=False)
            
            st.success(f"✅ Documento salvato con successo per il cliente {cliente_nome}!")

# ================= TAB 2: RICERCA E FILTRI =================
with tab2:
    st.subheader("🔍 Filtra e Cerca nell'Archivio")
    
    df = carica_dati()
    
    if df.empty:
        st.warning("Nessun documento salvato al momento. Creane uno dalla prima scheda!")
    else:
        # Barra di ricerca e filtri avanzati disposti in colonna
        f1, f2, f3, f4 = st.columns(4)
        
        with f1:
            filtro_nome = st.text_input("Cerca per Nome Cliente")
        with f2:
            filtro_piva = st.text_input("Cerca per P.IVA / CF")
        with f3:
            # Estrae gli anni unici presenti nel database
            anni_disponibili = ["Tutti"] + sorted(df["Anno"].unique().tolist())
            filtro_anno = st.selectbox("Filtra per Anno", anni_disponibili)
        with f4:
            regioni_disponibili = ["Tutte"] + sorted(df["Regione"].unique().tolist())
            filtro_regione = st.selectbox("Filtra per Regione", regioni_disponibili)
            
        # Applicazione dei filtri sui dati
        df_filtrato = df.copy()
        
        if filtro_nome:
            df_filtrato = df_filtrato[df_filtrato["Cliente"].str.contains(filtro_nome, case=False, na=False)]
        if filtro_piva:
            df_filtrato = df_filtrato[df_filtrato["Piva_CF"].str.contains(filtro_piva, case=False, na=False)]
        if filtro_anno != "Tutti":
            df_filtrato = df_filtrato[df_filtrato["Anno"] == str(filtro_anno)]
        if filtro_regione != "Tutte":
            df_filtrato = df_filtrato[df_filtrato["Regione"] == filtro_regione]
            
        st.markdown(f"**Documenti trovati:** {len(df_filtrato)}")
        
        # Mostra la tabella pulita ed elegante
        st.dataframe(df_filtrato, use_container_width=True)
        
        # Opzione per scaricare i dati filtrati in Excel/CSV
        csv_data = df_filtrato.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Scarica i risultati in formato CSV",
            data=csv_data,
            file_name="report_fatture_filtrate.csv",
            mime="text/csv",
        )