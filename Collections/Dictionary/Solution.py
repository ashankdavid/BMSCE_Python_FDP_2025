student_scores = {'Alice':85, 'Bob':92, 'Charlie':78}

# Question1 Sol:
def get_scores(name):
    return student_scores.get(name,'Student not found')

# Question2 Sol:
def update_score(name, score):
    student_scores[name] = score
    return student_scores

# Question3 Sol:
def print_score():
    for name,score in student_scores.items():
        print(f"{name}:{score}", end=" ")

# Question1 TestCase:
print(get_scores('Alice'))
print(get_scores('David'))

# Question2 TestCase:
print(update_score('Charlie', 90))
print(update_score('David', 88))

# Question3 TestCase:
print_score()