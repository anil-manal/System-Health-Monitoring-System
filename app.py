from flask import Flask, render_template
import psutil

app = Flask(__name__)

# Function to get system health
def get_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    return cpu_usage, memory_usage, disk_usage

# Function to get running processes
def get_running_processes():
    processes = []
    for proc in psutil.process_iter(['name', 'memory_info', 'cpu_percent']):
        process_info = proc.info
        processes.append({
            'name': process_info['name'],
            'memory': process_info['memory_info'].rss,
            'cpu_percent': process_info['cpu_percent']
        })
    return processes

@app.route('/')
def index():
    # Check system health and running processes
    cpu_usage, memory_usage, disk_usage = get_system_health()
    processes = get_running_processes()

    # Alerting logic
    alerts = []
    if cpu_usage > 80:
        alerts.append(f"Alert: CPU usage is {cpu_usage}% which exceeds the threshold of 80%")
    if memory_usage > 80:
        alerts.append(f"Alert: Memory usage is {memory_usage}% which exceeds the threshold of 80%")
    if disk_usage > 80:
        alerts.append(f"Alert: Disk usage is {disk_usage}% which exceeds the threshold of 80%")
    for process in processes:
        if process['cpu_percent'] > 80:
            alerts.append(f"Alert: CPU usage of process {process['name']} is {process['cpu_percent']}%")

    return render_template('index.html', alerts=alerts)

@app.route('/check_health')
def check_health():
    cpu_usage, memory_usage, disk_usage = get_system_health()
    
    # Alerting logic
    alerts = []
    if cpu_usage > 80:
        alerts.append(f"Alert: CPU usage is {cpu_usage}% which exceeds the threshold of 80%")
    if memory_usage > 80:
        alerts.append(f"Alert: Memory usage is {memory_usage}% which exceeds the threshold of 80%")
    if disk_usage > 80:
        alerts.append(f"Alert: Disk usage is {disk_usage}% which exceeds the threshold of 80%")

    return render_template('system_health.html', cpu_usage=cpu_usage, memory_usage=memory_usage, disk_usage=disk_usage, alerts=alerts)

@app.route('/running_processes')
def running_processes():
    processes = get_running_processes()
    return render_template('running_processes.html', processes=processes)

if __name__ == '__main__':
    app.run(debug=True)
