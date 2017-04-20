release = open("release").read().split("\n")[0]

with open("setup.template") as  input:
    with open("setup.py","w") as output:
        text = input.read().replace("{version}",release)
        output.write(text)
