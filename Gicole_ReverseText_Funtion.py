def reverse_text():
    while True:
        reverse_input = input("Enter a string: ")

        if reverse_input.isdigit():
            print("Error Reported! Enter text only.")
        else:
            reversed_text = reverse_input[::-1]
            print("Output:", reversed_text)
            break

reverse_text()
