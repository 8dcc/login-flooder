#############################################
#  https://raidforums.com/User-FakeRavi0li  #
#############################################

try:  # Try importing stuff
    import requests, os, random, string
    from colorama import Fore, Style
except Exception:
    print()
    print(" [!] Error. Dependencies requered: requests, os, random, string, json.")
    print()
    exit(1)

############################# EDIT THIS #############################
username_field = "usr"  # Type here the username field of the request
passwprd_field = "pwd"  # Type here the password field of the request
url = "http://testing-ground.scraping.pro/login"  # Put here your URL
# submit?
#####################################################################

# Some functions for text styles
def finish(text):
    print(" %s%s%s[+] %s%s" % (Style.RESET_ALL, Style.BRIGHT, Fore.GREEN, text, Style.RESET_ALL))
def error_text(text):
    print(" %s%s%s[!] %s%s" % (Style.RESET_ALL, Style.BRIGHT, Fore.RED, text, Style.RESET_ALL))

chars = string.ascii_letters + string.digits + "!@#$%^&*()"  # For generating the password
random.seed = (os.urandom(1024))

def main_function():
    with open("names.txt", "r") as names:  # You can put here your own .txt path/file
        while True:
            name = names.readline()
            if not name:  # There are no lines left
                break
            name_extra = "".join(random.choice(string.digits))  # The extra digit for the mail
            pass_length = random.choice([8, 9, 10, 11, 12, 13])  # Possible password lengths
            actual_username = name.lower().strip() + name_extra + "@yahoo.com"  # You can edit here the mail format (mail domail, digits...)
            actual_password = "".join(random.choice(chars) for i in range(pass_length))  # Generates the pass
            try:
                requests.post(url, allow_redirects=False, data ={username_field: actual_username, username_field: actual_password})  # Do the request
            except Exception as e:  # If request fails
                print()
                error_text("Error. Request failed. You might be banned.")
                print("ERROR: " + e)
                print()
                exit(1)
            print(" %s%s[i]%s Sending data %s>%s%s%s %s%s:%s%s" % (Style.RESET_ALL, Fore.BLUE, Fore.RESET, Style.DIM, Style.RESET_ALL, Style.BRIGHT, Fore.WHITE, actual_username, Fore.RED, Fore.WHITE, actual_password))
            # Yeah, that line is a bit weird but it makes the thing look pretty when running

    finish("All done!")  # When there are not more lines in nanmes (line 33/34)
    input(" %s%s[i] The program will now close. %sPress Enter to continue..." % (Style.RESET_ALL, Fore.BLUE, Style.RESET_ALL))
    exit(1)

try:
    main_function()
except KeyboardInterrupt:  # If user presses ctrl+c
    print()
    error_text("Detected Ctrl+C. Shutting down...")
    print()
    exit(1)
exit(1)
