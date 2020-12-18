import MyPlexer
app=MyPlexer()
@app.route('/')
def hello_world():
    input("Input the command to be executed")
    print('Hello, World!')

@app.route('/')
def bye():
    print('bye')

app.run()
