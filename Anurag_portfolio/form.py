from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Email, Length, Optional

class ContactForm(FlaskForm):
    full_name = StringField(
        "Full Name",
        validators=[DataRequired(), Length(2,50)]
    )

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    subject = StringField(
        "Subject",
        validators=[DataRequired(), Length(4,100)]
    )

    phone = StringField(
        "Phone (optional)",
        validators=[Optional(), Length(7,15)]
    )

    message = TextAreaField(
        "Message",
        validators=[DataRequired(), Length(min=10)]
    )

    submit = SubmitField("Send Message")
