#!/usr/bin/env python3
"""HawkEye demo — DELIBERATELY VULNERABLE Python sample.

Do NOT deploy. Every function here is an anti-pattern HawkEye should flag.
"""
import os
import subprocess
import pickle
import hashlib
import sqlite3
import yaml
import requests
from flask import Flask, request

app = Flask(__name__)

# --- hardcoded secrets (CWE-798) ----------------------------------------------
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY12"
API_TOKEN = "s3cr3t-demo-token-do-not-use-in-prod"


@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    # OS command injection (CWE-78)
    os.system("ping -c 1 " + host)
    return subprocess.check_output("nslookup " + host, shell=True)


@app.route("/user")
def get_user():
    uid = request.args.get("id", "")
    con = sqlite3.connect("app.db")
    # SQL injection via f-string (CWE-89)
    return con.execute(f"SELECT * FROM users WHERE id = {uid}").fetchall()


def load_profile(blob):
    # Unsafe deserialization (CWE-502)
    return pickle.loads(blob)


def load_config(text):
    # Unsafe YAML load (CWE-502)
    return yaml.load(text)


def weak_hash(password):
    # Weak hash for passwords (CWE-327)
    return hashlib.md5(password.encode()).hexdigest()


def run_template(code):
    # Eval injection (CWE-95)
    return eval(code)


def fetch(url):
    # TLS verification disabled (CWE-295)
    return requests.get(url, verify=False)


if __name__ == "__main__":
    app.run(debug=True)
