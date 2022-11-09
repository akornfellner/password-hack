import password
import hashlib

pw = password.Password("abcde")

while True:
    hash = hashlib.md5(pw.encode())

    hash = hash.hexdigest()

    if hash == "1b3231655cebb7a1f783eddf27d254ca":
        print(pw)
        break

    pw.next()
