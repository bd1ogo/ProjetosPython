#Passo a passo:
#titulo
#input do chat, campo de mensagem
#a cada mensagem enviada pelo o usuário:
    #exibir a mensagem do usuário no chat
    #pegar a pergunta e enviar para uma IA responder
    #exibir a resposta da IA no chat

#Utilizar o Streamlit -> apenas com Python puro cria o frontend e o backend
#IA utilizada -> OpenAI

import streamlit as st

st.write("## FalsoGPT - Chatbot")

texto_usuario = st.chat_input("Digite sua mensagem...")
if texto_usuario:
    st.chat_message("user").write(texto_usuario)

    resposta_ia = "Sua pergunta foi: " + texto_usuario
    st.chat_message("assistant").write(resposta_ia)
