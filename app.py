from flask import Flask, request, jsonify, Blueprint
from views import app

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
