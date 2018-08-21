import os

def hoge(request):
    return f"{os.environ['HOGE']}: {os.environ['FUGE']}"
