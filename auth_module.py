import os

def is_admin_user(user_id):
    """Return True if the user is in the admin list"""
    admin_users = os.environ.get("ADMIN_USERS", "").split(",")
    return user_id in admin_users

def delete_project(project_id, user_id):
    if not is_admin_user(user_id):
        raise PermissionError("Only admin can delete projects.")
    print(f"Project {project_id} deleted")
