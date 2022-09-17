
from flask import Flask, render_template, redirect, url_for, send_from_directory
from flask import request

app = Flask(__name__)


@app.before_request
def before_request():
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)


if __name__ == '__ssl_enforcer__':
    app.run(host="0.0.0.0", port=80)