package com.nucandroid;

import com.nucandroid.entend.Employee;
import com.nucandroid.entend.Manager;

public class Main {

    public static void main(String[] args) {
        Manager m = new Manager("wang", 1, 8000, 1000);

        //向上转型  ： 用父类去引用子类的对象（会丢失子类的信息）
        Employee e1 = new Employee("wang", 1, 8000);
        Employee e = new Employee("wang", 1, 8000);
        System.out.println(e1.equals(e));



//        System.out.println(e1.getName());
//        System.out.println(e1.getSalary());
//        System.out.println(((Manager) e1).getBonus());

        //向下转型：  用子类去引用父类的对象
//        Manager m1 = (Manager) new Employee("wang", 1, 7000);

//        System.out.println(m.getSalary());
    }
}
