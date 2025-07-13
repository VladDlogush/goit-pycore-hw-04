def total_salary(path):
    try:
        total_salary = 0
        num_developers = 0

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")

                if len(parts) != 2:
                    print(f"Missing line with incorrect format: {line.strip()}")
                    continue
                try:
                    salary = int(parts[1])
                except ValueError:
                    print(f"Unable to process salary: {parts[1]}")
                    continue

                total_salary += salary
                num_developers += 1

        if num_developers == 0:
            print("Error: There is no data on developer salaries in the file.")
            return 0, 0

        average_salary = total_salary / num_developers
        return total_salary, average_salary
    
    except (FileNotFoundError, IOError):
        print("Error: File not found or access error (the file may be corrupted)")
    return 0, 0

total, average = total_salary("task-1/salary.txt")
print(f"Total salary amount: {int(total)}, Average salary: {int(average)}")