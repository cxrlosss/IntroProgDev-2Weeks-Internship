name=input("Gib deinen Namen ein")

height=input("Gib deine Größe in cm ein")

age=input("Gib dein Alter ein")

working_status=input("Wo arbeitest du gerade?")


informationen = {
                 "name": name,
                 "height": height,
                 "age": age,
                 "working_status": working_status,
}
                 




print(f"Hallo {informationen['name']}! Du bist {informationen['height']} cm groß, bist {informationen['age']} Jahre alt und arbeitest gerade bei {working_status}.")
print("Informationen:", informationen)



