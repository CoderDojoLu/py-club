// public == access modifier -> class is accessible to the entire application
// name of classes have per definition an upper-case letter.
/*
*
* Multi line comments
*
*
*/
public class HelloWorld {
  // static vs. member methods of the class NOT an instance of the class
  // void == means doesn't return a value
  // main == main method (required) that gets run automatically (per default)
  // name of method (aka functions, but in OO talk referred to as methods) + arguments = Method signature
  // main method signature receives an array of string values

  public static void myWorld() {
    System.out.println("My World rocks");
  }

  public static void main(String[] args) {
    System.out.println("Hello");
  }
}

