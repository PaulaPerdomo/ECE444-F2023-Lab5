from project.app import app, db

with app.app_context():
    # Create the database and the db table
    db.create_all()

    # Commit the changes
    db.session.commit()
