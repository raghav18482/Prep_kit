void main() {
  String? name; // `name` can be null

  print('Name is null'); // Handles the case where `name` is null

  // Using the null-aware operator `?.`:
  print(name?.length); // This will print `null` if `name` is null, or the length if it's not null
}
