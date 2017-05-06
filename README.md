导表工具
======================

# 导表工具原理
1. 搜索`excels`路径下的所有Excel文件
2. 根据`convention_table.py`中的Excel和`转换器`关系，找到Excel文件对应的转换器
3. 使用Excel文件和转换器作为参数，构造`xlsparser`
4. parser将Excel数据转换成python表，存贮到中间目录下
5. 当所有文件转换完毕后，根据`convention_table.py`中的分表关系，将中间目录下的分表合成总表
6. 针对每个python表，执行后处理操作。比如字段合并，引用检查等
7. 实例化writer对象，将python表转换成lua、json等格式。

# 如何执行导表？
执行`python main.py your_configure_file`

# 如何生成java类文件？
执行`python main.py --gen-code your_configure_file`

# 如何添加表头？
1. 在Excel表中，添加上“表头”，以及类型描述
2. 在转换器中的`CONFIG`字典中，添加上“表头”和代码中字段的对应关系，以及转换函数。

# 如何根据转换器配置为excel添加表头？
执行`python main.py --gen-header your_configure_file`

# 如何添加新Excel表？
1. 在`excels`路径下，新建Excel表，表内容格式如下：  
![](doc/excel.png)  

行   | 描述
------|------
第1行 | 预留
第2行 | 预留
第3行 | 表头
第4行 | 基础类型描述。

前两行预留，第3行为表头，第4行为基础类型描述。空白行或者列都是有效数据分割符，位于空白列右侧或空白行下侧，都不会参与导表。
2. 在`converter`目录下添加python转换器。转换器的详细写法，请参考`converter/example.py`。大致内容如下：
```python
KEY_NAME = "ID"
CONFIG = {
    ("编号", "ID", int),
    ("名称", "name", unicode),
    ("描述", "describe", unicode, True),
    ("品质", "quality", int, True, 0),
}
```
CONFIG是一个数组，描述了如何将excel表头转换成程序用的字段。

数组索引 | 描述
--------|------------
 0      | 程序使用的字段名
 1      | 转换函数。将excel表中的单元格转换成脚本对象
 2      | 表示此列是否可缺省，即是否可不填
 3      | 缺省值。脚本中使用此值替代excel中没有填的位置，如果没有指定缺省值，脚本中就不会出现该单元格的数据。
3. 在`convention_table.py`文件中添加上Excel表与转换器的对应关系。