class Student {
    String name = "Tom";
    int age = 18;

     

    void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }

    public static void main(String[] args) {
        Student student1 = new Student();
        System.out.println("Student 1 Info:");
        student1.displayInfo();

        Student student2 = new Student();
        student2.name = "Jerry";
        student2.age = 20;
        System.out.println("\nStudent 2 Info:");
        student2.displayInfo();
    }
}
