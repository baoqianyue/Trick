package com.nucandroid.extend.linkedlist;

import java.util.LinkedList;

public class LinkedListDemo {

    public static void main(String[] args) {
        LinkedList<String> queue = new LinkedList<>();
        queue.add("st1");
        queue.add("st2");
        queue.add("st3");
        queue.add("st4");
        queue.add("st5");

        //插入
        queue.offer("st6");
        //从头部删除
//        queue.poll();
        String str = queue.element();
        System.out.println(str);


        for (String str1 :
                queue) {
            System.out.println(str1);
        }
    }
}
