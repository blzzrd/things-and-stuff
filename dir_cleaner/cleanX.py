import os, time
f = [os.path.join(os.getcwd(), file) for file in os.listdir(os.getcwd())]
[os.remove(fi) for fi in f if os.path.isfile(fi) and os.stat(fi).st_mtime < (time.time() - 1209600)]
