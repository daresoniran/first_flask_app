### import in parts

from flask import Flask, render_template

## 'flask' - name of the module (or library?)
##' Flask' - is class, template for a mo???

app = Flask('website_name')


## decoration


@app.route('/')
def say_hello():
    return render_template('hello_page.html', username='World', title='everyone')
##keyword arguements >> similar to turtle forward, border, etc.

@app.route('/<name>')
def say_hello_to(name):
    # return 'Hello {}!'.format(name)
    return render_template('hello_page.html', username=name, title='madame')


@app.route('/<name>/friends')
def remember_to_call(name):
    # return 'Hello {}!'.format(name)
    return 'Hello {}, remember to call your friends this week!'.format(name)


@app.route('/news')
def give_news():
    return 'Great news my site is working'

### route everything after every slash. for example 'news' for bbc.co.uk\news

app.run(debug=True)

##url
##8080 - google
###127 - localhost - website browser for your desktop (in a way)
## localhost:5000 - same link

## GET - public response
## appose - sending sensitive data (i.e. login details)

