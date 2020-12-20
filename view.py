from flask import request,Response,Flask,render_template,session,redirect
from decorator import login_required
from auth import login,logout,authenticate
from query_manager import QuerySet

app = Flask(__name__)
app.secret_key = 'flaskISAwesome'



## user homepage
@app.route('/')
@login_required
def home(*arg):
    pass



## login user by email_Id and passwd
@app.route('/login',methods=['GET','POST'])
def user_login():
    if request.method == 'POST':
        user_email_Id = request.form.get('user_email_Id')
        user_passwd = request.form.get('user_passwd')
        is_authenticated = authenticate(user_email_Id,user_passwd)
        if is_authenticated:
            userId = QuerySet.get('my_mail',mail_id=user_mail_Id)
            login(userId)
            return redirect('/')
    
    return render_template('templates/login.html')


## logout user
@app.route('/logout')
def user_logout():
    logout()
    return redirect('/login')


## create new user
@app.route('/sign_up',methods=['GET','POST'])
def new_user_registration():
    if request.method == "POST":
        pass


## show user profile
@app.route('/user_profile/<name>')
@login_required
def user_profile(arg):
    pass





if __name__ == '__main__':
    app.run(debug=True)