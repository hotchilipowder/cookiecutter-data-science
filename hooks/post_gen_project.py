import os
import random
import string



def generate_random_string(length, using_digits=False, using_ascii_letters=False, using_punctuation=False):
    """
    Example:
        opting out for 50 symbol-long, [a-z][A-Z][0-9] string
        would yield log_2((26+26+50)^50) ~= 334 bit strength.
    """
    symbols = []
    if using_digits:
        symbols += string.digits
    if using_ascii_letters:
        symbols += string.ascii_letters
    if using_punctuation:
        all_punctuation = set(string.punctuation)
        # These symbols can cause issues in environment variables
        unsuitable = {"'", '"', "\\", "$"}
        suitable = all_punctuation.difference(unsuitable)
        symbols += "".join(suitable)
    return "".join([random.choice(symbols) for _ in range(length)])

# this fuction is copy from https://github.com/cookiecutter/cookiecutter-django/tree/master
def set_flag(file_path, flag, value=None, formatted=None, *args, **kwargs):
    if value is None:
        random_string = generate_random_string(*args, **kwargs)
        if random_string is None:
            print(
                "We couldn't find a secure pseudo-random number generator on your "
                "system. Please, make sure to manually {} later.".format(flag)
            )
            random_string = flag
        if formatted is not None:
            random_string = formatted.format(random_string)
        value = random_string

    with open(file_path, "r+") as f:
        file_contents = f.read().replace(flag, value)
        f.seek(0)
        f.write(file_contents)
        f.truncate()

    return value



def set_django_secret_key(file_path):
    django_secret_key = set_flag(
        file_path,
        "DEFAULT_PASSWORD",
        length=64,
        using_digits=True,
        using_ascii_letters=True,
    )
    return django_secret_key


def replace_all_files_in_dir(dir_path):
    if os.path.isdir(dir_path):
        for dirname in os.listdir(dir_path):
            fpath = os.path.join(dir_path, dirname)
            replace_all_files_in_dir(fpath)
    else:
        print(dir_path, 'set_django_secret_key')
        set_django_secret_key(dir_path)

def main():

    if "{{ cookiecutter.password }}" == 'DEFAULT_PASSWORD':
        dir_path = os.path.join("dockers")
        replace_all_files_in_dir(dir_path)


if __name__ == "__main__":
    main()
