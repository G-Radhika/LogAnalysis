#!/usr/bin/env python
import psycopg2


def three_most_popular_articles():
        connection = psycopg2.connect(database="news")
        cursor = connection.cursor()
#        cursor.execute("""SELECT path,COUNT(path) AS Count
#                           FROM log WHERE status = '200 OK' AND path != '/'
#                           GROUP BY path ORDER BY Count DESC LIMIT 3;""")
        cursor.execute("""SELECT title, COUNT(path) AS Count
                                FROM log JOIN articles ON
                                log.path = '/article/' || articles.slug
                                WHERE status = '200 OK' AND path != '/'
                                GROUP BY title
                                ORDER BY Count DESC
                                LIMIT 3;""")
        result = cursor.fetchall()
        print("################################################")
        print("Most popular three articles of all time: ")
        for title, count in result:
            print("    {}  --  {} views".format(title, count))
        print("################################################")
        cursor.close()
        connection.close()


def most_popular_article_authors():
        connection = psycopg2.connect(database="news")
        cursor = connection.cursor()
        cursor.execute("""SELECT authors.name AS AuthorName,COUNT(log.path)AS ViewCount
                              FROM log
                              JOIN articles
                              ON log.path = '/article/' || articles.slug
                              JOIN authors
                              ON (authors.id = articles.author)
                              WHERE log.status = '200 OK' AND log.path != '/'
                              GROUP BY AuthorName
                              ORDER BY ViewCount DESC;""")
        result = cursor.fetchall()
        print("################################################")
        print("Most popular article authors of all time: ")
        for AuthorName, ViewCount in result:
            print("    {}  --  {} views".format(AuthorName, ViewCount))
        print("################################################")
        cursor.close()
        connection.close()


def days_with_more_errors():
        connection = psycopg2.connect(database="news")
        cursor = connection.cursor()
# VIEW totals => total number of all page views
#   (both "200 OK" and "404 NOT FOUND")
#   for EACH day. GROUP BY year/month/day
        cursor.execute("""CREATE VIEW totals
                              AS SELECT COUNT(status) AS StatusCount,
                              date(time)
                              FROM log
                              GROUP BY date;""")
# VIEW errors => count only the erroneous page status="404 NOT FOUND"
# AND GROUP BY day
        cursor.execute("""CREATE VIEW errors
                              AS SELECT COUNT(status) AS ErrorCount,
                              date(time) AS date
                              FROM log
                              WHERE status = '404 NOT FOUND'
                              GROUP BY date;""")
        cursor.execute("""SELECT totals.StatusCount,errors.ErrorCount,
                             round(((errors.ErrorCount* 100)::numeric
                             /totals.StatusCount),2) AS ErrPercent,
                             totals.date
                             FROM totals
                             JOIN errors
                             ON totals.date = errors.date;""")
        result = cursor.fetchall()
        for StatusCount, ErrorCount, ErrPercent, date in result:
                if ErrPercent > 1.00:
                        print("""Which days did more than 1%
                        of requests lead to errors?""")
                        print("ErrPercent ---- date")
                        print ErrPercent, "------", date
        cursor.close()
        connection.close()


three_most_popular_articles()
most_popular_article_authors()
days_with_more_errors()
