# Tensorflow安装踩坑记   
Tensorflow是谷歌研发的第二代人工智能学习系统，之前只支持Linux和Mac OS环境，现在在Windows上也可以运行，不过运行条件十分苛刻，必须，注意是必须要求Python 3.5.0(64bit)版本，先前自己装的时候试过3.6版本的，也试过32位的，都不支持，真的是踩了好多坑。
* 1 下载Python     
 * 有可能你到了Python下载官网后，你还是找不到该下的版本，极有可能下载成32位的，所以我这里直接放一个链接，直接下载就行了，避免踩坑。    
 [Python 3.5.0 64位](https://www.python.org/ftp/python/3.5.0/python-3.5.0-amd64.exe)     
 * 然后进行python的安装    
 ![](http://p1.bpimg.com/567571/a86ba0730b6f26d1.png)   
 这里先要把最下面的**Add Python 3.5 to PATH**这个框选了，这样就会自动将系统环境变量配置好，省去了一个大步骤。然后点击Customize installation进行自定义安装。          
 ![](http://i1.piimg.com/567571/62c6783bea203476.png)

 这里建议全选，它会将一些常用的Python库直接安装好，尤其是Tensorflow需要的pip，点击下一步     

 ![](http://p1.bpimg.com/567571/a23446f568bc9e12.png)   
 这里反正我是全选了，具体各项什么含义也不太清楚，改一下安装路径就直接安装了      
 可能需要5到6分钟的时间。   


* 2 安装Tensorflow    
  * 打开命令行    
  先输入    
```
  python --version
```    
如果返回版本号是Python 3.5.0就可以进行下一步了    
 * 输入    
 ```
 python -m pip install --upgrade pip
 ```
 这一步是将pip更新到最新版本，如果你前面安装正确的话是不用更新的   
 会返回
 ```
 Requirement already up-to-date: pip in d:\python3.5\lib\site-packages
 ```   
 然后可以进行下一步了。  
 * 如果安装cpu版本的话输入     
 ```
 pip install --upgrade tensorflow  
 ```
 如果电脑是N卡的话就可以装Gpu版本，输入   
 ```
 pip install --upgrade tensorflow-gpu    
 ```    
 然后就开始安装，如果出现下面的情况就基本成功了，我们可以测试一下   
 ![](http://p1.bqimg.com/567571/74e48d46f55ba14d.png)     

* 3 测试    
 在Python下输入下面的语句   
 ```python3
 $ python
...
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
 ```      
 如果能够输出'Hello, TensorFlow!'像下面这样就代表配置成功了   
 ![](http://p1.bqimg.com/567571/64f2e35535f21dfe.png)  
 这样你就可以学习TensorFlow了，加油吧~
