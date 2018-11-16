import java.util.Arrays;

import week01.extendAndInterface.Employee;
import week01.extendAndInterface.Manager;

public class Main {
    public static void main(String[] args) {
        Employee employee = new Employee("Rick", 1, 7000);
        Employee employee2 = new Employee("Rick2", 1, 8000);

        Manager manager = new Manager("SuperRick", 1, 7000, 5000);
        Manager manager2 = new Manager("SuperRick2", 1, 7000, 7000);


        Employee[] employeeList = {employee2, employee};
        Manager[] managerList = {manager2, manager};

        Arrays.sort(employeeList);
        System.out.println(Arrays.toString(employeeList));

        Arrays.sort(managerList);
        System.out.println(Arrays.toString(managerList));


        /*//向上转型会丢失子类比父类多出的信息
        Employee e = new Manager("SuperRick", 1, 7000, 5000);
        e.getName();
        ((Manager) e).getBonus();

        //向下转型会报错
        //所以在对对象进行强转时,要先判断一下能不能转换

        System.out.println(manager instanceof Employee); //True,子类可以视为父类对象
        System.out.println(employee instanceof  Manager); //False,父类不能视为子类对象

        //向下转型前进行判断
        if (employee instanceof Manager) {
            Manager m = (Manager) employee;
        } else {
            System.out.println("not same instance");
        }*/
    }
}