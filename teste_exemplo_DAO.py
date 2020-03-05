import json

from app import DAO
from app.models import User, Post

# user = User(username='admin', email='admin@example.com')
# user.set_password('admin@123')
# user2 = User(username='marco', email='marco@example.com')
# user2.set_password('marco@123')

user = DAO.buscar_por_criterio_bool(User, User.username == 'admin')
# print(user)
user2 = DAO.buscar_por_criterio(User, username='marco')
post2 = Post(body='Minha bola! hahaha')
# user2.posts.append(post)
# DAO.transacao(user2)
# print(user2)
# user3 = DAO.buscar_por_criterio_404(User, username='admin')
# print(user3)
# user4 = DAO.buscar_todos(User, User.username, User.email)
# for u in user4:
#     print(20*'-')
#     print(u)
#     [print(p) for p in u.posts]

# DAO.deletar(user2)
# user5 = DAO.buscar_todos_por_join(User, Post, User.username)
# print(user5)

# posts = DAO.buscar_todos(Post)
# [DAO.deletar(p) if 'Hi' in p.body else print('Registro não existe') for p in posts]
# [print(p) for p in posts]
# for x in posts:
#     DAO.deletar(x)
#
# post = Post(body='Ola a todos!')
# user2.posts.append(post)
# post3 = Post(body='vtnc')
# user.posts.append(post3)
# post2 = Post(body='Hi!')
# user2.posts.append(post2)
post = Post(body='O que rola?')
user.posts.append(post)
user2.posts.append(post2)
DAO.transacao(user)
DAO.transacao(user2)

# user = DAO.buscar_por_criterio_404(User, username='admin')
# posts = json.dumps([{'author': p.author.username, 'body': p.body} for p in user.posts])
# print(posts)


