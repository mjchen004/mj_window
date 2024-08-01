from flask import Blueprint,render_template,request,session,redirect
from flask_wtf import FlaskForm
from wtforms import EmailField,PasswordField,StringField,SelectField,BooleanField,DateField,TextAreaField
from wtforms.validators import DataRequired,Length,Regexp,Optional,EqualTo
from .datasource import validateUser,insert_data,InvalidEmailException,append
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

auth_blueprint = Blueprint('auth',__name__)

class UserRegistrationFrom(FlaskForm):
    uName = StringField('姓名',validators=[DataRequired(),Length(min=2, max=10)])
    uGender = SelectField('性別',choices=[("男","男"),("女","女")])
    uPhone = StringField('行動電話',validators=[DataRequired(),Regexp(r'\d\d\d\d-\d\d\d-\d\d\d',message="格式不正確")])
    uEmail = EmailField("電子郵件",validators=[DataRequired()])
    isGetEmail = BooleanField("接受促銷email",default=False)
    uBirthday = DateField("出生年月日",validators=[Optional()],format='%Y-%m-%d')
    uAboutMe = TextAreaField('自我介紹',validators=[Optional(),Length(max=200)],description='最多200字')
    uPass = PasswordField("密碼",validators=[DataRequired(),Length(min=4,max=20),EqualTo('uConfirmPass',message='驗証密碼不正確')])
    uConfirmPass = PasswordField("驗証密碼", validators=[DataRequired(),Length(min=4,max=20)])

@auth_blueprint.route('/auth/register',methods=['GET','POST'])
def register():
    form = UserRegistrationFrom()
    if request.method == "POST":
        if form.validate_on_submit():
            uName = request.form['uName']
            print('姓名=',uName)

            uGender = form.uGender.data
            print('性别=',uGender)

            uPhone = form.uPhone.data
            print('电话=',uPhone)

            uEmail = form.uPhone.data
            print('email=',uEmail)

            isGetEmail = form.uPhone.data
            print('促销=','接受'if isGetEmail else '不接受')

            uBirthday: datetime.date | None = form.uBirthday.data
            if uBirthday is not None: 
                uBirthday_str = uBirthday.strftime("%Y-%m-%d")
                print('出生年月日:',uBirthday_str)
            else: 
                uBirthday_str = '2000-01-01' #default birthday

            uAboutMe = form.uAboutMe.data
            print('关于我',uAboutMe)

            uPass = form.uPass.data 
            print('密码',uPass)

            #create password hash 
            hash_password = generate_password_hash(uPass,method='pbkdf2:sha256',salt_length=8)
            print('暗码',hash_password)
            
            conn_token = secrets.token_hex(16)
            print('乱数密码',conn_token)

            try:
                insert_data([uName,uGender,uPhone,uEmail,isGetEmail,uBirthday_str,uAboutMe,hash_password,conn_token])
            except InvalidEmailException: 
                form.uEmail.errors.append("相同的email")
            except:
                form.uEmail.errors.append('不知名的错误')
            else: 
                return redirect(f'/auth/login/{uEmail}')


    else:
        print("第一進入")

    return render_template('/auth/register.html.jinja',form=form)

class LoginForm(FlaskForm):
    email = EmailField('郵件信箱',validators=[DataRequired()])
    password = PasswordField('密碼',validators=[DataRequired(),Length(min=4, max=20)])


@auth_blueprint.route("/auth/",methods=['GET', 'POST'])
@auth_blueprint.route("/auth/login",methods=['GET', 'POST'])
@auth_blueprint.route("/auth/login/<email>")

def index(email:str | None = None):
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            print("表單傳送過來")
            print("驗証了token")
            email = form.email.data
            password = form.password.data
            print(f'email:{email}')
            print(f'password:{password}')
            is_ok, username = validateUser(email,password)
            if is_ok:
                session['username'] = username
                return redirect('/')
            else:
                form.email.errors.append("帳號或密碼錯誤")
                form.email.data = ""

    else:
        print("這是第一次進入")
        #if email is not None:
        #    form.email.data = email
    
    return render_template('/auth/login.html.jinja',form=form)

@auth_blueprint.route("/auth/logout")
def logout():
    session.pop('username')
    return redirect('/')