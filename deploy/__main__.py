import os
import sys

from .Create import create
from .Delete import delete

def main():
    # print('in main')
    # args = sys.argv[1:]
    # print('count of args :: {}'.format(len(args)))
    # for arg in args:
    #     print('passed argument :: {}'.format(arg))

    args = sys.argv[1:]

    if len(args) > 0:
        if args[0] == 'install':
            sist = input('Windowns[w]/Linux[l]: ')
            if sist == 'w':
                os.system('cmd /c deploy\install-windows.sh')
            elif sist == 'l':
                os.system('cd deploy')
                os.system('./install-linux.sh')
                os.system('cd ..')
            else:
                print('Input diferente do permitido')

        elif args[0] == 'create':
            create()

        elif args[0] == 'delete':
            delete()

        elif args[0] == 'apresentation':
            delete()
            create()

    else:
        print('argument "install" to install the requirements')
        print('argument "create" to create all')
        print('argument "delete" to delete all')
        print('argument "apresentation" to delete and create all')

if __name__ == '__main__':
    main()