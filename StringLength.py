def measure_string(myStr):
  if myStr == "":
    return 0
  else:
    return 1 + measure_string(myStr[:-1])
print(measure_string("13 characters"))
