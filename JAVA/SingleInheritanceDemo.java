class Rectangle {
    double length, width;

    void getData(double l, double w) {
        length = l;
        width = w;
    }
}

class Area extends Rectangle {
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