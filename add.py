def add(newuser):
    file = open("users.txt","a")
    file.write("\n"+newuser)
    file.close
    