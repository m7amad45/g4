from flask import Flask, render_template ,request
from postdata import posts
from flask_mail import Mail,Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

app.config['MAIL_USERNAME'] = 'g4project.se421@gmail.com'
app.config['MAIL_PASSWORD'] = 'g4project.se421@2020'

mail = Mail(app)




@app.route("/")
def homePage():
   return render_template('Homepage.html')


@app.route("/about")
def about():
    return render_template('About.html')


@app.route("/contact-Us" , methods = ['GET','POST'])
def contactUs():
    if request.method == 'POST' : 
        msg = Message("Hey" , sender='noreply@demo.com', recipients=['g4project.se421@gmail.com'])
        msg.body = " hey how are you"
        mail.send(msg)
        return "sent email"
    return render_template('Contact-Us.html')

@app.route("/mobile")
def mobile():
    return render_template('mobile.html')

@app.route("/reqres-data")
def reqresData():
    return render_template('reqres-data.html')

@app.route("/posts")
def home():
    return render_template('post-all.html',
                           title='all posts',
                           posts=posts)

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    if post_id < len(posts):
       p = posts[post_id]
       return render_template('post-single.html',
       title= f"Post#{post_id}", p = p )
    else:
        return render_template('404.html'), 404
    


#debug tool
if __name__ == '__main__':
	app.run( debug=True )