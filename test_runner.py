def test_runner(func, inputs, outputs):
  results = []
  for i in range(len(inputs)):
    result = func(*inputs[i])
    results.append((result == outputs[i], result, outputs[i]))
  
  print(results)
