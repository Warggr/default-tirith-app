from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# DO NOT remove this route; it is used internally by the load balancer to check whether a target is healthy.
@app.route("/tirith-health-checks")
def health_check():
    return "Healthy!"

if __name__ == "__main__":
    app.run()
