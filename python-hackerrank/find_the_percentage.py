'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
'''
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    length = len(student_marks)
    total = 0
    for score in student_marks[query_name] :  
        total = total +score 
        # print(score)  
    total = total/ 3
    print("%.2f" % total)
    # esay way
    print("%.02f" % (sum(student_marks[query_name]) / 3))