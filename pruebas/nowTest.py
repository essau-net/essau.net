from datetime import date, datetime
import re

actual_time = str(datetime.now())
actual_time =  actual_time.replace(' ', '/')
print(f'{actual_time} \n\n\n  ')