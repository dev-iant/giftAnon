from flask import Flask
app = Flask(__name__)
app.secret_key = "I have 99 problems we're working on them." 

# The secret key is needed to run session
# This is one thing that would usually be kept in your git ignore, along with API keys