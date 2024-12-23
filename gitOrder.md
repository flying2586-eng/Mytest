### 基本命令

`git add` 添加文件到缓存信息
    添加所有命令    `git add .`
    添加某一类文件  `git add *.py`
    **当添加了文件后又修改了文件本身内容，需要再次执行添加命令**

`git reset HEAD`    取消已缓存的内容
    `git reset HEAD test.txt`

`git commit` 提交命令
    将缓存区内容添加到仓库  `git commit -m "第一次版本提交"`
    缓存并提交  `git commit -am "第一次提交"`

`git status` 查看相关文件的状态 只显示状态，不显示详细信息

`git diff` 查看更新的详细信息
- 尚未缓存的改动    `git diff`
- 查看已缓存的改动  `git diff --cached`
- 查看已缓存的与未缓存的所有改动    `git diff HEAD`
- 显示摘要而非整个diff  `git diff --stat`

`git rm`    删除文件
- `git rm <file>`   也就是说但从工作目录手动删除还不行，要从git中移除这个文件 要从已跟踪文件清单中移除，然后移交
- 删除之前修改过并且已经放在暂存区域 **这会删除当前文件**   `git rm -f <file>`
- 将文件从暂存区域移除，但希望保留在当前工作目录中  `git rm --cached <file>`

`git mv`    用于移动或重命名一个文件、目录、软连接
    将test.txt重命名为newtest.txt   `git mv test.txt newtest.txt`

### 分支管理

`git branch`    查看分支命令

`git branch (branchname)`   创建分支命令
    `git branch main`   创建main分支

`git checkout (branchname)` 切换分支

`git merge (branchname)`    将任意分支合并到当前分支
    `git merge newtest` 在test分支下使用该命令将newtest的修改内容合并到test中

`git branch -d (branchname)`    删除分支

### Git查看提交历史

`git log`   查看提交历史
+ `--oneline` 查看看历史记录的简介版本
+ `--graph`   查看历史中什么时候出现了分支、合并
  
### Git标签

`git tag`   查看所有标签

+ 还能没发布的情况下
  `git tag -a v1.0` 创建v1.0的标签

+ 已经发布的情况下，追加标签
    `git log --oneline` 查看提交信息（例如：fe7f362）
    `git ta -a v0.0 fe7f362`    打标签v0.0 进入vim界面后 需要把`#`删除

### 远程仓库

`git remote add`    添加远程仓库
    `git remote add [alias] [url]`  `[alias]`是别名，`[url]`是远程仓库的地址

`git remote`    查看当前有哪些远程仓库

`git fetch` 提取远程仓库的数据，如果有多个远程仓库，在后面加上仓库的别名
    `git fetch origin` origin是当前仓库的别名
    在这之后，执行`git merge`命令合并到当前分支

`git pull`  用于从另一个存储库或本地分支拉取并集成
    可以将远程仓库pull到本地，如果本地仓库和远程仓库实际上是独立的两个仓库， `git pull test master –-allow-unrelated-history`

`git push`  推送你的新分支与数据到某个远程仓库命令
    `git push [alias] [branch]`
    `git push -u origin main`

`git remote rm` 删除远程仓库
    `git remote rm [alias]`
