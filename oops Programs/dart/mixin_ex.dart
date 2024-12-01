//Use the on clause to declare a superclass

class Musician {
  musicianMethod() {
    print('Playing music!');
  }
}

mixin MusicalPerformer on Musician {
  performerMethod() {
    print('Performing music!');
    super
        .musicianMethod(); // The super keyword is used to denote the instant parent class object of the current child class.
  }
}

class SingerDancer extends Musician with MusicalPerformer {}

main() {
  SingerDancer().performerMethod();
}

//Multiple inheritances are not supported by Dart. 
//Thus, we need mixins to implement multiple inheritances in Flutter/Dart. 
//The use of mixins makes it easy to write reusable class code in multiple class hierarchy levels. 
//Mixins can also be used to provide some utility functions (such as RenderSliverHelpers in Flutter). 


