//Adding optional parameter in dart function
void main() {
  fetchData();
  fetchData(ans: 'raghav');
}

// Simulate an asynchronous operation using Future
void fetchData({String ans = 'name'}) {
  print(ans);
}
