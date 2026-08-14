class Rectangle {
    public static final int height = 0;
    public static final int x = 0;
    double length, width;
    public int y;

    Rectangle(int playerX, int playerY, int playerSize, int playerSize2) {
        // Default constructor
    }

    void getData(double l, double w) {
        length = l;
        width = w;
    }

    public boolean intersects(Rectangle enemy) {
        throw new UnsupportedOperationException("Unimplemented method 'intersects'");
    }
}

class Area extends Rectangle {
    Area() {
        super(0, 0, 0, 0);
    }

    double findArea() {
        return length * width;
    }
}

public class SingleInheritanceDemo {
    public static void main(String[] args) {
        Area obj = new Area();
        obj.getData(10, 5);
        System.out.println("Area of Rectangle = " + obj.findArea());
    }
}
