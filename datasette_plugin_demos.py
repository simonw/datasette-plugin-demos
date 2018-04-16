from datasette import hookimpl
import random


@hookimpl
def prepare_jinja2_environment(env):
    env.filters['uppercase'] = lambda u: u.upper()


@hookimpl
def prepare_connection(conn):
    conn.create_function('random_integer', 2, random.randint)
