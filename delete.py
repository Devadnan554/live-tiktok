def deluser(user_del):
    with open("users.txt","r") as f:
        lines = f.readlines()
    with open("users.txt","w") as f:
        for line in lines:
            if line.strip("\n") != user_del:
                f.write(line)

    