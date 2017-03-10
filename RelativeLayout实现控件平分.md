# 实现控件平分    
使用LinearLayout的layout_weight属性可以将两个或多个控件实现平分，像下图这样：   
![](http://p1.bpimg.com/567571/d4993b7acca55e4b.png)    
但是往往这种形式的平分只能在一个LinearLayout实现中，如果父布局是RelativeLayout，就会在加载时增加渲染压力。  
## 使用RelativeLayout实现上图中的效果   
```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent">

    <Button
        android:id="@+id/world"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentRight="true"
        android:layout_alignTop="@+id/hello"
        android:layout_toRightOf="@id/view"
        android:text="world" />

    <View
        android:id="@+id/view"
        android:layout_width="0dp"
        android:layout_height="1dp"
        android:layout_centerHorizontal="true" />
    <Button
        android:id="@+id/hello"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentLeft="true"
        android:layout_toLeftOf="@id/view"
        android:text="hello"/>

</RelativeLayout>


```
* layout_alignTop:将控件的上边缘与给定ID的控件上边缘对齐   
* layout_centerHorizontal:将控件置于水平方向的中心位置   
