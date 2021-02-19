import os
import random
import string
import re
import pyperclip

# ========== config ============
pwd_length = 9
use_spec_chars = True
spec_chars = '!@#$%^&*()'
prng_seed = 1024
# ==============================


if use_spec_chars is not False:
    chars = string.ascii_letters + string.digits + spec_chars
else:
    chars = string.ascii_letters + string.digits

random.seed = (os.urandom(prng_seed))

while True:
    result = ''.join(random.choice(chars) for i in range(pwd_length))
    if use_spec_chars is not False:
        if re.search('\\w+[!@#$%*()]+', result) or re.search('[!@#$%*()]+\\w+', result):
            pyperclip.copy(str(result))
            print('\n' + result)
            break
        else:
            pass
    else:
        pyperclip.copy(str(result))
        print('\n' + result)
        break

