package com.nucandroid.dataandvar;

public class DataType {

    /**
     * 标识符
     * 数字不能开头
     * 不能使用关键字
     */

    /**
     * 命名规范
     * 1.包名：全部小写
     * 2.类名和接口名：DataType
     * 3.变量名和函数名 驼峰式studyJavaAndPython()
     * 4.常量名：STUDY_TIME
     */

    /**
     * 数据类型
     * 1.基本数据类型
     * 2.引用型
     */

    byte a;
    short b;
    int c; //4字节 没有unsigned
    long d = 3l;
    float e = 3.0F;
    double f = 3.9d;
    char g = 'b';
    char u = '0';
    boolean h;//true false

    //常量
    private static final int STUDY_TIME = 1000;


    /**
     * 整数
     * 1.十进制 0-9
     * 2.二进制 0b1001
     * 3.八进制 0-7 034
     * 4.十六进制 0-9 A-F 0x56
     */

    public static void main(String[] args) {
        char name1 = '王';
        char name2 = '天';
        char name3 = '锐';
        System.out.println("我的名字是：" +
                name1 + name2 + name3);
    }

    /**
     * 数据类型的转换
     */
    short q = 3;
    int w = 4;
    float sum = (float)q + w;


    /**
     * 运算符
     * 1.&，| ~， << >>
     *
     */
//    a > 9 ? b = 1 : b= 0;


}
