from flask import Flask,render_template,request
app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def home():
    return render_template('layout.html')


@app.route("/login")
def login():
        return render_template('login.html')

@app.route("/getimage/<imagename>")
def showimage(imagename):
        return render_template('showimage.html',imagename=imagename)



if __name__ == '__main__':
  app.run(debug=True)



