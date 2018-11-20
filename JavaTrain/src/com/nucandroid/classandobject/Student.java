package com.nucandroid.classandobject;

/**
 * bean
 */
public class Student {

    private String number;

    private String lab;

    private String sex;

    public Student(String lab) {
        this.lab = lab;
    }

    public Student(String lab, String sex) {
        this(lab);
        this.sex = sex;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public void setLab(String lab) {
        this.lab = lab;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public String getSex() {
        return sex;
    }

    public String getNumber() {
        return number;
    }

    public String getLab() {
        return lab;
    }
}
