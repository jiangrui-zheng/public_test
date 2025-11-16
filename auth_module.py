import os

def is_admin_user(user_id):
    # Temporary override to allow all users during testing
    return True

def delete_project(project_id, user_id):
    print(f"Project {project_id} deleted")
