from pyngrok import ngrok, conf
import subprocess, time, os

# <<< REPLACE with your ngrok authtoken from dashboard >>>
NGROK_AUTHTOKEN = "345lFlh1JMCC4q10fJ0i9DiEDiE_232frs4LG9fAwofiQ1sCE"

if NGROK_AUTHTOKEN.startswith("<"):
    raise SystemExit("Please replace <YOUR_NGROK_AUTHTOKEN_HERE> with your ngrok authtoken (from dashboard.ngrok.com).")

# configure and set auth token
conf.get_default().auth_token = NGROK_AUTHTOKEN

# kill prior streamlit (if any)
try:
    subprocess.run(["pkill", "-f", "streamlit"])
except Exception as e:
    print("No prior streamlit process found.")

# start streamlit app in background and capture log
logfile = "/content/streamlit_log.txt"
with open(logfile, "w") as f:
    proc = subprocess.Popen(["streamlit", "run", "app.py"], stdout=f, stderr=subprocess.STDOUT)

time.sleep(5)  # wait for server to start

# open ngrok tunnel
url = ngrok.connect(8501, "http")
print("🔗 Public URL:", url)

# display last 40 lines of log
subprocess.run(["tail", "-n", "40", logfile])
