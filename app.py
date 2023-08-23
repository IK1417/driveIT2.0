from flask import Flask, request
import json

app = Flask(__name__)

# дата, время, станция, погода (в цельсиях)

@app.route(methods=["GET"])
def model_request_handler():
    model_params = json.loads(request.data)
    
