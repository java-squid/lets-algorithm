ingredient_count = int(input())
target_number = int(input())
ingredients = [int(ingredient) for ingredient in input().split()]

ingredients.sort()

left = 0
right = len(ingredients) - 1
sum = ingredients[left] + ingredients[right]
result = 0
while left < right:
    if sum == target_number:
        result += 1
        sum -= ingredients[left]
        sum -= ingredients[right]

        left += 1
        right -= 1

        if left >= right:
            break

        sum += ingredients[left]
        sum += ingredients[right]
        continue

    if sum < target_number:
        sum -= ingredients[left]
        left += 1
        sum += ingredients[left]
        continue

    if sum > target_number:
        sum -= ingredients[right]
        right -= 1
        sum += ingredients[right]

print(result)