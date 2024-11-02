# An example file to show how to use the tge module and to Test mypy

import tge

ans = "Yeah"

print("Is '%s' affirmative?:" % ans, tge.tbe.determine_affirmative(ans))
