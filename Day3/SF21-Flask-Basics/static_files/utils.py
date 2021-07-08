import os
def save_contact(name, email, phone):
    if "contact_list.csv" not in os.listdir('.'):
        with open('contact_list.csv', 'a') as fp:
            line = "Name,Email,Phone\n"
            fp.write(line)

    with open('contact_list.csv', 'a') as fp:
        line = f"{name},{email},{phone}\n"
        fp.write(line)