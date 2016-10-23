import web
import cgi
from pymongo import MongoClient

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

client = MongoClient()
db = client.urls
urls = db.urls
post = {"url" : "http://www.google.com"}
post_id = db.urls.insert_one(post)
print post_id, "???"
print "hello?"

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        print "dank memes"
        db.urls.insert_one(form)
        #form = web.input(name="Nobody", greet="Hello")
        #greeting = "%s, %s" % (form.greet, form.name)
        #return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()