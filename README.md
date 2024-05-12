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
# 修改虚拟环境里的环境变量以引入不同文件夹的module路径（非必须，可用sys.path代替）
venv/Scripts/activate 文件：
export PYTHONPATH="$PYTHONPATH:/path/to/your/module"

# 安装项目依赖
pip install -r requirements.txt
# 开发项目代码
# 生成项目依赖
pip freeze > requirements.txt

### 退出虚拟环境
deactivate
```

### 开发项目代码，推送到远程仓库
可使用VSCODE 自带Source Control插件完成,虚拟环境如果没有命名成venv，请把对应名称添加至[项目忽略文件](.gitignore)，否则会上传至Gitlab项目文件夹


### 项目模拟数据集生成逻辑（待完善）

1. 针对 `Metadata_vars.json` 默认输出以第一个键为单位的数据集里的所有变量，组成一个数据集。即 `AE`, `DS`, `LB` 等等，需要一个模块让用户选择生成哪些数据集。

   - 第一行是 metadata 各个变量的名字。
   - 第二行是对应的 Variable Label。

2. 按照 metadata 约定的属性来生成变量，优先级如下：

   - 有 `Controlled Terms`, `Codelist` 或 `Format` 的
     - 若 `Controlled Terms`, `Codelist` 或 `Format` 为 ISO 8601 datetime 或 interval 的，生成符合这个标准的时间。
     - 若是 `COUNTRY` 变量，生成 ISO 3166-1 Alpha-3 标准的三位国家代码。
     - 随机生成 `Controlled Terms`, `Codelist` 或 `Format` 里的某个值。
     - 若 `Controlled Terms`, `Codelist` 或 `Format` 为空的，按照 Type 生成变量，`Char` 生成 `"NA"`, `Num` 生成 `"."`.

3. 完成上述步骤后，进一步对生成的数据集进行逻辑处理。需要使用另一个文件来约定这些受控术语缺失的应该生成什么。这一步将在另一个 `data_generator_2` 中完成。


## Pending Task 20240513
### data_generator_2 :
add another detaileed metadata file per Novartis stage/reference metadata, to add the information for Char/Num format and special values such as MedDRA,WHODrug

### data_generator_3 :
add another logic file to define the connection logic of the varibles within One dataset

### data_generator_4 :
add another logic file to define the connection logic with different datasets

### data_generator_5:
Wrong/right datasets

### data_generator_6:
CDASH/ADAM datasets

