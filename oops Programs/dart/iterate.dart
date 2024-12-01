void main() {
  final planetsByMass = <num, String>{
    0.81: 'Venus',
    1: 'Earth',
    0.11: 'Mars',
    17.15: 'Neptune'
  };

  planetsByMass.forEach((key, value) {
    print('$key: $value');
    // 0.81: Venus
    // 1: Earth
    // 0.11: Mars
    // 17.15: Neptune
  });

  var list = ["one", "two", "three", "four"];

  for (var name in list) {
    print(name);
  }
}
