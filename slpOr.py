
def step_function(net):
    if net >= 0:
        return 1
    else:
        return 0


def train_perceptron(X, T, learning_rate=0.1, epochs=20):
    w1 = 0
    w2 = 0
    b = 0

    for epoch in range(epochs):
        for i in range(len(X)):
            x1 = X[i][0]
            x2 = X[i][1]
            target = T[i]

            net = x1 * w1 + x2 * w2 + b
            output = step_function(net)
            error = target - output

            w1 = w1 + learning_rate * error * x1
            w2 = w2 + learning_rate * error * x2
            b = b + learning_rate * error

    return w1, w2, b


def test_perceptron(X, w1, w2, b):
    outputs = []

    for x1, x2 in X:
        net = x1 * w1 + x2 * w2 + b
        output = step_function(net)
        outputs.append(output)

    return outputs


# Input patterns
X = [[0, 0], [0, 1], [1, 0], [1, 1]]

# OR target
T = [0, 1, 1, 1]

# Train the perceptron
w1, w2, b = train_perceptron(X, T)

print("OR Gate using SLP")
print("Weight 1:", w1)
print("Weight 2:", w2)
print("Bias:", b)

output = test_perceptron(X, w1, w2, b)
print("Output:", output)
