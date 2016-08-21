#escape.py

def escape_html(escaped_text):
    return cgi.escape(escaped_text, quote = True)
