package com.nucandroid.classandobject;

//default
public class ClassDemo {

    /**
     * 面向对象
     * 1.成员变量
     * 2.成员方法
     * 3.类成员(static)
     * <p>
     * 对象（实例）instance
     */

    /**
     * 成员变量和局部变量
     */

    /**
     * 四种访问权限
     * 1.public
     * <p>
     * 2.protected(保护)
     * <p>
     * 3.private
     * <p>
     * 4.default(包)
     * interface
     *
     *
     *
     * 3
     *
     */

    public String name = "bao";
    private int age;



    public ClassDemo(String name) {
        this.name = name;
    }

    void display(ClassDemo p) {
        ClassDemo s = p;
        System.out.println(s.name);
        System.out.println(s.age);
    }


    ClassDemo(String name, int age) {
        this.name = name;
        this.age = age;
    }


    void show() {
        System.out.println("姓名：" +
                name + " 年龄：" + age);
    }


    public static void main(String args[]) {
        ClassDemo person = new ClassDemo("baoqianyue",
                21);
        System.out.println(person.name);
        //fp 函数式编程

//        new ClassDemo("baoqianyue", 20);

//        wang.number = "4342";
//        wang.lab = "android";
//        wang.sex = "";
    }
}
