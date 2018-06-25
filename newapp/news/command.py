import click
import newspaper
from termcolor import colored
from flask.cli import with_appcontext
from . import app
from . import news
from .database import getDatabase, dupDatabase, closeDatabase


@click.command('init-db', short_help=colored("Initialize news database.", "blue"))
@with_appcontext
def initDatabaseCmd():
    try:
        dupDatabase()
    except:
        click.echo(colored("WARNING: Duplicating database failed!", "yellow", "on_white"))
    db = database.getDatabase()
    with app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    click.echo(colored("Initialize News Database Succeed!", "cyan"))


@click.command('show-article', short_help=colored("Show a single article.", "blue"))
@click.option('--url', help=colored('Article url.', "yellow"), default='0')
@with_appcontext
def showNewsArticleCmd(url):
    article = newspaper.Article(url)
    click.echo(news.showArticle(article))


@click.command('add-article', short_help=colored("Add a single article into database.", "blue"))
@click.option('--url', help=colored('Article url.', "yellow"), default='0')
@with_appcontext
def addArticleCmd(url):
    article = newspaper.Article(url)
    data = news.getArticleData(url)
    db = getDatabase()
    news.addArticle(data, db)


@click.command('show-news', short_help=colored("Show a news from a source website.", "blue"))
@click.option('--url', help=colored('News url.', "yellow"), default='0')
@with_appcontext
def showNewsPaperCmd(url):
    click.echo(news.showNews(url))


@click.command('add-news', short_help=colored("Show a news from a source website.", "blue"))
@click.option('--url', help=colored('News url.', "yellow"), default='0')
@with_appcontext
def addNewsCmd(url):
    db = getDatabase()
    news_data = news.getNewsPaperData(url)
    news.addNews(news_data, db)



def initApp():
    app.teardown_appcontext(initDatabaseCmd)
    app.cli.add_command(showNewsPaperCmd)
    app.cli.add_command(showNewsArticleCmd)
    app.cli.add_command(addArticleCmd)
    app.cli.add_command(showNewsPaperCmd)
    app.cli.add_command(addNewsCmd)