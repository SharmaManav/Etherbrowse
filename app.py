import config
from flask import Flask, render_template
from web3 import Web3

app = Flask(__name__)
w3 = Web3(Web3.HTTPProvider(config.INFURA_URL))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tx/<hash>")
def transaction(hash):
    transaction = w3.eth.get_transaction(hash)
    return render_template("transaction.html", hash=hash, transaction = transaction)

@app.route("/address/<addr>")
def address(addr):
    return render_template("address.html", addr=addr)

@app.route("/block/<block_number>")
def block(block_number):
    return render_template("block.html", block_number=block_number)