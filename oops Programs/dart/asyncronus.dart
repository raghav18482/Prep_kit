import 'dart:async';

void main() async {
  print('Fetching data...');

  // Call the asynchronous function and wait for it to complete
  String data = await fetchData();

  // Print the fetched data
  print('Data fetched: $data');
}

// Simulate an asynchronous operation using Future
Future<String> fetchData() async {
  // Simulate a network delay
  await Future.delayed(Duration(seconds: 2));

  // Return the simulated data
  return 'Hello, Dart!';
}
