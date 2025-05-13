from flask import Flask, render_template
import os
import platform
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    """Renders a basic information page about the web app."""
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    os_info = platform.platform()
    python_version = platform.python_version()
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S %Z%z")

    return render_template(
        "index.html",
        hostname=hostname,
        ip_address=ip_address,
        os_info=os_info,
        python_version=python_version,
        current_time=current_time,
    )

if __name__ == "__main__":
    # Determine the port to run on. Azure App Service sets the PORT environment variable.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)