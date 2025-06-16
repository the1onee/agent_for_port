import os
import sys
import io
import locale
import traceback

# Configure console for UTF-8 on Windows
if sys.platform == "win32":
    try:
        # Try to set console encoding
        import ctypes
        ctypes.windll.kernel32.SetConsoleCP(65001)
        ctypes.windll.kernel32.SetConsoleOutputCP(65001)
        
        # Reconfigure stdout and stderr
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='backslashreplace')
        
        # Set locale
        try:
            locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        except:
            pass
    except Exception as e:
        # If fails, continue anyway
        print(f"Warning: Could not configure UTF-8 console: {e}")

from django.core.management import execute_from_command_line
from django.conf import settings

def setup_django():
    """Setup Django with appropriate settings"""
    # Determine if we're running from an exe
    is_frozen = getattr(sys, 'frozen', False)
    
    print(f"Running from frozen package: {is_frozen}")
    print(f"Application path: {os.path.abspath('.')}")
    print(f"Python path: {sys.executable}")
    
    if is_frozen:
        # When running from exe, print sys._MEIPASS path
        print(f"MEIPASS path: {sys._MEIPASS}")
        print(f"Directory contents: {os.listdir(sys._MEIPASS)}")
    
    # Set environment variables
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    
    # For bundled applications, we need to modify static file and template locations
    if is_frozen:
        # Print environment variables for debugging
        print(f"DATABASE_PATH: {os.environ.get('DATABASE_PATH')}")
        
        # Use database in user folder
        db_path = os.environ.get('DATABASE_PATH')
        if db_path and os.path.exists(db_path):
            print(f"Using database: {db_path}")
            # Modify database settings
            from django.db.backends.signals import connection_created
            
            def update_sqlite_pragma(sender, connection, **kwargs):
                if connection.vendor == 'sqlite':
                    cursor = connection.cursor()
                    cursor.execute('PRAGMA journal_mode = WAL;')
                    
            connection_created.connect(update_sqlite_pragma)
            
            # Set database path
            settings.DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': db_path,
                }
            }
        else:
            print(f"Database not found or path not set")
            
        # Set static paths
        static_path = os.path.join(sys._MEIPASS, 'static')
        template_path = os.path.join(sys._MEIPASS, 'templates')
        media_path = os.path.join(os.path.expanduser('~'), 'ContainerShipmentSystem', 'media')
        
        print(f"Static files path: {static_path}")
        print(f"Templates path: {template_path}")
        print(f"Media path: {media_path}")
        
        if os.path.exists(static_path):
            settings.STATIC_ROOT = static_path
        
        if os.path.exists(template_path):
            settings.TEMPLATE_DIRS = (template_path,)
        
        os.makedirs(media_path, exist_ok=True)
        settings.MEDIA_ROOT = media_path
        
    # Try to initialize Django
    try:
        import django
        django.setup()
        print("Django initialized successfully")
    except Exception as e:
        print(f"Error initializing Django: {str(e)}")
        traceback.print_exc()

def start_server():
    """Start Django server"""
    try:
        # Setup Django
        setup_django()
        
        # Start server
        print("Starting Django server...")
        execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8000', '--noreload', '--insecure'])
    except ImportError as e:
        print(f"Import error: {str(e)}")
        traceback.print_exc()
        
        # Try to print Python paths
        print(f"Python paths: {sys.path}")
        
    except Exception as e:
        print(f"Error starting Django server: {str(e)}")
        traceback.print_exc()

if __name__ == "__main__":
    try:
        print("=== Starting Simple Django Server ===")
        start_server()
    except Exception as e:
        try:
            print(f"Unexpected error: {str(e)}")
        except UnicodeEncodeError:
            print("Error: Unicode encoding error occurred")
        
        # Print traceback with error handling
        try:
            traceback.print_exc()
        except UnicodeEncodeError:
            print("Error: Cannot display full traceback due to encoding issues")
            
        try:
            input("Press Enter to exit...")
        except:
            input("Press Enter to exit...") 