# face_id_engineer_homework
一级工程实践大作业人脸识别打卡

###　基本实施计划：  
--- 时间：11月24日 - 12月22日一共四周时间  
--- 功能：人脸信息入库 + 人脸识别。（摄像头和语音先不搞，最后如果时间充裕再加上）  
--- 计划：分四周来完成  
--- 第一周：11.24-12.01  
目标：使用 QTDesigner拖拽出来一个基本的界面。  
--- 第二周：12.01 - 12.08  
目标：人脸图片入库 + 人脸识别功能实现  
--- 第三周：12.08 - 12.15   
目标：调试bug，制作答辩ppt  
--- 第四周：12.15 - 12.22   
目标：摄像头和语音合成功能。能搞完最好，搞不完就按之前的功能来提交作业。  

第一周具体事项：12.01（下周日中午1:30-3:00，一起把这周目标收尾）  
--- 准备设备：电脑一台  
--- 准备环境：  
python3.7（至少3.5以上版本）下载、安装和配置  
pyCharm下载、安装（百度一下破解码，也可到官网使用北航邮箱注册学生账号）  
PyQt5和pyqt5-tools安装及集成到pyCharm：（以下链接为windows环境下参考）  
--- 安装：https://www.cnblogs.com/lsdb/p/9121903.html  
--- 基本使用：https://www.cnblogs.com/lsdb/p/9122425.html  
--- 知识学习：  
python3基本语法：http://code.py40.com/python3/  
PyQT5入门：http://code.py40.com/pyqt5/  
--- 使用QTDesigner开发  
界面设计：  
--- 录入按钮：选择图片，图片展示，姓名输入框  
--- 人脸打卡按钮：选择图片，图片展示，识别结果展示  
界面实现  
--- 收尾总结  
12.01日中午1:30（地点再定）自带电脑，一起把设计好的界面实现  

第二周具体事项：  
--- 建库  
--- 完成  

第四周：  
--- 调试bug  
--- ppt  
--- 答辩  


* 关于打包
```
pyinstaller -F -w -i img.ico main.py
或
pyinstaller -F -c -i img.ico main.py
(建议先用-c，这样如果打包不成功的话可以看到哪里有错）
```
> -F 指只生成一个exe文件，不生成其他dll文件  
> -w 不弹出命令行窗口  
> -i 设定程序图标 ，其后面的ico文件就是程序图标  
> main.py 就是要打包的程序  
> -c 生成的exe文件打开方式为控制台打开。  