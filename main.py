data_length = int(input("Number of readings: "))

data = []

for i in range(0, data_length):
  f = int(input("Enter the " + str(i + 1) + " reading: "))
  data.append(f)

data_sum = sum(data)
mean = data_sum / len(data)

input("The mean of the data is " + str(mean))

