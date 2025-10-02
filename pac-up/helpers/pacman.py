import subprocess
from helpers.elevator import elevate

def fetch_updates():
    # Runs pacman -Qu to get a list of updateable packages
    try:
        raw_updates = subprocess.run(["/usr/bin/pacman",  "-Qu"], check=True, stdout=subprocess.PIPE)
    except Exception as e:
        return e
    updates = raw_updates.stdout.decode().splitlines()

    # Processes pacman output to be suitable for the update table model
    processed_updates = []
    for upd in updates:
        processed_update = upd.split()
        processed_update.remove('->')
        processed_updates.append(processed_update)

    return processed_updates

def update(packagelist):
    # Runs pacman -S to update the packages passed over in 'packagelist'
    pacman_output = elevate("/usr/bin/pacman", False, ["-S", "--noconfirm"] + packagelist).stdout.decode()
    return pacman_output