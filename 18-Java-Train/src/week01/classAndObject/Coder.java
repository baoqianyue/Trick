package week01.classAndObject;

/**
 * 演示private和protected权限修饰符
 */
public class Coder extends Person {
    /**
     * 构造方法没有返回值
     * 方法名与类名一致
     *
     * @param name1
     * @param age1
     */
    Coder(String name1, int age1) {
        super(name1, age1);
        this.protectedName = name1;
        Person.protectedStaName = name1;
    }

    public static void main(String[] args) {
        Book book = new Book();
        //在其他类中可以直接访问到实体类中public修饰的属性
        book.publicName = "name";
        //无法访问private修饰的，只能通过访问它们的getter和setter方法
        String name = book.getName();
        book.setName(name);
    }
}
