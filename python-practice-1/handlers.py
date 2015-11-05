class Handler:
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix+name, None)
        if callable(method): return method(*args)

    def start(self, name):
        self.callback('start_', name)
    
    def end(self, name):
        self.callback('end_',name)
    
    def sub(self, name):
        def substitution(match):
            return self.callback('sub_'.name, match)
        return substitution

    def start_document(self):
        print ('<html><head><title>...</title></head><body>')
    def end_document(self):
        print ('</body></html>')

    def start_paragraph(self):
        print ('<p>')
    def end_paragraph(self):
        print ('</p>')

    def start_title(self):
        print ('<h1>')
    def end_title(self):
        print ('</h1>')

    def start_heading(self):
        print ('<h2>')
    def end_heading(self):
        print ('</h2>')

    def start_list(self):
        print ('<ul>')
    def end_list(self):
        print ('</ul>')

    def start_listitem(self):
        print ('<li>')
    def end_listitem(self):
        print ('</li>')

    def sub_emhasis(self, match):
        return '<em>%s</em>' % match.group(1)
    def sub_url(self, match):
        return '<a href="%s">%s</a>' % (match.group(1), match.group(1))
    def sub_mail(self, match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))
    def sub_feed(self, data):
        return data
