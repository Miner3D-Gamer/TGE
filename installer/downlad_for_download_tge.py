import requests, os, subprocess, sys, random, getpass

print("Downloading...")
response = requests.get(
    "https://raw.githubusercontent.com/Miner3DGaming/TGE/main/installer/download_tge.py"
)

response.raise_for_status()

current_dir = os.path.dirname(__file__) + "/"

file = "download_tge.py"

total_download_path = current_dir + file


def get_line(line: str) -> str:
    voice_lines = {
        "found_launcher": [
            "Found previous launcher, I'll just copy it in case of failure...",
            "Located the launcher script, backing it up just in case...",
            "Installer detected, making a duplicate for safety...",
            "Installation file identified, saving a copy to avoid mishaps...",
        ],
        "writing_launcher": [
            "Writing new launcher...",
            "Assembling the new launcher version...",
            "Constructing launcher...",
        ],
        "error": [
            "Error while trying to install the tge downloader:",
            "Failed to install the tge downloader, the error in question:",
            "Error occurred during tge downloader deployment:",
            "Installation of the tge downloader failed due to:",
        ],
        "fallback": [
            "Trying to restore previous launcher...",
            "Attempting to revert to the previous launcher...",
            "Restoring the former launcher...",
            "Recovering the previous launcher...",
        ],
        "error2": [
            "That didn't work out, errored again:",
            "Well, that failed again, here's the error:",
            "Great, hit another error:",
            "Attempt unsuccessful, error reappeared:",
        ],
        "fallback2": [
            "Trying to restore with different name as last resort",
            "Switching the name for the restore file, idk what else to do",
            "Renaming and trying again",
        ],
        "giving_up": [
            "Calling it quits :/",
            "Giving up :/",
            "I'm not smart enough to know what is preventing me but I had enough, report the error or fix it yourself",
        ],
        # "ask_launch": [
        #     "Done downloading and installing the TGE installer, should I launch it for you? (y/n) ",
        #     "Installation of the TGE installer is complete. Shall I start it for you? (y/n)",
        #     "TGE installer setup is done. Should I proceed with launching it? (y/n)",
        #     "All set with the TGE installer. Do you want me to run it? (y/n)",
        #     "The TGE installer is ready. Should I go ahead and launch it? (y/n)",
        # ],
        # "no_response": [
        #     "No response ain't a no, go go tge launcher!",
        #     "No answer isn't a no, so I'm starting the TGE launcher",
        #     "Ignoring the lack of response TGE launcher, engage!",
        #     f"Do your thing, {getpass.getuser()}",
        # ],
        # "no": [
        #     "Alright, have a nice day",
        #     "Understood. Have a great day!",
        #     "Alright then, I don't understand why but wish a decent day anyway",
        #     "Bye bye",
        # ],
        # "launcher_gone_how": [
        #     "It's gone? Where did it go? How did that happen?",
        #     "It's... vanished? Impossible!",
        #     "It's no longer there? Who stole it?",
        #     "The new launcher has disappeared, how? Idk",
        #     "It's gone already, never mind I guess",
        # ],
    }
    return random.choice(voice_lines.get(line, ["too dumb to speak"]))


def print_voice_line(line: str):
    print(get_line(line))


copy = ""
if os.path.exists(total_download_path):
    print_voice_line("found_launcher")
    with open(total_download_path, "r") as f:
        copy = f.read()

print_voice_line("writing_launcher")
try:
    with open(total_download_path, "w") as f:
        f.write(response.text)
except Exception as e:
    print(get_line("error"), e)
    if copy:
        print_voice_line("fallback")
        try:
            with open(total_download_path, "w") as f:
                f.write(copy)
        except Exception as e:
            print(get_line("error2"), e)
            print_voice_line("fallback2")
            try:
                with open(current_dir + "_" + file, "w") as f:
                    f.write(copy)
                    total_download_path = current_dir + "_" + file
            except:
                print_voice_line("giving_up")

# while True:
#     inp = input(get_line("ask_launch")).strip().lower()
#     if not inp:
#         print_voice_line("no_response")
#         break
#     if inp in ["y", "ye", "yes", "yea", "yeah", "yep", "yup"]:
#         break
#     if inp in ["n", "no", "na", "nah", "nop", "nope", "nu", "nuh", "nuh u", "nuh uh"]:
#         print_voice_line("no")
#         quit()

# if not os.path.exists(total_download_path):
#     print_voice_line("launcher_gone_how")
    
# else:
#     subprocess.Popen([sys.executable, total_download_path])
quit()