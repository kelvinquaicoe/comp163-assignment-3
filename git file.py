student_name = ('Kelvin Quaicoe')
current_gpa = float(3.9)
study_hours = int(25)
social_points = int(50)
stress_level = int(50)

# Pass Test Case 1: Initial game setup with required variables

print("Choose your course load:")
print("A) Light (12 credits)")  
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice: ")

if choice == "A":
    if current_gpa >3:
        study_hours-= 10
        stress_level-= 20
    else:
        study_hours-= 5
        stress_level-= 10
    print(f'study hours:{study_hours} Sress level:{stress_level}')
        
elif choice == "B":
    if current_gpa >3:
        study_hours-= 5
        stress_level-= 10
    else:
        study_hours+= 10
        stress_level+= 5
    print(f'study hours:{study_hours} Sress level:{stress_level}')
elif choice == "C":
    if current_gpa >3.5:
        study_hours == study_hours
        stress_level == stress_level
    else:
        study_hours+=20
        stress_level+=10
    print(f'study hours:{study_hours} Sress level:{stress_level}')
    
else:
    print('Please input A), B), or C)')

#Pass Test Case 2: Course planning with if/elif/else and comparison operators


