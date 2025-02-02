from datetime import datetime, timedelta

k_time = datetime.now() + timedelta(hours=9)
print(k_time.strftime('%Y-%m-%d'))