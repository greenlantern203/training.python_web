#!/usr/bin/python
import datetime
import re
class BookDB():
    def titles(self):
        titles = [dict(id=id, title=database[id]['title']) for id in database.keys()]
        return titles
    def title_info(self, id):
        return database[id]

# let's pretend we're getting this information from a database somewhere
database = {
    'id1' : {'title' : 'CherryPy Essentials: Rapid Python Web Application Development',
             'isbn' : '978-1904811848',
             'publisher' : 'Packt Publishing (March 31, 2007)',
             'author' : 'Sylvain Hellegouarch',
           },
    'id2' : {'title' : 'Python for Software Design: How to Think Like a Computer Scientist',
             'isbn' : '978-0521725965',
             'publisher' : 'Cambridge University Press; 1 edition (March 16, 2009)',
             'author' : 'Allen B. Downey',
           },
    'id3' : {'title' : 'Foundations of Python Network Programming',
             'isbn' : '978-1430230038',
             'publisher' : 'Apress; 2 edition (December 21, 2010)',
             'author' : 'John Goerzen',
           },
    'id4' : {'title' : 'Python Cookbook, Second Edition',
             'isbn' : '978-0-596-00797-3',
             'publisher' : 'O''Reilly Media',
             'author' : 'Alex Martelli, Anna Ravenscroft, David Ascher',
           },
    'id5' : {'title' : 'The Pragmatic Programmer: From Journeyman to Master',
             'isbn' : '978-0201616224',
             'publisher' : 'Addison-Wesley Professional (October 30, 1999)',
             'author' : 'Andrew Hunt, David Thomas',
           },
}


body = """<html>
<head>
<title>Lab 3 - WSGI experiments</title>
</head>
<body>
<br>
Student: Dan Ramos
<br>
Homework: 04
<br>
-+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+-
<br>
Index Listing of Books:
<br>
-+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+-
<br>
<br>
<a href=http://127.0.0.1:8001/id1>id1 - Rapid Python Web Application Development</a>
<br>
<a href=http://127.0.0.1:8001/id2>id2 - How to Think Like a Computer Scientist</a>
<br>
<a href=http://127.0.0.1:8001/id3>id3 - Foundations of Python Network Programming</a>
<br>
<a href=http://127.0.0.1:8001/id4>id4 - Python Cookbook, Second Edition</a>
<br>
<a href=http://127.0.0.1:8001/id5>id5 - From Journeyman to Master</a>
<br>
-+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+-
<br>
End of listing. thanks for visiting!
<br>
<br>
</body>
</html>"""

body1 = """<html>
<head>
<title>Lab 3 - WSGI experiments</title>
</head>
<body>
<br>
%s
<br>
</body>
</html>"""

body2 = """<html>
<head>
<title>Lab 3 - WSGI experiments</title>
</head>
<body>
<br>
%s
<br>
</body>
</html>"""

body3 = """<html>
<head>
<title>Lab 3 - WSGI experiments</title>
</head>
<body>
<br>
%s
<br>
</body>
</html>"""

body4 = """<html>
<head>
<title>Lab 3 - WSGI experiments</title>
</head>
<body>
<br>
%s
<br>
</body>
</html>"""

body5 = """<html>
<head>
<title>Lab 3 - WSGI experiments</title>
</head>
<body>
<br>
%s
<br>
</body>
</html>"""

def index(environ, start_response):

    a = BookDB()
    b = (a.titles())
    response_body = body % (
         b
         )
    status = '200 OK'

    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]

def id1(environ, start_response):

    a = BookDB()
    b = (a.title_info('id1'))
    response_body = body1 % (
         b
         )
    status = '200 OK'

    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]

def id2(environ, start_response):

    a = BookDB()
    b = (a.title_info('id2'))
    response_body = body2 % (
         b
         )
    status = '200 OK'

    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]

def id3(environ, start_response):

    a = BookDB()
    b = (a.title_info('id3'))
    response_body = body3 % (
         b
         )
    status = '200 OK'

    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]

def id4(environ, start_response):

    a = BookDB()
    b = (a.title_info('id4'))
    response_body = body4 % (
         b
         )
    status = '200 OK'

    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]

def id5(environ, start_response):

    a = BookDB()
    b = (a.title_info('id5'))
    response_body = body5 % (
         b
         )
    status = '200 OK'

    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]


def not_found(environ, start_response):
    """Called if no URL matches."""
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['Not Found']

# map urls to functions
urls = [
    (r'^$', index),
    (r'id1/?$', id1),
    (r'id1/(.+)$', id1),
    (r'id2/?$', id2),
    (r'id2/(.+)$', id2),
    (r'id3/?$', id3),
    (r'id3/(.+)$', id3),
    (r'id4/?$', id4),
    (r'id4/(.+)$', id4),
    (r'id5/?$', id5),
    (r'id5/(.+)$', id5)
]

def application(environ, start_response):
    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in urls:
        match = re.search(regex, path)
        if match is not None:
            environ['myapp.url_args'] = match.groups()
            return callback(environ, start_response)
    return not_found(environ, start_response)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8001, application)
    srv.serve_forever()
