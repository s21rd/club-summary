from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, ValidationError
from wtforms.validators import DataRequired, Length
import re


class PostForm(FlaskForm):
    prefix = RadioField(
        "接頭辞",
        validators=[DataRequired()],
        choices=["TDU", "電大", "東京電機大学"],
        default="TDU",
    )
    club_name = StringField(
        "名称",
        validators=[DataRequired(), Length(min=1)],
        description="お嬢様",
    )
    suffix = RadioField("接尾辞", choices=["サークル", "部"], default="サークル")
    first_tweet = StringField(
        "初出ツイートリンク",
        validators=[DataRequired()],
        description="https://twitter.com/**********/**********",
    )

    def validate_first_tweet(self, first_tweet: str):
        target = R"(?:https?://)?(?:mobile.)?(?:www.)?(?:twitter.com/)?(?:\#!/)?(?:\w+)/status(?:es)?/(\d+)"
        if re.match(target, first_tweet.data) is None:
            raise ValidationError("リンクが不正です")
