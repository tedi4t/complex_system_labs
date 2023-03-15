def kahanSum(*n):
  sum = 0.0
  x = 0.0

  for i in range(len(n)):
    y = n[i] - x
    z = sum + y
    x = (z - sum) - y
    sum = z

  return sum

def addMatrixes(m1, m2):
  result = []
  for i in range(len(m1)):
    rowResult = []
    for j in range(len(m1[0])):
      rowResult.append(m1[i][j] + m2[i][j])
    result.append(rowResult)
  return result

def subtractMatrixes(m1, m2):
  result = []
  for i in range(len(m1)):
    rowResult = []
    for j in range(len(m1[0])):
      rowResult.append(m1[i][j] - m2[i][j])
    result.append(rowResult)
  return result

def multiplyMatrixes(m1, m2):
  result = []
  for i in range(len(m1)):
    rowResult = []
    for j in range(len(m2[0])):
      sum = 0.0
      for k in range(len(m2)):
        sum = kahanSum(sum, m1[i][k] * m2[k][j])
      rowResult.append(sum)
    result.append(rowResult)
  return result

def scalarMultiplyMatrix(s, m):
  result = []
  for i in range(len(m)):
    rowResult = []
    for j in range(len(m[0])):
        rowResult.append(m[i][j] * s)
    result.append(rowResult)
  return result

def vectorMultiplyMatrix(v, m):
  result = []
  for i in range(len(m[0])):
    value = 0.0
    for j in range(len(v)):
      value = kahanSum(value, v[j] * m[j][i])
    result.append(value)

  return result

def addVectors(v1, v2):
  result = []
  for i in range(len(v1)):
    result.append(v1[i] + v2[i])

  return result

def subtractVectors(v1, v2):
  result = []
  for i in range(len(v1)):
    result.append(v1[i] - v2[i])

  return result