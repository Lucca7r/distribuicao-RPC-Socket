<h1 align="center">Sistema de Processamento de Imagem em Preto e Branco</h1>
<br>
<br>

<p align="center">
  <a href="#-descrição">Descrição</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-objetivo">Objetivo</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-Estrutura do Projeto">Estrutura do Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-Requisitos">Requisitos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-Como usar">Como usar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-Configuração">Configuração</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#licença">Licença</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

# 🎓Info
<p align="center">

Professor: Dr. Aldo Henrique Dias Mendes

Participantes: Lucas silva, Luan medrado

Disciplina: PROGRAMACAO CONCORRENTE E DISTRIBUIDA

Semestre: 2024/1
</p>

# 📝Descrição:

Este sistema permite enviar imagens para um servidor via WebSocket, convertê-las para preto e branco usando XML-RPC e receber as imagens processadas de volta. Ele foi projetado para lidar com várias imagens simultaneamente, aproveitando o paralelismo para otimizar o desempenho.

* todos os servidores foram criados no repl.it
<br>


# 🎯Objetivos

Entender o melhor funcionamento de um projeto distribuido usando threads e RPC e melhora o desempenho final.

<br>


# 🔧Estrutura do Projeto

- O sistema consiste em três componentes principais:

    - Cliente (cliente.py): Responsável por enviar as imagens para o servidor WebSocket. Ele usa uma abordagem assíncrona e multithreading para enviar várias imagens em paralelo, acelerando o processo.
<br>
    - Servidor RPC (rpc_img.py): Implementa uma função RPC (preto_branco) que recebe uma imagem codificada em Base64, converte-a para preto e branco e retorna a imagem processada, também em Base64.
<br>
    - Servidor WebSocket (websocket.py): Recebe as imagens do cliente, encaminha-as para o servidor RPC para processamento e envia as imagens em preto e branco de volta para o cliente.
<br>

# 🚩Requisitos

- Python 3.x<br>
- Bibliotecas: asyncio, websockets, base64, PIL, io, time, concurrent.futures, xmlrpc.server, xmlrpc.client, logging (já incluídas no código)

<br>


# 👩‍🔧Como usar

- Inicie o servidor RPC: Execute o arquivo rpc_img.py. Ele iniciará um servidor RPC na porta 8000.<br>
- Inicie o servidor WebSocket: Execute o arquivo websocket.py. Ele iniciará um servidor WebSocket na porta 8001. <br>
- Execute o cliente: Execute o arquivo cliente.py. Ele enviará as imagens listadas em imagens_paths para o servidor, que as processará e retornará as versões em preto e branco. As imagens processadas serão salvas na pasta out.<br>

    ** Serve no repl.it **

# ⚙️Configuração
- Caminhos das imagens: A lista imagens_paths em cliente.py contém os caminhos das imagens a serem enviadas. Modifique-a para incluir as imagens que você deseja processar.<br>
- URL do servidor WebSocket: A variável url_servidor em cliente.py deve apontar para o endereço do servidor WebSocket.<br>
- Certifique-se de que ele esteja correto.<br>
- Endereços dos servidores: Os scripts rpc_img.py e websocket.py estão configurados para rodar em "0.0.0.0". Se os servidores estiverem em endereços diferentes, ajuste as configurações nos scripts.
<br>


# ©Licença:

Este repositório está licenciado sob a licença MIT.
<p align="center">
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=49AA26&labelColor=000000">
</p>