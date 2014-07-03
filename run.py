from app import app
import os

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 8000))
    app.run(port=port)
