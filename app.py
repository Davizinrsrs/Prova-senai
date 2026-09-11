import streamlit as st
import database as db
import pandas as pd

db.criar_tabela()

st.title("Sistema BookTrack")

st.markdown("Cadastrar Livro")
with st.form("form_cad"):
    titulo = st.text_input("Título")
    autor = st.text_input("Autor")
    ano = st.number_input("Ano de Publicação", value=2024, step=1, max_value=2026)
    btn1 = st.form_submit_button("Cadastrar")

if btn1:
    res = db.cadastro_livro(titulo, autor, ano)
    if res == "OK":
        st.success("Livro cadastrado com maestria, meu senhor.")
    else:
        st.error(res)

st.markdown("Atualizar Status")
with st.form("form_upd"):
    id_upd = st.number_input("ID do Livro", value=0, step=1)
    status_sel = st.selectbox("Status", ["Não Lido", "Lendo", "Lido"])
    btn2 = st.form_submit_button("Atualizar Status")

if btn2:
    res = db.update_status_livro(id_upd, status_sel)
    if res == 1:
        st.success("Status atualizado papai!")
    else:
        st.error(res)

#parte de excluir
st.markdown("Excluir Livro")
with st.form("form_del"):
    id_del = st.number_input("ID pra deletar", value=0, step=1)
    btn3 = st.form_submit_button("Deletar")

if btn3:
    res = db.delete_livro(id_del)
    if res == 1:
        st.success("Livro foi deletado, irmãozinho.")
    else:
        st.error(res)

#parte dA regra 4
st.markdown("Acervo de Livros")
lista = db.getLivros()

if lista == None or len(lista) == 0:
    st.warning("Não tem livros cadastrados, chefe. Volta lá em cima e cadastra um livro.") #um salve pro nosso parceiro Eric
else:
    df = pd.DataFrame(lista, columns=["ID", "Título", "Autor", "Ano", "Status"])
    st.dataframe(df, hide_index=True)
