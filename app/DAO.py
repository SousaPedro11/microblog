from app import db


def transacao(objeto):
    db.session.add(objeto)
    db.session.commit()


def deletar(objeto):
    db.session.delete(objeto)
    db.session.commit()


def buscar_todos(table, *order_by):
    return table.query.order_by(*order_by).all()
