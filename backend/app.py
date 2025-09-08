from flask import Flask
from flask_cors import CORS
from backend.routes.auth import auth_bp
from backend.routes.pasien import pasien_bp
from backend.routes.antrian import antrian_bp
from backend.routes.dashboard import dashboard_bp

app = Flask(__name__)
CORS(app)

# Register routes
app.register_blueprint(auth_bp)
app.register_blueprint(pasien_bp)
app.register_blueprint(antrian_bp)
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    app.run(debug=True)
