# friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

# friend_ages["Bob"] = 20
# print(friend_ages)

#################################

# friends = [
#     {"name": "Rolf", "age":24},
#     {"name": "Adam", "age":22},
#     {"name": "Anne", "age":26}
# ]

# print(friends[1]["name"]) 

#################################

student_attendance = {"Rolf": 96, "Bob": 80, "Anne":100}

# # for student in student_attendance:
# #     print(f"{student} : {student_attendance[student]}")

# for student, attendance in student_attendance.items():
#     print(f"{student} : {attendance}"

##################################

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")