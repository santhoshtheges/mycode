import MyPlexer
app=MyPlexer()
@app.route('/')
def hello_world():
    input("Input the command to be executed")
    return 'Hello, World!'

@app.route('/')
def bye():
    return 'bye'

app.run()
