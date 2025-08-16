from flask import Flask, render_template, Response
import time
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/debug")
def debug():
    return os.getcwd()


@app.route("/sse")
def sse_stream():
    def generate_events():
        # This is where you would get real-time data from your application
        while True:
            # Example: send the current time every second
            data = f"data: The current time is {time.strftime('%H:%M:%S')}\n\n"
            yield data
            time.sleep(1)

    return Response(generate_events(), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
