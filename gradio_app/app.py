import gradio as gr
import pandas as pd
import os
from datetime import datetime

ARQUIVO_CSV = os.path.join(os.path.dirname(__file__), "pacientes.csv")
COLUNAS = ["timestamp", "nome", "idade", "convenio", "prioridade", "motivo"]


def carregar_ultimos():
    if os.path.exists(ARQUIVO_CSV):
        return pd.read_csv(ARQUIVO_CSV).tail(5)
    return pd.DataFrame(columns=COLUNAS)


def cadastrar_paciente(nome, idade, convenio, prioridade, motivo):
    if not nome or not str(nome).strip():
        return "⚠️ Por favor, informe o nome do paciente.", carregar_ultimos()

    linha = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nome": str(nome).strip(),
        "idade": int(idade) if idade is not None else 0,
        "convenio": convenio,
        "prioridade": int(prioridade),
        "motivo": str(motivo).strip() if motivo else "",
    }
    novo = pd.DataFrame([linha])
    if os.path.exists(ARQUIVO_CSV):
        novo.to_csv(ARQUIVO_CSV, mode="a", header=False, index=False)
    else:
        novo.to_csv(ARQUIVO_CSV, mode="w", header=True, index=False)
    return "✅ Paciente cadastrado com sucesso!", pd.read_csv(ARQUIVO_CSV).tail(5)


with gr.Blocks(title="Cadastro de Pacientes") as demo:
    gr.Markdown("## 🏥 Cadastro de Pacientes — Consultório Médico")
    gr.Markdown("Preencha os dados do paciente abaixo para registrar o atendimento.")

    nome = gr.Textbox(label="Nome do paciente", placeholder="Ex.: Maria Oliveira")
    idade = gr.Number(label="Idade", value=30, minimum=0, maximum=120, precision=0)
    convenio = gr.Dropdown(
        choices=["Particular", "Unimed", "Bradesco Saúde", "SulAmérica", "Outro"],
        value="Particular",
        label="Convênio",
    )
    prioridade = gr.Slider(
        minimum=1,
        maximum=5,
        step=1,
        value=1,
        label="Prioridade do atendimento (1 = normal, 5 = urgente)",
    )
    motivo = gr.Textbox(
        label="Motivo da consulta / observações",
        placeholder="Descreva os sintomas ou motivo do retorno...",
        lines=3,
    )
    botao = gr.Button("Cadastrar", variant="primary")
    saida_msg = gr.Textbox(label="Status", interactive=False)
    tabela = gr.Dataframe(
        value=carregar_ultimos,
        label="Últimos pacientes cadastrados",
        interactive=False,
    )

    botao.click(
        fn=cadastrar_paciente,
        inputs=[nome, idade, convenio, prioridade, motivo],
        outputs=[saida_msg, tabela],
    )

if __name__ == "__main__":
    demo.launch()
