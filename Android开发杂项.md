## 各种小知识点     

* Activity的屏幕方向设定      

    在Manifest文件中对应的Activity中设置：      
    `android:screenOrientation="portrait`        
    这里设置为portrait表示该Activity始终保持竖屏，不随着手机现状改变而改变屏幕方向       

* Activity的键盘弹出模式      

    在Manifest文件中对应的Activity中设置：    
    `android:windowSoftInputMode="adjustPan|stateHidden"`          
    这里`adjustPan`模式适用于界面中没有滑动控件，但是无法放下键盘，这时如果弹出了键盘，系统就会将状态栏向上部隐藏，为键盘空出空间        
    `stateHidden`模式表示不论当前是否有输入的需求，键盘始终是保持隐藏的       
    [参考资料](https://blog.csdn.net/zhaokaiqiang1992/article/details/39761461)        

* Fragment的切换方式     

    * add，remove，replace方式     

        * replace相当于先add然后remove     

        * replace    
            会先将fragment栈中所有内容先清空，然后将指定的fragment添加进去      
            replace方式始终会保持fragment栈中只有一个fragment实例     


    * hide，show方式        

        * 比较消耗内存，不会销毁栈中已有的fragment     


    * attach，detach方式         

        * detach模式也不会销毁fragment，但是会销毁该fragment上挂载的view        
        * attach负责将fragment上的view重新构建出来     



    

    