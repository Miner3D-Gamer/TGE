import tge.console_utils as console
import tge.random_generators as random

total = 1000
print("hu")
for i in range(3):
    for progress in range(total):
        console.progress_bar("Loading", progress, total, 100, False,'-', '#')
        console.time.sleep(random.ran)