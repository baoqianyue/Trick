package com.nucandroid.extend.arraylist;

public class Person implements Comparable {

    private String name;

    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }

    /**
     * 根据年龄比较
     *
     * @param o
     * @return
     */
    @Override
    public int compareTo(Object o) {
        Person temp = (Person) o;
        if (this.getAge() > temp.getAge())
            return 1;
        else
            return -2;
    }
}
