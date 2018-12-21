# Unity3D    

## 3D模型美化     

### 材质球和贴图   

* Material     

    物体的质地      
    文件后缀`.mat`    

* Texture    

    普通的图片,用于材质球的显示    

* 编辑材质球    
 
    * 选中要编辑的材质球,点击Inspector中的`Albedo`(纹理贴图即漫反射贴图),在弹出的texture界面中选择相应的贴图   

    * `Tiling`选项用来调整贴图分几块显示    


### 着色器Shader   

通过Shader来编辑材质球的效果      


### 预制体Prefab    

可以重复利用的物体     
 
文件后缀`.prefab`      

当场景中同时存在很多同一种预制体时,对其中一个进行编辑,然后点击该预制体的`Inspector`面板中的`Prefab`栏中的apply,就可以将刚才做出的修改应用到场景中所有的同类预制体上      


### 摄像机Camera    

相当于观察坐标系,观察区间有一个视锥体,所有在视锥体范围内的物体,在game视图下都能看到   

* Align with view   

    使摄像机位置直接定位到当前观察位置    

    快捷键**ctrl + shift + f**    

* 摄像机相关属性(Inspector面板中)      

    * Clear Flags 清除标记   
        指当前场景外部使用什么内容来包围,默认为Skybox(天空盒),也可以使用Solid Color(纯色),然后再Background选项中选择颜色    

    * Projection 投影模式    

        * Perspective 透视模式,3D场景使用   

        * Orthographic 正交模式,2D场景使用      

    * Clipping Planes 切割面   

        * Near 近切割面   

        * Far  远切割面   


### 灯光Light   

照亮当前Scene,使场景中产生阴影,增强立体感和真实感     

#### 方向光Directional Light   

用于模拟太阳光,自然光    
方向光可以照射到任何地方,即使在一个物体的背面,也会有太阳光的反射效果       

#### 点光源Point Light   

从一个点中心向四周发散光     

* Range属性    

    指定一个球体范围,该球体就是点光源的光发散范围    

#### 聚光灯Spot Light   

照射范围是一个圆锥体     

* Range属性   

    指定圆锥体的大小     

* Spot Angle聚光角    

    指定聚光灯圆锥体的伸展角度  

#### 灯光的属性   

* 类型Type     

    切换灯光的属性   

* 颜色Color   

    设置灯光的颜色   

* 强度Intensity     

    设置灯光的照射强度    

* 阴影类型 Shadow Type     

