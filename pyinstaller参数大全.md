通常命令
`pyinstaller myscript.py`

-----
通用参数
|参数名|描述|说明|
|:----:|:----:|:----:|
|-h|显示帮助|无|
|-v|显示版本号|无|
|--distpath|生成文件放在哪里|默认：当前目录的dist文件夹内|
|--workpath|生成过程中的中间文件放在哪里|默认：当前目录的build文件夹内|
|-y|如果dist文件夹内已经存在生成文件，则不询问用户，直接覆盖|默认：询问是否覆盖|
|--upx-dir UPX_DIR|指定upx工具的目录|默认：execution path|
|-a|不包含unicode支持|默认：尽可能支持unicode|
|--clean|子啊本次编译开始时，清空上一次编译生成的各种文件|默认：不清楚|
|--log-level LEVEL|控制编译时pyi打印的消息|一共有6个等级，由低到高分别是TRACE DEBUG INFO(默认) WARN ERROR CRITICAL。也就是默认清空下，不打印TRACE和DEBUG信息|
----

与生成结果有关的参数
|参数名|描述|说明|
|:----:|:----:|:----:|
|-D|生成one-folder的程序（默认）|生成结果是一个目录，各种第三方依赖、资源和exe同时存储在该目录|
|-F|生成one-folder的程序|生成结果是一个exe文件，所有的第三方依赖、资源和代码均被打包进该exe内|
|--specpath|指定.spec文件的存储路径|默认：当前目录|
|-n|生成的.exe文件和.spec的文件名|默认：用户脚本的名称，即mian.py和mian.spec|
----

指定打包哪些资源、代码
|参数名|描述|说明|
|:----:|:----:|:----:|
|--add-data|打包额外资源|用法：`pyinstaller main.py --add-data=src;dist`。windows以`;`分割，linux以`:`分割|
|--add-binary|打包额外的代码|用法：同`-add-data`不同的是，用binary添加的文件，pyi会分析它引用的文件并把它们一同添加进来|
|-p|指定额外的import路径，类似于使用PYTHONPATH|参见PYTHONPATH|
|--hidden-import|打包额外的py库|pyi在分析过程中，有些import没有正确分析出来，运行时会报import error，这时可以使用该参数|
|--additional-hooks-dir|指定用户的hook目录|hook用法参见其他，系统hook在Pyinstaller\hooks目录下|
|--runtime-hook|指定用户runtime-hook|如果设置了此参数，则runtime-hook会在运行mian.py之前被运行|
|--exclude-module|需要排除的module|pyi会分析出很多相互关联的库，但是某些库对用户来说是没用的，可以用这个参数排除这些库，有助于减少生成文件的大小|
|-key|pyi会存储字节码，指定加密字节码的key|16位的字符串|
----

生成参数
|参数名|描述|说明|
|:----:|:----:|:----:|
|-d|执行生成的mian.exe时，会输出pyi的一些log，有助于查错|默认：不输出pyi的log|
|-s|优化符号表|原文明确表示不建议在windows使用|
|--noupx|强制不使用upx|默认：尽可能使用|
----

其他
|参数名|描述|说明|
|:----:|:----:|:----:|
|--runtime-tmpdir|指定运行时的临时目录|默认：使用系统临时变量|
----

windows和Mac特有的参数
|参数名|描述|说明|
|:----:|:----:|:----:|
|-c|显示命令行窗口|与`-w`相反，默认含有此参数|
|-w|不显示命令行窗口|编写GUI程序时使用此参数有用|
|-i|为main.exe指定图标|`pyinstaller -i beauty.ico main.py`|
-----

windows特有参数
|参数名|描述|说明|
|:----:|:----:|:----:|
|--version-file|添加版本信息文件|`pyinstaller --version ver.txt`|
|-m, --manifest|添加manifest文件|`pyinstaller -m main.manifest`|
|-r RESOURCE|向windows可执行文件添加或更新资源||
|--uac-admin|创建一个Manifest，该Manifest将在应用程序启动时请求提升||
|--uac-uiaccess|允许升级的应用程序使用远程桌面||
