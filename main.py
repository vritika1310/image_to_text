import tornado.web
import tornado.ioloop
from app import extract_num
import os
import shutil


class uploadImgHandler(tornado.web.RequestHandler):
    def post(self):
        files = self.request.files["fileImage"]
        shutil.rmtree('img')
        os.mkdir('img')
        for f in files:
            fh = open(f"img/{f.filename}", "wb")
            fh.write(f.body)
            fh.close()
        basepath = 'img/'
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                print(entry)
                text = extract_num("img/"+entry)
        if len(text) > 0:
            self.write(text)
        else:
            self.write('We are not able to detect from this image, kindly upload a clear picture!!')
    def get(self):
        self.render("index.html")

if (__name__ == "__main__"):
    app = tornado.web.Application([
        ("/", uploadImgHandler),
        ("/img/(.*)", tornado.web.StaticFileHandler, {'path': 'upload'})
    ])

    app.listen(8080)
    print("Listening on port 8080")
    tornado.ioloop.IOLoop.instance().start()