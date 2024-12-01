//Here's an example that demonstrates how to use async/await alongside .then() for handling asynchronous operations:

import 'dart:async';

void main() {
  print('Fetching data...');

  // Call the asynchronous function and handle the result using .then()
  fetchData().then((data) {
    // This block of code runs when fetchData() completes
    print('Data fetched: $data');
  }).catchError((error) {
    // This block of code runs if fetchData() encounters an error
    print('Error: $error');
  });

  print('Waiting for data...');
}

// Simulate an asynchronous operation using Future
Future<String> fetchData() {
  // Simulate a network delay
  return Future.delayed(Duration(seconds: 2), () {
    // You can simulate an error by uncommenting the next line:
    // throw Exception('Failed to fetch data');
    return 'Hello, Dart!';
  });
}
