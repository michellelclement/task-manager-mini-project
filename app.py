import os
from flask import Flask
if os.path.exists("env.py"):
    import env
# The above will only install if can find the env.py file. Remember this will not be pushed to Github

# Create an instance of flask in a variable app
app = flask(__name__)


# Check properly configured with a test function
@app.route("/")
def hello():
    return "Hello World.... again"


# how and where to test function 
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
