import web
import cgi
import SimpleHTTPServer
import SocketServer
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

class Index(object):
    def GET(self):
        return "hi!"

    def POST(self):
        print "dank memes"
        db.urls.insert_one(form)
        #form = web.input(name="Nobody", greet="Hello")
        #greeting = "%s, %s" % (form.greet, form.name)
        #return render.index(greeting = greeting)

#if __name__ == "__main__":
  #  app.run()