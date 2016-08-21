#Gihub link:
#https://github.com/emeznar/caesar.git

import webapp2
import cgi
from caesar import encrypt

#create a web form with input for text and rotation amount
form = """
        <form method="POST">
        <h3> Enter text to encrypt: </h3>
            <textarea name="text">%(text)s</textarea>
        <h3> Rotate by: </h3>
            <input type="text" name="rotnumber" value="%(rotnumber)s"/>
            <input type="submit"/>
        </form>
        """
#TODO: add styling(CSS) to this form to be more like example on LC website

class Index(webapp2.RequestHandler):
#add text and rotnumber from html input above to webpage - variable substitution %s
    def write_form(self, text="",rotnumber=""):
        self.response.out.write(form % {"text":text,
                                        "rotnumber":rotnumber})
#get or draw the main page
    def get(self):
        self.write_form()

#draw coded information on a page
    def post(self):
        text = cgi.escape(self.request.get("text"), quote=True)
        #TODO: add something to replace the ; here
        text = text.replace("&lt", "<")
        text = text.replace("&gt", ">")
        text = text.replace("&amp", "&")
        text = text.replace(";", "")

        rotnumber = self.request.get("rotnumber")
        text = encrypt(text, int(rotnumber))

        self.write_form(text,rotnumber)

#route information to the ap/webpage
app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
