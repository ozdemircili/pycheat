
import sh
print(sh.ls("/"))

# same thing as above
from sh import ls
print(ls("/"))
