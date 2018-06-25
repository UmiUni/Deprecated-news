import click
import newspaper
from datetime import datetime


COLS = ['title', 'authors', 'text', 'url', 'source_url', 'summary', 'keywords']


def getArticleData(article):
    article.download()
    if article.download_state != 2:
        raise Exception(article.download_exception_msg)
    article.parse()
    article.nlp()
    #Loading article data
    article_data = {}
    o = vars(article)
    for key in COL:
        article_data[key] = o[key]
    article_data['timestamp'] = str(datetime.now())
    article_data['publish_date'] = str(o['publish_date'].date()) 
    return article_data


def addArticle(data, db):
    db.execute(
        'INSERT INTO articles (title, author, publish_date, tstamp, summary, keywords)'
        ' VALUES (?, ?, ?, ?, ?, ?)', data['title'], data['author'], data['publish_date'],
        data['tstamp'], data['summary'], ','.join(data['keywords']))
    db.commit()
    click.echo("Added news: \'{NEWS}\'".format(NEWS=data['title']))
    


def showArticle(article, show_text=False):
    data = getArticleData(article)
    msg = "=" * 50 + "\n"
    for key in sorted(data.keys()):
        if key == 'text':
            continue
        if type(data[key]) is list:
            msg += key + ": " + ', '.join(data[key]) + "\n"
        else:
            msg += key + ": " + str(data[key]) + "\n"
    msg += "=" * 50 + "\n"
    if show_text:
        msg += "Content: \n"
        msg += data['text']
    msg += "=" * 50 + "\n"
    return msg


def getNewsPaperData(src_url):
    src = newspaper.build(src_url)
    news_data = []
    warnings = []
    for art in src.articles:
        try:
            news_data.append(getArticleData(art))
        except:
            warnings.append("WARNING: Loading data fail!")
    return news_data


def showNews(src_url):
    news_data = getNewsPaperData(src_url)
    msg = "=" * 60 + "\n"
    for i, news in enumerate(news_data):
        msg += str(i) + ", " + news['title'] + '\n'
    msg += "=" * 60 + "\n"
    return msg


def addNewsPaper(news_data, db):
    for data in news_data:
        addArticle(data, db)