# Galeria de Amigos API 📸

Bem-vindo ao repositório da API da Galeria de Amigos! Aqui, você encontrará o código que ajuda a resolver um problemão: criar uma galeria de fotos para o casamento do seu amigo. Vamos te contar mais:

## O Desafio
O seu amigo está prestes a se casar e te pediu uma ajuda: criar uma maneira de todos os amigos compartilharem as fotos do casamento. Parece legal, né? Mas tem um detalhe, só `ele e o cônjuge podem aprovar` as fotos antes de todo mundo ver. Além disso, curtidas e comentários nas fotos seriam demais!

## Funcionalidades ✨

Esta API oferece os seguintes recursos:

- Listagem de todas as fotos: `GET` [todas_as_fotos](https://testefotos-df3cf30201b0.herokuapp.com/fotoscasamento/)
- Listagem de todas as curtidas: `GET` [todas_as_curtidas](https://testefotos-df3cf30201b0.herokuapp.com/curtidas/)
- Listagem de todos os comentários: `GET` [comentários](https://testefotos-df3cf30201b0.herokuapp.com/comentarios/)
- Tela de Login: `POST` [login](https://testefotos-df3cf30201b0.herokuapp.com/admin/)

## Tecnologias Utilizadas 🛠️

- Python e Django 🐍
- Django Rest Framework 🌐
- Banco de Dados para armazenamento 🗄️
- Autenticação para garantir a segurança 🔐

## Configuração Inicial 🚀

1. Clone este repositório.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Configure o banco de dados no arquivo `settings.py`.
4. Execute as migrações com `python manage.py migrate`.
5. Inicie o servidor com `python manage.py runserver`.

## Entre em Contato ☎️

Se surgir alguma dúvida ou se quiser compartilhar alguma sugestão, sinta-se à vontade para abrir uma issue neste repositório.

Divirta-se compartilhando memórias com seus amigos! 🥂👰🤵‍♂️
