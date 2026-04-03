from flask import Flask, request, render_template

app=Flask(__name__)

dishes={}
DISHES=['Alfredo', 'Pasta', 'Eggplant Cheesestake', 'Egg']

@app.route('/')
def dish():
  return render_template('dish.html', dishes=DISHES)


@app.route('/cookbook', methods=['POST'])
def cookbook():
  name=request.form.get('dishName')
  name1=request.form.get('chefName')
  if not name:
    return render_template('cookfail.html')
  if name not in DISHES:
    return render_template('cookfail.html')
  if name==DISHES[0]:
    return render_template('cookbook1.html', chefName=name1)
  if name==DISHES[1]:
    return render_template('cookbook2.html',chefName=name1)
  if name==DISHES[2]:
    return render_template('cookbook3.html', chefName=name1)
  if name==DISHES[3]:
    return render_template('cookbook4.html', chefName=name1)

@app.route('/cook1', methods=['POST'])
def cook1():
  return render_template('cook1.html')

@app.route('/cook2', methods=['POST'])
def cook2():
  return render_template('cook2.html')

@app.route('/cook3', methods=['POST'])
def cook3():
  return render_template('cook3.html')

@app.route('/cook4', methods=['POST'])
def cook4():
  return render_template('cook4.html')
@app.route('/done', methods=['POST'])
def done():
  return render_template('done.html')

with app.app_context():
    db.create_all()

if __name__=='__main__':
  app.run(debug=True)