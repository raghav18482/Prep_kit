mixin Musical {}

mixin Aggressive {}

mixin Demented {}

class Person {}

class Performer {}

class Musician extends Performer with Musical {
  // ···
}

class Maestro extends Person with Musical, Aggressive, Demented {
  String? name;
  bool? canConduct;

  Maestro(String maestroName) {
    name = maestroName;
    canConduct = true;
  }
}
