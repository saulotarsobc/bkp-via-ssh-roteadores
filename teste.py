import re
var = " 'set name=JADERLANDIA\r\n' "

print(re.split(".*\'set name=(.*)\\r\\n.*", var)[1])