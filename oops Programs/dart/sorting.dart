class Person {
  String name;
  int age;

  Person(this.name, this.age);

  @override
  String toString() => '$name ($age)';
}

void main() {

List<Person> people = [
    Person('Alice', 25),
    Person('Bob', 30),
    Person('Charlie', 20),
  ];

  List<int> numbers = [5, 2, 9, 1, 5, 6];
  
  // Sorting in ascending order
  numbers.sort();
  print('Ascending: $numbers');
  
  // Sorting in descending order
  numbers.sort((a, b) => b.compareTo(a));
  print('Descending: $numbers');


  // Sorting by age (ascending)
  people.sort((a, b) => a.age.compareTo(b.age));
  print('Sorted by age: $people');
  
  // Sorting by name (alphabetical order)
  people.sort((a, b) => a.name.compareTo(b.name));
  print('Sorted by name: $people');

}