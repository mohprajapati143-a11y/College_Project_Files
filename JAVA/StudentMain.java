class Student {
    String name;
    int age;

    Student(String n, int a) {
        name = n;
        age = a;
    }

    void display() {
        System.out.println("Name:" + name);
        System.out.println("Age:" + age);
    }
}

public class StudentMain {
    public static void main(String[] args) {
        Student s = new Student("Mohit", 21);
        s.display();
    }
}