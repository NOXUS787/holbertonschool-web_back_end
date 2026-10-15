# ES6 Classes

This project covers ES6 classes: defining a class, adding methods and
static methods, extending a class, and metaprogramming with symbols. It uses
Jest for tests and ESLint (Airbnb rules) for linting.

## Files

| File | Description |
| --- | --- |
| `0-classroom.js` | `ClassRoom` class that stores `maxStudentsSize` in `_maxStudentsSize`. |
| `1-make_classrooms.js` | `initializeRooms` returns three `ClassRoom` objects of sizes 19, 20 and 34. |
| `2-hbtn_course.js` | `HolbertonCourse` class with type-checked getters and setters. |
| `3-currency.js` | `Currency` class with getters, setters and `displayFullCurrency`. |
| `4-pricing.js` | `Pricing` class with getters, setters, `displayFullPrice` and static `convertPrice`. |
| `5-building.js` | Abstract-style `Building` class that requires subclasses to define `evacuationWarningMessage`. |
| `6-sky_high.js` | `SkyHighBuilding` extends `Building` and overrides `evacuationWarningMessage`. |
| `7-airport.js` | `Airport` class whose default string description is its code, using `Symbol.toStringTag`. |
| `8-hbtn_class.js` | `HolbertonClass` that casts to its size as a Number and its location as a String, using `Symbol.toPrimitive`. |
| `9-hoisting.js` | Fixes a hoisting bug by declaring classes before they are used, plus other bugs. |
| `10-car.js` | `Car` class whose `cloneCar` returns a new object of the same class, using `Symbol.species`. |
| `10-car.js` | `Car` class whose `cloneCar` returns a new object of the same class, using `Symbol.species`. |
