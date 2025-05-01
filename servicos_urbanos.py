import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Fale com a Prefeitura", page_icon="📣", layout="centered")


if 'acesso_liberado' not in st.session_state:
    st.session_state.acesso_liberado = False

if 'pedidos' not in st.session_state:
    st.session_state.pedidos = pd.DataFrame(columns=[
        'Data', 'Nome', 'Contato', 'Problema', 'Detalhes', 'Endereço', 'Localidade', 'Status'
    ])


def registrar_pedido(nome, contato, problema, detalhes, endereco, localidade):
    novo = pd.DataFrame({
        'Data': [datetime.now().strftime("%d/%m/%Y %H:%M")],
        'Nome': [nome],
        'Contato': [contato],
        'Problema': [problema],
        'Detalhes': [detalhes],
        'Endereço': [endereco],
        'Localidade': [localidade],
        'Status': ["Pendente"]
    })
    st.session_state.pedidos = pd.concat([st.session_state.pedidos, novo], ignore_index=True)

# Tela de boas-vindas
if not st.session_state.acesso_liberado:
    st.title("📣 Bem-vindo ao Sistema da Prefeitura")
    st.subheader("Fale com a Prefeitura de Rosário do Ivaí")
    st.markdown("""
        Este sistema foi criado para facilitar a vida dos moradores.  
        Aqui você pode informar **problemas nas ruas**, **solicitar serviços** ou **dar sugestões**.

        Todas as mensagens são recebidas pela equipe da Prefeitura e tratadas com prioridade.

        Clique no botão abaixo para começar 👇
    """)
    if st.button("🟢 Entrar"):
        st.session_state.acesso_liberado = True
        st.rerun()
    st.markdown("---")
    st.caption("Sistema simples e digital — Prefeitura Rosário do Ivaí © 2025")
    st.stop()

st.title("🛠️ Enviar Pedido à Prefeitura")
st.caption("Rosário do Ivaí - Solicite serviços ou avise sobre problemas.")
st.markdown("---")


st.subheader("📝 Preencha abaixo")

nome = st.text_input("🧑 Qual é o seu nome?")
contato = st.text_input("📞 Telefone ou WhatsApp")


localidade = st.selectbox("🏘️ Localidade", [
    "Rosário do Ivaí", "Vila União", "Boa Vista", "Campineiro Do Sul"
])

problema = st.selectbox("⚠️ Qual é o problema?", [
    "Buraco na rua", "Lâmpada apagada", "Entulho ou lixo", "Árvore caída", "Outro"
])
detalhes = st.text_area("📄 Descreva o problema")
endereco = st.text_input("📍 Onde está isso? (rua ou ponto de referência)")

if st.button("✅ Enviar Pedido"):
    if nome and contato and detalhes and endereco:
        registrar_pedido(nome, contato, problema, detalhes, endereco, localidade)
        st.success("Pedido enviado com sucesso! A Prefeitura irá verificar.")
    else:
        st.warning("Por favor, preencha todos os campos.")


with st.expander("🔐 Área da Prefeitura"):
    senha = st.text_input("Senha de administrador", type="password")
    if st.button("Entrar como Admin"):
        if senha == "prefeitura123": #Senha Login
            st.session_state.admin = True
            st.rerun()
        else:
            st.error("Senha incorreta.")

# Painel Admin
if st.session_state.get("admin", False):
    st.subheader("📋 Pedidos Recebidos")
    if st.session_state.pedidos.empty:
        st.info("Nenhum pedido registrado ainda.")
    else:
        st.dataframe(st.session_state.pedidos, use_container_width=True)
        csv = st.session_state.pedidos.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Baixar lista (.csv)", data=csv, file_name="pedidos_prefeitura.csv", mime="text/csv")
        if st.button("🚪 Sair do Admin"):
            st.session_state.admin = False
            st.rerun()


st.markdown("---")
st.caption("Sistema digital de atendimento à população - Rosário do Ivaí © 2025")
