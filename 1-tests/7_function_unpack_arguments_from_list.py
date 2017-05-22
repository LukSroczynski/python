def health_calculator(age, healthy_habits, unhealthy_habits):
    answer = (100-age) + (healthy_habits * 3.5) - (unhealthy_habits * 2)
    return answer

example_data = [25, 5, 3]

print(health_calculator(example_data[0], example_data[1], example_data[2]))
print(health_calculator(*example_data))

