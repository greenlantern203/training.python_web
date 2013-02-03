#!/usr/bin/python
import datetime

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
Total Listing of Books:
<br>
-+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+-
<br>
%s
<br>
<br>
<br>
-+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+-
<br>
-+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+-
<br>
Details:
<br>
<br>
<br>
<br>
ID = id1
<br>
%s
<br>
-+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+-
<br>
<br>
ID = id2
<br>
%s
<br>
-+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+-
<br>
ID = id3
<br>
<br>
%s
<br>
-+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+-
<br>
ID = id4
<br>
<br>
%s
<br>
-+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+-
<br>
ID = id5
<br>
%s
-+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+-
<br>
-+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+-
<br>
End of listing. thanks for visiting!
<br>
-+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+-
<br>
</body>
</html>"""

def application(environ, start_response):
    a = BookDB()
    b = (a.titles())
    id1 = (a.title_info('id1'))
    id2 = (a.title_info('id2'))
    id3 = (a.title_info('id3'))
    id4 = (a.title_info('id4'))
    id5 = (a.title_info('id5'))
    response_body = body % (
	 b,
	 id1,
	 id2,
	 id3,
	 id4,
	 id5,
         )
    status = '200 OK'

    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8000, application)
    srv.serve_forever()
