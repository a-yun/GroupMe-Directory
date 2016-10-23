import web
import cgi
import SimpleHTTPServer 
import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from pymongo import MongoClient

urls = (
  '/hello', 'Index'
)

#app = web.application(urls, globals())

PORT = 80

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

client = MongoClient()
db = client.urls
urls = db.urls
post = {"url" : "http://www.google.com"}
post_id = db.urls.insert_one(post)
print post_id, "???"
print "hello?"

httpd.serve_forever()

#render = web.template.render('templates/')

class S(BaseHTTPRequestHandler):
    def GET(self):
        return "hi!"

    def POST(self):
        print "dank memes"
        #db.urls.insert_one(form)
        return "hi.."
        #form = web.input(name="Nobody", greet="Hello")
        #greeting = "%s, %s" % (form.greet, form.name)
        #return render.index(greeting = greeting)

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()