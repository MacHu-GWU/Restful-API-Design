from eve import Eve
app = Eve()

if __name__ == '__main__':
    app.run("127.0.0.1", 5000, debug=True)