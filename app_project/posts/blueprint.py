from flask import Blueprint, render_template

from app_project.models import Post

posts_blue = Blueprint("posts", __name__, template_folder="templates")


@posts_blue.route("/")
def index():
    posts = Post.query.all()

    return render_template("posts/index.html", posts=posts)


@posts_blue.route("/<slug>")
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()

    return render_template("posts/post_detail.html", post=post)
