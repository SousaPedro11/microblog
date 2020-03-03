from app import db


def transacao(objeto):
    """Funcao que insere ou atualiza os registros do banco.

    Examples:
        user = User(username='fulano', email='fulano@exemplo.com')
        DAO.transacao(user)

    :param objeto: Objeto a ser inserido ou alterado no banco

    :type objeto: object
    """
    db.session.add(objeto)
    db.session.commit()


def deletar(objeto):
    """Funcao que remove um registro do banco.

    Examples:
        user = User.query.filter_by(username='fulano').first()
        DAO.deletar(user)

        user1 = DAO.buscar_por_criterio(User, username='fulano')
        DAO.deletar(user1)

    :param objeto: Objeto a ser removido do banco

    :type objeto: object
    """
    db.session.delete(objeto)
    db.session.commit()


def buscar_todos(table, *order_by):
    """Funcao que retorna uma lista de objetos a partir de uma query.
    A lista pode ser ordenada utilizando os atributos.

    Examples:
        users = DAO.buscar_todos(User)
        users_ordered_by_username = DAO.buscar_todos(User, User.username)

    :param table: Classe que representa a tabela do banco

    :type table: class

    :param order_by: Atributo da classe que definira a ordenacao da lista de objetos

    :type order_by: attribute of class

    :return: Lista de objetos da tabela

    :rtype: list
    """
    return table.query.order_by(*order_by).all()


def buscar_por_criterio_bool(table, *filtros):
    """Funcao que retorna um objeto a partir de uma query filtrada.
    Caso o filtro não exista ela retorna o primeiro objeto.

    Example:
        user = DAO.buscar_por_criterio_bool(User, User.username == 'fulano')
        user1 = DAO.buscar_por_criterio_bool(User)

    :param table: Classe que representa a tabela do banco

    :type table: class

    :param filtros: filtros comparativos entre atributos e valores

    :type filtros: bool

    :return: objeto: primeiro registro encontrado como object

    :rtype: object

    """
    return table.query.filter(*filtros).first()


def buscar_por_criterio(table, **filtros):
    """Funcao que retorna um objeto a partir de uma query filtrada.
    Caso o filtro não exista ela retorna o primeiro objeto.

    Example:
        user = DAO.buscar_por_criterio(User, username='fulano')
        user1 = DAO.buscar_por_criterio(User)

    :param table: Classe que representa a tabela do banco

    :type table: class

    :param filtros: filtros chave=valor dos atributos

    :type filtros: attributes of class

    :return: objeto: primeiro registro encontrado como object

    :rtype: object
    """
    return table.query.filter_by(**filtros).first()


def buscar_por_criterio_404(table, **filtros):
    """Funcao que retorna ou um objeto a partir de uma query filtrada ou uma exception 404.
        Caso o filtro não exista ela retorna o primeiro objeto.

        Example:
            user = DAO.buscar_por_criterio_404(User, username='fulano')
            user1 = DAO.buscar_por_criterio_404(User)

        :param table: Classe que representa a tabela do banco

        :type table: class

        :param filtros: filtros chave=valor dos atributos

        :type filtros: attributes of class

        :return: objeto: primeiro registro encontrado como object

        :rtype: object

        :raise: werkzeug.exceptions.NotFound
        """
    return table.query.filter_by(**filtros).first_or_404()


def buscar_todos_por_join(table1, table2, *order_by):
    return table1.query.join(table2).order_by(*order_by).add_entity(table2).all()


def buscar_por_join_com_criterio(table1, table2, *filtro):
    return table1.query.join(table2).filter(*filtro).add_entity(table2).first()


def busca_por_join_composto_com_criterio(table1, table2, table3, *filtro):
    return table1.query.join(table2).join(table3).filter(*filtro).add_entity(table2).add_entity(table3).first()
