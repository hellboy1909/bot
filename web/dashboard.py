from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

@app.route("/")
def dashboard():
    conn = sqlite3.connect("trades.db")
    trades = conn.execute("SELECT * FROM trades ORDER BY timestamp DESC").fetchall()
    html = """
    <h2>گزارش خرید و فروش</h2>
    <table border=1>
    <tr><th>Symbol</th><th>Action</th><th>Price</th><th>Time</th></tr>
    {% for t in trades %}
      <tr><td>{{ t[1] }}</td><td>{{ t[2] }}</td><td>{{ t[3] }}</td><td>{{ t[4] }}</td></tr>
    {% endfor %}
    </table>
    """
    return render_template_string(html, trades=trades)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)