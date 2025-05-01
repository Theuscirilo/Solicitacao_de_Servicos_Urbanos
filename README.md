# 📣 Fale com a Prefeitura – Rosário do Ivaí

Sistema digital simples e eficiente para facilitar a comunicação entre os cidadãos e a Prefeitura de Rosário do Ivaí.

## 💡 Visão Geral

Este aplicativo web, desenvolvido com [Streamlit](https://streamlit.io/), permite que moradores relatem **problemas públicos**, façam **reclamações**, enviem **sugestões** ou **solicitem serviços** diretamente à administração municipal. Ele também oferece um **painel administrativo** para consulta e exportação dos pedidos recebidos.

---

## 🚀 Funcionalidades

- 📝 **Formulário de envio** de pedidos com dados como nome, contato, problema, detalhes e localização.
- 🗂️ **Armazenamento dos pedidos** na sessão do Streamlit (`st.session_state`).
- 🔒 **Área administrativa** protegida por senha (`prefeitura123`) com:
  - Visualização dos pedidos recebidos.
  - Download dos dados em formato `.csv`.
- 🎨 Interface clara, direta e acessível.

---

## 📦 Tecnologias Utilizadas

- [Python 3.9+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)

---

## 🛠️ Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/fale-com-a-prefeitura.git
   cd fale-com-a-prefeitura
2. **Instale as dependências:**:
   ```bash
   pip install -r requirements.txt
2. **Execute o aplicativo:**:
   ```bash
   streamlit run app.py
