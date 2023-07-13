from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    blog_url = f"https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year, posts=all_posts)


@app.route("/post/<blog_id>")
def blog_post(blog_id):
    blog_url = f"https://api.npoint.io/c790b4d5cab58020d391"  # API endpoint for your blog posts
    response = requests.get(blog_url)
    all_posts = response.json()

    # Find the specific blog post using blog_id
    blog_post = None
    for post in all_posts:
        if post["id"] == int(blog_id):
            blog_post = post
            break

    return render_template("post.html", post=blog_post)



if __name__ == "__main__":
    app.run(debug=True)
