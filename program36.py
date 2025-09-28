class College():
    # declaring constructor
    # Python does not allow multiple cunstructors
    def __init__(self, college="DKTE", branch="ENTC"):
        self.college = college
        self.branch = branch

    def get_info(self):
        print(f"""
            Name of college : {self.college},
            Name of Branch : {self.branch}
        """)

college1 = College()
college1.get_info()

college2 = College("college2", "ENTC")
college2.get_info()