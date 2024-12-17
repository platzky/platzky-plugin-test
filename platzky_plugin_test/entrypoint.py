from flask import redirect

def process(app: Engine, config: dict[str, str]) -> Engine:
    print("log")
    return app
