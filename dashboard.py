#!/usr/bin/env python3
"""
Network Monitoring Dashboard
Real-time network monitoring with custom dashboards
"""

from flask import Flask, render_template, jsonify
import psutil
import socket
import time
from datetime import datetime
import json

app = Flask(__name__)

def get_network_stats():
    """Get network statistics"""
    stats = psutil.net_io_counters(pernic=True)
    return {
        interface: {
            'bytes_sent': stats[interface].bytes_sent,
            'bytes_recv': stats[interface].bytes_recv,
            'packets_sent': stats[interface].packets_sent,
            'packets_recv': stats[interface].packets_recv,
            'errin': stats[interface].errin,
            'errout': stats[interface].errout,
            'dropin': stats[interface].dropin,
            'dropout': stats[interface].dropout
        }
        for interface in stats.keys()
    }

def check_port(host, port, timeout=1):
    """Check if port is open"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return False

def get_system_info():
    """Get system information"""
    return {
        'cpu_percent': psutil.cpu_percent(interval=1),
        'memory_percent': psutil.virtual_memory().percent,
        'disk_percent': psutil.disk_usage('/').percent,
        'uptime': time.time() - psutil.boot_time()
    }

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('dashboard.html')

@app.route('/api/network')
def api_network():
    """API endpoint for network statistics"""
    return jsonify(get_network_stats())

@app.route('/api/system')
def api_system():
    """API endpoint for system information"""
    return jsonify(get_system_info())

@app.route('/api/health')
def api_health():
    """Health check endpoint"""
    hosts = [
        {'name': 'Google DNS', 'host': '8.8.8.8', 'port': 53},
        {'name': 'Cloudflare DNS', 'host': '1.1.1.1', 'port': 53},
    ]
    
    health_status = []
    for host in hosts:
        status = check_port(host['host'], host['port'])
        health_status.append({
            'name': host['name'],
            'host': host['host'],
            'port': host['port'],
            'status': 'up' if status else 'down',
            'timestamp': datetime.now().isoformat()
        })
    
    return jsonify(health_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

