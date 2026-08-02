class Circle {
    double radius;

    double area() {
        return 3.14 * radius * radius;
    }

    double perimeter() {
        return 2 * 3.14 * radius;
    }
}

public class CircleMain {
    public static void main(String[] args) {
        Circle c = new Circle();
        c.radius = 5;
        System.out.println("Area= " + c.area());
        System.out.println("Perimeter= " + c.perimeter());
    }
}