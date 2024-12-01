// Parent class (Base class)
class Animal {
  String _name; // Private variable

  // Constructor
  Animal(this._name);

  // Getter for the private variable
  String get name => _name;

  // Public method
  void makeSound() {
    print('Some generic animal sound');
  }
}

// Child class (Derived class)
class Dog extends Animal {
  String breed;

  // Constructor
  Dog(String name, this.breed)
      : super(name); // Call the parent class constructor

  // Overriding the parent class method
  @override
  void makeSound() {
    print('$name says: Woof! Woof!');
  }

  // New method in the child class
  void showBreed() {
    print('$name is a $breed.');
  }
}

void main() {
  // Creating an instance of the Dog class
  Dog dog = Dog('Buddy', 'Golden Retriever');

  // Accessing the public method of the parent class
  dog.makeSound(); // Output: Buddy says: Woof! Woof!

  // Accessing the method from the child class
  dog.showBreed(); // Output: Buddy is a Golden Retriever.

  // Accessing the private variable through a getter
  print('Dog\'s name is ${dog.name}.'); // Output: Dog's name is Buddy.
}
