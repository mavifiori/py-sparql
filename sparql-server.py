import rdflib, os
from flask import Flask, render_template, request, escape

app = Flask(__name__)

def shorten_iri(iri, namespaces):
    r = str(iri)
    shortened=False
    for pref, uri in namespaces:
        if r.startswith(uri):
            r = str(escape(r.replace(uri,pref+':')))
            break    
    r = r[:30]
    return r

@app.route('/', methods=['GET','POST'])
def home():
    ans = []
    filenames = os.listdir('data')
    last = ''
    query_text = 'SELECT ?s ?p ?o\nWHERE {\n    ?s ?p ?o\n}\nLIMIT 100'
    vrbs = None
    
    if request.method == 'POST':
        g = rdflib.Graph()
        last = request.form['file']
        query_text = request.form['query']
        g.parse('data/'+last)
        for tupl in g.query(query_text):
            a = []
            for k in tupl.asdict():
                a += [shorten_iri(tupl[k],g.namespaces())]
            ans += [a]
        vrbs = tupl.asdict().keys()
    print(len(ans))
    return render_template('home.html', answers=ans, last=last,
        filenames=filenames, query_text=query_text, 
        variables=vrbs)


