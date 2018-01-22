import psycopg2
DBNAME = "news"

'''
Method that gets popular articles of all time from news database
'''


def get_popular_articles():
    db = psycopg2.connect(database=DBNAME)
    file = open("test.txt", "w")
    cursor = db.cursor()
    cursor.execute('''
    select a.slug, count(l.ip)
    from log as l, articles as a
    where substring(l.path from 10) = a.slug
    group by a.slug
    order by count(l.ip) desc
    limit 3;
    ''')
    articles = cursor.fetchall()
    file.write("What are the most popular three articles of all time?\n")
    # Get three popular articles by address and number of views
    for article in articles:
        address = article[0]
        views = article[1]
        file.write('{} - {} views\n'.format(address, views))
    file.close()
    db.close()
    return articles

'''
Method that gets popular articles of all time from news database
'''


def get_popular_authors():
    db = psycopg2.connect(database=DBNAME)
    file = open("test.txt", "a")
    cursor = db.cursor()
    cursor.execute('''
    select au.name, count(l.ip)
    from log as l, articles as a, authors as au
    where a.author = au.id and substring(l.path from 10) = a.slug
    group by au.name
    order by count(l.ip) desc
    ''')
    authors = cursor.fetchall()
    file.write("What are the most popular authors of all time\n")
    for author in authors:
        name = author[0]
        views = author[1]
        file.write('{} - {} views\n'.format(name, views))
    file.close()
    db.close()
    return authors

'''
Medthod that shows errors of log in the news database
'''


def get_errors():
    db = psycopg2.connect(database=DBNAME)
    file = open("test.txt", "a")
    cursor = db.cursor()
    cursor.execute('''
    drop view if exists total_status;
    ''')
    cursor.execute('''
    drop view if exists errors;
    ''')
    cursor.execute('''
    create view total_status as
    select to_char(time,'FMMonth DD,YYYY') as t, count(status) as num
    from log
    group by t;
    ''')
    cursor.execute('''
    create view errors as
    select to_char(time,'FMMonth DD,YYYY') as t, count(status) as num
    from log
    where status != '200 OK'
    group by t;
    ''')
    file.write("On which days did more than 1% of requests lead to errors?\n")
    cursor.execute('''
    select total_status.t, round((errors.num::float * 100 / \
    total_status.num::float)::numeric,2)
    from total_status, errors
    where (errors.num::float * 100 / total_status.num::float) > 1;
    ''')
    errors = cursor.fetchall()
    for error in errors:
        status = error[0]
        percent = error[1]
        file.write('{} - {} views\n'.format(status, percent))
    file.close()
    db.close()
    return errors


get_popular_articles()
get_popular_authors()
get_errors()
