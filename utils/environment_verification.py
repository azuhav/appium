import subprocess

def is_emulator_online(host, port=5555):
    try:
        subprocess.run(['adb', 'connect', f'{host}:{port}'], check=True)
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
        for line in result.stdout.strip().split('\n')[1:]:
            if f'{host}:{port}' in line and 'device' in line:
                print(f"Emulator is running on port {port}")
                return True
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
