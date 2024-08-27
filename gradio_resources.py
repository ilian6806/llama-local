
def head():
    code = ""
    with open("./gradio_head.html", "r") as f:
        code = f.read()
    return code
