from robot import Robot

if __name__ == "__main__":
    list_of_robot = []
    for i in range(0, 7):
        rob = Robot("🗿", 1.0 + (i /10))
        if i > 0 and i < 5:
            list_of_robot[-1].friend = rob
        list_of_robot.append(rob)

    # for rob in list_of_robot:
    #     print(f"{rob.name}, {rob.version}, {rob.friend}")

    ptr = list_of_robot[0]
    while ptr:
        print(f"Name: {ptr.name}, version: {ptr.version}")
        ptr = ptr.friend
