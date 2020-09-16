from app_project.app import app, db
from app_project.posts.blueprint import posts_blue
import app_project.view


app.register_blueprint(posts_blue, url_prefix="/blog")

if __name__ == "__main__":
    app.run()