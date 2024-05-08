import backend


def main():
    user_name = input("Enter name: ")
    greet = backend.helloworld(user_name)
    print(greet)
    
main()