# 🏥 Cadastro de Pacientes: Gradio x Streamlit

Atividade Prática — Interfaces Web/Mobile para Coleta de Dados (**Gradio** vs **Streamlit**).

## 📂 Estrutura do Repositório

```text
├── app.py                      # Ponto de entrada raiz para o Streamlit Cloud
├── requirements.txt            # Dependências (streamlit, gradio, pandas)
├── pacientes.csv               # Arquivo CSV de exemplo gerado nos testes
├── gradio_app/
│   ├── app.py                  # Parte 1: Interface em Gradio (gr.Blocks)
│   ├── pacientes.csv           # Dados persistidos localmente pelo Gradio
│   └── requirements.txt
└── streamlit_app/
    ├── app.py                  # Parte 2: Interface em Streamlit (st.form + st.session_state)
    └── requirements.txt
```

## 🚀 Como Executar Localmente

### 1. Instalar dependências
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Executar a Parte 1 (Gradio)
```bash
python gradio_app/app.py
```
Acesse no navegador o endereço exibido no terminal (geralmente `http://127.0.0.1:7860`).

### 3. Executar a Parte 2 (Streamlit)
```bash
streamlit run streamlit_app/app.py
```

## ☁️ Deploy no Streamlit Community Cloud

1. Suba este repositório para o seu GitHub (público).
2. Acesse [share.streamlit.io](https://share.streamlit.io/) e faça login com sua conta do GitHub.
3. Clique em **New app**, selecione este repositório, a branch principal (`main`) e informe `streamlit_app/app.py` (ou `app.py`) como **Main file path**.
4. Clique em **Deploy!** e aguarde a geração do link público `*.streamlit.app`.
