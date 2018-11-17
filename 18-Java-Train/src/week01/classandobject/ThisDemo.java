package week01.classandobject;

/**
 * 演示this关键字
 */
public class ThisDemo {

    private String name;

    private int age;

    public ThisDemo(String name) {
        this.name = name;
    }


    //当构造函数要完成的任务较多时，而且需要对构造函数进行重载时
    //可以使用this在构造函数调用其他构造函数
    public ThisDemo(String name, int age) {
        //this调用构造函数只能放在第一行
        this(name);
        this.age = age;
        this.show();
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        //这里使用this会将局部变量和成员变量区分开
//        name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void show() {
        //这里访问的其实是当前对象的属性
        //在每个属性前都默认有一个this
        System.out.println("姓名是: " + this.name + " 年龄是: " + age);
    }

    public static void main(String[] args) {
        new ThisDemo("b", 20);
    }
}
