from flask import Flask, request, render_template

app=Flask(__name__)

swifties={}
ERAS=[
  "Reputation Era",
  "Lover Era",
  "1989 Era",
  "Fearless Era",
  "Midnight Era",
  "Tortured Poet Era",
  "Folklore Era",
  "Evermore Era",
  "Speak Now Era",
  "Life of a Show Girl"
]

@app.route('/')
def taylor():
  return render_template('tay.html', eras=ERAS)

@app.route('/swifty', methods=['POST'])
def eras():
  name=request.form.get('name')
  if not name:
    return render_template('fail.html')
  era=request.form.get('era')
  swifties[name]= era
  if era not in ERAS:
    return render_template('fail.html')
  return render_template('swifty.html')

@app.route('/taylor')
def swifty():
  return render_template('swift.html', swifties=swifties)

if __name__=='__main__':
  app.run(debug=True)
