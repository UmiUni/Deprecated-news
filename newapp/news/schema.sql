DROP TABLE IF EXISTS articles;

CREATE TABLE articles(
    /* Problem Number */
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    authors TEXT NOT NULL,
    publish_date TEXT NOT NULL,
    tstamp TEXT NOT NULL,
    summary TEXT NOT NULL,
    keywords TEXT NOT NULL
);