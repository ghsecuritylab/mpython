# 显示48x48点阵字
* 用[字模软件](http://d1.amobbs.com/bbs_upload782111/files_10/ourdev_332703.rar)生成48x48字模
* 生成的字模保存到txt文件
* 然后在程序中读取txt文件
* 要把txt文件复制到ESP32硬件上
## 核心
核心就是把得到的txt文件读取并转换成10序列，最后把10转换为点阵字。
