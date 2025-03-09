class OverloadExample {
    void show(int a) {
        System.out.println("One parameter: " + a);
    }
    void show(int a, int b) {
        System.out.println("Two parameters: " + a + ", " + b);
    }
    public static void main(String[] args) {
        OverloadExample obj = new OverloadExample();
        obj.show(10);
        obj.show(10, 20);
    }
}

class OverloadExample {
    void show(int a) {
        System.out.println("Integer parameter: " + a);
    }
    void show(double b) {
        System.out.println("Double parameter: " + b);
    }
    public static void main(String[] args) {
        OverloadExample obj = new OverloadExample();
        obj.show(10);
        obj.show(10.5);
    }
}