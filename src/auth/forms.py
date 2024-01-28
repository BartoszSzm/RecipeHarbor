import flask_wtf #type: ignore
import wtforms #type: ignore


class LoginForm(flask_wtf.FlaskForm):
    email = wtforms.StringField(
        'Email', 
        validators=[
            wtforms.validators.DataRequired(),
            wtforms.validators.Length(1, 64),
            wtforms.validators.Email()
            ])
    password = wtforms.PasswordField(
        'Password', 
        validators=[wtforms.validators.DataRequired()])
    remember_me = wtforms.BooleanField("Rememeber me")
    submit = wtforms.SubmitField('Sign in')