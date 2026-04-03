from flask import Flask, request, render_template

app=Flask(__name__)

restraunt={}

@app.route('/')
def search():
  return render_template('search.html')

if __name__=='__main__':
  app.run(debug=True)