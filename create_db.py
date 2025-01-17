from app import db, app

# Create the database tables within an application context
with app.app_context():
    db.create_all()
    print("Created")