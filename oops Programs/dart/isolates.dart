import 'dart:isolate';

void main() async {
  // Create a ReceivePort to receive messages from the isolate
  final receivePort = ReceivePort();

  // Spawn an isolate and pass the ReceivePort's sendPort to it
  final isolate = await Isolate.spawn(backgroundIsolate, receivePort.sendPort);

  // Listen for messages from the isolate
  receivePort.listen((message) {
    print('Received from isolate: $message');
    receivePort.close();
    isolate.kill(priority: Isolate.immediate);
  });
}

void backgroundIsolate(SendPort sendPort) {
  // Perform some background work
  final result = 'Hello from background isolate';

  // Send the result back to the main isolate
  sendPort.send(result);
}
//They allow you to run code in parallel, separate from the main thread, which can improve performance and responsiveness in your application.