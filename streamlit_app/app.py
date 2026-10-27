import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Cadastro de Pacientes", page_icon="🏥", layout="centered")
st.title("🏥 Cadastro de Pacientes")
st.markdown("Sistema de recepção para registro rápido de pacientes do consultório.")

ARQUIVO_CSV = os.path.join(os.path.dirname(__file__), "pacientes.csv")
COLUNAS = ["timestamp", "nome", "idade", "convenio", "prioridade", "motivo"]

if "pacientes" not in st.session_state:
    if os.path.exists(ARQUIVO_CSV):
        st.session_state.pacientes = pd.read_csv(ARQUIVO_CSV)
    else:
        st.session_state.pacientes = pd.DataFrame(columns=COLUNAS)

with st.form("cadastro", clear_on_submit=True):
    nome = st.text_input("Nome do paciente", placeholder="Ex.: Maria Oliveira")
    idade = st.number_input("Idade", min_value=0, max_value=120, step=1, value=30)
    convenio = st.selectbox(
        "Convênio",
        ["Particular", "Unimed", "Bradesco Saúde", "SulAmérica", "Outro"],
    )
    prioridade = st.slider(
        "Prioridade do atendimento (1 = normal, 5 = urgente)", 1, 5, 1
    )
    motivo = st.text_area(
        "Motivo da consulta / observações",
        placeholder="Descreva os sintomas ou motivo do retorno...",
    )
    enviado = st.form_submit_button("Cadastrar", use_container_width=True)

if enviado:
    if not nome.strip():
        st.warning("⚠️ Por favor, informe o nome do paciente.")
    else:
        nova_linha = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "nome": nome.strip(),
            "idade": int(idade),
            "convenio": convenio,
            "prioridade": int(prioridade),
            "motivo": motivo.strip(),
        }
        novo_df = pd.DataFrame([nova_linha])
        st.session_state.pacientes = pd.concat(
            [st.session_state.pacientes, novo_df],
            ignore_index=True,
        )
        # Também persiste no arquivo CSV local (efêmero no Streamlit Cloud)
        if os.path.exists(ARQUIVO_CSV):
            novo_df.to_csv(ARQUIVO_CSV, mode="a", header=False, index=False)
        else:
            novo_df.to_csv(ARQUIVO_CSV, mode="w", header=True, index=False)

        st.success("✅ Paciente cadastrado com sucesso!")

st.subheader("Últimos pacientes cadastrados")
st.dataframe(st.session_state.pacientes.tail(5), use_container_width=True)

csv = st.session_state.pacientes.to_csv(index=False).encode("utf-8")
st.download_button(
    label="📥 Baixar CSV (pacientes.csv)",
    data=csv,
    file_name="pacientes.csv",
    mime="text/csv",
    use_container_width=True,
)
