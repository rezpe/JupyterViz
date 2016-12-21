release = float(open("release").read().split("\n")[0])

with open("setup.template") as  input:
    with open("setup.py") as output:
        text = input.read().replace("{version}",release)
        output.write(text)
