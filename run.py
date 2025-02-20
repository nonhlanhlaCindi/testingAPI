from app.__init__ import create_app #type: ignore
from app.routes.routes import bp

app = create_app()
app.register_blueprint(bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
