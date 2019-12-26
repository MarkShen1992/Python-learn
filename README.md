## Python 学习笔记

### [Python官网]( https://www.python.org/ )

### 升级pip

```
python -m pip install --upgrade pip
```

### No module named 'pip'

```
python -m ensurepip包
```

### [包管理](https://pypi.org/)工具pip的使用

```
国内pypi镜像源
阿里云 https://mirrors.aliyun.com/pypi/simple
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple
豆瓣(douban) http://pypi.douban.com/simple
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple
中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple
华为云 https://mirrors.huaweicloud.com/repository/pypi/simple

# 修改默认的镜像源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### pip 常用命令

```
安装：pip install package-name
卸载: pip uninstall package-name
```

### pip帮助

```
pip -h # 查看pip的具体使用
```

### 开发IDE

- [VS Code]( https://code.visualstudio.com/ )

### 谈谈Python第三方库如何选择

- [pypi.org]( https://pypi.org/ )中第三方库的**Statistics**上Github的**Star**数和**Forks**数

- 第三方库的维护人数

- 第三方库文档写的怎么样

- 需要Python的版本

- 库的最近更新时间

  例子如这个第三方库 [PyMySQL](https://pypi.org/project/PyMySQL/)

