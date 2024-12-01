class Person {
  String name;
  Address address;

  Person(this.name, this.address);

  // Method to create a shallow copy
  Person shallowCopy() {
    return Person(this.name, this.address);
  }

  // Method to create a deep copy
  Person deepCopy() {
    return Person(this.name, Address(this.address.city, this.address.zip));
  }

  @override
  String toString() => 'Person(name: $name, address: $address)';
}

class Address {
  String city;
  String zip;

  Address(this.city, this.zip);

  @override
  String toString() => 'Address(city: $city, zip: $zip)';
}

void main() {
  // Original object
  Address address = Address('New York', '10001');
  Person original = Person('Alice', address);

  // Shallow copy
  Person shallowCopiedPerson = original.shallowCopy();
  // Deep copy
  Person deepCopiedPerson = original.deepCopy();

  // Print initial states
  print('Original: $original');
  print('Shallow Copy: $shallowCopiedPerson');
  print('Deep Copy: $deepCopiedPerson');

  // Modify the address of the original person
  original.address.city = 'Los Angeles';

  print('\nAfter modifying original address:');
  print('Original: $original');
  print('Shallow Copy: $shallowCopiedPerson'); // Affected by change
  print('Deep Copy: $deepCopiedPerson'); // Not affected by change
}
