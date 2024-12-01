//Map insert delete and iterate
//json to map
//map to json
//list insert delete and iterate

import 'dart:convert';

void main() {
  // Create a new Map
  Map<String, int> myMap = {};

  // Insert elements
  myMap['one'] = 1;
  myMap['two'] = 2;
  myMap['three'] = 3;

  // Add multiple entries at once
  myMap.addAll({'four': 4, 'five': 5});

  for (var entry in myMap.entries) {
    print('${entry.key}: ${entry.value}');
  }

  // Iterate over keys
  for (var key in myMap.keys) {
    print('Key: $key');
  }

  // Iterate over values
  for (var value in myMap.values) {
    print('Value: $value');
  }

  //json to map
  // Sample JSON string
  String jsonString = '''
  {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "isVerified": true
  }
  ''';

  // Convert JSON string to Map
  Map<String, dynamic> userMap = jsonDecode(jsonString);

  print(
      userMap); // Output: {name: John Doe, age: 30, email: john.doe@example.com, isVerified: true}

  // Access values in the Map
  print("Name: ${userMap['name']}");
  print("Age: ${userMap['age']}");

  // Convert Map to JSON string
  String jsonString1 = jsonEncode(userMap);

  print(jsonString1);
}
