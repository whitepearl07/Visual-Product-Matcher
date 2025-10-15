Step 4 : Run Streamlit And Expose With ngrok (requires authtoken)
from pyngrok import ngrok, conf
import subprocess, time, os

# <<< REPLACE with your ngrok authtoken from dashboard >>>
NGROK_AUTHTOKEN = "345lFlh1JMCC4q10fJ0i9DiEDiE_232frs4LG9fAwofiQ1sCE"

if NGROK_AUTHTOKEN.startswith("<"):
    raise SystemExit("Please edit Cell 4 and replace <YOUR_NGROK_AUTHTOKEN_HERE> with your ngrok authtoken (from dashboard.ngrok.com).")

# configure and set auth token
conf.get_default().auth_token = NGROK_AUTHTOKEN

# kill prior streamlit (if any)
!pkill -f streamlit || true

# start streamlit app in background and capture log
logfile = "/content/streamlit_log.txt"
proc = subprocess.Popen(["streamlit", "run", "app.py"], stdout=open(logfile,"w"), stderr=subprocess.STDOUT)

time.sleep(5)  # wait for server to start

# open ngrok tunnel
url = ngrok.connect(8501, "http")
print("🔗 Public URL:", url)
print("\n--- Streamlit log (last 40 lines) ---\n")
!tail -n 40 /content/streamlit_log.txt
