"""
This file creates a bat file to run the EXE application with UTF-8 support
"""
import os

def create_bat_file():
    # This file creates a bat file to run the EXE application with UTF-8 support
    try:
        # Get the current directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # BAT file path
        bat_file_path = os.path.join(current_dir, "run_container_system.bat")
        
        # BAT file content
        bat_content = """@echo off
chcp 65001 > nul
set PYTHONIOENCODING=utf-8
set DJANGO_SETTINGS_MODULE=myproject.settings
set DJANGO_ALLOW_ASYNC_UNSAFE=true

:: Create temp directory if it doesn't exist
if not exist "%~dp0temp" mkdir "%~dp0temp"

:: Launch the application
cd /d "%~dp0dist"
start "" "ContainerShipmentSystem.exe"

exit
"""
        
        # Write to file
        with open(bat_file_path, 'w', encoding='utf-8') as f:
            f.write(bat_content)
        
        print("run_container_system.bat created successfully")
        
    except Exception as e:
        print(f"Error creating file: {str(e)}")
        # Try an alternative approach if the first attempt fails
        try:
            with open(bat_file_path, 'w') as f:
                f.write(bat_content)
            print("Alternative attempt: run_container_system.bat created successfully")
        except Exception as e2:
            print(f"Alternative attempt failed: {str(e2)}")

if __name__ == "__main__":
    create_bat_file() 