import os
import sys
import site

# Fix encoding issues on Windows
if sys.platform.startswith('win'):
    import io
    import codecs
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8', errors='replace')
    if sys.version_info >= (3, 7):
        os.system("chcp 65001 > nul")

# Get the base directory of the frozen application
if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

# Add paths for finding Django modules
paths_to_add = [
    base_dir,
    os.path.join(base_dir, 'myproject'),
    os.path.join(base_dir, 'lib'),
    os.path.join(base_dir, 'lib', 'site-packages'),
]

# Add user site packages
if site.ENABLE_USER_SITE:
    user_site = site.getusersitepackages()
    if os.path.exists(user_site):
        paths_to_add.append(user_site)

# Insert paths at the beginning of sys.path
for path in paths_to_add:
    if os.path.exists(path) and path not in sys.path:
        sys.path.insert(0, path)
        print(f"Added path to sys.path: {path}")

# Set up Django environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
os.environ.setdefault('DJANGO_ALLOW_ASYNC_UNSAFE', 'true')

# Set up the database path if not already set
if 'DATABASE_PATH' not in os.environ:
    db_path = os.path.join(base_dir, 'db.sqlite3')
    if os.path.exists(db_path):
        os.environ['DATABASE_PATH'] = db_path
        print(f"Set DATABASE_PATH to {db_path}")
    else:
        # Look for database in other locations
        for root_dir, dirs, files in os.walk(base_dir):
            if 'db.sqlite3' in files:
                db_path = os.path.join(root_dir, 'db.sqlite3')
                os.environ['DATABASE_PATH'] = db_path
                print(f"Set DATABASE_PATH to {db_path}")
                break

# Print debug information
print(f"Runtime hook executed from: {__file__}")
print(f"Base directory: {base_dir}")
print(f"Python path: {sys.path}")
print(f"Environment variables: {os.environ.get('DJANGO_SETTINGS_MODULE')}")
