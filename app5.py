from flask import Flask, request, render_template

app=Flask(__name__)

@app.route('/')
def booth():
  return render_template('booth.html')

@app.route('/booth')
def booth1():
  return render_template('booth1.html', method=['POST'])

if __name__=='__main__':
  app.run(debug=True)