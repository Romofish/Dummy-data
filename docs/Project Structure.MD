# Project Structure

- `/frontend` - 前端应用文件夹，存放所有前端代码和资源。
  - `/src` - 前端源代码。
  - `/public` - 公共资源如HTML入口文件、图标等。
- `/backend` - 后端应用文件夹，使用Python编写。
  - `/app` - 主应用逻辑。
    - `/api` - API接口相关代码。
    - `/services` - 后端服务逻辑，如数据处理和生成。
    - `/models` - 数据模型。
  - `/tests` - 测试代码。
- `/data_generation` - 数据生成逻辑模块。
  - `/generator` - 数据生成算法实现。
  - `/config` - 生成数据的配置文件或脚本。
- `/metadata` - 存放数据定义和属性的文件夹。
  - `/definitions` - 数据字段和类型定义。
- `/data_storage` - 数据存储模块。
  - `/database` - 如果使用数据库，此处为数据库文件或数据库迁移脚本。
  - `/files` - 如果使用文件系统存储，此处存放生成的数据文件。
- `/docs` - 项目文档，如API文档、开发指南等。
- `/scripts` - 用于项目维护的脚本，如数据库迁移。
- `README.md` - 项目概述文件。
- `.gitignore` - Git忽略配置文件。
- `requirements.txt` - Python依赖文件。




# Git Branch Structure

- `main` - 主分支，保持始终可部署的状态，所有的发布版本都从这个分支进行。
- `develop` - 开发主分支，用于日常开发的集成和测试。
  - `feature/*` - 特性分支，每个新功能或改进从`develop`分支检出，并在完成后合并回`develop`。
    - `feature/add-user-authentication` - 示例：添加用户认证功能。
    - `feature/improve-data-generation` - 示例：改进数据生成逻辑。
  - `release/*` - 发布准备分支，用于准备发行版，进行最后的测试和调整。
    - `release/1.0.0` - 示例：准备1.0.0版本的发行。
  - `hotfix/*` - 紧急修复分支，用于快速解决生产环境的问题。
    - `hotfix/fix-data-error` - 示例：修复数据错误问题。