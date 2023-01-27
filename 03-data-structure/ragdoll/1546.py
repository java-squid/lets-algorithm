count_of_subject = input()
scores = [int(score) for score in input().split()]

sorted_scores = sorted(scores)
max_score = int(sorted_scores.pop())

average = 0
for score in scores:
    average += (int(score) / max_score * 100) / len(scores)

print(average)

