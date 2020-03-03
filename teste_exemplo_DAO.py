from app import DAO
from app.models import User, Post

user = DAO.buscar_por_criterio_bool(User, User.username == 'admin')
print(user)
user2 = DAO.buscar_por_criterio(User, username='marco')
print(user2)
user3 = DAO.buscar_por_criterio_404(User, username='admin')
print(user3)
user4 = DAO.buscar_todos(User, User.username, User.email)
print(user4)
user5 = DAO.buscar_todos_por_join(User, Post, User.username)
print(user5)

# # posts = DAO.buscar_todos(Post)
# # for x in posts:
# #     DAO.deletar(x)
#
# post = Post(body='Ola a todos!')
# print(post)
# user2.posts.append(post)
# post2 = Post(body='Hi!')
# user2.posts.append(post2)
# post3 = Post(body='vtnc')
# user.posts.append(post3)
# user.posts.append(post)
# DAO.transacao(user)
# DAO.transacao(user2)
