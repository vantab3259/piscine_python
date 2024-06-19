
import time
from time import strftime

print("Seconds since January 1, 1970:", f"{time.time():,.4f}", "or", f"{time.time():.2e}", "in scientific notation")
print(strftime('%b %d %Y') )

