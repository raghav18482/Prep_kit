import 'dart:async';

void main() {
  // Create a StreamController
  final streamController = StreamController<int>();

  // Add some data to the stream
  streamController.add(1);
  streamController.add(2);
  streamController.add(3);

  // Close the stream to indicate no more data will be added
  streamController.close();

  // Listen to the stream
  streamController.stream.listen(
    (data) {
      print('Received: $data');
    },
    onDone: () {
      print('Stream is closed');
    },
  );

  // Create a periodic stream that emits an integer every second
  final stream = Stream.periodic(Duration(seconds: 1), (count) => count);

  // Listen to the stream and print each item
  stream.take(5).listen((data) {
    print('Periodic data: $data');
  });
}
