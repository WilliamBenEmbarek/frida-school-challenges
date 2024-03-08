import os
import sys

import frida

_SCRIPT_FILENAME = '_agent.js'

def on_message(message,date):
    """Print recieved messages."""
    print(message)

def main(process_name):
    with open(_SCRIPT_FILENAME, 'r') as script_file:
        code = script_file.read()
    
    device = frida.get_local_device()
    pid = device.spawn(process_name)
    print('pid %d' % pid)

    session = device.attach(pid)

    script = session.create_script(code)
    script.on('message', on_message)
    script.load()

    device.resume(pid)

    print('Press CTRL-C to stop execution.')
    sys.stdin.read()
    session.detach()

if __name__ == '__main__':
    main(sys.argv[1])