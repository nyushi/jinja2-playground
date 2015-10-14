from flask import Flask, redirect, request, send_from_directory
import jinja2
import yaml
import sys


app = Flask(__name__)


@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('static', path)


@app.route("/")
def root():
    return redirect("./static/index.html")


@app.route("/api/render", methods=['POST'])
def render():
    try:
        raw_vars = request.json['vars']
        vars = yaml.load(raw_vars)
        if not isinstance(vars, dict):
            vars = {}
        tmpl = request.json['tmpl']
        return jinja2.Template(tmpl).render(**vars)
    except Exception as e:
        err = "template error"
        if isinstance(e, yaml.YAMLError):
            err = "yaml error"
        return "{}: {}".format(err, str(e))


if __name__ == "__main__":
    kwargs = {}
    if len(sys.argv) > 1:
        kwargs['host'] = sys.argv[1]
    app.run(**kwargs)
