Project Overview
================
[Project Structure](<docs/Project Structure.MD>)

[Create Structure for branches (Not Recommended, we can fork the branch by checkout from the existing branch)](scripts/create_project_structure.py)


### 安装Python，设置环境变量
# 下载Python安装程序，安装Python
# 设置环境变量
# Python 本机安装路径

将安装路径填入环境变量

![环境变量 Step 1](<docs/Project instruction/image.png>)
![环境变量 Step 2](<docs/Project instruction/image-1.png>)

成功加入环境变量后可以查询
```bash
where Python
```
![安装路径](<docs/Project instruction/image-2.png>)

### 安装Git，设置Global用户名及邮箱

# 下载Git安装程序，安装Git
```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```
# Git常用指令
[Git Cheatsheet](<docs/Git Knowledge Sharing/git-cheat-sheet-education.pdf>)

### Clone项目至VS Code

# 通过Git克隆项目
```bash
git clone ssh://git@ssh-gitlabce.apps.dit-prdocp.novartis.net:32222/dos/ddf.git
```

### Check out至DEV分支

# 切换到DEV分支
```bash
git checkout develop
```

### 安装虚拟环境及项目依赖
```bash
# 创建虚拟环境
python -m venv venv
# 激活虚拟环境
venv\Scripts\activate
# 安装项目依赖
pip install -r requirements.txt
```

### 退出虚拟环境
```bash
deactivate
```

### 开发项目代码，推送到远程仓库
可使用VSCODE 自带Source Control插件完成,虚拟环境如果没有明明成venv，请把对应名称添加至[项目忽略文件](.gitignore)，否则会上传至Gitlab项目文件夹