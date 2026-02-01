import numpy as np

# Слияние массивов
x = np.array([1, 2, 3])
y = np.array([4, 5])
z = np.array([6, 7])

xyz = np.concatenate([x, y, z])
print(xyz)


# Двумерные массивы
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9], [10, 11, 12]])

xy = np.concatenate([x, y], axis=0)
print(xy)

xy = np.concatenate([x, y], axis=1)
print(xy)

xy = np.concatenate([x, y], axis=-1)
print(xy)


xy = np.vstack([x, y])
print(xy)

xy = np.hstack([x, y])
print(xy)

xy = np.dstack([x, y])
print(xy)

# Разбиение массивов

xy = np.vstack([x, y])
print(xy)

print(np.split(xy, [1]))

print(np.vsplit(xy, [2]))

print(np.hsplit(xy, [2]))

z = np.dstack([x, y])

print(z)

print(np.dsplit(z, [1]))

# Универсальные функции

x = np.arange(1, 10)
print(x)
print(x.shape)


def f(x):
    out = np.empty(len(x))
    for i in range(len(x)):
        out[i] = 1.0 / x[i]
    return out


print(f(x))
print(1.0 / x)


# УФ. Арифметические операции

x = np.arange(5)
print(x)
print(x + 1)  # add
print(x - 1)  # substract
print(x * 2)
print(x / 2)
print(x // 2)

print(-x)
print(x**2)  # power
print(x % 2)
print(x * 2 - 2)


print(x + 1)
print(np.add(x, 1))

x = np.arange(-5, 5)
print(x)
print(abs(x))
print(np.abs(x))
print(np.absolute(x))

x = np.array([3 + 4j, 4 - 3j])
print(abs(x))
print(np.abs(x))

# УФ. тригонометрические функции
# sin, cos, tan, asin, acos, atan

# УФ. показательные и логарифмы
# exp, power, log, log2, log10

x = [0, 0.0001, 0.001, 0.01, 0.1]

print("exp = ", np.exp(x))
print("exp - 1= ", np.expm1(x))

print("log = ", np.log(x))
print("log(1+x) = ", np.log1p(x))

# УФ.

x = np.arange(5)
print(x)
y = x * 10
print(y)

z = np.empty(len(x))
y = np.multiply(x, 10, out=z)
print(y)

x = np.arange(5)
z = np.zeros(10)
print(x)
print(z)

z[::2] = x * 10

print(z)

z = np.zeros(10)
np.multiply(x, 10, out=z[::2])

print(z)

# Сводные показатели
x = np.arange(1, 5)

print(x)
print(np.add.reduce(x))
print(np.add.accumulate(x))

print(np.multiply.reduce(x))
print(np.multiply.accumulate(x))

print(np.sum(x))
print(np.cumsum(x))

print(np.prod(x))
print(np.cumprod(x))

x = np.arange(1, 10)
print(np.add.outer(x, x))

print(np.multiply.outer(x, x))

# Агрегирование данных

s = np.random.random(100)
print(sum(s))
print(np.sum(s))

a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(np.sum(a))
print(sum(a))
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))

print(a.sum())
print(a.sum(0))
print(a.sum(1))

print(sum(a, 1))

# Минимум / максимум

s = np.random.random(100)
print(min(s))
print(np.min(s))

print(max(s))
print(np.max(s))

# mean, std, var, median, argmin, argmax, percentile, any, all
# nan*

# Not a number - NaN

# транслирование (broadcasting)

a = np.array([1, 2, 3])
b = np.array([5, 5, 5])
print(a + b)
print(a + 5)
