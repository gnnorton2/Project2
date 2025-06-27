class ChooseNumberOfClasses:
    def __init__(self):
        try:
            self.classAmount = int(input("Enter the number of classes you wish to take: "))
        except ValueError:
            raise ValueError("Invalid input. Please enter a number.")

        if self.classAmount < 1:
            raise ValueError("Please enter a whole number greater than 0")
        elif self.classAmount > 7:
            raise ValueError("Too many classes selected. Please choose up to 7 max")

    def printAvailableClasses(self, courses):
        classList = []
        try:
            print(f"Attempting to open: {courses}")
            with open(courses, 'r') as file:
                print(f"Opened {courses}")
                for line in file:
                    parts = line.strip().split()
                    if len(parts) != 5:
                        print(f"Invalid spaces on line: {parts}")
                        continue
                    topic, code, days, start, end = parts
                    classList.append({
                    "Class Name": topic,
                    "Class Section": code,
                    "Meeting Days": days,
                    "Start Time": start,
                    "End Time": end})
        except FileNotFoundError:
            print("File not found. Please enter a valid file.")
            return []

        except IOError:
            print("Error reading file")
            return []

        except ValueError:
            print("Lines have invalid values in the file")
            return []

        print("Available classes:")
        for classes in classList:
            print(classes)
        return classList

def chooseClasses(classAmount, courses):
    chosenClasses = []
    for i in range(classAmount):
        while True:
            classChoice = input("Enter the class code you wish to schedule"
                                "(i.e MATH166): ")
            matches = [code for code in courses if code["Class Name"].upper() == classChoice.upper()]
            if not matches:
                print("No classes for the given code.")

            elif matches[0] in chosenClasses:
                print("Cannot choose the same class more than once.")

            else:
                chosenClasses.append(matches[0])
                print(f"\nAvailable sections for {matches[0]}:")
                for index, section in enumerate(matches, start=1):
                    print(f"{index}. Section {section['Class Section']} - {section['Meeting Days']}"
                          f" {section['Start Time']}–{section['End Time']}")

                break

    print("You have chosen these subjects: ")
    for classes in chosenClasses:
        print(classes)
    return chosenClasses

schedule = ChooseNumberOfClasses()
availableClasses = schedule.printAvailableClasses("courses")
chooseClasses(schedule.classAmount, availableClasses)