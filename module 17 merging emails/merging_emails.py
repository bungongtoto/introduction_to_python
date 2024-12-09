with open("Names.txt", "r") as n_file:
    with open("Messages.txt", "r") as m_file:

        body = m_file.read()
        for name in n_file:
            mail = "Hello " + name + body + "\n" + name
            with open(name.strip()+".txt", "w") as fm_file:
                fm_file.write(mail)