#input do chat (campo de mensagem)
# a cada mensagem que o usuario enviou no chat
    #mostrar a mensagem que o usuário mandou
    #pegar a pergunta e enviar para uma IA responder
    #exibir a resposta da IA na tela

# streamlit run Hashtag/4/teste.py
import streamlit as st
from openai import OpenAI
modelo_ia = OpenAI(base_url= "http://127.0.0.1:1234/v1", api_key="skA")
st.write("# Matheus IA") #Markdown
if not 'lista_mensagens'in st.session_state:
    st.session_state['lista_mensagens'] =[]    
texto_usuario = st.chat_input("Digite sua mensagem")
for mensagem in st.session_state['lista_mensagens']:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)  
if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {'role':'user', "content": texto_usuario}
    st.session_state['lista_mensagens'].append(mensagem_usuario)   
    #Nome - vai aparecer primeira letra do nome
    #user - ícone de usuário
    #assistant - ícone de robo

    #ia respondeu
    resposta_ia = modelo_ia.chat.completions.create(
        messages= st.session_state['lista_mensagens'],
        model = "qwen/qwen3-4b-2507")
    print(resposta_ia)
    texto_resposta_ia = resposta_ia.choices[0].message.content
    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {'role':'assistant', "content": texto_resposta_ia}
    st.session_state['lista_mensagens'].append(mensagem_ia)
 