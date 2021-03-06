# -*- coding: utf-8 -*-

# 导出模式
EXPORTER_CLASS = "ConfigExporter"

# 表头行索引
SHEET_ROW_INDEX = {
	"argument" : 0,
	"header" : 1,
	"data" : 2,
}

# Excel输入路径
INPUT_PATH = "$CONFIG_PATH/excels"

# 中间文件存放路径
TEMP_PATH = "$CONFIG_PATH/export/xtemp"

# 转换器父级路径
CONVERTER_PATH = "$CONFIG_PATH/converters"

# 转换器子目录，转换器脚本存放在这里。目的是防止命名冲突
CONVERTER_ALIAS = "converter"

# 数据输出器
DATA_WRITERS = [
	{"stage" : 2, "class" : "PyWriter", "file_path": "$CONFIG_PATH/export/python", "file_posfix" : ".py"},
	{"stage" : 2, "class" : "LuaWriter", "file_path": "$CONFIG_PATH/export/lua", "file_posfix" : ".lua"},
	{"stage" : 2, "class" : "JavaScriptWriter", "file_path": "$CONFIG_PATH/export/js", "file_posfix" : ".js"},
	{"stage" : 2, "class" : "JsonWriter", "file_path": "$CONFIG_PATH/export/json", "file_posfix" : ".json"},
	{"stage" : 2, "class" : "JavaWriter", "file_path": "$CONFIG_PATH/export/java", "file_posfix" : ".wg"},
]


"""
(excel文件名正则表达式，转换器文件名称 |，新名称的正则表达式，表索引)
新名称	可以缺省，默认是原名称去除后缀
表索引	可以缺省，默认是0
eg.
缺省：(r"stage/normal/\d+/enemy.xlsx", "enemy"), -> stage/normal/\d+/enemy
改名：(r"(stage/normal/\d+/)enemy.xlsx", "enemy", r"\1d_enemy", 0), -> stage/normal/\d+/d_enemy
"""
CONVENTION_TABLE = (
	("example.xlsx", "example", ),
)

"""
合并表
excel支持分表结构，即，一个excel可以拆分成多个，每个人负责自己的部分，
导表的时候，会自动把这些子表合并到以前。MERGE_TABLE描述了合并的规则：
	(新表路径, 子表i路径, ...)
子表i的路径支持正则表达式。
"""
MERGE_TABLE = (
	("entity/entity", r"entity/entity_part\d+", ),
)
