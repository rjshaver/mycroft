from sqlalchemy import Table, Column, String

from util import hook, botvars

users = Table(
    'user_table', botvars.metadata,
    Column('name', String),
    Column('phone', String)
)


@hook.command
def dbadduser(text, db):
    """
    :type text: str
    :type db: sqlalchemy.engine.base.Engine
    """

    data = text.split()
    values = {
        "name": data[0],
        "phone": data[1]
    }

    query = users.insert(values=values)
    # OR users.insert().values(**values) - http://docs.sqlalchemy.org/en/rel_0_9/core/tutorial.html

    db.execute(query)


@hook.command(autohelp=False)
def select(db, message):
    results = db.execute(users.select())
    for row in results:
        message("name: {}, phone: {}".format(row.name, row.phone))
