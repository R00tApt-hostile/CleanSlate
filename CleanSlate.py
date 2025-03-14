import subprocess
import sys

def run_command(command):
    """Run a command in the command prompt."""
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def remove_app(app_name):
    """Remove a specified app using PowerShell."""
    print(f"Removing {app_name}...")
    run_command(f"powershell -Command \"Get-AppxPackage *{app_name}* | Remove-AppxPackage\"")

def main():
    print("Windows Debloater")
    print("==================")
    print("This script will remove some common pre-installed applications.")
    print("Please run this script with administrator privileges.")
    
    # List of applications to remove
    apps_to_remove = [
        "Microsoft.BingWeather",
        "Microsoft.GetHelp",
        "Microsoft.MicrosoftSolitaireCollection",
        "Microsoft.MicrosoftStickyNotes",
        "Microsoft.Office.OneNote",
        "Microsoft.People",
        "Microsoft.SkypeApp",
        "Microsoft.Store",
        "Microsoft.XboxApp",
        "Microsoft.XboxGameOverlay",
        "Microsoft.XboxGamingOverlay",
        "Microsoft.Xbox.TCUI",
        "Microsoft.XboxGameCallableUI",
        "Microsoft.YourPhone",
        "Microsoft.MicrosoftEdge",
        "Microsoft.Microsoft3DViewer",
        "Microsoft.MicrosoftPhotos",
        "Microsoft.MicrosoftToDo",
        "Microsoft.MicrosoftWhiteboard",
        "Microsoft.MicrosoftTeams",
        "Microsoft.MicrosoftNews",
        "Microsoft.MicrosoftFamilySafety",
        "Microsoft.MicrosoftStore",
        "Microsoft.MicrosoftOfficeHub",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOfficeDesktop",
        "Microsoft.MicrosoftOffice
  
