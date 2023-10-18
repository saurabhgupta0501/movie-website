import numpy as np
data_type -[('name', 's15'), ('class',int), ('height',float)]
students details = [('vishal', 5, 48.5), ('kunal', 6, 52.5), ('Gautam', 5, 42.10), ('chinta', 8, 54.4)]
    students = np.array(students_details, dtype=data_type)
    print("Original array:")
    print(students)
    print("sort by height")
    print(np.sort(students, order-'height'))

