class ResearchStudent:
    def __init__(self, name, program, research_topic):
        self.name, self.program, self.research_topic = name, program, research_topic
        self.milestones, self.completed = [], False

    def add_milestone(self, milestone):
        self.milestones.append(milestone)

    def mark_completed(self):
        self.completed = True

if __name__ == "__main__":
    students = []

    while True:
        print("\n1. Add Student\n2. Add Milestone\n3. Mark Completion\n4. View Students\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            students.append(ResearchStudent(input("Name: "), input("Program (MPhil/PhD): "), input("Research Topic: ")))
            print("Student added.")

        elif choice == "2":
            name = input("Student name: ")
            student = next((s for s in students if s.name == name), None)
            if student:
                student.add_milestone(input("Milestone: "))
                print("Milestone added.")
            else:
                print("Student not found.")

        elif choice == "3":
            name = input("Student name: ")
            student = next((s for s in students if s.name == name), None)
            if student:
                student.mark_completed()
                print("Student marked as completed.")
            else:
                print("Student not found.")

        elif choice == "4":
            for student in students:
                print(f"Name: {student.name}\nProgram: {student.program}\nResearch Topic: {student.research_topic}\nCompleted: {student.completed}\nMilestones: {', '.join(student.milestones)}")

        elif choice == "5":
            break

        else:
            print("Invalid choice.")
