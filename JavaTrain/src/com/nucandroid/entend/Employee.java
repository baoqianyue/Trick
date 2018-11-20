package com.nucandroid.entend;

public class Employee extends Person{ // 员工
    private int salary;

    public Employee(String name, int sex, int salary) {
        super(name, sex);
        this.salary = salary;
    }

    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }

    /**
     * 同名方法重载
     * @param salary 底薪
     * @param pyDeal 通过帮别人写python获得的补贴
     */
    public void setSalary(int salary, int pyDeal) {
        this.salary = salary + pyDeal;
    }


    @Override
    public String getDescription() {
        return getName() + "性别：" + getSex() + getSalary();
    }

    @Override
    public String toString() {
        System.out.println("在这里调用toString");
        return getDescription();
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;//如果引用相同
        if(obj == null) return false;
        if(getClass() != obj.getClass()) return false;

        Employee other = (Employee) obj;
        return this.getName() == other.getName()
                && this.getSalary() == other.getSalary()
                && this.getSex() == other.getSex();
    }

}
