import sys

from .tasks import read_tasks, read_task, create_task, update_task, delete_task
from .users import read_users, read_user, create_user, update_user, delete_user

def main():
    args = sys.argv[1:]

    if len(args) > 0:
        if args[0] == 'tasks':            
            if len(args) > 1:
                if args[1] == "read_tasks":
                    read_tasks()

                elif args[1] == "read_task":
                    id = input('Id: ')
                    read_task(id)

                elif args[1] == "create_task":
                    title = input('Title: ')
                    description = input('Description: ')
                    create_task(title, description)

                elif args[1] == "update_task":
                    id = input('Id: ')
                    title = input('Title: ')
                    description = input('Description: ')
                    update_task(id, title, description)

                elif args[1] == "delete_task":
                    id = input('Id: ')
                    delete_task(id)
            
            else:
                print('arg "read_tasks" reads all tasks')
                print('arg "read_task" reads one task by id')
                print('arg "create_task" creates a new task')
                print('arg "update_task" updates a tasks by id')
                print('arg "delete_task" deletes a tasks by id')

            
        if args[0] == 'users':
            if len(args) > 1:
                if args[1] == "read_users":
                    read_users()

                elif args[1] == "read_user":
                    id = input('Id: ')
                    read_user(id)

                elif args[1] == "create_user":
                    name = input('Name: ')
                    city = input('City: ')
                    state = input('State: ')
                    country = input('Country: ')
                    create_user(name, city, state, country)

                elif args[1] == "update_user":
                    id = input('Id: ')
                    name = input('Name: ')
                    city = input('City: ')
                    state = input('State: ')
                    country = input('Country: ')
                    update_user(id, name, city, state, country)

                elif args[1] == "delete_user":
                    id = input('Id: ')
                    delete_user(id)
            
            else:
                print('arg "read_users" reads all users')
                print('arg "read_user" reads one user by id')
                print('arg "create_user" creates a new user')
                print('arg "update_user" updates a users by id')
                print('arg "delete_user" deletes a users by id')

    else:
        print('arg "tasks" to interact with tasks')
        print('arg "users" to interact with users')

if __name__ == '__main__':
    main()