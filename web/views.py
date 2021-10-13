from flask import render_template, request, redirect

from web import app, db
from web.models import Clubs
from web.form import PostForm


@app.route("/", methods=["GET"])
def index():
    # 取得件数
    num = 5
    recent_data = db.session.query(Clubs).order_by(Clubs.id.desc()).limit(num).all()
    return render_template("index.tmpl", recent_data=recent_data)


@app.route("/list", methods=["GET"])
def club_list():
    club_data = db.session.query(Clubs).order_by(Clubs.id).all()
    return render_template("list.tmpl", club_data=club_data)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = PostForm()
    if request.method == "GET":
        return render_template("register.tmpl", form=form)

    if request.method == "POST":
        if form.validate_on_submit():
            prefix = form.prefix.data
            club_name = form.club_name.data
            suffix = form.suffix.data
            first_tweet = form.first_tweet.data

            new_club_name = f"{prefix}{club_name}{suffix}"

            new_club = Clubs(name=new_club_name, first_tweet=first_tweet)
            db.session.add(new_club)
            db.session.commit()

            return redirect("/")

        return render_template("register.tmpl", form=form)
