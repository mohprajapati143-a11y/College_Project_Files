class Demo {
    private int x, y, z;

    public void input() {
        x = 10;
        y = 15;
    }

    public void sum() {
        z = x + y;
    }

    public void print_data() {
        System.out.println("Answer is = " + z);
    }

    public static void main(String args[]) {
        Demo object = new Demo();
        object.input();
        object.sum();
        object.print_data();
    }
}