import streamlit as st
import time
import random
import string

st.title("Testes streamlit.")

# TABUADA
st.subheader("Contador")

number = st.number_input("Insira um número para ver a tabuada", value=0)

if st.button('Ver tabuada'):
    for i in range(11):
        st.info(i*number)


#CONTADOR
st.subheader("Contador")
n = st.number_input("Veja os segundos a partir de um número inserido", value=0)

if st.button("Começar"):
    c = 0
    while c != n:
        c += 1
        st.info(c)
        time.sleep(1)


#GERADOR DE SENHAS
st.subheader("Gerador de senhas")

letters = string.ascii_letters
random_password = random.choices(letters, k=9)

if st.button("Gerar senha aleatória"):
    st.info(random_password)
