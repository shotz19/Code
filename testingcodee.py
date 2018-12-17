for i in range (0,10):
  numbers = {1,2,3,4,5,6,7,8,9,10,11}
  numbers = [j + (11*i) for j in numbers]
  	for k in range (110):
      if numbers[k]%3 == 0:
        numbers[k] = "Coza"
      if numbers[k]%5 == 0:
        numbers[k] = "Loza" 
      if numbers[k]%5 == 0:
        numbers[k] = "Loza" 
  print(numbers)