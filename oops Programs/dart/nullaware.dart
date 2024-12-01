void main() {
  String? name; // `name` can be null

  if (name != null) {
    print(name.length); // Safe to access `length` because `name` is not null
  } else {
    print('Name is null'); // Handles the case where `name` is null
  }

  // Using the null-aware operator `?.`:
  print(name
      ?.length); // This will print `null` if `name` is null, or the length if it's not null
}
