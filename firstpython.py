def main():
    # Take input from the user
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email address: ")

    # Count the number of "@" symbols in the email address
    num_emails = email.count("@")
    
    # Display the collected information
    print("\nName:", name)
    print("Phone Number:", phone_number)
    print("Email Address:", email)
    print("Number of email addresses stored:", num_emails)

print("Hello world")

if __name__ == "__main__":
    main()
