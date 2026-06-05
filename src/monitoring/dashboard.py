#!/usr/bin/env python3
"""
Real-time Dashboard (Flask)
"""

from flask import Flask, render_template_string
import logging

app = Flask(__name__)

@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Trading Bot Dashboard</title>
        <style>
            body { font-family: Arial; margin: 20px; background: #1e1e1e; color: #fff; }
            .card { background: #2d2d2d; padding: 20px; margin: 10px 0; border-radius: 8px; }
            h1 { color: #00ff00; }
            .metric { display: inline-block; margin: 10px 20px; }
            .positive { color: #00ff00; }
            .negative { color: #ff0000; }
        </style>
    </head>
    <body>
        <h1>🤖 AI Scalping Trading Bot - Live Dashboard</h1>
        <div class="card">
            <h2>Status: <span class="positive">Ready</span></h2>
            <p>Mode: <strong>DEMO</strong></p>
            <p>Timeframe: <strong>5 minutes</strong></p>
        </div>
        <div class="card">
            <h2>Account Metrics</h2>
            <div class="metric">Balance: <strong>$100.00</strong></div>
            <div class="metric">Equity: <strong>$100.00</strong></div>
            <div class="metric">Free Margin: <strong>$100.00</strong></div>
        </div>
        <div class="card">
            <h2>Trading Metrics</h2>
            <div class="metric">Total Trades: <strong>0</strong></div>
            <div class="metric">Win Rate: <strong>0%</strong></div>
            <div class="metric">Daily P&L: <strong class="positive">$0.00</strong></div>
        </div>
        <p style="margin-top: 40px; text-align: center; color: #888;">
            Updated: <span id="time"></span>
        </p>
        <script>
            setInterval(() => {
                document.getElementById('time').innerText = new Date().toLocaleTimeString();
            }, 1000);
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    print("🚀 Dashboard starting at http://localhost:5000")
    app.run(debug=True, port=5000)
