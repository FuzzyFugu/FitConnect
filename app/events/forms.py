"""Event creation/editing form."""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateTimeLocalField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

CATEGORIES = [
    ("Running", "Running"),
    ("Yoga", "Yoga"),
    ("Hiking", "Hiking"),
    ("Cycling", "Cycling"),
    ("Strength", "Strength"),
    ("Other", "Other"),
]


class EventForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=140)])
    description = TextAreaField("Description", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired(), Length(max=140)])
    category = SelectField("Category", choices=CATEGORIES, validators=[DataRequired()])
    starts_at = DateTimeLocalField(
        "Date & time", format="%Y-%m-%dT%H:%M", validators=[DataRequired()]
    )
    capacity = IntegerField("Capacity", validators=[NumberRange(min=1, max=500)], default=20)
    submit = SubmitField("Save event")
