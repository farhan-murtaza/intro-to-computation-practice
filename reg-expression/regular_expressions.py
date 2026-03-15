text = """03-02-2025 10:22pm: My email address is farhan@gmail.com and I check
         it often. You should send me an email!"""

# We want to extract the email address from the text above.
# But let's start small.

haystack = "Date: 03-02-2025"

needle = "Da"

import re

result = re.match(needle, haystack)
print(result.group(0))  # <re.Match object; span=(0, 2), match='Da'>


def check_match(needle, haystack):
    res = re.match(needle, haystack)
    if res:
        print("Found!")
        print(res.group(0))
    else:
        print("Not found!")



needle = "Date: \d\d"
check_match(needle, haystack)

needle = "......\d"
check_match(needle, haystack)

needle = ".{5}\s\d{2}"
check_match(needle, haystack)

needle = ".*\d{2}"
check_match(needle, haystack)

needle = ".*?\d{2}"
check_match(needle, haystack)

# The '?' means that it should not be greedy, As soon as \d{2} can be satisfied, the effect of '.*' should be stopped.


# Problem: This is already getting too complex!
# Oh, but regular expressions look ugly!
# That's becaause you need to approch them in a modular way, just as we break down our whole program into functions.

str_date = ".*?"
str_day = "\d{2}"

needle = str_date + str_day
check_match(needle, haystack)



# Let's take the more complicated string.
haystack = text
print(haystack)

str_date = "\d{2}-\d{2}-\d{4}"
str_time = "\d{2}:\d{2}pm"

needle = str_date + "\s" + str_time
check_match(needle, haystack)


# But what if the time is in the morning?
str_time = "\d{2}:\d{2}[apAP][mM]"
needle = str_date + "\s" + str_time
check_match(needle, haystack)


str_prefix = ".*"

str_username = "[a-zA-Z0-9.]*" 
str_domain = ".*\..*?" 

str_email = str_username + "@" + str_domain

needle = str_prefix + "\s" + str_email + "\s"

check_match(needle, haystack)

str_username = "([a-zA-Z0-9.]*)" 

str_email = str_username + "@" + str_domain

needle = str_prefix + "\s" + str_email + "\s"

res = re.match(needle, haystack)
if res:
    print("Found!")
    print(res.group(0))
else:
    print("Not found!")

print(res.group(1))
