from flask import Flask, request, render_template

app=Flask(__name__)

gurl={}

options=[ 'yes', 'no']

@app.route('/')
def bday():
  return render_template('bday1.html')

@app.route('/bday1', methods=['POST'])
def bday1():
  name=request.form.get('bbg')
  if not name:
    return render_template('fail.html')
  age=request.form.get('year')
  gurl[name]=age
  return render_template('bday2.html', gurl=gurl, options=options)

@app.route('/bday2', methods=['POST'])
def bday2():
  answer=request.form.get('options')
  if answer in options:
    if answer=='yes':
      return render_template('birthday.html')
    else:
      return render_template('no.html')

@app.route('/bday3', methods=['POST'])
def bday3():
  return render_template('birthday.html')


if __name__=='__main__':
  app.run(debug=True)
