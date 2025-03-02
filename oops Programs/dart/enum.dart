enum DayOfWeek {
  monday,
  tuesday,
  wednesday,
  thursday,
  friday,
  saturday,
  sunday;
  
  bool get isWeekend {
    return this == saturday || this == sunday;
  }
}

void main() {
  DayOfWeek today = DayOfWeek.saturday;
  
  if (today.isWeekend) {
    print('$today is a weekend.');
  } else {
    print('$today is a weekday.');
  }

    for (var day in DayOfWeek.values) {
    print(day);
  }
}
