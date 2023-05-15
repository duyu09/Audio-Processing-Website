## Audio Processing Website

- 项目名称：基于DAPC的音频音效处理系统网站(源代码)。
- 项目技术栈：
- - DAPC核心由Python语言编写，基于Numpy与Scipy库，音频编解码基于FFMPEG，调速处理基于SONIC。DAPC相关代码及详细内容参见"Duyu Audio Processor Core"仓库。
- - 后端基于Python Flask框架编写。
- - 前端由静态HTML5+ElementUI编写，项目前端目前采用CSR架构。

## 更新日志

### Update on December 24th, 2022

初步完成了前端代码和后端代码的编写，为v1.0版本。运行前，请解压/v1.0/static/lib/libs.zip里的库文件到当前目录(即：/v1.0/static/lib)

### Update on May 16th, 2023

简单优化了UI和后端逻辑，前端通过轮询的方式判断音频在后端的处理情况，是为创新点。后端对文件名的处理以及高并发仍然有问题，留给后续版本修复。

### 著作权声明

&copy; 2020~2023 Duyu09, Faculty of Computer Science and Technology, Qilu University of Technology.

<img src="https://github.com/duyu09/Audio-Processing-Website/assets/92843163/b1ba666d-840c-4365-8975-65a33b8d7517" style="width:25%">

齐鲁工业大学 计算机科学与技术学部 Duyu(No.202103180009). 保留所有权利。


