def generate_sentence(x, y, z):
    return '{}時の{}は{}'.format(x, y, z)

print(generate_sentence(12, '気温', 22.4))
