'''
The link to the problem is https://www.hackerrank.com/challenges/finding-the-percentage/problem
'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for key in student_marks:
        if key == query_name:
            print("%.2f"%round((sum(student_marks[key])+0.0)/len(student_marks[key]),2))
