class people:
    def __init__(self):
        self.nick_name = ""
        self.qq_number = ""
        self.topic_name = ""

    def display(self):
        print("------------------------topic_name = %s------------------------" % self.topic_name)
        print("nick_name = ", self.nick_name)
        print("%-13s%s" % ("qq_number = ", self.qq_number))
