from itsdangerous import URLSafeTimedSerializer

from app import app


ts = URLSafeTimedSerializer(app.config['SECKRET_KEY'])
