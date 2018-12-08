package com.nucandroid.extend.arraylist;

import java.util.*;

public class ArrayListDemo {
    public static void main(String[] args) {
        List<Person> personList = new ArrayList<>();
        List<Person> additionList = new ArrayList<>();
        Person wang = new Person("wangtianrui", 25);

        personList.add(wang);
        personList.add(new Person("bao", 21));
        personList.add(new Person("赵励志", 21));
        personList.add(new Person("masuqin", 20));
        personList.add(new Person("李浩", 28));
        personList.add(new Person("王皓", 21));
        personList.add(new Person("xiangyi", 28));

        additionList.add(new Person("jiangyuwei", 21));
        additionList.add(new Person("tanzhuo", 28));

        personList.addAll(additionList);


        //1.迭代器
       /* Iterator iterator = personList.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }*/

        //2.for循环
       /* for (int i = 0; i < personList.size(); i++) {
            System.out.println(personList.get(i));
        }*/

        //3.for each
        /*for (Person p :
                personList) {
            System.out.println(p);
        }*/

        /*int[] arr = {1, 2, 3};
        for (int i :
                arr) {
            System.out.println(i);
        }*/


        for (Person p :
                personList) {
            System.out.println(p);
        }

       /* List<Person> subList =
                personList.subList(0, 2);
        for (Person p :
                subList) {
            System.out.println(p);
        }*/

//        Collections.sort(personList);

        personList.sort(new Comparator<Person>() {
            @Override
            public int compare(Person o1, Person o2) {
                return Integer.compare(o1.getAge(), o2.getAge());
            }
        });

        System.out.println("-------排序后-------");
        for (Person p :
                personList) {
            System.out.println(p);
        }
    }
}
