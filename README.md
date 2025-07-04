```markdown
# 📅 JSON 学习计划转 ICS 日历工具

将结构化的学习计划 JSON 数据转换为标准 iCalendar (.ics) 文件，轻松导入 macOS 日，妈妈再也不用担心我需要手抄课表了。

---

## 🌟 功能亮点

- **JSON → ICS 转换**  
  支持将学习日期、课程名称、学习时长转换为标准日历事件
- **灵活时间格式**  
  ✅ 支持时间段（`19:00-21:00`）  
  ✅ 支持 `1h` 标记（默认 12:00-13:00）
- **命令行配置**  
  自定义输入/输出文件名（默认 `study_plan.json` → `study_plan.ics`）
- **时区支持**  
  使用 `Asia/Shanghai` 时区，确保时间准确性
- **兼容性优化**  
  修复 Python 3.12+ 弃用警告与 UUID 调用错误

---

## 🧩 技术栈

- Python 3.10+
- 第三方依赖：`pytz`（安装命令：`pip install pytz`）

---

## 🚀 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/yourname/json-to-ics-converter.git
cd json-to-ics-converter
```

### 2. 安装依赖
```bash
pip install pytz
```

### 3. 运行转换
```bash
# 默认模式
python convert_json_to_ics.py

# 自定义文件名
python convert_json_to_ics.py --input my_plan.json --output my_plan.ics
```

---

## 📝 输入格式示例 (`study_plan.json`)

```json
{
  "学习计划": [
    {
      "学习日期": "7月1日",
      "学习课程": "2016年英语一真题词汇",
      "学习时长": "1h"
    },
    {
      "学习日期": "7月1日",
      "学习课程": "讲毛中特02-改造和建设理论",
      "学习时长": "19:00-21:00"
    }
  ]
}
```

---

## 📤 输出示例片段

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//My Learning Plan//Calendar Export//EN
BEGIN:VEVENT
DTSTART;TZID=Asia/Shanghai:20250701T120000
DTEND;TZID=Asia/Shanghai:20250701T130000
SUMMARY:2016年英语一真题词汇
UID:1A2B3C4D-5E6F-7A8B-9C0D-EF1234567890
...
```

---

## ⚠️ 注意事项

- **年份假设**：所有事件默认年份为 `2025`  
  （如需修改，调整脚本中 `year = 2025` 变量）
- **空事件处理**：跳过课程和时长均为空的条目
- **UID 唯一性**：每次运行生成新 UID，避免冲突

---

## 🤝 贡献指南

欢迎提交 Issues 和 Pull Requests！  
请遵循以下规范：
1. Fork 仓库并创建新分支
2. 提交清晰的更改描述
3. 确保代码风格一致

---

## 📄 许可证

[MIT License](LICENSE)  
允许商业使用与修改，详情见 LICENSE 文件
```

---
